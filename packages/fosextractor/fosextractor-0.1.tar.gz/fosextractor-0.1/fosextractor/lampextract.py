import os
import math
import numpy as np
import astropy.io.fits as fits
from astropy.table import Table
import scipy.interpolate as intp
import scipy.optimize as opt
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib.figure import Figure
from mpl_toolkits import mplot3d
from scipy.ndimage import median_filter

from gamse.echelle.imageproc import combine_images
from gamse.utils.onedarray import iterative_savgol_filter
from gamse.utils.regression import get_clip_mean
def load_obslog():
    for fname in os.listdir('./'):
        if fname[-7:]=='.obslog':
            print('Load logtable:', fname)
            logtable = Table.read(filename=fname,
                                format='ascii.fixed_width_two_line',
                                delimiter='|')
    return logtable
class Figure2D(Figure):
    def __init__(self, dpi=300, figsize=(10,6), data=None,
                scale=(10,99), title=''):
        Figure.__init__(self, dpi=dpi,figsize=figsize)
        b1 = 0.10
        h1 = 0.8
        w1 = h1/figsize[0]*figsize[1]
        l2 = 0.66
        w2 = 0.30
        hgap1 = 0.08
        h3 = 0.02
        h2 = (h1-2*hgap1-h3)/2
        self.ax_image = self.add_axes([b1, b1,  w1, h1])
        self.ax_hist1 = self.add_axes([l2, b1+h3+hgap1*2+h2, w2, h2])
        self.ax_hist2 = self.add_axes([l2, b1+h3+hgap1, w2, h2])
        self.ax_cbar0 = self.add_axes([l2, b1,  w2, h3])

        vmin = np.percentile(data, scale[0])
        vmax = np.percentile(data, scale[1])
        cax = self.ax_image.imshow(data, origin='lower', vmin=vmin, vmax=vmax)
        self.colorbar(cax, cax=self.ax_cbar0, orientation='horizontal')
        self.ax_image.set_xlabel('X (pixel)')
        self.ax_image.set_ylabel('Y (pixel)')

        # plot hist1, the whole histogram
        self.ax_hist1.hist(data.flatten(), bins=50)
        self.ax_hist1.axvline(x=vmin, color='k', ls='--', lw=0.7)
        self.ax_hist1.axvline(x=vmax, color='k', ls='--', lw=0.7)
        y1, y2 = self.ax_hist1.get_ylim()
        self.ax_hist1.text(vmin, 0.1*y1+0.9*y2, str(scale[0])+'%')
        self.ax_hist1.text(vmax, 0.1*y1+0.9*y2, str(scale[1])+'%')
        self.ax_hist1.set_ylim(y1, y2)

        self.ax_hist2.hist(data.flatten(), bins=np.linspace(vmin, vmax, 50))
        self.ax_hist2.set_xlim(vmin, vmax)
        self.suptitle(title)
def errfunc(p, x, y, fitfunc):
    return y - fitfunc(p, x)
def gaussian(A, fwhm, c, x):
    s = fwhm/2.35482
    return A*np.exp(-(x-c)**2/2./s**2)

def gengaussian(A, alpha, beta, c, x):
    return A*np.exp(-(np.abs(x-c)/alpha)**beta)
def fitfunc2(p, x):
    return gengaussian(p[0], p[1], p[2], p[3], x) + p[4]
def find_shift_ccf(f1, f2, shift0=0.0):
    x = np.arange(f1.size)
    interf = intp.InterpolatedUnivariateSpline(x, f1, k=3)
    func = lambda shift: -(interf(x - shift)*f2).sum(dtype=np.float64)
    res = opt.minimize(func, shift0, method='Powell')
    return res['x']
def parttwo():
    selection_file = 'file_selection.txt'  # selection file
    bias_file = 'bias.fits'
    flat_file = 'flat.fits'
    figpath = 'images/'
    selection_file = 'file_selection.txt'  # selection file
    wl_guess_file = 'wl_guess.txt'  # an initial guess of wavelengths
    wavebound = 6900
    logtable = load_obslog()
    bias_data = fits.getdata(bias_file)
    hdu_lst = fits.open(flat_file)
    flat_data = hdu_lst[0].data
    flat_sens = hdu_lst[1].data
    hdu_lst.close()
    ########### read file_selection.txt ##########
    if os.path.exists(selection_file):
        file1 = open(selection_file)
        for row in file1:
            row = row.strip()
            if len(row) == 0 or row[0] == '#':
                continue
            col = row.split(':')
            key = col[0].strip()
            value = col[1].strip()
            # if key == 'trace' and value in logtable['fileid']:
            #    trace_fileid = value
            if key == 'wlcalib_red' and value in logtable['fileid']:
                wlcalib_red_fileid = value
            elif key == 'wlcalib_blue' and value in logtable['fileid']:
                wlcalib_blue_fileid = value
            else:
                continue
        file1.close()
    else:
        pass

    def frameid_to_fileid(frameid):
        m = logtable['frameid'] == frameid
        if m.sum() == 0:
            return None
        elif m.sum() == 1:
            return logtable[m][0]['fileid']
        else:
            raise ValueError

    if None in [
        # trace_fileid,
        wlcalib_red_fileid, wlcalib_blue_fileid
    ]:
        ####################### select trace file ############################
        ## select trace file
        # while(trace_fileid is None):
        #    string = input('Select FileID for tracing: ')
        #    try:
        #        trace_frameid = int(string)
        #        trace_fileid  = frameid_to_fileid(trace_frameid)
        #        break
        #    except:
        #        continue
        ################### select wavelength calibration file ###############
        while (wlcalib_red_fileid is None):
            string = input('Select FileID for wavelength calibration in RED: ')
            try:
                wlcalib_red_frameid = int(string)
                wlcalib_red_fileid = frameid_to_fileid(wlcalib_red_frameid)
                break
            except:
                continue
        while (wlcalib_blue_fileid is None):
            string = input('Select FileID for wavelength calibration in BLUE: ')
            try:
                wlcalib_blue_frameid = int(string)
                wlcalib_blue_fileid = frameid_to_fileid(wlcalib_blue_frameid)
                break
            except:
                continue
        ############### write selections to file_selection.txt ###############
        file1 = open(selection_file, 'w')
        # file1.write('trace: '+trace_fileid+os.linesep)
        file1.write('wlcalib_red: {}'.format(wlcalib_red_fileid) + os.linesep)
        file1.write('wlcalib_blue: {}'.format(wlcalib_blue_fileid) + os.linesep)
        file1.close()

    # get the men Y position
    # ycen0 = np.int32(np.round(ycen.mean()))

    ###################### extract calibration lamp #########################
    # make a plot of line idenification
    figs = plt.figure(dpi=300, figsize=(15, 8))
    nrow, ncol = 4, 6
    count_line = 0
    center_lst = []
    wave_lst = []
    spec_lst = {}  # use to save the extracted 1d spectra of calib lamp

    for fileid in [wlcalib_red_fileid, wlcalib_blue_fileid]:
        # dt = logitem['dateobs'].datetime
        # fname = '{:04d}{:02d}{:02d}-{:04d}.fit'.format(
        #        dt.year, dt.month, dt.day, logitem['frameid'])
        fname = fileid + '.fit'
        filename = os.path.join('rawdata', fname)
        data = fits.getdata(filename)
        data = data - bias_data
        data = data / flat_sens

        ny, nx = data.shape
        allx = np.arange(nx)
        ally = np.arange(ny)

        # make a plot
        title = '{} ({})'.format(fileid, 'FeAr')
        fig2 = Figure2D(data=data, scale=(10, 90), title=title)
        figname = 'loc_{}.png'.format(fileid)
        figfilename = os.path.join(figpath, figname)
        fig2.savefig(figfilename)
        plt.close(fig2)

        # extract 1d sepectra of wavelength calibration lamp
        hwidth = 5
        spec = data[ny // 2 - hwidth:ny // 2 + hwidth + 1, :].sum(axis=0)
        spec_lst[fileid] = spec

        linelist = np.loadtxt(wl_guess_file)
        if fileid == wlcalib_red_fileid:
            m = linelist[:, 1] > wavebound
            band = 'red'
        elif fileid == wlcalib_blue_fileid:
            m = linelist[:, 1] < wavebound
            band = 'blue'
        else:
            continue
        linelist = linelist[m]

        init_pixl_lst = linelist[:, 0]
        init_wave_lst = linelist[:, 1]

        for x, wave in zip(init_pixl_lst, init_wave_lst):
            i = np.searchsorted(allx, x)
            i1, i2 = i - 9, i + 10
            xdata = allx[i1:i2]
            ydata = spec[i1:i2]
            p0 = [ydata.max() - ydata.min(), 3.6, 3.5, (i1 + i2) / 2, ydata.min()]
            fitres = opt.least_squares(errfunc, p0,
                                       args=(xdata, ydata, fitfunc2))
            p = fitres['x']
            A, alpha, beta, center, bkg = p
            center_lst.append(center)
            wave_lst.append(wave)

            print('{:4s} {:9.4f} {:5.2f} {:8.3f}'.format(
                band, wave, alpha, center))

            ix = count_line % ncol
            iy = nrow - 1 - count_line // ncol
            axs = figs.add_axes([0.07 + ix * 0.16, 0.08 + iy * 0.23, 0.12, 0.20])
            if band == 'red':
                color = 'C3'
            elif band == 'blue':
                color = 'C0'
            else:
                color = 'k'
            axs.scatter(xdata, ydata, s=10, alpha=0.6, color=color)
            newx = np.arange(i1, i2, 0.1)
            newy = fitfunc2(p, newx)
            axs.plot(newx, newy, ls='-', color='C1', lw=1, alpha=0.7)
            axs.axvline(x=center, color='k', ls='--', lw=0.7)
            axs.set_xlim(newx[0], newx[-1])
            x1, x2 = axs.get_xlim()
            y1, y2 = axs.get_ylim()
            axs.text(0.95 * x1 + 0.05 * x2, 0.2 * y1 + 0.8 * y2,
                     '{:9.4f}\n{:s}'.format(wave, fileid),
                     fontsize=9)
            axs.xaxis.set_major_locator(tck.MultipleLocator(5))
            axs.xaxis.set_minor_locator(tck.MultipleLocator(1))
            for tick in axs.yaxis.get_major_ticks():
                tick.label1.set_fontsize(9)

            count_line += 1

    figname = 'fitlines.png'
    figfilename = os.path.join(figpath, figname)
    figs.savefig(figfilename)
    plt.close(figs)

    wave_lst = np.array(wave_lst)
    center_lst = np.array(center_lst)

    args = center_lst.argsort()
    center_lst = center_lst[args]
    wave_lst = wave_lst[args]

    coeff_wave = np.polyfit(center_lst, wave_lst, deg=4)
    allwave = np.polyval(coeff_wave, allx)
    stdwave = (wave_lst - np.polyval(coeff_wave, center_lst)).std()

    # save to ascii files
    for fileid, spec in sorted(spec_lst.items()):
        filename = 'wlcalib.{}.dat'.format(fileid)
        outfile = open(filename, 'w')
        for w, f in zip(allwave, spec):
            outfile.write('{:9.4f} {:+12.7e}'.format(w, f) + os.linesep)
        outfile.close()

    # make a wavelength solution figure
    '''
    fig3 = plt.figure(figsize=(9, 6), dpi=200)
    ax31 = fig3.add_axes([0.1, 0.52, 0.85, 0.35])
    ax32 = fig3.add_axes([0.1, 0.10, 0.85, 0.35])
    ax31.plot(allwave, spec)
    ax32.plot(allx, spec)
    for w, c in zip(wave_lst, center_lst):
        ax31.axvline(x=w, color='k',ls='--', lw=0.7)
        ax32.axvline(x=c, color='k',ls='--', lw=0.7)
    ax31.set_xlabel(u'Wavelength (\xc5)')
    ax32.set_xlabel('Pixel')
    ax31.set_xlim(allwave[0], allwave[-1])
    ax32.set_xlim(nx-1, 0)
    '''

    # plot wavelength solution
    figt = plt.figure(figsize=(12, 6), dpi=300)
    axt1 = figt.add_axes([0.07, 0.66, 0.44, 0.26])
    axt2 = figt.add_axes([0.07, 0.38, 0.44, 0.26])
    axt3 = figt.add_axes([0.07, 0.10, 0.44, 0.26])
    axt4 = figt.add_axes([0.58, 0.54, 0.37, 0.38])
    axt5 = figt.add_axes([0.58, 0.10, 0.37, 0.38])
    axt1.scatter(center_lst, wave_lst, s=20)
    axt1.plot(allx, allwave)
    axt2.scatter(center_lst, wave_lst - np.polyval(coeff_wave, center_lst), s=20)
    axt2.axhline(y=0, color='k', ls='--')
    axt2.axhline(y=stdwave, color='k', ls='--', alpha=0.4)
    axt2.axhline(y=-stdwave, color='k', ls='--', alpha=0.4)
    coeff_wave0 = np.polyfit(center_lst, wave_lst, deg=1)
    axt3.scatter(center_lst, wave_lst - np.polyval(coeff_wave0, center_lst), s=20)
    axt3.plot(allx, allwave - np.polyval(coeff_wave0, allx))
    axt3.axhline(y=0, color='k', ls='--')
    for ax in figt.get_axes():
        ax.grid(True, color='k', alpha=0.4, ls='--', lw=0.5)
        ax.set_axisbelow(True)
        ax.set_xlim(0, nx - 1)
    y1, y2 = axt2.get_ylim()
    axt2.text(0.03 * nx, 0.2 * y1 + 0.8 * y2, u'RMS = {:5.3f} \xc5'.format(stdwave))
    axt2.set_ylim(y1, y2)
    axt3.set_xlabel('Pixel')
    axt1.set_ylabel(u'\u03bb (\xc5)')
    axt2.set_ylabel(u'\u0394\u03bb (\xc5)')
    axt3.set_ylabel(u'\u0394\u03bb (\xc5)')
    axt1.set_xticklabels([])
    axt2.set_xticklabels([])
    axt4.plot(allx[0:-1], -np.diff(allwave))
    axt5.plot(allx[0:-1], -np.diff(allwave) / (allwave[0:-1]) * 299792.458)
    axt4.set_ylabel(u'd\u03bb/dx (\xc5)')
    axt5.set_xlabel('Pixel')
    axt5.set_ylabel(u'dv/dx (km/s)')
    title = 'Wavelength Solution'
    figt.suptitle(title)
    figname = 'wavelength.png'
    figfilename = os.path.join(figpath, figname)
    figt.savefig(figfilename)
    plt.close(figt)


    exit()
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
def partthree():
    figpath = 'images/'  # path to the figures
    ccd_gain = 1.41  # CCD gain (electron/ADU)
    ccd_ron = 4.64  # CCD readout noise (electron/pixel)
    bias_file = 'bias.fits'  # bias FITS file
    flat_file = 'flat.fits'  # flat FITS file
    plot_bias = True  # plot bias image
    plot_flat = True  # plot flat image
    selection_file = 'file_selection.txt'  # selection file
    wl_guess_file = 'wl_guess.txt'  # an initial guess of wavelengths
    wavebound = 6900  # wavelength boundary to separate red and blue
    background_rows = [(340, 500), (1600, 1820)]  # rows to exctract background
    plot_opt_columns = False  # column-by-column figure of optimal extraction
    bias_data = fits.getdata(bias_file)
    hdu_lst = fits.open(flat_file)
    flat_data = hdu_lst[0].data
    flat_sens = hdu_lst[1].data
    hdu_lst.close()
    # load obslog table
    logtable = load_obslog()

    if os.path.exists(selection_file):
        file1= open(selection_file)
        for row in file1:
            row = row.strip()
            if len(row)==0 or row[0]=='#':
                continue
            col = row.split(':')
            key = col[0].strip()
            value = col[1].strip()
            #if key == 'trace' and value in logtable['fileid']:
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
    for fileid in [wlcalib_red_fileid, wlcalib_blue_fileid]:
        #dt = logitem['dateobs'].datetime
        #fname = '{:04d}{:02d}{:02d}-{:04d}.fit'.format(
        #        dt.year, dt.month, dt.day, logitem['frameid'])
        fname = fileid + '.fit'
        filename = os.path.join('rawdata', fname)
        data = fits.getdata(filename)
        data = data - bias_data
        data = data/flat_sens

        ny, nx = data.shape
        allx = np.arange(nx)
        ally = np.arange(ny)
    ################## find CCD spatial curvature ##########################
    coeff_lst = {}
    fig22 = plt.figure(figsize=(8, 6), dpi=300)
    ax22 = fig22.add_axes([0.1, 0.1, 0.85, 0.8])
    for fileid in [wlcalib_red_fileid, wlcalib_blue_fileid]:
        fname = fileid + '.fit'
        filename = os.path.join('rawdata', fname)
        data = fits.getdata(filename)
        data = data - bias_data
        data = data / flat_sens
        hwidth = 5
        ref_spec = data[ny // 2 - hwidth:ny // 2 + hwidth + 1, :].sum(axis=0)
        if fileid == wlcalib_red_fileid:
            band = 'red'
            mask = allwave > wavebound
        else:
            band = 'blue'
            mask = allwave < wavebound
        ref_spec = ref_spec[mask]
        xcoord = np.arange(nx)[mask]

        ycoord_lst = []
        xshift_lst = []

        fig = plt.figure(dpi=300, figsize=(8, 6))
        ax01 = fig.add_axes([0.1, 0.55, 0.85, 0.36])
        ax02 = fig.add_axes([0.1, 0.10, 0.85, 0.36])
        for i, y in enumerate(np.arange(100, ny - 100, 200)):
            spec = data[y - hwidth:y + hwidth + 1, :].sum(axis=0)
            spec = spec[mask]
            shift = find_shift_ccf(ref_spec, spec)
            if i == 0:
                ax01.plot(xcoord, spec, color='w', lw=0)
                y1, y2 = ax01.get_ylim()
                offset = (y2 - y1) / 20
            ax01.plot(xcoord - shift, spec + offset * i, lw=0.5)
            ax02.plot(xcoord, spec + offset * i, lw=0.5)
            ycoord_lst.append(y)
            xshift_lst.append(shift)
        ax01.set_xlim(xcoord[0], xcoord[-1])
        ax02.set_xlim(xcoord[0], xcoord[-1])
        ax02.set_xlabel('Pixel')
        fig.suptitle('{}'.format(fileid))
        figname = 'distortion_{}.png'.format(fileid)
        figfilename = os.path.join(figpath, figname)
        fig.savefig(figfilename)
        plt.close(fig)

        coeff = np.polyfit(ycoord_lst, xshift_lst, deg=2)
        if fileid == wlcalib_red_fileid:
            coeff_lst['red'] = coeff
        elif fileid == wlcalib_blue_fileid:
            coeff_lst['blue'] = coeff
        else:
            print('Warning')

        # determine the color and label
        if band == 'red':
            color = 'C3'
            label = u'{} (\u03bb > {} \xc5)'.format(fileid, wavebound)
        else:
            color = 'C0'
            label = u'{} (\u03bb < {} \xc5)'.format(fileid, wavebound)

        ax22.scatter(xshift_lst, ycoord_lst, c=color, alpha=0.7,
                     label=label)
        ax22.plot(np.polyval(coeff, ally), ally, color=color, alpha=0.7)
    ax22.axhline(y=ny // 2, ls='-', color='k', lw=0.7)
    ax22.set_ylim(0, ny - 1)
    ax22.xaxis.set_major_locator(tck.MultipleLocator(1))
    ax22.set_xlabel('Shift (pixel)')
    ax22.set_ylabel('Y (pixel)')
    ax22.grid(True, ls='--')
    ax22.set_axisbelow(True)
    ax22.legend(loc='upper left')
    figname = 'distortion_fitting.png'
    figfilename = os.path.join(figpath, figname)
    fig22.savefig(figfilename)
    plt.close(fig22)
    ##################  extract sci spectra ##################
    curve_coeff = (coeff_lst['red'] + coeff_lst['blue']) / 2.
    xshift_lst = np.polyval(curve_coeff, ally)

    sci_logitem_lst = filter(lambda item: item['imgtype'] == 'sci', logtable)

    for logitem in sci_logitem_lst:
        # dt = logitem['dateobs'].datetime
        # fileid= '{:04d}{:02d}{:02d}-{:04d}'.format(
        #        dt.year, dt.month, dt.day, logitem['frameid'])
        print('* FileID: {} - 1d spectra extraction'.format(logitem['fileid']))
        fname = logitem['fileid'] + '.fit'
        filename = os.path.join('rawdata', fname)
        data = fits.getdata(filename)
        data = data - bias_data
        data = data / flat_sens

        ny, nx = data.shape
        allx = np.arange(nx)
        ally = np.arange(ny)
        xdata = ally

        figname = 'trace_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        title = 'Trace for {} ({})'.format(logitem['fileid'], logitem['object'])
        coeff_loc, fwhm_mean, profile_func = trace(data, figfilename, title)

        # generate order location array
        ycen = np.polyval(coeff_loc, allx)

        # generate wavelength list considering horizontal shift
        xshift_lst = np.polyval(curve_coeff, ycen)
        wave_lst = np.polyval(coeff_wave, allx - xshift_lst)

        # extract 1d sepectra

        # summ extraction
        yy, xx = np.mgrid[:ny, :nx]
        upper_line = ycen + fwhm_mean
        lower_line = ycen - fwhm_mean
        upper_ints = np.int32(np.round(upper_line))
        lower_ints = np.int32(np.round(lower_line))
        extmask = (yy > lower_ints) * (yy < upper_ints)
        mask = np.float32(extmask)
        # determine the weights in the boundary
        mask[upper_ints, allx] = (upper_line + 0.5) % 1
        mask[lower_ints, allx] = 1 - (lower_line + 0.5) % 1

        # extract
        spec_sum = (data * mask).sum(axis=0)
        nslit = mask.sum(axis=0)

        # make a plot of image
        # title = '{} ({})'.format(logitem['fileid'], logitem['object'])
        # fig2 = Figure2D(data=data, scale=(10, 99), title=title)
        # fig2.ax1.plot(allx, ycen,
        #                color='C3', ls='-', lw=0.5, alpha=1)
        # fig2.ax1.plot(allx, upper_line,
        #                color='C3', ls='--', lw=0.5, alpha=1)
        # fig2.ax1.plot(allx, lower_line,
        #                color='C3', ls='--', lw=0.5, alpha=1)
        # figname = 'loc_{}.png'.format(logitem['fileid'])
        # figfilename = os.path.join(figpath, figname)
        # fig2.savefig(figfilename)
        # plt.close(fig2)

        # correct image distortion
        ycen0 = ycen[0:-200].mean()
        cdata = np.zeros_like(data, dtype=data.dtype)
        for y in np.arange(ny):
            row = data[y, :]
            shift = np.polyval(curve_coeff, y) - np.polyval(curve_coeff, ycen0)
            f = intp.InterpolatedUnivariateSpline(allx, row, k=3, ext=3)
            cdata[y, :] = f(allx + shift)

        # initialize background mask
        bkgmask = np.zeros_like(data, dtype=np.bool)
        for r1, r2 in background_rows:
            bkgmask[r1:r2, :] = True

        # plot image after distortion correction
        title = 'Curvature Correction for {} ({})'.format(
            logitem['fileid'], logitem['object'])
        fig3 = Figure2D(data=cdata, scale=(10, 99), title=title)
        fig3.ax_image.plot(allx, ycen,
                           color='C3', ls='-', lw=0.5, alpha=1)
        fig3.ax_image.plot(allx, upper_line,
                           color='C3', ls='--', lw=0.5, alpha=1)
        fig3.ax_image.plot(allx, lower_line,
                           color='C3', ls='--', lw=0.5, alpha=1)
        # plot background mask regions
        for r1, r2 in background_rows:
            fig3.ax_image.plot(allx, np.repeat(r1, nx),
                               color='C1', ls='-', lw=0.5, alpha=1)
            fig3.ax_image.plot(allx, np.repeat(r2, nx),
                               color='C1', ls='-', lw=0.5, alpha=1)
        figname = 'loc_curve_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        fig3.savefig(figfilename)
        plt.close(fig3)

        # remove cosmic rays in the background region
        # ori_bkgspec= (cdata*bkgmask).sum(axis=0)/(bkgmask.sum(axis=0))

        # method 1
        # for r1, r2 in background_rows:
        #    cutdata = cdata[r1:r2, :]
        #    fildata = median_filter(cutdata, (1, 5), mode='nearest')
        #    resdata = cutdata - fildata
        #    std = resdata.std()
        #    mask = (resdata < 3*std)*(resdata > -3*std)
        #    bkgmask[r1:r2, :] = mask

        # method 2
        for r1, r2 in background_rows:
            bkgmask[r1:r2, :] = True
            cutdata = cdata[r1:r2, :]
            mean = cutdata.mean(axis=0)
            std = cutdata.std()
            mask = (cutdata < mean + 3 * std) * (cutdata > mean - 3 * std)
            bkgmask[r1:r2, :] = mask

        # plot the bkg and bkg mask
        # fig0 = plt.figure()
        # ax01 = fig0.add_subplot(121)
        # ax02 = fig0.add_subplot(122)
        # for r1, r2 in background_rows:
        #    for y in np.arange(r1, r2):
        #        ax01.plot(cdata[y, :]+y*15, lw=0.5)
        #        m = ~bkgmask[y, :]
        #        ax01.plot(allx[m], cdata[y, :][m]+y*15, 'o', color='C0')
        # bkgspec = (cdata*bkgmask).sum(axis=0)/(bkgmask.sum(axis=0))
        # ax02.plot(ori_bkgspec)
        # ax02.plot(bkgspec)
        # plt.show()

        # remove the peaks in the spatial direction
        # sum of background mask along y
        bkgmasksum = bkgmask.sum(axis=1)
        # find positive positions
        posmask = np.nonzero(bkgmasksum)[0]
        # initialize crossspec
        crossspec = np.zeros(ny)
        crossspec[posmask] = (cdata * bkgmask).sum(axis=1)[posmask] / bkgmasksum[posmask]
        fitx = ally[posmask]
        fity = crossspec[posmask]
        fitmask = np.ones_like(posmask, dtype=np.bool)
        maxiter = 3
        for i in range(maxiter):
            c = np.polyfit(fitx[fitmask], fity[fitmask], deg=2)
            res_lst = fity - np.polyval(c, fitx)
            std = res_lst[fitmask].std()
            new_fitmask = (res_lst > -2 * std) * (res_lst < 2 * std)
            if new_fitmask.sum() == fitmask.sum():
                break
            fitmask = new_fitmask

        # block these pixels in bkgmask
        for y in ally[posmask][~fitmask]:
            bkgmask[y, :] = False

        # plot the cross-section of background regions
        fig100 = plt.figure(figsize=(9, 6), dpi=300)
        ax1 = fig100.add_axes([0.07, 0.54, 0.87, 0.36])
        ax2 = fig100.add_axes([0.07, 0.12, 0.87, 0.36])
        newy = np.polyval(c, ally)
        for ax in fig100.get_axes():
            ax.plot(ally, cdata.mean(axis=1), alpha=0.3, color='C0', lw=0.7)
        y1, y2 = ax1.get_ylim()

        ylst = ally[posmask][fitmask]
        for idxlst in np.split(ylst, np.where(np.diff(ylst) != 1)[0] + 1):
            for ax in fig100.get_axes():
                ax.plot(ally[idxlst], crossspec[idxlst], color='C0', lw=0.7)
                ax.fill_betweenx([y1, y2], idxlst[0], idxlst[-1],
                                 facecolor='C2', alpha=0.15)

        for ax in fig100.get_axes():
            ax.plot(ally, newy, color='C1', ls='-', lw=0.5)

        ax2.plot(ally, newy + std, color='C1', ls='--', lw=0.5)
        ax2.plot(ally, newy - std, color='C1', ls='--', lw=0.5)
        for ax in fig100.get_axes():
            ax.set_xlim(0, ny - 1)
            ax.grid(True, ls='--', lw=0.5)
            ax.set_axisbelow(True)
        ax1.set_ylim(y1, y2)
        ax2.set_ylim(newy.min() - 6 * std, newy.max() + 6 * std)
        ax2.set_xlabel('Y (pixel)')
        title = '{} ({})'.format(logitem['fileid'], logitem['object'])
        fig100.suptitle(title)
        figname = 'bkg_cross_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        fig100.savefig(figfilename)
        plt.close(fig100)

        # plot a 2d image of distortion corrected image
        # and background region
        fig3 = plt.figure(dpi=300, figsize=(12, 6))
        ax31 = fig3.add_axes([0.07, 0.1, 0.4, 0.8])
        ax32 = fig3.add_axes([0.55, 0.1, 0.4, 0.8])
        vmin = np.percentile(cdata, 10)
        vmax = np.percentile(cdata, 99)
        ax31.imshow(cdata, origin='lower', vmin=vmin, vmax=vmax)
        bkgdata = np.zeros_like(cdata, dtype=cdata.dtype)
        bkgdata[bkgmask] = cdata[bkgmask]
        bkgdata[~bkgmask] = (vmin + vmax) / 2
        ax32.imshow(bkgdata, origin='lower', vmin=vmin, vmax=vmax)
        for ax in fig3.get_axes():
            ax.set_xlim(0, nx - 1)
            ax.set_ylim(0, ny - 1)
            ax.set_xlabel('X (pixel)')
            ax.set_ylabel('Y (pixel)')
        title = '{} ({})'.format(logitem['fileid'], logitem['object'])
        fig3.suptitle(title)
        figname = 'bkg_region_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        fig3.savefig(figfilename)
        plt.close(fig3)

        # background spectra per pixel along spatial direction
        bkgspec = (cdata * bkgmask).sum(axis=0) / (bkgmask.sum(axis=0))
        # background spectra in the spectrum aperture
        background_sum = bkgspec * nslit

        spec_sum_dbkg = spec_sum - background_sum

        # plot spatial profile
        '''
        figp = plt.figure(dpi=300,figsize=(12,4), tight_layout=True)
        axp1 = figp.add_subplot(121)
        axp2 = figp.add_subplot(122)
        for x in np.arange(10, nx-200, 10):
            i1 = lower_ints[x]-15
            i2 = upper_ints[x]+15
            xdata = ally[i1:i2]
            ydata = data[i1:i2, x-5:x+6].mean(axis=1)
            offset = x*0.0002
            axp1.plot(xdata-ycen[x], (ydata-bkgspec[x])/spec1d[x]+offset,
                    alpha=0.5, lw=0.5)
            yflux = (ydata-bkgspec[x])/spec1d[x]
            axp2.plot((xdata-ycen[x])/fwhm_mean, yflux/yflux.sum(),
                    alpha=0.5, lw=0.5)
        for ax in figp.get_axes():
            ax.grid(True, ls='--', lw=0.5)
            ax.set_axisbelow(True)
        axp2.set_ylim(-0.05, 0.15)
        figp.savefig('images/profile_{}.png'.format(logitem['fileid']))
        plt.close(figp)
        '''

        # optimal extraction
        debkg_data = data - np.repeat([bkgspec], ny, axis=0)

        fitprof_func = lambda p, x: p[0] * profile_func(x) + p[1]
        f_opt_lst = []
        b_opt_lst = []
        for x in np.arange(nx):
            ycenint = np.int32(np.round(ycen[x]))
            y1 = ycenint - 18
            y2 = ycenint + 19
            fitx = ally[y1:y2] - ycenint
            flux = data[y1:y2, x]
            debkg_flux = debkg_data[y1:y2, x]
            mask = np.ones(y2 - y1, dtype=np.bool)

            # b0 = (flux[0]+flux[-1])/2
            b0 = bkgspec[x]
            p0 = [flux.max() - b0, b0]
            maxiter = 6
            for ite in range(maxiter):
                fitres = opt.least_squares(errfunc, p0,
                                           args=(fitx[mask], flux[mask], fitprof_func))
                p = fitres['x']
                res_lst = errfunc(p, fitx, flux, fitprof_func)
                std = res_lst[mask].std()
                new_mask = res_lst < 3 * std
                if new_mask.sum() == mask.sum():
                    break
                mask = new_mask

            # plot the column-by-column fitting figure
            if plot_opt_columns:
                nrow = 5
                ncol = 7
                if x % (nrow * ncol) == 0:
                    fig = plt.figure(figsize=(14, 8), dpi=200)
                iax = x % (nrow * ncol)
                icol = iax % ncol
                irow = int(iax / ncol)
                w1 = 0.95 / ncol
                w2 = w1 - 0.025
                h1 = 0.96 / nrow
                h2 = h1 - 0.025
                ax = fig.add_axes([0.05 + icol * w1, 0.05 + (nrow - irow - 1) * h1, w2, h2])
                ax.scatter(fitx, flux, c='w', edgecolor='C0', s=15)
                ax.scatter(fitx[mask], flux[mask], c='C0', s=15)
                newx = np.arange(y1, y2 + 1e-3, 0.1) - ycenint
                newy = fitprof_func(p, newx)
                ax.plot(newx, newy, ls='-', color='C1')
                ax.plot(newx, newy + std, ls='--', color='C1')
                ax.plot(newx, newy - std, ls='--', color='C1')
                ylim1, ylim2 = ax.get_ylim()
                ax.text(0.95 * fitx[0] + 0.05 * fitx[-1], 0.1 * ylim1 + 0.9 * ylim2,
                        'X = {:4d}'.format(x))
                ax.axvline(x=0, c='k', ls='--', lw=0.5)
                ax.set_ylim(ylim1, ylim2)
                ax.set_xlim(fitx[0], fitx[-1])
                if iax == (nrow * ncol - 1) or x == nx - 1:
                    figname = 'fit_{:s}_{:04d}.png'.format(
                        logitem['fileid'], x)
                    figfilename = os.path.join('images/tmp/', figname)
                    fig.savefig(figfilename)
                    plt.close(fig)

            # variance array
            s_lst = 1 / (np.maximum(flux * ccd_gain, 0) + ccd_ron ** 2)
            profile = profile_func(fitx)
            normpro = profile / profile.sum()
            fopt = ((s_lst * normpro * debkg_flux)[mask].sum()) / \
                   ((s_lst * normpro ** 2)[mask].sum())

            bkg_flux = np.repeat(bkgspec[x], y2 - y1)
            bopt = ((s_lst * normpro * bkg_flux)[mask].sum()) / \
                   ((s_lst * normpro ** 2)[mask].sum())
            f_opt_lst.append(fopt)
            b_opt_lst.append(bopt)
        f_opt_lst = np.array(f_opt_lst)
        b_opt_lst = np.array(b_opt_lst)

        spec_opt_dbkg = f_opt_lst
        background_opt = b_opt_lst
        spec_opt = spec_opt_dbkg + background_opt

        # now:
        #                      |      sum       |    optimal
        # ---------------------+----------------+----------------
        # backgroud:           | background_sum | background_opt
        # target + background: | spec_sum       | spec_opt
        # target:              | spec_sum_dbkg  | spec_opt_dbkg

        # save 1d spectra to ascii files
        fname = 'spec_{}.dat'.format(logitem['fileid'])
        spec1d_path = 'onedspec'
        if not os.path.exists(spec1d_path):
            os.mkdir(spec1d_path)
        filename = os.path.join(spec1d_path, fname)
        file1 = open(filename, 'w')
        for w, f1, b1, f2, b2 in zip(
                wave_lst[::-1],
                spec_opt_dbkg[::-1],
                background_opt[::-1],
                spec_sum_dbkg[::-1],
                background_sum[::-1]):
            file1.write('{:9.4f} {:+12.7e} {:+12.7e} {:+12.7e} {:+12.7e}'.format(
                w, f1, b1, f2, b2) + os.linesep)
        file1.close()

        # plot 1d spec and backgrounds
        fig2 = plt.figure(figsize=(9, 6), dpi=300)
        ax21 = fig2.add_axes([0.10, 0.55, 0.85, 0.35])
        ax22 = fig2.add_axes([0.10, 0.10, 0.85, 0.40])
        ax21.plot(wave_lst, spec_opt, color='C0', lw=0.5,
                  alpha=0.9, label='Target + Background')
        ax21.plot(wave_lst, background_opt, color='C1', lw=0.5,
                  alpha=0.9, label='Background')
        ax22.plot(wave_lst, spec_opt_dbkg, color='C3', lw=0.5,
                  alpha=0.9, label='Target')
        for ax in fig2.get_axes():
            ax.grid(True, color='k', alpha=0.4, ls='--', lw=0.5)
            ax.set_axisbelow(True)
            ax.set_xlim(wave_lst.min(), wave_lst.max())
            ax.xaxis.set_major_locator(tck.MultipleLocator(1000))
            ax.xaxis.set_minor_locator(tck.MultipleLocator(100))
        ax21.legend(loc='upper left')
        ax22.legend(loc='upper left')
        ax22.set_xlabel(u'Wavelength (\xc5)')
        title = 'Spectra of {} ({})'.format(logitem['fileid'], logitem['object'])
        fig2.suptitle(title)
        figname = 'spec_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        fig2.savefig(figfilename)
        plt.close(fig2)

        # make a plot of comparison of sum extraction and optimal extraction
        fig3 = plt.figure(figsize=(9, 6), dpi=300)
        ax31 = fig3.add_axes([0.10, 0.10, 0.85, 0.8])
        ax31.plot(wave_lst, spec_sum, color='C1', lw=0.5, alpha=0.9,
                  label='Sum Extraction')
        ax31.plot(wave_lst, spec_opt, color='C0', lw=0.5, alpha=0.9,
                  label='Optimal Extraction')
        ax31.grid(True, ls='--', lw=0.5)
        ax31.set_axisbelow(True)
        ax31.set_xlim(wave_lst.min(), wave_lst.max())
        ax31.set_xlabel(u'Wavelength (\xc5)')
        ax31.set_ylabel(u'Count')
        ax31.xaxis.set_major_locator(tck.MultipleLocator(1000))
        ax31.xaxis.set_minor_locator(tck.MultipleLocator(100))
        ax31.legend(loc='upper left')
        title = 'Extraction Comparison of {} ({})'.format(
            logitem['fileid'], logitem['object'])
        fig3.suptitle(title)
        figname = 'extcomp_{}.png'.format(logitem['fileid'])
        figfilename = os.path.join(figpath, figname)
        fig3.savefig(figfilename)
        plt.close(fig3)
    exit()
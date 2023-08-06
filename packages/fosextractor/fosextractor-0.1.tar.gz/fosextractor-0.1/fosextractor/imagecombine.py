#!/usr/bin/env python3
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
def partone():
    # config table

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

    # load obslog table
    logtable = load_obslog()

    # check if figpath exists
    if not os.path.exists(figpath):
        os.mkdir(figpath)

    ############################ combine bias ##############################
    if os.path.exists(bias_file):
        bias_data = fits.getdata(bias_file)
        print('Load bias from', bias_file)
    else:
        print('Combine Bias')
        data_lst = []
        for logitem in logtable:
            if logitem['object'] == 'Bias':
                filename = os.path.join('rawdata', logitem['fileid'] + '.fit')
                data = fits.getdata(filename)
                data_lst.append(data)
        data_lst = np.array(data_lst)

        bias_data = combine_images(data_lst, mode='mean',
                                   upper_clip=5, maxiter=10, maskmode='max')

        fits.writeto(bias_file, bias_data, overwrite=True)

    if plot_bias:
        bias_fig = Figure2D(data=bias_data, scale=(5, 95), title=bias_file)
        figfilename = os.path.join(figpath, 'bias.png')
        bias_fig.savefig(figfilename)

    ############################ combine flat ##############################
    if os.path.exists(flat_file):
        hdu_lst = fits.open(flat_file)
        flat_data = hdu_lst[0].data
        flat_sens = hdu_lst[1].data
        hdu_lst.close()
        print('Load flat from', flat_file)
    else:
        print('Combine Flats')
        data_lst = []
        for logitem in logtable:
            if logitem['object'] == 'Flat':
                t = logitem['dateobs'].datetime
                fileid = '{:04d}{:02d}{:02d}-{:04d}'.format(
                    t.year, t.month, t.day, logitem['frameid'])
                print(fileid)
                filename = os.path.join('rawdata', fileid + '.fit')
                data = fits.getdata(filename)
                data = data - bias_data
                data_lst.append(data)
        data_lst = np.array(data_lst)

        flat_data = combine_images(data_lst, mode='mean',
                                   upper_clip=5, maxiter=10, maskmode='max')

        ny, nx = flat_data.shape
        allx = np.arange(nx)

        flat_sens = np.ones_like(flat_data, dtype=np.float64)
        for y in np.arange(ny):
            flat1d = flat_data[y, 20:]
            flat1d_sm, _, mask, std = iterative_savgol_filter(flat1d,
                                                              winlen=51, order=3,
                                                              upper_clip=3, lower_clip=3, maxiter=10)
            flat_sens[y, 20:] = flat1d / flat1d_sm

        hdu_lst = fits.HDUList([fits.PrimaryHDU(data=flat_data),
                                fits.ImageHDU(data=flat_sens),
                                ])
        hdu_lst.writeto(flat_file, overwrite=True)

    if plot_flat:
        flat_fig = Figure2D(data=flat_sens, scale=(5, 95), title=flat_file)
        figfilename = os.path.join(figpath, 'flat.png')
        flat_fig.savefig(figfilename)
    exit()
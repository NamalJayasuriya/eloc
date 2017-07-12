import pylab as pl
from scipy import signal
from scipy import fftpack
import numpy as np


def plotSpec(d1,d2,fs):
    ln1=len(d1)
    ln2=len(d2)
    fs =fs*1.0
    time_s=ln1/fs

    pl.subplot(321)
    pl.plot(d1)
    pl.subplot(322)
    pl.plot(d2)

    pl.subplot(323)
    pxx, freq, t, cax = pl.specgram(d1, Fs=fs)
    pl.subplot(324)
    pxx, freq, t, cax = pl.specgram(d2, Fs=fs)

    pl.subplot(325)
    yf = fftpack.fft(d1)
    xf = fftpack.fftfreq(ln1, 1 / fs)
    yf = 2.0 / ln1 * np.abs(yf[0:ln1 / 2])
    pl.plot(xf[1:int(100 * time_s)], yf[1:int(100 * time_s)])
    pl.subplot(326)
    yf = fftpack.fft(d2)
    xf = fftpack.fftfreq(ln2, 1 / fs)
    yf = 2.0 / ln2 * np.abs(yf[0:ln2 / 2])
    pl.plot(xf[1:int(100 * time_s)], yf[1:int(100 * time_s)])
    pl.show()


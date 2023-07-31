#!/usr/bin/python3

import numpy as np
import sys
import re
import h5py
import matplotlib.pyplot as plt

def anticorrwin(x):
    return -3.0*x + 0.0010
def corrwin(x):
    return 5.*x + 0.0005

def main(fname):
    data = np.loadtxt(fname)
    ch1 = data[:,2]
    ch2 = data[:,6]
    stage = data[:,9]
    cinds = np.where((np.abs(ch2 - corrwin(ch1)))<.0001)
    ainds = np.where((np.abs(ch2 - anticorrwin(ch1)))<.00005)
    x = np.linspace(np.min(ch1),np.max(ch1),10)
    fig = plt.figure(figsize=(12,16))
    plt.plot(ch1,ch2,'.')
    #plt.plot(ch1[cinds],ch2[cinds],'.')
    #plt.plot(ch1[ainds],ch2[ainds],'.')
    plt.xlabel('channel 1')
    plt.ylabel('channel 2')
    plt.legend(['data','corwin','antiwin'])
    plt.savefig('./figures/data_selection.png')
    cfig = plt.figure(figsize=(16,12))
    plt.plot(stage[cinds],ch1[cinds],'.')
    plt.plot(stage[cinds],ch2[cinds],'.')
    plt.legend(['channel 1','channel 2'])
    plt.xlabel('stage position')
    plt.ylabel('signal')
    plt.savefig('./figures/sigVstage_correlated.png')
    afig = plt.figure(figsize=(16,12))
    plt.plot(stage[cinds],ch1[cinds],'.')
    plt.plot(stage[ainds],ch1[ainds],'.')
    plt.plot(stage[cinds],ch2[cinds],'.')
    plt.plot(stage[ainds],ch2[ainds],'.')
    plt.legend(['channel 1 corr','channel 1 anti','channel 2 corr','channel 2 anti'])
    plt.xlabel('stage position')
    plt.ylabel('signal')
    plt.savefig('./figures/sigVstage_corranti.png')
    icfig = plt.figure(figsize=(16,12))
    plt.plot(np.squeeze(cinds),ch1[cinds],'.')
    plt.plot(np.squeeze(cinds),ch2[cinds],'.')
    plt.legend(['channel 1','channel 2'])
    plt.xlabel('data index' )
    plt.ylabel('signal')
    plt.savefig('./figures/sigVindex_correlated.png')
    iafig = plt.figure(figsize=(16,12))
    #plt.plot(np.squeeze(cinds),ch1[cinds],'.')
    plt.plot(np.squeeze(ainds),ch1[ainds],'.')
    #plt.plot(np.squeeze(cinds),ch2[cinds],'.')
    plt.plot(np.squeeze(ainds),ch2[ainds],'.')
    plt.legend(['channel 1 anti','channel 2 anti'])
    #plt.legend(['channel 1 corr','channel 1 anti','channel 2 corr','channel 2 anti'])
    plt.xlabel('data index')
    plt.ylabel('signal')
    plt.savefig('./figures/sigVindex_corr_anti.png')
    plt.show()

    return

if __name__ == '__main__':
    if len(sys.argv)>1:
        fname = sys.argv[1]
        main(fname)
    else:
        print('extract_correlation.py <fname>')

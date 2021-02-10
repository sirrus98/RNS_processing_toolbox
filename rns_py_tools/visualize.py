#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualization
(RNS Processing Toolbox)

Functions in this file: 
    vis_event(AllData, AllTime, Ecog_Events, datapoints)
    
"""
import matplotlib.pyplot as plt
import numpy as np
from rns_py_tools import conversion as cnv

def vis_event(AllData, AllTime, Ecog_Events, datapoints):
    
    dlen = len(datapoints)
    
    # If datapoints are indices
    start= Ecog_Events['Event Start idx']
    end= Ecog_Events['Event End idx']
    
    ievent = [np.argmax(np.where((start-datapoints[i])<0)) for i in range(0,dlen)]
    
    fig, ax= plt.subplots(dlen,1)
    fig.subplots_adjust(hspace=0.5)    
    
    for i in range(0,dlen):
        idx= ievent[i]
        dt= cnv.posix2dt_UTC(AllTime[start[idx]:end[idx]+1])
        dat = AllData[:,start[idx]:end[idx]+1].T+np.arange(4)*100
        
        ymax = max([i for lis in dat for i in lis])
        ymin = min([i for lis in dat for i in lis])
        
        ax[i].plot(dt, dat)
        ax[i].vlines(cnv.posix2dt_UTC(AllTime[datapoints[i]]),ymin, ymax)
        plt.sca(ax[i])
        plt.xticks(rotation=20)
        plt.title("%s Event"%(Ecog_Events['ECoG trigger'][idx]))
    
    return ax
    
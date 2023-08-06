# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:12:21 2022

@author: filou
"""
import numpy as np


def marge(provenance, destination, t_init, t_final):

    A = np.genfromtxt(provenance)
    temps = A[:,0]
    volt = A[:,1]

    marge_temps = []
    for items in temps:
        if t_init <= items <= t_final:
            marge_temps.append(items)

    index = []
    for items in marge_temps:
        liste = list(temps)
        a = liste.index(items)
        index.append(a)

    marge_volt = []
    for items in index:
        marge_volt.append(volt[items])

    marge_temps_dec = np.subtract(marge_temps, t_init)
    B = np.matrix([marge_temps_dec, marge_volt])
    np.savetxt(destination, np.transpose(B))

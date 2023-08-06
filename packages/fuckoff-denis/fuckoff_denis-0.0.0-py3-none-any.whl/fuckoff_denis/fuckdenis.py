# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:04:24 2022

@author: filou
"""

import numpy as np


def save(provenance, destination):
    t = donnee_brute(provenance)[0::2]
    v = donnee_brute(provenance)[1::2]
    np.savetxt(destination, np.transpose([t, v]))


def donnee_brute(nom_fichier):
    file = open(nom_fichier)
    a = file.read().split(",")
    b = []
    for item in a:
        try:
            b.append(float(item))
        except ValueError:
            pass
    return b

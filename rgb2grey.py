# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:08:20 2019

@author: Himanshu
"""
import numpy as np

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.21 , 0.72, 0.07])
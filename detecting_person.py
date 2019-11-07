# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:58:51 2019

@author: Himanshu
"""
import torch
from data import BaseTransform
from ssd import build_ssd
from imageio import get_reader as gr
from detect import detect
from itertools import chain
import numpy as np
from rgb2grey import rgb2grey
from cnn import cnn
from glob import glob
import matplotlib.pyplot as plt
import cv2


# Creating the SSD neural network
net = build_ssd('test')
net.load_state_dict(torch.load('ssd300_mAP_77.43_v2.pth', map_location = lambda storage, loc: storage))

# Creating the transformation
transform = BaseTransform(net.size, (104/256.0, 117/256.0, 123/256.0))


reader = gr('fi1_xvid.avi')
#mat = cv2.imread('BoardingPass_MyNameOnMars2020.png')

#gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)

thing = []
for i, frame in enumerate(reader):
    thing.append(detect(frame, net.eval(), transform))
    print(i)

flatten_list = list(chain.from_iterable(thing))
count = flatten_list.count('person') / len(thing) > .5
del(thing)
del(flatten_list)
del(frame)
'''
if(count):
    mat = np.array(list(reader))
    grey_video = np.zeros(shape = [mat.shape[0],mat.shape[1],mat.shape[2]])
    for i in range(mat.shape[0]):
        grey_video[i] = rgb2grey(mat[i])
        
shape = mat.shape
mat = mat[np.newaxis, ...].shape
'''
# Reading videos
img_mask = 'Dataset\\fights\*.avi'
fights_file_name = glob(img_mask)
for i in range(len(fights_file_name)):
    fights_file_name[i] = fights_file_name[i][15:]

img_mask = 'Dataset\\noFights\*.mpg'
no_fights_file_name = glob(img_mask)
for i in range(len(no_fights_file_name)):
    no_fights_file_name[i] = no_fights_file_name[1][18:]
    
del(img_mask)
#del(i)

fights = np.zeros(shape = [4,42, 576, 720, 3])

for i, name in enumerate(fights_file_name):
    video = np.array(list(gr(name)))
    print(video.shape)
    fights[i] = video[:42,:,:,:]
    if i == 3:
        break





arch = cnn(shape[0],shape[3],shape[1],shape[2])
arch.fit(x,steps_per_epoch = 2, epochs = 100, verbose = 1)

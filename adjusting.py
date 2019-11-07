# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:07:00 2019

@author: Himanshu
"""

import cv2
from glob import glob

# Reading videos
img_mask = 'Dataset\\fights\*.avi'
fights_file_name = glob(img_mask)
img_mask = 'Dataset\\noFights\*.mpg'
no_fights_file_name = glob(img_mask)


vidcap = cv2.VideoCapture('myvid2.mp4')
success,image = vidcap.read()

while success:
  success,image = vidcap.read()
  height , width , layers =  image.shape
  new_h=height/2
  new_w=width/2
  resize = cv2.resize(image, (new_w, new_h)) 
  cv2.imwrite("%03d.jpg" % count, resize) 
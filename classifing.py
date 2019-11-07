# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:58:51 2019

@author: Himanshu
"""
import torch
from data import BaseTransform
from ssd import build_ssd
from imageio import get_reader as gr
from detect_person import detect
from itertools import chain
from glob import glob
from adjusting import adjust
from joblib import load
classifier = load('classifier.joblib')


# Creating the SSD neural network
net = build_ssd('test')
net.load_state_dict(torch.load('ssd300_mAP_77.43_v2.pth', map_location = lambda storage, loc: storage))

# Creating the transformation
transform = BaseTransform(net.size, (104/256.0, 117/256.0, 123/256.0))
reader = 'To be filled later'
thing = []
for i, frame in enumerate(gr(reader)):
    thing.append(detect(frame, net.eval(), transform))

flatten_list = list(chain.from_iterable(thing))
count = flatten_list.count('person') / len(thing) > .5
del(thing)
del(flatten_list)
del(frame)

if(count): #Person is detected in the video
    test = adjust('Path')
    check = classifier.predict(test)
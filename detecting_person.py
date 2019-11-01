# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:58:51 2019

@author: Himanshu
"""

import torch
from torch.autograd import Variable
from data import BaseTransform, VOC_CLASSES as labelmap
from ssd import build_ssd
import imageio

# Defining a function that will do the detections
def detect(frame, net, transform):
    height, width = frame.shape[:2]
    frame_t = transform(frame)[0]
    x = torch.from_numpy(frame_t).permute(2, 0, 1)
    x = Variable(x.unsqueeze(0))
    y = net(x).cuda()
    detections = y.data
    ans = []
    for i in range(detections.size(1)):
        j = 0
        while detections[0, i, j, 0] >= 0.7:
            j += 1
            print(labelmap[i - 1])
            ans.append(labelmap[i - 1])
    return ans

# Creating the SSD neural network
net = build_ssd('test')
net.load_state_dict(torch.load('ssd300_mAP_77.43_v2.pth', map_location = lambda storage, loc: storage))

# Creating the transformation
transform = BaseTransform(net.size, (104/256.0, 117/256.0, 123/256.0))


reader = imageio.get_reader('fi1_xvid.avi')

thing = []
for i, frame in enumerate(reader):
    thing.append(detect(frame, net.eval(), transform))
    print(i)

for

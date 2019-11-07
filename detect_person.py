# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:06:03 2019

@author: Himanshu
"""

import torch
from torch.autograd import Variable
from data import VOC_CLASSES as labelmap

# function that will do the detections
def detect(frame, net, transform):
    #height, width = frame.shape[:2]
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
            ans.append(labelmap[i - 1])
    return ans
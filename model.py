# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:48:50 2019

@author: Himanshu
"""
from glob import glob
from adjusting import adjust, dataset
from cnnlstm import cnnlstm
from joblib import dump


# Training/nofights
img_mask = 'Dataset/Training/noFights/*.mpg'
names = glob(img_mask)
train_nofights = adjust(names)
# Training/fights
img_mask = 'Dataset/Training/fights/*.avi'
names = glob(img_mask)
train_fights = adjust(names)
# dataset(fights, nofights)
data = dataset(train_fights, train_nofights)
train, target = data[0], data[1]


del(names, img_mask, data, train_nofights, train_fights)

# Architecture of cnnlstm
arch = cnnlstm(40, 1, 64, 64)

# Fitting the model
arch.fit(train, target, batch_size = 4, epochs = 100, verbose = 1)

# Saving the weights
dump(arch, 'classifier.joblib')
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:07:00 2019

@author: Himanshu
"""
'''Functions of this:
1. This file converts the video into gray
2. Then resize it to 288 * 350 pixels and 40 frames
'''

import cv2
import numpy as np


def adjust(names):
    new_image = np.zeros(shape = [len(names),40, 64, 64])
    new_h = 64
    new_w = 64
    for it, name in enumerate(names):
        vidcap = cv2.VideoCapture(name)
        i = j = 0
        while True:
            success,image = vidcap.read()
            if 0<=i<40:
                image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                resize = cv2.resize(image, (new_w, new_h))
                new_image[it,j] = resize
                j = j + 1
            elif i >40:
                break
            i = i + 1
    return new_image

def dataset(fights, nofights):
    limit = fights.shape[0] + nofights.shape[0]
    target = np.zeros(shape = (limit,1))
    data = np.zeros(shape = [limit, 40, 64, 64])
    count1 = count2 = 0
    for i in range(limit):
        if count1 < fights.shape[0] and count2 < nofights.shape[0]:
            group = np.random.randint(1,3)
            which = np.random.randint(0,min(fights.shape[0], nofights.shape[0]))
            if group == 1:
                data[i] = fights[which]
                count1 = count1 + 1
                fights = np.delete(fights, which, 0)
                target[i] = 1
            else:
                data[i] = nofights[which]
                count2 = count2 + 1
                nofights = np.delete(nofights, which, 0)
                target[i] = 0
        elif nofights.shape[0]:
            data = np.append(data, nofights, axis = 0)
            target = np.append(target, np.zeros(shape = (nofights.shape[0], 1)))
            break
        else:
            data = np.append(data, fights, axis = 0)
            target = np.append(target, np.ones(shape = (fights.shape[0], 1)))
            break
    
    data = np.reshape(data, (data.shape[0], 40, 1, 64, 64))
    
    return [data, target]

'''
# Testing/fights
img_mask = 'Dataset/Testing/fights/*.avi'
names = glob(img_mask)
test_fights = np.zeros(shape = [len(names),40, 288, 360])
new_h = 288
new_w = 360
for it, name in enumerate(names):
    x = names
    vidcap = cv2.VideoCapture(name)
    i = j = 0
    while success:
        success,image = vidcap.read()
        if 0<=i<40:
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            resize = cv2.resize(image, (new_w, new_h)) 
            plt.imshow(resize)
            print(i)
            test_fights[it,j] = resize
            j = j + 1
        elif i >40:
            break
        i = i + 1'''
        
'''creating target variable
    target = np.zeros(shape = (161,1))
    train = np.zeros(shape = [161, 40, 64, 64])
    count1 = count2 = 0
    for i in range(161):
        if count1 < 80 and count2 < 81:
            group = np.random.randint(1,3)
            which = np.random.randint(0,min(train_fights.shape[0], train_nofights.shape[0]))
            if group == 1:
                train[i] = train_fights[which]
                count1 = count1 + 1
                train_fights = np.delete(train_fights, which, 0)
                target[i] = 1
            else:
                train[i] = train_nofights[which]
                count2 = count2 + 1
                train_nofights = np.delete(train_nofights, which, 0)
                target[i] = 0
        elif train_nofights.shape[0]:
            train = np.append(train, train_nofights, axis = 0)
            target = np.append(target, np.zeros(shape = (train_nofights.shape[0], 1)))
            break
        else:
            train = np.append(train, train_fights, axis = 0)
            target = np.append(target, np.ones(shape = (train_fights.shape[0], 1)))
            break
        
    del(train_fights)
    del(train_nofights)
    train = np.reshape(train, (train.shape[0], 40, 1, 64, 64))
    '''
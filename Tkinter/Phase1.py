# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:38:37 2019

@author: Hitesh
"""

from tkinter import *
from tkinter import filedialog
from adjusting import single
from joblib import load
classifier = load('classifier.joblib')
root = Tk()
def get_Path():
    global file_path
    file_path = filedialog.askopenfilename()
    print('Selected:', file_path)
    fileAddress.insert(0,file_path);

def run():
    #Person is detected in the video 1- violence 0- no
    global check
    test = single(file_path)
    check = classifier.predict(test)
    print(int(check))

fileFrame = Frame(root)
fileAddress = Entry(fileFrame,selectborderwidth= '20px',bg = 'black' , fg = 'white' )
fileButton = Button(fileFrame , text = 'Select Address',command = get_Path)
analysisButton = Button(fileFrame , text = 'Perform Analysis', command = run)
fileAddress.insert(0,file_path);
fileAddress.pack()
fileButton.pack()
analysisButton.pack()
fileFrame.pack()

root.mainloop()


# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:38:37 2019

@author: Hitesh
"""

from tkinter import *
from tkinter import filedialog
root = Tk()
global file_path
file_path = 'Not Path Selected'
def get_Path():
    file_path = filedialog.askopenfilename()
    print('Selected:', file_path)
    fileAddress.insert(0,file_path);


fileFrame = Frame(root)
fileAddress = Entry(fileFrame,selectborderwidth= '20px',bg = 'black' , fg = 'white' )
fileButton = Button(fileFrame , text = 'Select Address',command = get_Path)
analysisButton = Button(fileFrame , text = 'Perform Analysis')
fileAddress.insert(0,file_path);
fileAddress.pack()
fileButton.pack()
analysisButton.pack()
fileFrame.pack()

root.mainloop()


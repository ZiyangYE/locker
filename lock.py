# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:27:48 2020

@author: Thermit
"""
import sys
import os
import usb.core
import ctypes
from time import sleep


while True:
    a=sys.stdout
    b=sys.stderr
    sys.stderr = os.devnull 
    sys.stdout = os.devnull 
    exist=0
    try:
        dev = usb.core.find(idProduct=4776)
        for i in dev:
            exist=1
            break
        dev=0
        i=0
    except:
        pass
    sys.stdout=a
    sys.stderr=b
    #print(exist)
    if(exist==0):
        #begin func
        ctypes.WinDLL('user32.dll').LockWorkStation()
        #end func
    sleep(0.5)
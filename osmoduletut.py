# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:49:55 2018

@author: Raunak
"""

import os
import time


curDir = os.getcwd()

print(curDir)

os.mkdir('newDir')

time.sleep(2)

os.rename('newDir', 'newDir2')

time.sleep(2)

os.rmdir('newDir2')
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:13:22 2018

@author: Raunak
"""

import time

import datetime as dt

import numpy as np

print(time.time())

example = time.time()

print(example)


print(dt.datetime.fromtimestamp(example))


dateconv = np.vectorize(dt.datetime.fromtimestamp)


print(dateconv(example))
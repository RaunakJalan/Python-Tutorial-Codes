# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:56:36 2018

@author: Raunak
"""

import sys


sys.stderr.write('This is stderr text\n')
sys.stderr.flush()

sys.stdout.write('This is stdout text\n')

print(sys.argv)


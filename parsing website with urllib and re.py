# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 03:16:25 2018

@author: Raunak
"""

import urllib.request as ur
import urllib.parse as up
import re

url = 'http://pythonprogramming.net'

values = {'s':'basics',
          'submit':'search'}

data = up.urlencode(values)

data = data.encode('utf-8')

req = ur.Request(url, data)

resp = ur.urlopen(req)

respData = resp.read()

print(respData)

'.*? means to find everything between given tags i.e. <p> and </p>'

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)
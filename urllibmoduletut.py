# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 01:37:30 2018

@author: Raunak
"""

import urllib.request as ur
import urllib.parse as up


#x = ur.urlopen('https://www.google.com')

#print(x.read())
'''

url = 'http://pythonprogramming.net'

values = {'s' : 'basic',
       'submit' : 'search'}


data = up.urlencode(values)

data = data.encode('utf-8')

req = ur.Request(url, data)
resp = ur.urlopen(req)

respData = resp.read()

print(respData)
'''

#BYPASSING if BLOCKED by SITE


try:
    x = ur.urlopen('https://www.google.com/search?q=test')
    
    print(x.read())
    
except Exception as e:
    print(str(e))
    
try:
    url = 'https://www.google.com/search?q=test'
    
    headers = {}
    
    #useing user agent in data sent to google
    
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    
    req = ur.Request(url, headers = headers)
    
    resp = ur.urlopen(req)
    
    respData = resp.read()
    
    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
    
    
except Exception as e:
    print(str(e))
    
    


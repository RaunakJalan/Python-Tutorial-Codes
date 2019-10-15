# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 02:44:05 2018

@author: Raunak
"""

'''

IDENTIFIERS: 
    
    \d: any number
    \D: anything but a number
    \s: space
    \S: anything but a space
    \w: any character
    \W: anything but a character
    . : any character, except a new line
    \b: the white space around words
    \.: a period
    
MODIFIERS:
    
    {1,3}: we're expecting 1-3
    +    : match 1 or more
    ?    : match 0 or 1
    *    : match 0 or more
    $    : match the end of a string
    ^    : matching the beginning of a string
    |    : either or
    []   : range or "variance"
    {x}  : expecting "x" amount
    
WHITE SPACE CHARACTERS:
    
    \n: new line
    \s: space
    \t: tab
    \e: escape
    \f: form feed
    \r: return
    
DON'T FORGET:
    
    .
    +
    *
    ?
    [ ]
    $
    ^
    ( )
    { }
    |
    \
    

'''


import re


'''
 __________________________________________
|                |                         |
|   Modifier     |      DESCRIPTION        |
|________________|_________________________|
|                |                         |
|    re.I        |  Ignore case matching.  |
|________________|_________________________|
|                |                         |
|                |Make $ match the end of  |
|    re.M        |line and ^ at start of   |
|                |line.                    |
|________________|_________________________|
|                |                         |
|                |Make .(dot) match any    |
|    re.S        |character even the new   |
|                |line character.          |         
|________________|_________________________|
|                |                         |
|    re.U        |Interprets in Unicode.   |
|________________|_________________________|
|                |                         |
|                |Ignores whitespace with- |
|    re.X        |in the pattern.          |
|                |                         |
|________________|_________________________|


'''

exampleString = '''
                Jessica is 15 years old, and Daniel is 27 years old.
                Edward is 47, and his grandfather, Oscar, is 102.
                '''
                
ages = re.findall('\d{1,3}', exampleString)
names = re.findall('[A-Z][a-z]*', exampleString)

print(ages)
print(names)


ageDict = {}

x = 0

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)




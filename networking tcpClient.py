# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 04:22:50 2018

@author: Raunak
"""

import socket



def main():
    
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    
    s.connect((host, port))
    
    message = input("-> ")
    
    while message!= 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Recieved from server: " + data)
        message = input("-> ")
        
    s.close()
    

if __name__ == "__main__":
    
    main()
    
    
    
    
    
    
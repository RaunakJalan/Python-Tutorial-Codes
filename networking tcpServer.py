# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 04:17:34 2018

@author: Raunak
"""

import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    
    s.bind((host, port))
    
    s.listen(1)
    
    #accepting the connection using socket object of client
    c, addr = s.accept()
    print("Connection from: "+str(addr))
    
    while True:
        
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        
        print("From connected user: "+ data)
        
        data = data.upper()
        print("Sending: "+ data)
        
        c.send(data.encode('utf-8'))
        
    
    c.close()
    

if __name__ == "__main__":
    main()
        
        
        
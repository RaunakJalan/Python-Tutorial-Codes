# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 03:28:21 2018

@author: Raunak
"""

import socket

def main():
    
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind((host, port))
    
    print("SERVER STARTED")
        
    while True:
        
        data, addr = s.recvfrom(1024)
        
        data = data.decode('utf-8')
        print("Message From: " +str(addr))
        print("From Connected User: "+ data)
        data = data.upper()
        print("Sending: "+data)
        s.sendto(data.encode('utf-8'),addr)
    
    s.close()
        
        
if __name__ == "__main__":
    main()       

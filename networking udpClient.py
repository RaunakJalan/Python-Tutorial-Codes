# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 03:28:24 2018

@author: Raunak
"""

import socket

def main():
    
    host = '127.0.0.1'
    port = 8888
    
    server = ('127.0.0.1', 5000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind((host, port))
    
    message = input("-> ")
    
    while message != 'q':
        
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recieve From Server: "+data)
        message = input("-> ")
        
    s.close()
    
    
    
    
    
if __name__ == "__main__":
    main()
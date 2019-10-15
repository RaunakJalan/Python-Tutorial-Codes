# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 02:41:49 2018

@author: Raunak
"""

'''

SOCKET METHODS:
    
    1. socket(socket_family, socket_type)
        
        ->The Constructor creates a new socket
    
    2. bind((hostname, port))
    
        ->Bind takes a tuple of a host address and port
        
    3. listen()
    
        ->Starts listening for TCP connections
        
    4. accept()
    
        ->Accepts a connection when found.
        (returns new socket)

    5. connect((hostname, port))
    
        ->Takes a tuple of a host address and port
        
    6. recv(buffer)
    
        ->Tries to grab data from a TCP connection.(waits)
          The buffer size determines how many bytes of 
          data to recieve at a time
          
    7. send(bytes)
        
        ->attempts to send the bytes given to it
        
    8. close()
    
        ->Closes a socket/connection and frees the port
        
    
    


'''
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:33:32 2018

@author: Raunak
"""

import argparse


def fibo(n):
    
    a, b = 0, 1
    for i in range(n):
        
        a, b = b, a+b
        
    return a

def main():
    
    parser = argparse.ArgumentParser()
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action = "store_true")
    group.add_argument("-q", "--quiet", action = "store_true")    
    parser.add_argument("num",
                        help = "The fibonacci number you wish to calculate", 
                        type = int)
    
    #arg to save output to file
    parser.add_argument("-o", "--output",
                        help = "Output result to a file.",
                        action = "store_true")
    
    #mutually exclusive group
    #eg: verbose output or quiet output
    
    
    
    args = parser.parse_args()
    
    result = fibo(args.num)
    
    
    if args.verbose:
    
        print("The "+str(args.num)+"th fibonacci number is "+str(result))

    elif args.quiet:
        print(result)
        
    else:
        print("Fib("+str(args.num)+") = "+str(result))
    
    
    if args.output:
        with open('fibonacci.txt', 'a') as f:
            f.write(str(result)+'\n')
    
    
    
if __name__ == "__main__":
    main()
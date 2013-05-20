#!/usr/bin/env python

import math

def main() :
  mult = 1
  for i in range(1,20) :
    a = gcd(mult,i)
    if a == 0 :
      a = 1
    mult = mult*(i/a)
  print(mult)  
         
def gcd(a,b):
        if b == 0:
                return a
        else:
                return gcd(b, (a%b))      
      
if __name__ == "__main__" :
  main()   

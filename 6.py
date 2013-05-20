#!/usr/bin/env python

import math

def main() :
  a = 0
  b = 0
  for i in range(1,101) :
    a = a + i
    b = b + i*i
  a = a*a
  print (a - b)           
      
if __name__ == "__main__" :
  main()   

#!/usr/bin/env python

import math


def main() :
  a = 0
  for i in range(1000) :
    for j in range (1000) :
      n = i*j
      if pal(n) > a :
	a = pal(n)
  print(a)	
         
def pal(num) :
   a = num
   rev = 0
   while num > 0 :
     dig = num % 10
     rev = rev * 10 + dig
     num = num / 10;
   if  a == rev :
     return a
   else :
    return 0
    
       
if __name__ == "__main__" :
  main()  
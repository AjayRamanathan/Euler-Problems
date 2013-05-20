#!/usr/bin/env python

import math


def main() :

 for a in range (1,1000) :
   for b in range (1,1000) :
    for c in range (1,1000) :
      if a+b+c == 1000 :
	if a*a + b*b == c*c :
	  print a*b*c
      	     
if __name__ == "__main__" :
  main()  
 


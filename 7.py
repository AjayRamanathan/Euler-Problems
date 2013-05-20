#!/usr/bin/env python

import math

def main() :
  print nthprime(100001)      

def nthprime(n):
         counter = 1
	if n==1: 
	  return 2
	elif n<1: 
	  return None
	prime = 2
	while counter <= n :
	  while 1:
	    a = 2
	    s=range(3,a+1,2)
	    counter = 1
	    root = a ** 0.5
	    half=(a+1)/2-1
	    i=0
	    r=3
	    while r <= root:
		if s[i]:
			j=(r*r-3)/2
			s[j]=0
			counter = counter +1
			while j<half:
				s[j]=0
				j+=r
			        counter = counter +1
	        i=i+1
		r=2*i+3
	  if counter == n :
	    break
		
	return a
      
if __name__ == "__main__" :
  main()  
 


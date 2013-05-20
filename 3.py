#!/usr/bin/env python

import math

def main() :
  prime = 0
  num = 600851475143
  num2 = math.sqrt(600851475143)
  for i in primes(int(num2)) :
    if num%i == 0 :
      prime = i

  print prime      

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	root = n ** 0.5
	half=(n+1)/2-1
	i=0
	r=3
	while r <= root:
		if s[i]:
			j=(r*r-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=r
		i=i+1
		r=2*i+3
	return [2]+[x for x in s if x]
      
if __name__ == "__main__" :
  main()  
 

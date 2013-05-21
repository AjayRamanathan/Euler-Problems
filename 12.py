#!/usr/bin/env python

def main() :
 
  a = 0
  n = 1
  while a <= 500 :
    a = numdiv (nthtri(n))
    print a
  print n
    
def numdiv (n) :
  rem = 0
  a = []
  list1 = primes (n)
  for i in list1 :
    x = 0
    while rem != 0 :
      n = n/i
      x = x + 1
    a.append(x)
  return a


def nthtri(n) :
  x = 0
  for i in range (1, n+1) :
    x = x + i
  return x  

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

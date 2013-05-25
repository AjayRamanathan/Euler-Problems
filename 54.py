#!/usr/bin/env python

def main() :
  n = 100
  list1 = fac(n)
  total = 0
  for i in range(1,101) :
    for x in range(1,i) :
      z = list1[i]/(list1[x]*list1[i-x])
      print z
      if z >= 1000000 :
	total = total +1
  print total
  
def fac(n):
	b = [0,1]
	for i in range(2,n+1): 
		b.append (i*b[i-1])
	return b     
      	     
if __name__ == "__main__" :
  main()  
 



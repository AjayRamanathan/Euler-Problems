#!/usr/bin/env python

def main() :
  l = []
  for a in range(2,101) :
    for b in range (2,101) :
      l.append(a**b)
  x = len(set(l))
  print x
	 	     
if __name__ == "__main__" :
  main()  
 



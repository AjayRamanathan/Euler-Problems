#!/usr/bin/env python
import time

def main() :
  start_time = time.time()
  total = 0
  a = len(factors(2))
  for i in range(2,100000) :
    b = len(factors(i+1))
    if a == b :
      total = total + 1
    a = b  
  print total 
  print time.time() - start_time, "seconds" 


def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
                          	     
if __name__ == "__main__" :
  main() 
 
                
#!/usr/bin/env python
import time

def main() :
  start_time = time.time()
  b = [0]
  n = 10**6
  for i in xrange(1,n+1) :
    total = 0
    a = factors(i)
    for x in list(a) :
      total = total + x*x  
    b.append(total + b[i-1])
  print b[n]
  print time.time() - start_time, "seconds"
def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
      	     
if __name__ == "__main__" :
  main()  
  
 



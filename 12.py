#!/usr/bin/env python

def main() :
 
  a = 0
  n = 1
  while a <= 500 :
    x = tri(n)
    y = factors(x)
    a = len(y)
    n = n +1
  print  x
  
def tri(n) :
  total = 0
  for i in range(1, n+1) :
    total = total + i
  return total  

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

if __name__ == "__main__" :
  main()  

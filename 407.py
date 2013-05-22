#!/usr/bin/env python

import time
''''def main() :
  total = 0
  n = 1
  while n <= 10000 :
    total = total + M(n)
    n = n+1
  print total

def M(n) :
  high = 0
  a = 0
  while a <= n :
    z = (a**2) % n
    a = a+1
    if z > high :
      high = z
    return high '''

def main() :
  start_time = time.time()
  n = 100000
  global list1 
  list1= listsq(n)
  total = 0
  for i in range (1, n+1) :
    total = total + M2(i)
  print total
  print time.time() - start_time, "seconds"

def M2(n) :
  high = 0
  a = 1
  while a <= n :
    z = list1[a] % n
    a = a+1
    if z > high :
      high = z
  return high  
      
def listsq(n) :
  a = []
  b = 0
  while  b <= n :
    a.append(b**2)
    b = b+1
  return a  
      

      	     
if __name__ == "__main__" :
  main()  
  

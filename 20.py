#!/usr/bin/env python

def main() :
  a = factorial(100)
  b = str(a)
  total = 0
  for i in b : 
    total = total + int(i)
  print(total)  
  
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)     
      	     
if __name__ == "__main__" :
  main()  
 


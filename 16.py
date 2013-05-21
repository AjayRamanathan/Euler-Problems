#!/usr/bin/env python

def main() :
  a = 2**1000
  print a
  b = str(a)
  total = 0
  for i in b : 
    total = total + int(i)
  print(total)  
            
if __name__ == "__main__" :
  main()  

#!/usr/bin/env python

def main() :
  total = 0
  for i in range(1,1000001) :
    a = bin(i)[2:]
    c = a[::-1]
    x = str(i)[:: -1]
    if a == c and x == str(i) :
      total = total + i
  print total     
         	     
if __name__ == "__main__" :
  main()   

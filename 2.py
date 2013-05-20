#!/usr/bin/env python

def main() :
  x = 0
  a = 1
  b = 1
  for i in range(100) :
    a = a+b
    b = b+a
    rema = a%2
    remb = b%2
    if rema == 0 :
      x = x + a
    if remb == 0 :
      x = x + b
    if a > 4000000 :
      break
    if b > 4000000 :
      break
  print x
if __name__ == "__main__" :
  main()  

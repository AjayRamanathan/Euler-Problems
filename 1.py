#!/usr/bin/env python

def main() :
  x = 0
  for i in range(1000):
    rem3 = i%3
    rem5 = i%5
    if rem3 == 0:
      x=x+i
    elif rem5 == 0:
      x=x+i
  print(x)               

if __name__ == "__main__" :
  main() 

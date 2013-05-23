#!/usr/bin/env python

def main() :
  a = 2540160
  t = 0
  for i in range(1, a+1) :
    b = checkth(i)
    if b == True :
       t = t + i
  print(t - 3)
  
def checkth(i) :
  c = 0
  for x in str(i) :
    c = c + (fact(int(x)))
  if c == i :
    return True
  else :
    return None

def fact(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 6
  elif n == 4:
    return 24
  elif n == 5:
    return 120
  elif n == 6:
    return 720
  elif n == 7:
    return 5040
  elif n == 8:
    return 40320
  elif n == 9:
    return 362880
  
              
      	     
if __name__ == "__main__" :
  main()   

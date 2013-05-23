#!/usr/bin/env python

def main() :
  a = 4*(9**5)
  print a
  t = 0
  for i in range(1, a+1) :
    b = checkth(i)
    if b == True :
       t = t + i
  print(t - 1)
  
def checkth(i) :
  c = 0
  for x in str(i) :
    c = c + (int(x)**5)
  if c == i :
    return True
  else :
    return None
      	     
if __name__ == "__main__" :
  main()  
 

 

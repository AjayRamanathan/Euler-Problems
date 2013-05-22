#!/usr/bin/env python

def main() :
   
  a = 1
  while 1 :
    z =str(fibonaci(a))
    x = len(z)
    if x >= 1000 :
      break
    else :
      a = a+1
  print x
  print a 

#def fibonaci(n) :
  #if n == 1 :
    #return 1
  #elif n == 2 :
    #return 1
  #else :
    #return (fibonaci(n-1) + fibonaci(n-2))
    
def fibonaci(n) :
  fibValues = [0,1]
  for i in range(2,n+1):
    fibValues.append(fibValues[i-1] + fibValues[i-2])
  return fibValues[n]   
     
if __name__ == "__main__" :
  main()  
  

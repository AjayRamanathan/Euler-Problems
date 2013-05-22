#!/usr/bin/env python

def main() :
   
  #b = []
  b2 = []
  for n in range (0,10) :
    #x = s(n)
    x2 = sv2(n)
    #z = t(x)
    y = t(x2)
    #b.append(int(z))
    b2.append(int(y))
  #print b
  print b2
  
def t(n) :

  a = (n%64) + 1
  return a

#def s(n):
  #if n == 0 :
    #return  290797
  #else :
    #return (s(n-1)*s(n-1)) % 50515093

   
def sv2(n) :
  if n == 0 :
    return  290797
  else :
    sValues = [290797]
    for i in range(1,n+1):
      sValues.append((sValues[i-1]**2) % 50515093)
    return sValues[n]     
      	     
if __name__ == "__main__" :
  main()   

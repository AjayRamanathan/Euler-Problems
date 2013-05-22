#!/usr/bin/env python

def main() :
  print(Spi(5))


def Spi(n) :
  SpiValues = [0,1]
  a = 3
  for i in range(2,n/2) :
    SpiValues.append(SpiValues[i-1] + 2*a -2)
    SpiValues.append(SpiValues[i-1] + 4*a -4)    
    a = a+2  
  return SpiValues[n/2 -1]
        	     
if __name__ == "__main__" :
  main()  
 

 

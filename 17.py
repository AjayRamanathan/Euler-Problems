#!/usr/bin/env python
# could do it with a calculator duh !
#sum from 1 to 10

def main() :
  sum10 =  3+3+5+4+4+3+5+5+4
  sum20 = 3+6+6+8+8+7+7+9+8+8
  sum100 =  10*(6+6+5+5+5+7+6+6) + 8*sum10
  print sum10 
  print sum20 
  print sum100
  sum1000 = sum10*100 + 9*(sum10 + sum20 + sum100) + 7*9 + 10*9*99
  print sum1000
  sum1001 = sum1000 + 8 + 3 + sum10 + sum20 + sum100
  print sum1001
      	     
if __name__ == "__main__" :
  main()  
 


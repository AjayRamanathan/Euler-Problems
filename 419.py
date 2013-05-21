#!/usr/bin/env python

def main() :
  a = '111221'
  print(digpart(a))
    
def digpart(a) :
  
  b = []
  length = len(a)
  x = a[:1]
  counter = 0
  j = 1
  for i in a :
    if i == x :
      counter = counter + 1
    else :
      b.append(counter)
      b.append(int(x))
      counter = 0
      x = a[:j-1]
      counter = 1
    j = j+1
    if counter == 0 :
      continue
    elif j == length+1 :
      b.append(counter)
      b.append(int(x))
  str1 = ''.join(str(e) for e in b)
  return str1
    
	
	
if __name__ == "__main__" :
  main()  
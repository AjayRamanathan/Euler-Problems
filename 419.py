#!/usr/bin/env python

def main() :
  
  a = '1'
  i = 1
  n = 40
  #n = 10**12
  print n
  while i < n :
    a = digpart(a)
    i = i +1 
  print(abc(a)) 
    
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
      x = a[j-1:j]
      counter = 1
    j = j+1
    if j == length+1 :
      b.append(counter)
      b.append(int(x))
  str1 = ''.join(str(e) for e in b)
  return str1

def abc(a) :
  a1 = 0 
  b1 = 0
  c1 = 0
  for i in a :
    if i == '1':
      a1 = a1 + 1
    elif i == '2':
      b1 = b1 + 1
    elif i == '3':
      c1 = c1 + 1
  ex = [a1, b1, c1] 
  return ex

	
if __name__ == "__main__" :
  main()  
#!/bin/env python
import re 

def check(floatnum):
  floatcheck=re.compile(r'^[\s+-]?(\d*\.?\d+)$')
  intcheck=re.compile(r'^[\s+-]?\d+$')
  #floatcheck = '[+-]?[0-9]+\.[0-9]+'
  #intcheck = '[+-]?[0-9]+'
  if intcheck.match(floatnum):
    return(int(floatnum))
  elif floatcheck.match(floatnum):  
    return(float(floatnum))        
  else:  
    return('nonfloat')  

def zerocheck(a,b):
  if b==0.0:
    myerror='ERROR'
  else:
    myerror='ok'
  return(myerror)

def operate(a,b,op):
  intcheck=re.compile(r'^[\s+-]?(\d*\.?[0]*)$')
  if op=='plus':
    num=a+b
  elif op=='minus':
    num=a-b
  elif op=='multiply':
    num=a*b
  elif op =='divide':
    if zerocheck(a,b) == ('ERROR'):
      num='DIVIDE BY 0. TRY AGAIN'
    else:
      num=float(a)/float(b)
      if intcheck.match(str(num)):
        num=int(num)
      else:
        num=float(num)
  else:
    num='PLEASE ENTER AN OPERATION' 
  return(num)

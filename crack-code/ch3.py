#!/usr/bin/python

def hanoi(n, start, middle, target):
  """hanoi puzzle"""
  if n>0:
    hanoi(n-1, start, middle, target)
    if start:
      item = start.pop()
      target.append(item)
    hanoi(n-1, middle, start, target)

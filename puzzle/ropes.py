#!/usr/bin/python

#Assume you have some number of ropes of varying length.
#For example:     2 ft,   5 ft,   6 ft,   6 ft    (possible to have two or more ropes of the same length). 
#Write a program that determines if it is possible to string together the ropes to produce length of exactly N. 
#For the example set above, your program would answer:
#N of 7    : yes
#N of 11   : yes
#N of 3    : no
#N of 12   : yes
#N of 18   : no
#Note: Please write your solution without using the itertools package.

import sys

def getNumbers():
  """Return a list of numbers split by ','. Pop prompt if there is invalid input"""
  prompt = 'Enter length of ropes, split by ",": '
  while True:
    try:
      nums = raw_input(prompt).split(',')
      numbers = map(int, nums)
      return numbers
    except:
      print "Invalid input, try again."

def possibleTotal(numbers):
  """Return possible total value of input numbers"""
  dict_sum = {}
  for n in range(2, len(numbers)+1):
    for i in combinations(numbers, n):
      total = sum(i)
      if total not in dict_sum:
        dict_sum[total] = 1
  return dict_sum
  
def combinations(iterable, r):
  pool = tuple(iterable)
  n = len(pool)
  if r > n:
    return
  indices = range(r)
  yield tuple(pool[i] for i in indices)
  while True:
    for i in reversed(range(r)):
      if indices[i] != i + n - r:
        break
    else:
      return
    indices[i] += 1
    for j in range(i+1, r):
      indices[j] = indices[j-1] + 1
    yield tuple(pool[i] for i in indices)

def printAnswers(dict_N, lengths):
  """Print answers that determine if it is possible to string together 
     the ropes to produce length of exactly N"""
  print 'String together : '
  for length in lengths:
    if length in dict_N:
      print 'N of %d : yes' % length
    else:
      print 'N of %d : no' % length

def main():
  args = sys.argv[1:]
  if not args:
    print 'usage: exact_number exact_number ...'
    sys.exit(1)

  try:
    arguments = map(int,args)
  except:
    print 'usage: exact_number exact_number ...'
    sys.exit(1)
  
  ropes_list = getNumbers()
  dict_N = possibleTotal(ropes_list)
  printAnswers(dict_N, arguments)


if __name__ == '__main__':
  main()
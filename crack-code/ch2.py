#!/usr/bin/python

import sys

def remove_duplicates(input_list):
  """Write code to remove duplicates from an unsorted linked list."""
  util_dict = {}
  output_list = []
  for c in input_list:
    if c not in util_dict:
      util_dict[c] = 1
  for key in util_dict.keys():
    output_list.append(key)
  return output_list

def nth_to_last(input_list, k):
  """Implement an algorithm to find the kth to last element of a singly linked 
  list."""
  return input_list[-k]

def partition(input_list, x):
  """Write code to partition a linked list around a value x, such that all 
  nodes less than x come before alt nodes greater than or equal to x."""
  #could add type check type(...)
  for item in input_list:
    if item < x:
      list1.append(item)
    else:
      list2.append(item)
  return list1.extend(list2)

def add_list(list1, list2):
  """You have two numbers represented by a linked list, where each node 
  contains a single digit. The digits are stored in reverse order, such that 
  the 1's digit is at the head of the list. Write a function that adds the two 
  numbers and returns the sum as a linked list."""
  #could use izip_longest to simplified function
  list_sum = []
  tens = 0
  
  if len(list1)>=len(list2):
    list1_new = list1[:len(list2)]
    list2_new = list2
    list_rest = list1[len(list2):]
  else:
    list1_new = list1
    list2_new = list2[:len(list1)]
    list_rest = list2[len(list1):]

  for i, j in zip(list1_new, list2_new):
    temp = i + j + tens
    digit = temp%10
    tens = temp/10
    list_sum.append(digit)
  for k in list_rest:
    temp = k + tens
    digit = temp%10
    tens = temp/10
    list_sum.append(digit)

  if tens > 0:
    list_sum.append(tens)
  return list_sum

def has_loop(first):
  """detect if a linked list has a loop."""
  #Node() is dummy class that contains attributes like node
  if first is None:
    return False
  slow = Node(first)
  fast = Node(first)

  while True:
    slow = slow.next
    if fast.next != None:
      fast = fast.next.next
    else:
      return False

    if slow is None or fast is None:
      return False
    if fast == slow:
      return True

def find_beginning(first):
  """Given a circular linked list, implement an algorithm which returns the 
  node at the beginning of the loop."""
  if first is None:
    return None
  slow = Node(first)
  fast = Node(first)
  
  while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break

  slow = first
  while slow != fast:
    slow = slow.next
    fast = fast.next
  
  return fast

def palindrome(input_list):
  """Check if a linked list is a palindrome"""
  #solution 1:check every element in list
  length = len(input_list)
  if length == 1:
    return True
  mid = length/2
  for i in range(mid):
    if input_list[i] != input_list[length-1-i]:
      return False
  if i == mid:
    return True
  else:
    return False
  #solution 2:reverse the list [::-1]
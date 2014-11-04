#!/usr/bin/python

class SetOfStacks:
  '3.3 SetOfStacks'
  
  def __init__(self):
    self.stack_list = []

  def pop(self):
    if len(self.stack_list) == 0:
      return None
    last = self.stack_list[-1]
    item = last.pop()
    if len(last) == 0:
      self.stack_list.pop()
    return item
  
  def push(self, item):
    if len(self.stack_list) == 0:
      new_list = []
      self.stack_list.append(new_list)
    last = self.stack_list[-1]
    if len(last) == 10:
      last.append(item)
    else:
      new_list = []
      new_list.append(item)
      self.stack_list.append(new_list)

  def popAt(self, index):
    try:
      stack = self.stack_list[index]
      stack.pop()
    except IndexError:
      print 'index error'
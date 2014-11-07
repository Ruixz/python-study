#!/usr/bin/python

import sys

def check_height(root):
  if root is None:
    return 0
  left_height = check_height(root.left)
  if left_height == -1:
    return -1
  right_height = check_height(root.right)
  if right_height == -1:
    return -1
  height_diff = left_height - right_height
  if abs(height_diff) > 1:
    return -1
  else: 
    return max(left_height, right_height)+1
  
def is_balanced(root):
  """check if the tree is balanced"""
  if check_height(root) == -1:
    return False
  else:
    return True

def dfs(graph, start):
  """deep first search loop"""
  visited, stack = set(), [start]
  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      stack.extend(graph[vertex] - visited)
  return visited

def dfs_rec(graph, start, visited=None):
  """deep first search loop recursively"""
  if visited is None:
    visited = set()
  visited.add(start)
  for next in graph[start]:
    if next not in visited:
      dfs_rec(graph, next, visited)
  return visited

def dfs_paths(graph, start, end):
  """find paths using dfs"""
  stack = [(start, [start])]
  while stack:
    (vertex, path) = stack.pop()
    for next in graph[vertex] - set(path):
      if next == end:
        yield path + [next]
      else:
        stack.append((next, path + [next]))

def dfs_paths_rec(graph, start, end, path=None):
  """find paths using dfs recursively"""
  if path is None:
    path = [start]
  if start == end:
    yield path
  for next in graph[start] - set(path):
    for p in dfs_paths_rec(graph, next, end, path+[next]):
      yield p
  #could use yield from expression in python 3

def bfs(graph, start):
  """bread first search"""
  visited, queue = set(), [start]
  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      visited.add(vertex)
      queue.extend(graph[vertex] - visited)
  return visited

def bfs_paths(graph, start, end):
  """find paths using bfs"""
  queue = [(start, [start])]
  while queue:
    (vertex, path) = queue.pop(0)
    for next in graph[vertex] - set(path)
      if next == end:
        yield path + [next]
      else:
        queue.append((next, path + [next]))

def create_min_bst(array, start, end):
  """
  Given a sorted (increasing order) array with unique integer elements, write 
  an algorithm to create a binary search tree with minimal height
  """
  if start > end:
    return None
  mid = (start+end)/2
  tree_node = TreeNode(array[mid])
  mid.left(create_min_bst(array, start, mid-1))
  mid.right(create_min_bst(array, mid+1, end))
  return tree_node

def create_min_bst(array):
  """wrapper class of create minimal bst"""
  return create_min_bst(array, 0, len(array)-1)


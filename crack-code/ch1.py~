import sys

def check_unique(str_in):
	"""Check the String unique"""
	if len(str_in) == 1:
		return True
	for i in range(1, len(str_in)):
		if str_in[i] in str_in[0:i]:
			return False
	return True

def reverse_string(str_in):
	"""Reverse string without[::-1]"""
	output = ''
	for i in range(len(str_in)-1, -1, -1):
		output += str_in[i]
	return output

def check_permutation(str1, str2):
	"""Check if the 2 inputs are permutation"""
	sort1 = sorted(list(str1))
	sort2 = sorted(list(str2))
	if sort1 == sort2:
		return True
	return False

def compress_str(str_in):
	"""Implement a method to perform basic string compression using the 
	counts of repeated characters. For example, the string aabcccccaaa would 
	become a2blc5a3. If the "compressed" string would not become smaller 
	than the original string, your method should return the original string."""
	
	list_op = []
	for c in str_in:
		if c not in list_op:
			count = 1
			list_op.append(c)
			list_op.append(count)
		else:
			count_index = list_op.index(c) + 1
			list_op[count_index] += 1
	list_str = [str(item) for item in list_op]
	return ''.join(list_str)

##need review
def rotate_matrix(matrix, n):
	"""Given an image represented by an NxN matrix, where each pixel in the 
	image is 4 bytes, write a method to rotate the image by 90 degrees. """
	
	for layer in range(n/2):
		first = layer
		last = n - 1 - layer
		for i in range(first, last):
			offset = i - first
			temp = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = temp
	for row in matrix:
		for item in row:
			print item
			
def setMNZero(matrix):
	"""Write an algorithm such that if an element in an MxN matrix is 0, 
	its entire row and column are set to 0."""
	##prepare boolean array to record whether need to set zero
	for i in range(len(matrix)):
		list_row[i] = False
		for j in range(len(matrix[i])):
			list_col[j] = False
	
	##check 0 field and set boolean array
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 0:
				list_row[row] = True
				list_col[col] = True
	
	##set zero to the row and col
	for m in range(len(matrix)):
		for n in range(len(matrix[row])):
			if list_row[m] or list_col[n]:
				matrix[m][n] = 0
	
def checkRotation(s1, s2):
	"""Assume you have a method isSubstring which checks if one word is a 
	substring of another. Given two strings, si and s2, write code to check 
	If s2 is a rotation of s1 using only one call to isSubstring 
	(e.g., "waterbottLe" is a rotation of "erbottLewat")."""
	if len(s1) == len(s2) and len(s1) > 0:
		for n in range(len(s1)):
			if s1[n:] == s2[:-n] and s1[:n] == s2[-n:]:
				return True
	return False
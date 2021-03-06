#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def find_special_file(dirname):
	filenames = os.listdir(dirname)
	results = []
	for filename in filenames:
		match = re.search(r'__\w+__', filename)
		if match:
			path = os.path.join(dirname, filename)
			results.append(os.path.abspath(path))
	return results

def copy_dir(paths, dest):
	if not os.path.exists(dest):
		os.mkdir(dest)
	for path in paths:
		shutil.copy(path, os.path.abspath(dest))
	
def copy_zip(paths, zip_name):
	cmd = 'zip -j ' + zip_name + ' ' + ' '.join(paths)
	print 'Processing: ' , cmd
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dirname in args:
  	paths = paths + find_special_file(dirname)
  	if todir:
  		copy_dir(paths, todir)
  	elif tozip:
  		copy_zip(paths, tozip)
  	else:
  		print '\n'.join(paths)
  
if __name__ == "__main__":
  main()

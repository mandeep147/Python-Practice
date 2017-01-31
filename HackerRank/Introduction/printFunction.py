# Read an integer .
# Without using any string methods, try to print the following:
# Note that "" represents the values in between.
from __future__ import print_function
n = int(input())
print (*range(1, n+1), sep='')
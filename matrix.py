import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

if n < 0 or m < 0:
  print('the length and height of the matrix cannot be negative')
  exit(1)  
matrix = []

for _ in range(n):
  matrix_item = input()
  matrix.append(matrix_item)

string = ''
#reading top to bottom, left to right
for column in range(m):
    for line in matrix:
      string+=line[column]
#replace all non alphanumeric characters that are inbetween two alphanumeric characters with a single space
result = re.sub(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])',' ', string)
print(result)
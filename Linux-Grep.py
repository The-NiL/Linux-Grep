#!/usr/bin/env python3
import re
expression = input("Enter a regular expression: ")
path = input("Enter a path to the file u wanna search through: ")
pathsplitted = path.split("/")
filename = pathsplitted[len(pathsplitted)-1]
handle = open(path)
count = 0
for line in handle:
    line = line.rstrip()
    words = re.findall(expression, line )
    if len(words) > 0:
        count += 1
print(filename, "had", count, "lines that matched", expression)

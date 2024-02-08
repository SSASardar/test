"""
Aim: this script counts the number of lines in standard input
Input: strings for the ... idk I didnt pay attention
"""

import sys

count = 0

for line in sys.stdin:
	count += 1

print(count, "lines in standard input")

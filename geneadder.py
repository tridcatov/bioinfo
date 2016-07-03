#!/bin/python

import sys
import string

input = sys.argv[1]
dict = {}
totalCount = 0

for line in open(input, 'r'):
	[_, gene, count] = line.split()
	if ( not count.isdigit() ):
		continue
	
	count = int(count)
	totalCount += count
	if ( gene in dict ):
		dict[gene] += count
	else:
		dict[gene] = count

genes = sorted(dict, key=dict.__getitem__, reverse=True)

output = input + ".summed.txt"
file = open(output, 'w')

for gene in genes:
	count = dict[gene]
	line = gene + '\t' + str(count) + '\t' + str(totalCount) + '\n'
	totalCount -= count
	file.write(line)
	

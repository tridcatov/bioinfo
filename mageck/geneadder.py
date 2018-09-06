#!/usr/bin/python

import sys
import string

dict = {}
totalCount = 0

for line in sys.stdin:
	[_, gene, count] = line.split("\t")

	if ( not count.isdigit()):
		try:
			count = float(count)
		except:
			continue
	else:
		count = int(count)
	
	totalCount += count
	if ( gene in dict ):
		dict[gene] += count
	else:
		dict[gene] = count

genes = sorted(dict, key=dict.__getitem__, reverse=True)


for gene in genes:
	count = dict[gene]
	line = gene + '\t' + str(int(count)) + '\t' + str(int(totalCount))
	totalCount -= count
	print(line)
	

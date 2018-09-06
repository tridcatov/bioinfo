#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Analyze input ranked genes tables')
parser.add_argument('files', metavar='file', type=str, nargs='+', help='Input files')
parser.add_argument('-n', dest='n', type=int, default=100, help='Number of files to process from tables')

args = parser.parse_args()

files = args.files
n = args.n

print("Trimming input files:")
print(files)
print("Taking first " + str(n) + " genes")

table = []

import csv

for f in files:
	with open(f, 'r') as content:
		reader = csv.reader(content, delimiter= '\t')
		column = []
		count = 0
		for row in reader:
			count += 1
			if count == 1:
				continue
			column.append(row[0])
			if count == n:
				break
			
		table.append(column)
		
print("Gene table obtained:")
print(str(table))

result = set(table[0])
for s in table[1:]:
	result.intersection_update(s)
	
result = list(result)

print("Gene intersection table has " + str(len(result)) + " entries")
print(str(result))

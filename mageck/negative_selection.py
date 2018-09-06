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

table = []

import csv

for f in files:
	with open(f, 'r') as content:
		reader = csv.reader(content, delimiter= '\t')
		column = []
		for row in reader:
			amount = int(row[1])
			if (amount == 0):
				column.append(row[0])
		table.append(column)
		
print("Gene table obtained:")
for row in table:
	print("{} entries".format(len(row)))

result = set(table[0])
for s in table[1:]:
	result = result & set(s)	
	
result = list(result)

print("Gene intersection table has " + str(len(result)) + " entries")
print(str(result))

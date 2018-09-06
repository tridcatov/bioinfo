#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Analyze input ranked genes tables')
parser.add_argument('files', metavar='file', type=str, nargs='+', help='Input files')
parser.add_argument('-p', dest='p', type=float, default=0.05, help='P-value to trim')

args = parser.parse_args()

files = args.files
p = args.p

print("Taking only genes with p-value lesser than " + str(p))

table = []

import csv

for f in files:
    with open(f, 'r') as content:
        reader = csv.reader(content, delimiter= '\t')
        print('Analyzing ' + f)
        column = []
        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue

            gene = row[0]
            if ( gene.startswith('hsa-mir') or gene.startswith('Non')):
                continue

            pvalue = float(row[9])
            if ( pvalue >= 0.05 ):
                break

            count += 1
            column.append(gene)
			
        print('Retained ' + str(count) + ' genes')
        table.append(column)
		
#print("Gene table obtained:")
#print(str(table))

result = set(table[0])
for s in table[1:]:
	result.intersection_update(s)
	
result = list(result)

print("Gene intersection table has " + str(len(result)) + " entries")
print(str(result))

#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description='Analyze input ranked genes tables')
parser.add_argument('files', metavar='file', type=str, nargs='+', help='Input files')

args = parser.parse_args()

files = args.files

cache = {}
fc = {}

import csv

for f in files:
    with open(f, 'r') as content:
        reader = csv.reader(content, delimiter= '\t')
        print('Analyzing ' + f)
        file = len(fc) + 1
        fc[file] = f
        count = 0
        for row in reader:
            if count == 0:
                count += 1
                continue

            gene = row[0]
            if ( gene.startswith('hsa-mir') or gene.startswith('Non')):
                continue

            if not gene in cache:
                cache[gene] = []

            pvalue = float(row[9])
            rank = int(row[11])
            cache[gene].append((file, rank, pvalue))
            count += 1
			
        print('Loaded ' + str(count) + ' genes')
		
print('Load complete, input full gene name to search database')
for gene in sys.stdin:
    gene = gene.strip()
    if not gene in cache:
        print("No gene {} in cache".format(gene))
        continue

    for info in cache[gene]:
        file, rank, pvalue = info
        print("Rank {:d} with pvalue {} in sample {}".format(rank, pvalue, fc[file]))

#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description='find file in input count tables')
parser.add_argument('-g', metavar='gene', type=str, nargs='+', help='Genes to find')
parser.add_argument('-f', metavar='file', type=str, nargs='+', help='Files to look at')

args = parser.parse_args()

genes = args.g
files = args.f

print("Obtaining counts of incoming genes:")
print(genes)
print("Scanned files:")
print(files)

import csv

for f in files:
  with open(f, 'r')  as content:
    reader = csv.reader(content, delimiter= '\t')
    result = {}
    row_num = 0
    zero_gene = 0
    for row in reader:
      row_num += 1
      gene_sum_count = int(row[2])
      if ( row[0] in genes ):
	result[row[0]] = (row_num, gene_sum_count)
      if ( gene_sum_count == 0 and zero_gene == 0 ):
       	zero_gene = row_num
	result["ZERO_GENE"] = (row_num, 0) 


    print("Scanned {} count table:".format(f))
    print(result)
	

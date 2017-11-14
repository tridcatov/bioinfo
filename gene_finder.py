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
    for row in reader:
      if ( row[0] in genes ):
	result[row[0]] = int(row[1])
    print("Scanned {} count table:".format(f))
    print(result)
	

#!/usr/bin/python

import sys
import itertools

import re

csgrna = "GTGGAAAGGACGAAACACCG"
p = re.compile("GTGGA[ATGC]*?ACCG")

def debug_print(string):
	print(string, file=sys.stderr)

incoming = 0
processed = 0
with sys.stdin as f:
	for lines in itertools.zip_longest(*[f]*4):
		incoming += 1
		trimmed = [x.strip() for x in lines]
		match = p.search(trimmed[1])
		if ( not match ):
			continue
		
		processed += 1
		print(trimmed[0])
		print(csgrna + trimmed[1][match.end(): match.end() + 30])
		print(trimmed[2])
		print(("F" * 20) + trimmed[3][match.end(): match.end() + 30])

retain = float(processed) / incoming * 100
debug_print("Source lines: {}".format(incoming))
debug_print("Trimmed lines: {}".format(processed))
debug_print("Retain: {0:0.2f}".format(retain))
# debug_print("CSV: {},{},{0:0.2f}".format(incoming, processed, retain))

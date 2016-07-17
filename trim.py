#!/usr/bin/python

import sys
import itertools

import re

csgrna = "GTGGAAAGGACGAAACACCG"
p = re.compile("GTGG[ATGC]*?CACCG")

with sys.stdin as f:
	for lines in itertools.zip_longest(*[f]*4):
		trimmed = [x.strip() for x in lines]
		match = p.search(trimmed[1])
		if ( not match ):
			continue
		
		print(trimmed[0])
		print(csgrna + trimmed[1][match.end(): match.end() + 30])
		print(trimmed[2])
		print(("F" * 20) + trimmed[3][match.end(): match.end() + 30])

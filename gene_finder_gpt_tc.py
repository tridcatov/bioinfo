#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description='find file in input count tables')
parser.add_argument('-g', metavar='gene', type=str, nargs='+', help='Genes to find')
parser.add_argument('-f', metavar='file', type=str, nargs='+', help='Files to look at')
parser.add_argument('-s', metavar='sample', type=str, help='File with basic gpt descriptions')

args = parser.parse_args()

genes = args.g
files = args.f
sample = args.s



print("Obtaining counts of incoming genes:")
print(genes)
print("Scanned files:")
print(files)

template = ""
with open(sample, 'r') as template_file:
  template = template_file.read()

import csv

for f in files:
  with open(f, 'r')  as content:
    reader = csv.reader(content, delimiter= '\t')
    result = {}
    row_num = 0
    total_reads = 0
    top_reads = 0
    zero_gene = 0
    for row in reader:
      gene_sum_count = int(row[2])
      if ( row[0] in genes ):
	result[row[0]] = (row_num, gene_sum_count)
      if ( gene_sum_count == 0 and zero_gene == 0 ):
       	zero_gene = row_num
	result["000"] = (row_num, 0) 
      if ( row_num == 0 ):
        total_reads = gene_sum_count
        top_reads = int(row[1])
      row_num += 1

    output_file = f.split('.')[0] + ".gpt"
    with open(output_file, 'w') as output:
      output.write(template) 
      output.write("set xrange [ 0 : {}]\n".format(row_num))
      output.write("set yrange [ 0 : {}]\n".format(total_reads))
      xtics = ", ".join(['"{}" {}'.format(key, index) for (key, (index, _)) in result.items()])
      output.write("set xtics ({})\n".format(xtics))
      output.write('plot "{}" using 3 pt 7 ps 0.4 lc rgb "black"\n'.format(f))
    

#!/usr/bin/env python

# Returns N50 (or N of your choice) and other stats of a FASTA file of sequences.
# N50 is calculated as the sequence length above which 50% of the total sequence 
# length lies when the sequences are sorted in order of descending length.

import getopt, sys
import copy
import numpy as np
from Bio import SeqIO

def get_stats(fasta, n):
	lengths = []
	for seq in SeqIO.parse(fasta, 'fasta'):
		lengths.append(len(seq))
	num_seqs = len(lengths)
	total_length = sum(lengths)
	average_length = total_length/float(len(lengths))
	lengths = sorted(lengths, reverse=True)
	max_length = max(lengths)
	min_length = min(lengths)
	med_length = np.median(lengths)
	cumulative_length = 0
	n50_value = 0
	i = 0
	while cumulative_length < total_length*(n/100.0):
		l = lengths[i]
		cumulative_length += l
		n50_value = l
		i += 1
	return (num_seqs, n50_value, average_length, med_length, total_length, min_length, max_length)

def usage():
	print 	"""
\ncfasta_stats.py.\n
Returns N50 (or N of your choice) and other stats of a FASTA file of sequences.\n
N50 is calculated as the sequence length above which 50% of the total sequence 
length lies when the sequences are sorted in order of descending length.\n
Basic usage:
\tpython fasta_stats.py -i <fastafile> -n 50\n
Arguments:
\t-h, --help\t\t\tPrint this information.
\t-i, --in <fastafile>\t\tFASTA-formatted input file.
\t-n, --number <number>\t\tA number between 1 and 100."""

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'n:i:h', ['number=', 'in=', 'help'])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-n', '--number'):
			n = int(arg)
		elif opt in ('-i', '--in'):
			fasta = arg
		elif opt in ('-h', '--help'):
			usage()
			sys.exit(2)
		else:
			usage()
			sys.exit(2)
		
	try:
		num_seqs, n50_value, average_length, med_length, total_length, min_length, max_length  = get_stats(fasta, n)
		print '\n***Results for %s***\n' % fasta
		print 'There are %i sequences' % (num_seqs)
		print 'The N%i is: %i' % (n, n50_value)
		print 'The average length is: %i' % (average_length)
		print 'The median length is %f' % (med_length)
		print 'The total length is: %i' % (total_length)
		print 'The shortest length is: %i' % (min_length)
		print 'The longest length is: %i\n' % (max_length)
		print '***\n'
	except:
		usage()
		sys.exit(2)

if __name__ == "__main__":
    main()

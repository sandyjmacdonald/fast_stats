fast_stats.py
===========

Returns N50 (or N of your choice) and other stats of a fasta/fastq file of sequences. 
N50 is calculated as the sequence length above which 50% of the total sequence 
length lies when the sequences are sorted in order of descending length.

### Dependencies

Requires [Numpy](http://www.numpy.org) for calculating the median read length and
[Biopython](http://biopython.org) to read in the fasta file.

### Usage

    python fast_stats.py -i <infile> -n 50

> ##### Arguments

> `-i` The fasta/q file for which you want to calculate the stats.

> `-n` The value of n (usually 50) that you want to use.

> `-h` Displays help.

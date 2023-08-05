#!python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from itertools import chain as chain

sys.path.pop(0)
import repeatfinder as rf
from genbank.file import File
from genbank.locus import Locus

def is_valid_file(x):
	if not os.path.exists(x):
		raise argparse.ArgumentTypeError("{0} does not exist".format(x))
	return x

def is_in(repeats, repeat):
	print(repeat)
	(a,b),(c,d) = repeat
	if ((a,b+1),(c,d+1)) in repeats:
		return True
	return False

if __name__ == '__main__':
	usage = '%s [-opt1, [-opt2, ...]] infile' % __file__
	parser = argparse.ArgumentParser(description='', formatter_class=RawTextHelpFormatter, usage=usage)
	parser.add_argument('infile', type=is_valid_file, help='input file')
	parser.add_argument('-l', '--len', help='The minimum length for repeats', type=int, default=12)
	parser.add_argument('-g', '--gap', help='Allow mismatch gap of length g', type=int, default=0)
	parser.add_argument('-o', '--outfile', action="store", default=sys.stdout, type=argparse.FileType('w'), help='where to write output [stdout]')
	args = parser.parse_args()

	header = ''
	dna = ""
	with open(args.infile) as fp:
		for line in chain(fp, '>'):
			if line.startswith(">"):
				if dna:
					repeats = rf.get_repeats(dna, args.gap)
					locus = Locus(header, dna)
					for repeat in repeats:
						if 1 + repeat[1] - repeat[0] >= args.len and 'n' not in locus.seq(repeat[0],repeat[1]):
							a,b,c,d = map(str, repeat)
							pairs = ((a,b),(c,d))
							locus.add_feature('repeat_region', 0, pairs)
					locus.write()
				header = line[1:].rstrip()
				dna = ""
			else:
				dna += line.rstrip() #.replace('N','').replace('n','')
	

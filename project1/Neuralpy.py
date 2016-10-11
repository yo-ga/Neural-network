#!/usr/bin/env python

import argparse
from argparse import ArgumentParser
from datetime import date
import sys

def parse():
	parser = ArgumentParser(description='Neutral net analysis tool.')
	parser.add_argument('-o', '--output-prefix', help='Set the output file prefix', action='store', nargs='?', dest='outPre', default='Neutru'+str(date.today()))
	parser.add_argument('-O', '--output-destination', help='Set the output file directory', action='store',dest='outDir',default='./')
	parser.add_argument('-T', '--testing-data', help='Set the file to test the program, including training data and examinng data', dest='testData',type=argparse.FileType('r'))
	parser.add_argument('-t', '--training-data', help='Set the file for training data', action='store', dest='trainData', type=argparse.FileType('r'))
	parser.add_argument('-e', '--examining-data', help='Set the file to examine the data', action='store', dest='examData', type=argparse.FileType('r'))
	#parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true', dest='verbose')
	args = parser.parse_args()

def main():
	parse()

if __name__ == "__main__":
	main()
#!/usr/bin/env python

import argparse
from argparse import ArgumentParser
from datetime import date
import sys

def parse():
	parser = ArgumentParser(description='Neutral net analysis tool.')
	parser.add_argument('-o', '--output-prefix', help='Set the output file prefix', action='store', dest='outPre', default='Neutru'+str(date.today()))
	parser.add_argument('-O', '--output-destination', help='Set the output file directory', action='store',dest='outDir',default='./')
	parser.add_argument('-T', '--test-Data', help='Set the file to test the program, including training data and examinng data', dest='testData',type=argparse.FileType(mode='r',encoding='utf-8'))
	parser.add_argument('-t', '--train-data', help='Set the file for training data', action='store', dest='trainData', type=argparse.FileType(mode='r',encoding='utf-8'))
	parser.add_argument('-e', '--exam-data', help='Set the file to examine the data', action='store', dest='examData', type=argparse.FileType(mode='r',encoding='UTF-8'))
	#parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true', dest='verbose')
	args = parser.parse_args()
	return args

def main():
	args=parse()
	if((args.testData is not None or args.trainData is not None )and args.examData is not None):
		print ("Error: you couldn\'t use two modes in the same time.")
	elif (args.testData is not None):

	elif (args.trainData is not None and args.examData is not None):


if __name__ == "__main__":
	main()
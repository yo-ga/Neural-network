#!/usr/bin/env python

from algorithm import *
from useData import *
from drawPlat import *
import argparse
from argparse import ArgumentParser
from datetime import date
import sys

def parse():
	parser = ArgumentParser(description='Neutral net analysis tool.')
	parser.add_argument('-o', '--output-prefix', help='Set the output file prefix', action='store', dest='outPre', default='Neutru'+str(date.today()))
	parser.add_argument('-O', '--output-destination', help='Set the output file directory', action='store',dest='outDir',default='./')
	parser.add_argument('-T', '--test-Data', help='Set the file to test the program, including training data and examinng data', dest='testData',type=argparse.FileType(mode='r',encoding='utf-8'),default=None)
	parser.add_argument('-t', '--train-data', help='Set the file for training data', action='store', dest='trainData', type=argparse.FileType(mode='r',encoding='utf-8'),default=None)
	parser.add_argument('-e', '--exam-data', help='Set the file to examine the data', action='store', dest='examData', type=argparse.FileType(mode='r',encoding='UTF-8'),default=None)
	#parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true', dest='verbose')
	args = parser.parse_args()
	return args

def main():
	args=parse()
	suc = False
	if((args.examData is not None or args.trainData is not None )and args.testData is not None):
			print ("Error: you couldn\'t use two modes in the same time.")
			quit()
	elif (args.testData is not None):
		testList,group=transDataToList(args.testData)
		args.testData.close()
		trainList, examList=cutList(testList)
	elif (args.trainData is not None and args.examData is not None):
		trainList,group=transDataToList(args.trainData)
		examList,group1=transDataToList(args.examData)
	while not suc:
		vector = [float(x) for x in input("Please input the initial vector: ").split()]
		tdata=list(trainList)
		# print(tdata)
		gr,trainList=divide2Group(trainList)
		line = normalAlgo(trainList,vector,0.9)
		# print(line)
		if line==-1:
			print("Please choose another initial vector.")
			continue
		else:
			suc = True
			draw(trainList,group,line, len(trainList[0])-1)
			

if __name__ == "__main__":
	main()
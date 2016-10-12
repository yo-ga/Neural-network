#!/usr/bin/env python
import re

def transDataToList(data):
	dataList=[]
	group=0
	lines=data.readlines()
	for l in lines:
		l=l.strip(' \t\n\r')
		lineList=[float(x) for x in re.split(r'[ \t\n]+', l, maxsplit=0, flags=0)]
		if(lineList[-1]>group):
			group=int(lineList[-1])
		dataList.append(lineList)
	return dataList, group+1

def cutList(test):
	cutPoint=int(len(test)/3)
	train = test[0:-cutPoint]
	exam = test[-cutPoint:]
	return train, exam
#!/usr/bin/env python
import re
import copy

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
	
def divide2Group(data):
	group=[]
	# print(data)
	da=copy.deepcopy(data)
	for x in data:
		has=False
		for y in group:
			if x[-1]==y:
				has=True
		if not has:
			group.append(x[-1])
	groupstamp=[1,-1]
	#print(group)
	for x in range(0,len(data)):
		for i in range(0,len(group)):
			if data[x][-1]==group[i]:
				da[x][-1]=(-1)**(i)

	# print(da)
	# print(data)
	return len(group), da
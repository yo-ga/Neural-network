#!/usr/bin/env python

def normalAlgo(trainData,vector,learning_rate):
	roundBound=len(trainData)
	# print(trainData,roundBound)
	final_vector=[-1]
	i=0
	for x in vector:
		final_vector.append(x)
	
	while(i<roundBound):
		round=i%len(trainData)
		learning_vector=[-1]
		for x in trainData[round][:-1]:
			learning_vector.append(x)
		output=trainData[round][-1]
		dot=dotVector(final_vector, learning_vector)
		# print(dot,output)
		if dot*output<0:
			if dot<=0:
				final_vector=plusVector(final_vector,learning_vector,learning_rate)
			else:
				final_vector= minusVector(final_vector, learning_vector, learning_rate)
			roundBound=i+1+len(trainData)
		i=i+1
		if(i>1000000 ):
			# final_vector=-1
			break
	return final_vector

def dotVector(vector1,vector2):
	if len(vector1)!=len(vector2):
		print("Error: two vector are not in the same length.")
		quit()
	sumNum=0
	for i in range(0, len(vector1)):
		sumNum+=float(vector1[i])*float(vector2[i])
	return sumNum

def plusVector(vector1,vector2,learning_rate):
	# print(vector1,vector2)
	if len(vector1)!=len(vector2):
		print("Error: two vector are not in the same length.")
		quit()
	sumVec = [vector1[i]+vector2[i]*learning_rate for i in range(0,len(vector1))]
	# print(sumVec)
	return sumVec

def minusVector(vector1,vector2,learning_rate):
	# print(vector1,vector2)
	if len(vector1)!=len(vector2):
		print("Error: two vector are not in the same length.")
		quit()
	sumVec = [vector1[i]-vector2[i]*learning_rate for i in range(0,len(vector1))]
	# print(sumVec)
	return sumVec

def checkData(trainData):
	return True
#!/usr/bin/env python

from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

colorList=['k','g', 'b', 'y', 'm' ,'c' ,'r' ]
shapelist=['*','^','s','o']

def draw(points,group,vector,dimension):
	fig = plt.figure()
	if dimension==2:
		ax=fig.add_subplot(111)
		for i in range(-1, group):
			for x in points:
				if(x[-1]==i):
					points_x=[x[0]]
					points_y=[x[1]]
					t=ax.scatter(points_x,points_y,color=colorList[(x[-1]+1)%7],marker=shapelist[(x[-1]+1)%4])
		xlimit=plt.gca().get_xlim()
		ylimit=plt.gca().get_ylim()
		if(vector[2]==0):
			linex=[vector[0]/vector[1] for x in xlimit]
			liney=[x for x in xlimit]
		elif(vector[1]==0):
			linex=[y for y in ylimit]
			liney=[vector[0]/vector[2] for x in ylimit]
		else:
			linex=[x for x in xlimit]
			liney=[(-x*vector[1]+vector[0])/(-vector[1]) for x in xlimit]
		# print(vector)
		plt.plot(linex,liney,'r-')
		# plt.xlim(xlimit)
		plt.show()
	elif dimension==3:
		print(vector)
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1, projection='3d')
		if vector[2]==0 and vector[1]==0:
			X=np.arange(-5,5,1)
			Y=np.arange(-5,5,1)
			Z=-vector[0]/vector[3]
		elif vector[3]==0 and vector[1]==0:
			X=np.arange(-5,5,1)
			Z=np.arange(-5,5,1)
			Y=-vector[0]/vector[2]
		elif vector[2]==0 and vector[3]==0:
			Z=np.arange(-5,5,1)
			Y=np.arange(-5,5,1)
			X=-vector[0]/vector[1]
		# elif vector[1]==0:
			# X=np.arange(1,100,1)
			# Y=np.arange(1,100,1)
		else:
			X=np.arange(1,10,1)
			Y=np.arange(1,10,1)
			X, Y = np.meshgrid(X, Y)
			Z = (vector[1]*X + vector[2]*Y - vector[0])/vector[3]
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.jet,linewidth=0, antialiased=False)
		ax.set_zlim3d(-5,5)
		fig.colorbar(surf, shrink=0.5, aspect=5)
		plt.show()
	elif dimension>3:
		print("Dimension: ")
	else:
		print ("Error: the dimension should be not below 2")
		quit()
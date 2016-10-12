#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

colorList=['r','g', 'b', 'y', 'm' ,'c' ,'k' ]

def draw(points,group,vector,dimension):
	fig = plt.figure()
	if dimension==2:
		ax=fig.add_subplot(111)
		for i in range(0, group):
			for x in points:
				if(x[2]==i):
					points_x=[x[0]]
					points_y=[x[1]]
					t=ax.scatter(points_x,points_y,color=colorList[i])
		plt.show()
	elif dimension==3:
		ax = Axes3D(fig)
		X = np.arange(-4, 4, 0.25)
		Y = np.arange(-4, 4, 0.25)
		X, Y = np.meshgrid(X, Y)
		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)
		ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
		plt.show()
	elif dimension>3:
		print("Dimension: ")
	else:
		print ("Error: the dimension should be not below 2")
		quit()
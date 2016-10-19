#!/usr/bin/env python

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from algorithm import *
from useData import *
from drawPlat import *
import sys

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Analysis Practice")
        self.master.rowconfigure(4, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.resizable(0,0)
        self.grid(sticky=W+E+N+S)
        self.trainData=StringVar()
        self.trainData.set("")

        self.label= Label(self,text="Training data: ",width=15)
        self.label.grid(row=1,column=0,sticky=W)
        self.label1= Entry(self,textvariable=self.trainData,width=20)
        self.label1.grid(row=1,column=1)
        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=2, sticky=E)
        self.label2=Label(self,text="Initial vector:\n(example: 0 1)",width=15)
        self.label2.grid(row=2,column=0,sticky=W)
        self.vector= Entry(self,width=20)
        self.vector.grid(row=2,column=1,sticky=W)
        self.learning=Label(self,text="Learning rate:\n(between 0 ~ 1.0)",width=15)
        self.learning.grid(row=3,column=0,sticky=W)
        self.learningrate=Entry(self,width=20)
        self.learningrate.grid(row=3,column=1,sticky=W)
        self.button2 = Button(self, text="Run", command=self.runAnaly, width=10)
        self.button2.grid(row=2, column=2, sticky=E)
        self.button3 = Button(self,text="Reset",command=self.reset,width=10)
        self.button3.grid(row=3, column=2,sticky=E)

    def load_file(self):
        fname = askopenfilename(title="Choose Data",filetypes=(("Text data","*.txt"),("All files", "*.*") ))
        if fname:
            try:
                self.trainData.set(fname)
            except:
                self.trainData.set("")
            return
        self.update()

    def runAnaly(self):
        suc = False
        testData=open(self.trainData.get(),'r',encoding='utf-8')
        if testData is not None:
            trainList,group=transDataToList(testData)
            testData.close()
            # trainList, examList=cutList(testList)
        while not suc:
            vector = [float(x) for x in self.vector.get().split()]
            tdata=list(trainList)
        # print(tdata)
            gr,trainList=divide2Group(trainList)
            line = normalAlgo(trainList,vector,float(self.learningrate.get().strip()))
        # print(line)
            if line==-1:
                showerror(title="Warning",message="We couldn't find the vector.\nYou should choose another initial vector.")
                break
            else:
                suc = True
                draw(trainList,group,line, len(trainList[0])-1)
        

    def reset(self):
        self.trainData.set("")
        self.vector.delete(first=0,last=END)
        self.learningrate.delete(first=0,last=END)
        self.update()

if __name__ == "__main__":
    MyFrame().mainloop()
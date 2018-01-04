# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:59:27 2017

@author: Erman
"""

import pandas as pd
import numpy as np
import random as rand

fileName="MLproject.xlsx"
sheetName="page1"

df1=pd.read_excel(fileName,sheetName)

columnNames= df1.columns
rLength=len(columnNames)

#Coefficients

coef=np.zeros(len(columnNames))
coef[0]=-45.5
coef[1]=1.3
coef[2]=-1.1
coef[3]=-2.1
coef[4]=5.0
coef[5]=22.438
coef[6]=90.0

#Learning Rate
eta=0.000005

#Number of Iterations
nOfIterations=1200


#Error List
errorList=[]

def getError(df1,coef):
    
    error=0.0
    columnNames= df1.columns
    rLength=len(columnNames)
    cLength=len(df1[columnNames[0]])
    
    for jj in range(cLength):
        funcValue=0.0
        for ii in range(rLength-1):
            funcValue+=coef[ii]*df1[columnNames[ii]][jj]
        funcValue+=coef[rLength-1]
        #print jj, funcValue, df1[columnNames[rLength-1]][jj] 
        error+=(df1[columnNames[rLength-1]][jj]-funcValue)**2   
    
    
    return error/cLength
    

def getGradientOfIndex(df1,coef,index):
    columnNames= df1.columns
    rLength=len(columnNames)
    cLength=len(df1[columnNames[0]])
    
    gradientValue=0.0
    
    for jj in range(cLength):
        
        #Calculate the function
        funcValue=0.0
        for ii in range(rLength-1):
             funcValue+=coef[ii]*df1[columnNames[ii]][jj]
        funcValue+=coef[rLength-1]
#        print funcValue
        #.gradient
        if index==rLength-1:
            gradientValue+=-(2.0/cLength)*(df1[columnNames[rLength-1]][jj]-funcValue)
        else:
            gradientValue+=-(2.0/cLength)* df1[columnNames[index]][jj]*(df1[columnNames[rLength-1]][jj]-funcValue)
#            print df1[columnNames[rLength-1]][jj],funcValue
    
    return gradientValue
    
#print   getGradientOfIndex(df1,coef,2) 
    
def updatedIndex(df1,coef,index,lRate):
    
    gradient = getGradientOfIndex(df1,coef,index)
    updateValue=lRate*gradient
    
    updatedCoef=coef.copy()
    updatedCoef[index]+=-updateValue

#    print updateValue
    print "First Error: ", getError(df1,coef),"Second Error: ", getError(df1,updatedCoef)
#    print coef
#    print updatedCoef
    
    print getError(df1,coef)>getError(df1,updatedCoef)
    
    if getError(df1,coef)>getError(df1,updatedCoef):
        errorList.append(getError(df1,updatedCoef))
        return updatedCoef
    else:
        return coef
        

   

 
def optimize(df1,coef,lRate,iterations):
    
    for it in range(iterations):
        rand.seed()
        index=rand.randint(0,len(coef)-1)
        coef=updatedIndex(df1,coef,index,lRate)
        
    
    return getError(df1,coef),coef


finalError,finalCoeff=optimize(df1,coef,eta,nOfIterations)        
    
import matplotlib.pyplot as plt
plt.plot(errorList)
   


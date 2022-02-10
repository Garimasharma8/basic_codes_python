# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% Factorial of a number
import math
import numpy as np
import pandas as pd


def fact(num):
    if num<0:
        return 0
    elif num==0 or num==1:
        return 1
    else:
        fact=1
        while(num>0):
            fact =fact* num
            num = num-1
        return fact

num = 3
print("Factorial of number", num, "is", fact(num))

#%% Simple interest formula

def interet(P,R,T):
    if P==0 or R==0 or T==0:
        return 0
    else:
        S= P*R*T/100
        return S

P=10000
R=1
T=10
simple_interest= interet(P,R,T)    
print("Simple intesrt is", simple_interest)

#%%  checkerboard pattern
import numpy as np


def checkerboard(n):
    if n==0 or n==1:
        print("pattern is not possible")
    else:
        arr = np.zeros((n,n), dtype=int)  #n x n array with all zeros
        arr[1::2,::2]=1 # selecting rows from index 1 to end with jump of 2, selecting alternate columns
        arr[::2,1::2]=1
    print(arr)    

print(checkerboard(8))     

#%% print a pattern


def pattern(num):
    if num==0:
        print("no pattern possible")
    else:
        for i in num:
            print("*" * int(i))
            

pattern("123")           # catch is to input number as a string

#%% Armstrong number

def order(num):
    n=0
    while(num !=0):
        n=n+1
        num = num // 10
    return n    


def armstrong(num):
    arm=0
    n=num
    while(n !=0):
        r = n % 10
        arm= arm + (r) ** order(num)
        n = n //10
    return(num==arm)
        

   


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
        
#%% prime number

def prime(x,y): 
    list_prime = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                list_prime.append(i)
    return list_prime

print("list of prime numbers are:", prime(2,7))
            
   
#%% check if a num is prime

def prime(N):
    for i in range(2,int(N/2)+1):
        if N % i ==0:
            print("Not a prime number")
            break
    else:
        print("its a prime no")
            
#%%  fibonacci numbers

def fibonacci(n):
    fib=[]
    if n <0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        sum= fibonacci(n-1) + fibonacci(n-2)
        print(fib.append(sum))
    return sum
  
#%% check if number is fibonacci      
# a number n is fibonacci is it is a perfect square : (5n^2 +4) or (5n^2-4)

import math

def isperfectsqrt(x):
    s = int(math.sqrt(x))
    return s*s ==x

def isfibonacci(n):
    condition1 = (5*n*n)+4
    condition2 = (5*n*n)-4
    if isperfectsqrt(condition1) or isperfectsqrt(condition2):
        print("number is fibonacci")
    else:
        print("number is not fibonacci")

# driver statement

isfibonacci(8)    

#%% sum of squares for first n numbers

def sumsquares(n):
    sum=0
    for i in range(0,n+1):
        sum = sum + i *i
    return sum

#%%     sum of array elements

def sumofarray(arr):
    sum=0
    for i in range(0,len(arr)+1):
        sum = sum + i
    return sum
        
#%%  find the largest number is array

import math

def largest(arr):
    largest = max(arr)
    return largest

#%% rotate array elemets by d position

def arrayrot(arr):
    d= int(input('enter the no of position to shift'))
    n=len(arr)+1
    temp = arr[0:int(d)]
    rest= arr[d:len(arr)+1]
    rotated = rest[:] + temp[:]
    return rotated

    
#%%   find reminder of array multiplication divided by n

def reminder(arr):
    mul =1
    n = int(input('number'))
    for i in range(0, len(arr)):
        mul = mul * arr[i]
    return mul%n

#%% perfect number

def perfectnum(num):
    sum=0
    for i in range(1,int(num/2)+1):
        if num % i ==0:
            sum = sum + i
    return (sum==num)
            
        
            


        

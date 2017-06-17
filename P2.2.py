# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:49:28 2017

@author: Rao
"""

def fiboeve():
    sum=0
    fibo=[1,1]
    for i in range(1,4000000,1):
        nt=fibo[i]+ fibo[i-1]
        fibo.append(nt)
        if( nt%2==0):
            sum=sum+nt
    print("sum is ",sum)
    print("yo")
    print(fibo)
        
        
    

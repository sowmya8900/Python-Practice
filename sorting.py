#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
k = len(a)-1
while(k>0):
    for i in range (0,k):
        if a[i]>a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            count = count + 1

    k = k-1
        
print("Array is sorted in" , str(count) , "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a)-1])

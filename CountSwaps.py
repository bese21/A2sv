#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    counter=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i] >a[j]:
                counter+=1
                a[i],a[j]=a[j],a[i]
    print("Array is sorted in",counter ,"swaps.")
    print("First Element:",a[0]) 
    print("Last Element:",a[len(a)-1])
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

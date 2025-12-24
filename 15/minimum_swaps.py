#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)

    # pair (value, original_index)
    indexed = list(enumerate(arr))
    indexed.sort(key=lambda x: x[1])

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or indexed[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = indexed[j][0]   
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps
    n = len(arr)
    visited = [False] * n
    pos = {}
    swaps = 0
    
    for i in range(n):
        pos[arr[i]] = i
        
    arr.sort
    
    for i in range(n):
        if visited[i] or  pos[arr[i]] == i:
            continue 
        
        j = 0
        cycle_size = i
        
        while not vis[j]:
            vis[j] = True
            j = pos[arr[j]]
            cycle_size += 1
            
        if cycle_size > 0:
            swaps += cycle_size - 1
    return swaps
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


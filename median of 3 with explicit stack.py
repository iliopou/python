import time
import math
import numpy as np


def insertion_sort(arr, low, high):
    for j in range(low + 1, high + 1):  
        for i in range(j, low, -1):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            break


def median (arr, low, high):
    
    mid = math.floor((low + high) // 2 )
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]


def partition(arr, low, high):
    median (arr, low, high)
    pivot = arr[high]                   # median of 3 is the pivot   
     
    i, j = low - 1, high        
    while True:
        i += 1; j -= 1;
        while arr[i] < pivot:  
            i += 1
            # if i==high: break          # test can be discarded as i will stop on equal value(s) to pivot
        
        while arr[j] > pivot:
            j -= 1
            if j==low: break             # ensure j does not run out of bounds
        
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[i], arr[high] = arr[high], arr[i]
    return i
    

def quicksort_iterative (arr, low, high):
    stack = [(0, len(arr)-1)]
    while stack:                          # stack in worst case is of order of arr size
        low, high = stack.pop ()
       
        if high - low + 1 <= 6:
            insertion_sort (arr, low, high)
        
        p = partition (arr, low, high)
        if p - 1 > low:
            stack.append ((low, p - 1))
        if high > p + 1:
            stack.append ((p + 1, high))                           
        
        
         
######################### Testbed of median of 3 ######################

num_runs = 100
running_times = []
for i in range(num_runs):
  A = np.random.rand(pow(2, 16))
  start_time = time.time()
  quicksort_iterative (A, 0, np.size(A)-1)
  end_time = time.time()
  execution_time = end_time - start_time
  running_times.append(execution_time)
  

rounded_times = [round(t, 2) for t in running_times]
print("Execution times in seconds:", rounded_times)
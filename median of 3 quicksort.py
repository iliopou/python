import time
import math
import numpy as np


def insertion_sort(arr, low, high):
    for j in range(low + 1, high + 1):  
        for i in range(j, low, -1):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            else:
                break


def median (arr, low, high):                      # compute the median of elements at positions low, mid, high and place it at location high
    
    mid = math.floor((low + high) // 2 )
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]


def partition(arr, low, high):
    median (arr, low, high)
    pivot = arr[high]                               # median of 3 is the pivot   
     
    i, j = low - 1, high        
    while True:
        i += 1; j -= 1;
        while arr[i] < pivot:  
            i += 1
            #if i==high: break                     # test can be discarded as i will stop on equal value(s) to pivot
        
        while arr[j] > pivot:
            j -= 1
            if j==low: break                        # ensure j does not run out of bounds
        
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    
    while low < high: 
        if high - low + 1 <= 6:                 
            insertion_sort (arr, low, high)                  # Insertion sort small arrays each of size at most 6. Cutoff value of 6 selected experimentally.                          
        p = partition (arr, low, high)
        if p - low < high - p:                               # Recurse on smaller array in order to use at most log(arr size) stack space
            quicksort(arr, low, p - 1)
            low = p + 1
        quicksort(arr, p + 1, high)
        high = p - 1
        
    

######################### Testbed of median of 3 ######################

num_runs = 100
running_times = []
for i in range(num_runs):
  A = np.random.rand(pow(2, 16))
  start_time = time.time()
  quicksort(A, 0, np.size(A)-1)
  end_time = time.time()
  execution_time = end_time - start_time
  running_times.append(execution_time)

rounded_times = [round(t, 2) for t in running_times]
print("Execution times in seconds:", rounded_times)

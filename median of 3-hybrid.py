import time
import math
import numpy as np
import random

    
def insertion_sort(arr, low, high):
    for j in range(low + 1, high + 1):  
        for i in range(j, low, -1):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            else:
                break
                



def median(arr, low, high):                                # compute the median of elements at locations low, mid, high and place it at location high
    
    mid = math.floor((low + high) // 2 )
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

def partition(arr, low, high):
    i, j = low, high - 1;
    l = low
    pivot = arr[high]      
    
    while i <= j:                                           # 3-way partition. Smaller elements than pivot go to left, equal to middle, greater to the right
        if arr[i] < pivot:
            arr[l], arr[i] = arr[i], arr[l];
            i += 1; l += 1
        elif arr[i] > pivot:
            arr[i], arr[j] = arr[j], arr[i];
            j -= 1
        else:
            i += 1;
    
    arr[i], arr[high] = arr[high], arr[i]
    return l, i


def quicksort (arr, low, high):
    if low < high:                                         # if array has at least two elements
        if high - low + 1 <= 7:
            insertion_sort (arr, low, high) 
            return                                         # insertion sort small arrays
        
        elif high - low + 1 <= 50:                         # else if array has at most 50 elements quicksort on a randomly chosen pivot
            m = random.randint(low, high);                  
            arr[m], arr[high] = arr[high], arr[m]
        else:
            median(arr, low, high)                         # for large arrays use median of 3 quicksort
                                                           # cutoff values of 7 and 50 derived empirically. Optimal values?
        p, q = partition (arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, q+1, high)

   
######################### Testbed of median of 3-hybrid ######################

num_runs = 100
running_times = []
for i in range(num_runs):
  A = np.random.rand(pow(2, 15))                                  # if all n elements are equal (e.g. np.zeros) the algorithm sorts A with 2 x (n-1) comparisons
  start_time = time.time()                                        # test for various inputs
  quicksort(A, 0, np.size(A)-1)
  end_time = time.time()
  execution_time = end_time - start_time
  running_times.append(execution_time)

rounded_times = [round(t, 2) for t in running_times]
print("Execution times in seconds:", rounded_times)

import time
import numpy as np


    
def insertion_sort(A):    
 for j in range(1,len(A)):
     key  = A[j];
     i = j - 1;
     while (i >= 0 and A[i] > key):            
      A[(i + 1)] = A[i]
      i -= 1 
     A[(i + 1)] = key    


def lomuto_partition(A, lo, hi):
    pivot = A[hi]
    i = lo-1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    return i+1



def qsort(A, lo, hi):
    while (lo + 8 < hi):
        p = lomuto_partition(A, lo, hi);
        if (p-lo < hi-p):                                            # Tail call optimisation. Recur on smaller array and loop on bigger - O(log(n)) stack
            qsort(A, lo, p-1);
            lo = p + 1; 
        else: 
            qsort(A, p+1, hi);
            hi = p - 1;
    else:
     insertion_sort(A);                                                 # Arrays with at most 9 elements are sorted by insertion sort

'''''
num_runs = 100
running_times = []
for i in range(num_runs):
  A = np.random.rand(pow(2, 11))                                        # if all n elements are equal (e.g. np.zeros) the algorithm sorts A with 2 x (n-1) comparisons
  start_time = time.time()                                              # test for various inputs
  qsort (A, 0, np.size(A)-1)
  end_time = time.time()
  execution_time = end_time - start_time
  running_times.append(execution_time) 
  #print(f"Is A sorted? {is_sorted(A)}")    check

rounded_times = [round(t, 2) for t in running_times]
print("Execution times in seconds:", rounded_times)

'''
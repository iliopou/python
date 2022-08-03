from random import sample
from statistics import median

def insertion_sort(A):    
 for j in range(1,len(A)):
     key  = A[j];
     i = j - 1;
     while (i >= 0 and A[i] > key):            
      A[(i + 1)] = A[i]
      i -= 1 
     A[(i + 1)] = key    


def lomuto_partition(A, lo, hi):
    pivot = median(sample(A,3))                                    # Pivot is the median of a random sample of 3 keys
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
     insertion_sort(A);                                           # Arrays with at most 9 elements are sorted by insertion sort


arr = [3,4,5,0,-4,2,4,5,6,3,2,-1,-9,4,3,2,5,6,7,4,3,0,11111,6,22,3,44,-66,5,-77,-6,4,3,2,0,3,4,-33,4,11,2,33,6,7,8,9,-88,-900,8999]
n = len(arr)
qsort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")
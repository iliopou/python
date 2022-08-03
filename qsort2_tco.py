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

def Hoare_partition(A, lo, hi):
  pivot = A[lo];                                              # Pivot is the leftmost key of A
  i = lo-1; j = hi+1;
  while (True):
    i +=1
    while A[i] < pivot:
      i +=1
    j -=1 
    while A[j] > pivot:
      j -= 1
    if i>=j:
      return j 
    A[i], A[j] = A[j], A[i]
  
def qsort(A, lo, hi):
 while (lo + 8 < hi):                                                        # Arrays with at most 9 elements are sorted by insertion sort
  q = Hoare_partition(A, lo, hi);
  if q - lo < hi - q:                                                        # Recur on smaller subarray and loop on larger - at most log(n) stack frames
    qsort(A, lo, q-1); 
    lo = q + 1
  else:
   qsort(A, q+1, hi);
   hi = q - 1;
 else:
  insertion_sort(A);
                                            

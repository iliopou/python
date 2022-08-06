import random
from statistics import median 
import array as arr
A = arr.array('i')                                                                     # i - int in [-2^31, 2^31]

def insertion_sort(A):    
 for j in range (1,len(A)):
     key  = A[j];
     i = j - 1;
     while (i >= 0 and A[i] > key):            
      A[i + 1] = A[i]
      i -= 1 
     A[i + 1] = key 

def Hoare_partition(A, lo, hi):
  pivot = median(random.sample(A, 3)); 
  i = lo; j = hi; 
  while (i < j):
   while (A[i] < pivot):
    i += 1
   while (A[j] > pivot):
    j -= 1
   A[i], A[j] = A[j], A[i]; i +=1; j -= 1;
  return j
  
def qsort(A, lo, hi):
 while (lo + 8 < hi):                                                        # Arrays with at most 9 elements are sorted by insertion sort
  q = Hoare_partition(A, lo, hi);
  if (q - lo < hi - q):                                                      # Recur on smaller subarray and loop on larger - at most log(n) stack frames
    qsort(A, lo, q-1); 
    lo = q + 1
  else:
   qsort(A, q+1, hi);
   hi = q - 1
 else:
  insertion_sort(A)


import time
import numpy as np
from matplotlib import pyplot as plt
#import pdb

A = np.array('i'); 


def partition(A, lo, hi):
  i = lo; j = hi;
  pivot = A[lo];
  
  while (i < j):
   
    while A[i] < pivot:
      i +=1;
      
    while A[j] > pivot:
      j -= 1;
    
    if (i>=j):
      pivot, A[j] = A[j], pivot;    # At end of outer while loop swap pivot with key at position j. Quicksort is then recursively invoked on (lo, j - 1) and (j + 1, hi)
      return j; 
    A[i], A[j] = A[j], A[i]
      

    
def qsort(A, lo, hi):
 while (lo < hi):
  p = partition(A, lo, hi);
  if (p - lo < hi - p ):
    qsort(A, lo, p-1);
    lo = p + 1;
  else:
    qsort(A, p + 1, hi);
    hi = p - 1;


"""


##############################################################################################
############# Simple testbed of qsort2_tco ###################
#######################################################################################

elements = []
times = [] 


def is_sorted(A):                              # check
    for i in range(0, np.size(A) - 1):
         if A[i] > A[i + 1] :
               return False
    return True

for i in range(1, 4):
  A = np.random.rand(pow(10, 6) * i);
  startTime = time.time();
  qsort(A, 0, np.size(A)-1);
  executionTime = (time.time() - startTime);
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)

plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='qsort2_tco')
plt.grid()
plt.legend()
plt.show()

"""

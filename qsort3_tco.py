import numpy as np
from matplotlib import pyplot as plt
import time
#import pdb

A = np.array('i')  



def Hoare_partition(A, lo, hi):
  i = lo; j = hi;
  pivot = A[(hi + lo) // 2];   # Pick pivot the element of A that is on the middle of the array
  
  while True:
    
    while A[i] < pivot:
      i +=1;
    
    while A[j] > pivot:
      j -= 1;
    
    if (i >= j):
      return j;
    A[i], A[j] = A[j], A[i];
  

    
  
def qsort(A, lo, hi):
 while (lo < hi):
  p = Hoare_partition(A, lo, hi);
  if (p - lo < hi - p - 1):
    qsort(A, lo, p);
    lo = p + 1;
  else:
    qsort(A, p + 1, hi);
    hi = p - 1;


 

#"""

##############################################################################################
############# Simple testbed of qsort3_tco ###################
#######################################################################################

elements = []
times = [] 


def is_sorted(A):                                   #Check
  for i in range(0, np.size(A)-1):
    if A[i+1] < A[i]:
      return False
  return True

for i in range(1, 4):

  A = np.random.rand(pow(10, 6) * i)
  startTime = time.time()
  qsort(A, 0, np.size(A)- 1)
  #pdb.set_trace()
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)
  
plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='qsort3_tco')
plt.grid()
plt.legend()
plt.show()

#"""

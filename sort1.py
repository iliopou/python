import numpy as np
from matplotlib import pyplot as plt
#import pdb
import time

A = np.array('i');                                                                

def insertion_sort(A):
  for j in range (1, np.size(A)):
    key  = A[j];
    i = j - 1;
    while (i >= 0 and A[i] > key):
      A[i + 1] = A[i];
      i -= 1;
    A[i + 1] = key;

#pdb.set_trace()

def partition(A, lo, hi):
  if (lo >= hi):
    return;
  m = np.random.randint(lo, hi); A[lo], A[m] = A[m], A[lo];    # Randomly choose index m and swap A[m] with leftmost element A[lo] 
  pivot = A[lo]; left = i = lo; right = hi;                    # to mitigate worst case occurrence (when pivot is the smallest or largest key - consider array 1,2,.., n)
  while (i <= right):
    if A[i] < pivot:
      A[left], A[i] = A[i], A[left];
      left += 1; i += 1;
    elif A[i] > pivot:
      A[i], A[right] = A[right], A[i];
      right -= 1;
    else:
      i += 1;
  return left, right;                                            # 3-way partition



def qsort(A, lo, hi):                                # Quicksort applied when array size is >= 20
  if (lo + 18 < hi):
    left, right = partition (A, lo, hi)
    qsort(A, lo, left - 1);
    qsort(A, right + 1, hi);
                           

                                            
def sort1(A, lo, hi):
  qsort(A, lo, hi);
  insertion_sort(A)                                 # Complete sorting with final pass of straight insertion

##############################################################################################
################ Simple testbed of sort1 ##################
##############################################################################################

elements = []
times = [] 


def is_sorted(A):                                   #Check
  for i in range(0, np.size(A)-1):
    if A[i+1] < A[i]:
      return False
  return True

for i in range(10, 21):

  A = np.random.rand(pow(10, 6) * i)
  startTime = time.time()
  sort1(A, 0, np.size(A) - 1)
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)
  
plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='sort1')
plt.grid()
plt.legend()
plt.show()

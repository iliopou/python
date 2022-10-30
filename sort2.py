import numpy as np
from matplotlib import pyplot as plt
from collections import deque
#import pdb
import time
import math


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
       A[i], A[right] = A[right], A[i];                        # 3-way partition
       right -= 1;
    else:
       i += 1;
  return left, right;

def qsort_iterative(A, lo, hi):
  if (lo + 18 < hi):                                                    # Cutoff value 18
   stack = deque([], maxlen=math.ceil(math.log2(np.size(A))));          # Programmed stack with max length set to ceiling of log2(size of array)
   stack.append((lo, hi));
   while stack:
    ((lo, hi)) = stack.pop();
    left, right = partition(A, lo, hi);
    if (left - 1 - lo > 18):                                                  
      if (hi - right > left - lo):
        stack.append((right + 1, hi));                                 # Always push first the larger partition to stack to ensure max stack size log2(size of array)
        stack.append((lo, left - 1)); 
      elif (hi - right - 1 > 18):
        stack.append((lo, left - 1));
        stack.append((right + 1, hi));
      else:
        stack.append((lo, left- 1));
    elif (hi - right - 1 > 18):
      stack.append((right + 1, hi)); 


def sort2(A, lo, hi):
  qsort_iterative(A, lo, hi);
  insertion_sort(A)                                               # Complete sorting by insertion sort.


         

##############################################################################################
############# Simple testbed of sort2 ###################
#######################################################################################

elements = []
times = [] 


def is_sorted(A):                              # check
    for i in range(0, np.size(A) - 1):
         if A[i] > A[i + 1] :
               return False
    return True

for i in range(10, 21):
  A = np.random.rand(pow(10, 6) * i);
  startTime = time.time();
  sort2(A, 0, np.size(A)-1);
  executionTime = (time.time() - startTime);
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)

plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='sort2')
plt.grid()
plt.legend()
plt.show()



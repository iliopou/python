def insertion_sort(A):    
 for j in range(1, len(A)):
    for i in range(j, 0, -1):
      if A[i] < A[i-1]:
        A[i-1], A[i] = A[i], A[i-1]
      else:
        break


""" 
import time
import numpy as np
from matplotlib import pyplot as plt

elements = list()
times = list()   

def is_sorted(A):                                   # Check
  for i in range(0, np.size(A)-1):
    if A[i+1] < A[i]:
      return False
  return True

for i in range(0, 100):

  A = np.random.rand(pow(10, 2) * i)
  startTime = time.time()
  insertion_sort(A)
  #pdb.set_trace()
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)
  
plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='Insertion sort')
plt.grid()
plt.legend()
plt.show()

"""



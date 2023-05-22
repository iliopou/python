import math


def shellsort(A): 
    for t in range(1, math.ceil(math.log2(len(A) + 1))):   
      m = math.floor(len(A)/pow(2, t));                    # gap sequence floor(len(A)/2), floor(len(A)/4), ..., 1
      for j in range(m, len(A)):
        for i in range(j, 0, -m):
          if A[i] < A[i-m]:
            A[i-m], A[i] = A[i], A[i-m];
          else:
            break;
    

  

"""

import time
import numpy as np
from matplotlib import pyplot as plt

elements = list()
times = list()   


#def is_sorted(A):                                   #Check
#  for i in range(0, np.size(A)-1):
#    if A[i+1] < A[i]:
#      return False
#  return True

for i in range(0, 100):

  A = np.random.rand(pow(10, 1) * i)   
  startTime = time.time()
  shellsort(A)
  #pdb.set_trace()
  executionTime = (time.time() - startTime)
  print('Execution time in seconds: ' + str(executionTime))
  print('Is A sorted? ' + str(is_sorted(A)))
  elements.append(np.size(A))
  times.append(executionTime)
  
plt.xlabel('Array length')
plt.ylabel('Running time in seconds')
plt.plot(elements, times, label ='Shellsort')
plt.grid()
plt.legend()
plt.show()

"""



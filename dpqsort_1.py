import array as arr                                                        # Dual pivot quicksort with Yaroslavskiy's partition algorithm
A = arr.array('i')                                                         # https://codeblab.com/wp-content/uploads/2009/09/DualPivotQuicksort.pdf
																		   
def insertion_sort(A):    
 for j in range (1,len(A)):
     key  = A[j];
     i = j - 1;
     while (i >= 0 and A[i] > key):            
      A[i + 1] = A[i]
      i -= 1 
     A[i + 1] = key 

def partition(A, lo, hi):
	if A[lo] > A[hi]:
		A[lo], A[hi] = A[hi], A[lo];
	p = A[lo]; q = A[hi];
	l = lo + 1; i = l; r = hi - 1;
	
	while i <= r:
		if A[i] < p:                                 
			A[i], A[l] = A[l], A[i]                                                   
			l += 1
		elif A[i] >= q:
			while A[r] > q: 
				r -= 1;
			if i < r:
				if A[r] < p:
					A[i], A[r] = A[r], A[i]; 
					r -= 1;
			if A[i] < p:
				A[i], A[l] = A[l], A[i];
				l += 1;
		i += 1;
	l -= 1;
	r += 1;
	A[lo], A[l] = A[l], A[lo];
	A[r], A[hi] = A[hi], A[r];
	return l, r
    
    
def dpqsort_Yaro(A, lo, hi):
	if lo + 18 < hi:                                                           
		l, r = partition(A, lo, hi)
		dpqsort_Yaro(A, lo, l - 1)
		dpqsort_Yaro(A, l + 1, r - 1)
		dpqsort_Yaro(A, r + 1, hi)
	else:                                                                      # Use insertion sort for small arrays. cutoff parameter is 18
		insertion_sort(A)

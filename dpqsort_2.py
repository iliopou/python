import array as arr                                           # Dual pivot quicksort, In this partitioning algorithm, each key smaller to 'small' pivot p
A = arr.array('i')                                            # is compared once with p. Every other key is compared twice with p and q (the 'large' pivot)
                                                              # Comparison count identical to one pivot Quicksort - see http://repository.essex.ac.uk/13266/1/iliop%20thesis.pdf
def insertion_sort(A):    
 for j in range (1,len(A)):
     key  = A[j];
     i = j - 1;
     while (i >= 0 and A[i] > key):            
      A[i + 1] = A[i]
      i -= 1 
     A[i + 1] = key 

def partition(A, lo, hi):
	if (A[lo] > A[hi]):
		A[lo], A[hi] = A[hi], A[lo];
	p = A[lo]; q = A[hi];                     # p <= q
	l = lo + 1; i = l; r = hi - 1;
	
	while i <= r:
		if A[i] < p:                                                                     
			A[i], A[l] = A[l], A[i]         # swap to left elements less than 'small' pivot                                          
			l+= 1
		elif A[i] >= q:                                              
			while A[r] < p: 
				r -= 1;
			if i < r:
				if A[r] < q:
					A[i], A[r] = A[r], A[i];   # swap to right elements at least as large as the 'large' pivot
					r -= 1;
		i += 1;	
	l -= 1;
	r += 1;			
				
	A[lo], A[l] = A[l], A[lo];                                      # put pivots in place
	A[r], A[hi] = A[hi], A[r];
	return l, r                                                     # return pivots' indices
    

def dpqsort(A, lo, hi):
	if lo + 18 < hi:                                                           
		l, r = partition(A, lo, hi)
		dpqsort(A, lo, l - 1)
		dpqsort(A, l + 1, r - 1)
		dpqsort(A, r + 1, hi)
	else:                                                             # Use insertion sort for small arrays. cutoff parameter is 18
		insertion_sort(A)


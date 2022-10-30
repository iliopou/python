This repository contains various python scripts.

Added on 20220803 an optimised quicksort using tail call optimisation (qsort_tco.py).

The algorithm is recursively called on smaller sub array and 
looped on the larger one. This ensures using no more than log(n)
stack frames for sorting n keys.

Another characteristic of this algorithm is that for sorting small arrays,
insertion sort is used. The cutoff point is array size equal to 9.

Added on 20220803: another version added (qsort_tco1.py) with the difference that pivot is 
the median of a random sample of 3 keys from the array to be quicksorted. In the script qsort2_tco.py
Hoare's original partition algorithm is used where on average it makes a third of the number of exchanges
made by the partition algorithm of the other two scripts (qsort_tco.py and qsort_tco1.py). In these two scripts Lomuto's partition
algorithm is used. 


Added on 20220804: In qsort3_tco.py while loops are changed (adding AND) to test for crossing pointers in either branch.

Added on 20220806: two quicksort scripts qsort4_tco.py and qsort5_tco.py. Compare their partition functions.

Added on 20220807: two dual pivot quicksort algorithms.

Added on 20221030: sort1.py and sort2.py. Both algorithms use 3-way partition and switch to insertion sort 
below a cutoff number. sort2 utilises iterative
quicksort with an explicit stack of size at most
the (base 2) logarithm of array size. In both scripts I have used
a simple test bed for experiments on the running
times with various input arrays.

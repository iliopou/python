This repository contains various python scripts.

Added on 20220803 an optimised quicksort using tail call optimisation (qsort_tco.py).

The algorithm is recursively called on smaller sub array and 
looped on the larger one. This ensures using no more than log(n)
stack frames for sorting n keys.

Another characteristic of this algorithm is that for sorting small arrays,
insertion sort is used. The cutoff point is array size equal to 9.

Added on 20220803: another version added (qsort_tco1.py) with the difference that pivot is 
the median of a random sample of 3 keys from the array to be quicksorted. In the script qsort_tco2.r
Hoare's original partition algorithm is used where on average it makes a third of the number of exchanges
made by the partition algorithm of the other two scripts (qsort_tco.r and qsort_tco1.r). In these two scripts Lomuto's partition
algorithm is used. 

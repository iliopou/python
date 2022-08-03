This repository contains various python scripts.

Added on 20220803 an optimised quicksort using tail call optimisation.

The algorithm is recursively called on smaller sub array and 
looped on the larger one. This ensures using no more than log(n)
stack frames for sorting n keys.

Another characteristic of this algorithm is that for sorting small arrays,
insertion sort is used. The cutoff point is array size equal to 9.

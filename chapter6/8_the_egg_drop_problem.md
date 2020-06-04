# The Egg Drop Problem

## Question

There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break. If it's dropped from any floor below, it will not break. You're given two eggs. Find N, while minimizing the number of drops for the worst case. 

## Answer

Partition the building floors into a sorted list of half-open intervals I_k = (a_k, b_k]. Use the first egg to find the correct interval (for increasing values of k, drop it at b_k; if it breaks, N is in I_k), and use the second egg to find the correct floor (drop it on every floor in I_k starting at the lowest and moving up; the floor where it breaks is N).

Naively, we can split into 10 intervals I_k = (10 * k, 10 * (k + 1)], where k = 0 to 9. In the worst case, N = 100, we will take 19 drops (dropping on floors 10, 20, ..., 90, 100, 91, 92, ..., 98, 99).

We will get the optimal partitioning when we make the size of the intervals decrease by 1 as we increase k by 1. This way, the number of drops of the second egg needed to find N in the worst case (N = b_k) remains the same even as we go up.

Let x be the floor of the first drop. Then we want to partition the floors such that x + (x - 1) + (x - 2) + (x - 3) + ... + 2 + 1 >= 100 ==> x (x + 1) / 2 >= 100 ==> k = 14.

Thus, consider this set of b_k: {14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99}. In the worst case for each of the corresponding intervals, N = b_k, we will take 14 drops. (If it cracks on none of the intervals, we will also test to see if N=12; either way, this takes 12 drops).

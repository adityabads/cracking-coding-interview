# Poison

## Question

You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible?

FOLLOW UP:
Write code to simulate your approach.

See code in `10_poison.py`.

## Answer

Enumerate the 1000 bottles and look at the binary representation. For each bottle, put a drop on test strip i iff there is a 1 in the ith digit. This is possible because 1000 < 2^10. Wait seven days and read the results. The bottle has binary representation such that there is a 1 in the ith digit iff test strip i is poisoned.

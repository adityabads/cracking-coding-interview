# The Heavy Pill

## Question

You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once.

## Answer

Enumerate the bottles from 1 through 20 inclusive, and for each bottle `i`, put `i` pills from that bottle onto the scale. If bottle `i` has the 1.1 gram pills, then we would expect a measurement of 1 + 2 + ... + 20 + 0.1 \* i = 210 + 0.1 \* i = m ==> i = (m - 210) \* 10. Thus, no matter which bottle `i` contains the heavy pills, we would be able to solve for it.

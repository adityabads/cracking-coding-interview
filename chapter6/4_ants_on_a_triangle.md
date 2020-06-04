# Ants on a Triangle

## Question

There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed. Similarly, find the probability of collision with n ants on an n-vertex polygon.

## Answer

The only cases when the ants will not collide are when they all pick the same direction. There are 2 directions for the each of them to pick, so this probability is 2 \* (1/2)^3 = 1/4. The probability they collide is therefore 1 - 1/4 = 3/4.

With n ants, the probability they collide is 1 - 2 \* (1/2)^n = 1 - (1/2)^(n-1).

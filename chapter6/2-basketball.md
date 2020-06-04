# Basketball

## Question

You have a basketball hoop and someone says that you can play one of two games.

1. You get one shot to make the hoop.
2. You get three shots and you have to make two of three shots.

If p is the probability of making a particular shot, for which values of p should you pick one game or the other?

## Answer

The odds of winning the first game are p, and the odds of winning the second are p^3 + 3p^2. I should pick the first game when p > p^3 + 3p^2(1-p) ==> 2p^3 - 3p^2 + p > 0 ==> p(2p - 1)(p - 1) < 0

Thus, when p is between 1/2 and 1, we should prefer the first game. When p = 0, or p = 1/2, or p = 1, the two games are equivalent.

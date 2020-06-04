# The Apocalypse

## Question

In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy — that is, they have continue to have
children until they have one girl, at which point they immediately stop — what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.

## Answer

See the corresponding `.py` file for the code.

Let's find the expected value of the number of boys and girls birthed by an arbitrary family.

The probability 1 girl is born is 1, and the probability any other number of girls is born is 0. So the expected number of girls born is 1.

The probability 0 boys is born is 1/2, the probability exactly 1 is born is 1/4, the probability exactly 2 are born is 1/8, and so on. So the expected number of boys born is

sum\_{i=0}^{infinity} [i \* (1/2)^(i+1)] = 1

So the expected ratio of girls to boys is 1:1.

# The Apocalypse

## Question

In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy — that is, they have continue to have children until they have one girl, at which point they immediately stop — what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.

## Answer

See the corresponding `.py` file for the code.

The expected gender ratio of the new generation is 1:1. Intuitively, the birthing policy each family uses doesn't change biology; there will still be an equal chance of birthing a boy or a girl.

In other words, the division of families is arbitrary, so no birthing policy will affect the boy-girl ratio. If we represent boys with "B" and girls with "G", we can assign each family a string to represent their children. For example, a family that births two boys before a girl will be represented by "BBG". When calculating the total number of boys and girls, we can concatenate the strings in any order we like. We can understand this overall string as: when one family stops having kids because they had a girl, another family immediately starts having kids. In other words, the division of families doesn't matter; the sequence of births is unaffected by any family's birthing policy. If a family births a boy, they have an equal chance of birthing a boy or girl next. If a family births a girl, even though they stop having kids, the next family in the sequence will still have an equal chance of birthing a boy or girl.

We can also solve this mathematically by finding expected values of the number of girls and boy each individual family births.

The probability 1 girl is born is 1, and the probability any other number of girls is born is 0. So the expected number of girls born is 1.

The probability 0 boys is born is 1/2, the probability exactly 1 is born is 1/4, the probability exactly 2 are born is 1/8, and so on. So the expected number of boys born is:

sum\_{i=0}^{infinity} [i \* (1/2)^(i+1)] = 1

Thus, the expected ratio of girls to boys is 1:1.

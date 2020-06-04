# The Apocalypse
# In the new post-apocalyptic world, the world queen is desperately concerned
# about the birth rate. Therefore, she decrees that all families should ensure
# that they have one girl or else they face massive fines. If all families
# abide by this policy — that is, they have continue to have children until
# they have one girl, at which point they immediately stop — what will the
# gender ratio of the new generation be? (Assume that the odds of someone
# having a boy or a girl on any given pregnancy is equal.) Solve this out
# logically and then write a computer simulation of it.

# See the corresponding `.md` file for the mathematical answer.

import random


def fails_until_success() -> int:
    """Returns number of failures until success, P(fail) = P(succeed) = 1/2"""
    i = 0
    while not random.getrandbits(1):
        i += 1
    return i


def average_fails_until_success(k: int) -> float:
    """Returns average number of failures until success over `k` trials, 
    where P(fail) = P(succeed) = 1/2"""
    sum_ = 0
    for _ in range(k):
        sum_ += fails_until_success()
    return sum_ / k


if __name__ == "__main__":
    for i in range(5):
        print(average_fails_until_success(1000))

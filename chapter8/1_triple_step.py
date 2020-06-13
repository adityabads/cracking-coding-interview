# Triple Step
# A child is running up a staircase with n steps and can hop either 1 step,
# 2 steps, or 3 steps at a time. Implement a method to count how many possible
# ways the child can run up the stairs.

import unittest

# f(n) =    1,                              n == 1
#           2,                              n == 2
#           4,                              n == 3
#           f(n - 1) + f(n - 2) + f(n - 3), otherwise


def triple_step_recursive(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return triple_step_recursive(n - 1) + triple_step_recursive(n - 2) + triple_step_recursive(n - 3)


def triple_step_memo(n: int, memo=None) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    if memo is None:
        memo = [None] * (n + 1)
    if memo[n] is None:
        memo[n] = triple_step_memo(n - 1, memo) + triple_step_memo(n - 2, memo) + \
            triple_step_memo(n - 3, memo)
    return memo[n]


def triple_step_dp(n: int) -> int:
    dp = [0, 1, 2, 4]
    if n in range(3):
        return dp[n]
    for i in range(4, n + 1):
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = dp[3]
        dp[3] = dp[0] + dp[1] + dp[2]
    return dp[3]


class TestTripleStep(unittest.TestCase):
    def test_triple_step(self):
        tests = [
            [1, 1],
            [2, 2],
            [3, 4],
            [4, 7],
            [5, 13]
        ]
        for n, ways in tests:
            with self.subTest(n=n):
                self.assertEqual(triple_step_recursive(n), ways)
                self.assertEqual(triple_step_memo(n), ways)
                self.assertEqual(triple_step_dp(n), ways)


if __name__ == "__main__":
    unittest.main()

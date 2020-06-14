# Poison
# You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test
# strips which can be used to detect poison. A single drop of poison will turn
# the test strip positive permanently. You can put any number of drops on a
# test strip at once and you can reuse a test strip as many times as you'd like
# (as long as the results are negative). However, you can only run tests once
# per day and it takes seven days to return a result. How would you figure out
# the poisoned bottle in as few days as possible?

# FOLLOW UP:
# Write code to simulate your approach.
#
# See answer in `10_poison.md`.

import random
import unittest


class Poison:
    def __init__(self, poisoned):
        if poisoned < 1 or poisoned > 1000:
            raise Exception("Bottle must be between 1 and 1000")
        self.poisoned = poisoned
        self.strips = [set() for _ in range(10)]
        self.results = [False] * 10

    def do_all(self) -> int:
        """Sets up, runs, and interprets tests"""
        self.set_up_tests()
        self.run_tests()
        return self.interpret_tests()

    def set_up_tests(self) -> None:
        """Sets up test strips as described in `10_poison.md`"""
        for bottle in range(1, 1001):
            num = bottle
            i = 0
            while num > 0:
                if (num & 1) == 1:
                    self.strips[i].add(bottle)
                num >>= 1
                i += 1

    def run_tests(self) -> None:
        """Runs tests results, to be called 7 days later"""
        for i in range(10):
            if self.poisoned in self.strips[i]:
                self.results[i] = True

    def interpret_tests(self) -> int:
        """Returns poisoned bottle"""
        num = 0
        for i in reversed(range(10)):
            num <<= 1
            num += int(self.results[i])
        return num


class TestPoison(unittest.TestCase):
    def test_poison(self):
        for i in range(20):
            poisoned = random.randint(1, 1000)
            poisontest = Poison(poisoned)
            self.assertEqual(poisontest.do_all(), poisoned)


if __name__ == "__main__":
    unittest.main()

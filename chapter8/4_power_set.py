# Power Set
# Write a method to return all subsets of a set


from typing import List, Set
import unittest

# f(s = {s1, s2, ..., sn}) =    {{}},                           len(s) = 0
#                               {s, f(s - {si}) for si in s},   otherwise


def power_set(s: Set) -> List[Set]:
    """Returns power set of s"""
    sets = _power_set_util(s)
    sets.add(())
    return sets


def _power_set_util(s: Set) -> Set[List]:
    if len(s) == 0:
        return set()
    sets = {tuple(s)}
    for si in s:
        for subset in _power_set_util(s.difference({si})):
            sets.add(tuple(subset))
    return sets


class TestPowerSet(unittest.TestCase):
    def test_power_set(self):
        print(power_set(set()))
        print(power_set({1}))
        print(power_set({1, 2}))
        print(power_set({1, 2, 3}))
        print(power_set({5, 2, 3, 1}))


if __name__ == "__main__":
    unittest.main()

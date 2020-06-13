# Power Set
# Write a method to return all subsets of a set

from typing import Dict, List, Set, Tuple
import unittest

# f(s = {s1, s2, ..., sn}) =    {{}},                           len(s) = 0
#                               {s, f(s - {si}) for si in s},   otherwise


def power_set(s: Set) -> List[Set]:
    """Returns power set of s"""
    sets = _power_set_util(s)
    sets.add(())
    return [set(set_) for set_ in sets]


def _power_set_util(s: Set) -> Set[Tuple]:
    if not s:
        return set()
    sets = {tuple(s)}
    for si in s:
        subsets = _power_set_util(s.difference({si}))
        for subset in subsets:
            if subset:
                sets.add(tuple(subset))
    return sets


def power_set_memo(s: Set) -> List[Set]:
    """Returns power set of s"""
    sets = _power_set_memo_util(s)
    sets.append(set())
    return sets


def _power_set_memo_util(s: Set, memo: Dict[Tuple, List[Set]] = None) -> List[Set]:
    if not s:
        return []
    if memo is None:
        memo = {}
    sets = [s]
    for si in s:
        s_minus_si = s.difference({si})
        tuple_s_minus_si = tuple(s_minus_si)
        if tuple_s_minus_si not in memo:
            memo[tuple_s_minus_si] = _power_set_memo_util(s_minus_si, memo)
            sets.extend(
                [subset for subset in memo[tuple_s_minus_si] if subset])
    return sets


class TestPowerSet(unittest.TestCase):
    def test_power_set(self):
        sets = [
            {},
            {1},
            {1, 2},
            {2, 1, 3},
            {5, 2, 3, 1}
        ]
        for set_ in sets:
            print(power_set(set_))
            print(power_set_memo(set_))


if __name__ == "__main__":
    unittest.main()

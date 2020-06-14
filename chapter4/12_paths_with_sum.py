# Paths with Sum
# You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an algorithm to count the
# number of paths that sum to a given value. The path does not need to start
# or end at the root or a leaf, but it must go downwards (traveling only
# from parent nodes to child nodes).

from collections import defaultdict
from mybinarytree import TreeNode, make_binary_tree
from typing import Dict, List
import unittest

def subarrays_with_sum_k(arr: List[int], k: int) -> int:
    """Returns number of consecutive subarrays summing to k"""
    sums = defaultdict(int)
    rolling_sum = 0
    result = 0
    for val in arr:
        rolling_sum += val
        if rolling_sum == k:
            result += 1
        result += sums[rolling_sum - k]
        sums[rolling_sum] += 1
    return result


def paths_with_sum(root: TreeNode, k: int, rolling_sum: int = 0,
                   sums: Dict[int, int] = None) -> int:
    """Returns number of paths with given sum"""
    if not root:
        return 0

    if not sums:
        sums = defaultdict(int)

    # modified DFS
    rolling_sum += root.val
    result = 0
    if rolling_sum == k:
        result += 1
    result += sums[rolling_sum - k]

    sums[rolling_sum] += 1
    result += paths_with_sum(root.left, k, rolling_sum, sums)
    result += paths_with_sum(root.right, k, rolling_sum, sums)
    sums[rolling_sum] -= 1
    return result


class TestPathsWithSum(unittest.TestCase):
    def test_paths_with_sum(self):
        tree = make_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(paths_with_sum(tree, 8), 3)

    def test_sum_to_k(self):
        tests = [
            [[1, 2, 1, 3], 3, 3],
            [[1, 2, 2], 4, 1],
            [[1, 1, 1], 2, 2],
            [[4, 3, 5, 9], 2, 0],
            [[1, 3, 4, -2, -5, 1, 3], 4, 4],
            [[1, 3, 4, -2, -5, -3, 1, 3], 4, 3]
        ]
        for arr, k, expected in tests:
            self.assertEqual(subarrays_with_sum_k(arr, k), expected)


if __name__ == "__main__":
    unittest.main()

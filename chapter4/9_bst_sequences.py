# BST Sequences: A binary search tree was created by traversing through an array
# from left to right and inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could have led to this tree.
#
# EXAMPLE
# Input:      2
#           1   3
#
# Output: {2, 1, 3}, {2, 3, 1}

from collections import deque
from mybinarytree import TreeNode, make_binary_tree
from typing import List
import unittest.result


def bst_sequences(root: TreeNode) -> List[List[int]]:
    result = []
    if not root:
        result.append([])
        return result

    prefix = [root.val]
    leftseqs = bst_sequences(root.left)
    rightseqs = bst_sequences(root.right)
    for leftseq in leftseqs:
        for rightseq in rightseqs:
            tempresults = []
            interleave(leftseq, rightseq, tempresults, prefix)
            result.extend(tempresults)
    return result


def interleave(leftseq: List[int], rightseq: List[int],
               results: List[List[int]], prefix: List[int]) -> None:
    if not leftseq or not rightseq:
        result = prefix.copy()
        result.extend(leftseq)
        result.extend(rightseq)
        results.append(result)
        return

    head = leftseq.pop(0)
    prefix.append(head)
    interleave(leftseq, rightseq, results, prefix)
    prefix.pop()
    leftseq.insert(0, head)

    head = rightseq.pop(0)
    prefix.append(head)
    interleave(leftseq, rightseq, results, prefix)
    prefix.pop()
    rightseq.insert(0, head)


class TestBSTSequences(unittest.TestCase):
    def test_bst_sequences(self):
        arrs = [[i for i in range(1, j + 1)] for j in range(1, 6)]
        for arr in arrs:
            tree = make_binary_tree(arr)
            print(bst_sequences(tree))


if __name__ == "__main__":
    unittest.main()

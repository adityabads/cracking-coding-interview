# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
#
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

from collections import deque
from mygraph import Graph
from typing import List
import unittest


def topological_sort(G: Graph) -> List[int]:
    """Topologically sorts graph G"""
    # modified DFS
    topological_order = deque()
    visited = [False] * (len(G) + 1)
    for i in range(1, len(G) + 1):
        topological_stack = []
        if not visited[i]:
            stack = [G.nodes[i]]
            while stack:
                n = stack.pop()
                if not visited[n.val]:
                    topological_stack.append(n.val)
                    visited[n.val] = True
                    for neighbor in reversed(n.neighbors):
                        stack.append(neighbor)
        while topological_stack:
            topological_order.appendleft(topological_stack.pop())
    return list(topological_order)


class TestBuildOrder(unittest.TestCase):
    def test_topological_sort(self):
        G = Graph(6, [(1, 4), (6, 2), (2, 4), (6, 1), (4, 3)])
        print(topological_sort(G))
        G = Graph(8, [(1, 3), (1, 4), (2, 4), (3, 4), (3, 5),
                      (5, 8), (6, 5), (6, 7), (7, 8)])
        print(topological_sort(G))


if __name__ == "__main__":
    unittest.main()

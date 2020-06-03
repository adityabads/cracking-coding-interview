# Route Between Nodes
# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

from mygraph import Graph
import unittest


def is_route(G: Graph, root: int, goal: int) -> bool:
    """Returns true iff there is a route between root and goal in graph G"""
    return G.dfs_iterative(root, goal)


class TestRouteBetweenNodes(unittest.TestCase):
    def test_is_route(self):
        G = Graph(6, [(1, 2), (2, 3), (1, 4), (5, 6), (6, 5)])
        for u in [1, 2, 3, 4]:
            for v in [5, 6]:
                with self.subTest(u=u, v=v):
                    self.assertFalse(is_route(G, u, v))
                    self.assertFalse(is_route(G, v, u))
        for (u, v) in [(1, 2), (2, 3), (1, 4)]:
            with self.subTest(u=u, v=v):
                self.assertTrue(is_route(G, u, v))
                self.assertFalse(is_route(G, v, u))
        self.assertTrue(is_route(G, 5, 6))
        self.assertTrue(is_route(G, 6, 5))


if __name__ == "__main__":
    unittest.main()

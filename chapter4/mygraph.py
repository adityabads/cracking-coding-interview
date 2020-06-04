from collections import deque
from typing import List, Tuple, Union
import unittest


class Node:
    """Node class for graph"""

    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def __str__(self):
        return str(self.val)


class Graph:
    """Graph class"""

    def __init__(self, n: int, edges: List[Tuple[int, int]], undirected=False):
        """Inits graph with nodes {1, ..., n} and edges {(u, v)}"""
        self.nodes = [None]
        self.nodes.extend([Node(i) for i in range(1, n+1)])
        for (u, v) in edges:
            self.add_edge(u, v)
            if undirected:
                self.add_edge(v, u)

    def __len__(self):
        return len(self.nodes) - 1

    def __str__(self):
        edges = []
        for node in self.nodes:
            for neighbor in node.neighbors:
                edges.append(map(str, [node, neighbor]))
        return " ".join(edges)

    def add_edge(self, u: int, v: int) -> None:
        """Adds edge (u, v) to graph"""
        self.nodes[u].neighbors.append(self.nodes[v])

    def bfs(self, root: int) -> None:
        """Breadth-first search from root"""
        # Validate input
        if root < 1 or root > len(self):
            raise IndexError("bfs() called on out of bounds root")

        # BFS
        rootnode = self.nodes[root]
        visited = [False] * (len(self) + 1)
        print(rootnode, end=" ")
        visited[root] = True
        q = deque([rootnode])
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if not visited[neighbor.val]:
                    print(neighbor, end=" ")
                    visited[neighbor.val] = True
                    q.append(neighbor)
        print()

    def dfs_iterative(self, root: int, goal: int = None) -> bool:
        """Depth-first search for goal from root, iteratively"""
        # Validate input
        if root < 1 or root > len(self):
            raise IndexError("dfs_iterative() called on out of bounds root")

        # DFS
        visited = [False] * (len(self) + 1)
        stack = [self.nodes[root]]
        while stack:
            n = stack.pop()
            if not visited[n.val]:
                print(n, end=" ")
                visited[n.val] = True
                for neighbor in reversed(n.neighbors):
                    stack.append(neighbor)
        print()

    def dfs_recursive(self, root: int) -> None:
        """Depth-first search from root, recursively"""
        if root < 1 or root > len(self):
            raise IndexError(
                "dfs_recursive() called on out of bounds root")
        visited = [False] * (len(self) + 1)
        Graph._dfs_util(self.nodes[root], visited)
        print()

    @staticmethod
    def _dfs_util(n: Node, visited: List[bool]) -> None:
        if n is not None and not visited[n.val]:
            print(n, end=" ")
            visited[n.val] = True
            for neighbor in n.neighbors:
                Graph._dfs_util(neighbor, visited)


class TestGraph(unittest.TestCase):
    def test_graph(self):
        G = Graph(6, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)])
        G.bfs(1)
        G.dfs_iterative(1)
        G.dfs_recursive(1)


if __name__ == "__main__":
    unittest.main()

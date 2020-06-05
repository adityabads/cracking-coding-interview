from mybinarytree import TreeNode, level_traverse_iterative
import unittest


def make_bst(arr) -> TreeNode:
    """Returns a binary search tree made by inserting values in `arr` in order"""
    root = None
    if arr:
        for val in arr:
            root = insert_into_bst(root, val)
    return root


def insert_into_bst(root: TreeNode, val) -> None:
    """Inserts `n` into binary search tree with root `root`"""
    if root is None:
        root = TreeNode(val)
    elif val <= root.val:
        root.left = insert_into_bst(root.left, val)
        if root.left is not None:
            root.left.parent = root
            root.size += 1
    else:
        root.right = insert_into_bst(root.right, val)
        if root.right is not None:
            root.right.parent = root
            root.size += 1
    return root


def is_in_bst_iterative(root: TreeNode, val) -> bool:
    """Returns true iff `val` is in binary search tree with root `root`, iteratively"""
    while root is not None:
        if val == root.val:
            return True
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return False


def is_in_bst_recursive(root: TreeNode, val) -> bool:
    """Returns true iff `val` is in binary search tree with root `root`, recursively"""
    if root is None:
        return False
    if val == root.val:
        return True
    elif val < root.val:
        return is_in_bst_recursive(root.left, val)
    else:
        return is_in_bst_recursive(root.right, val)


class TestBST(unittest.TestCase):
    def test_bst(self):
        arrs = [
            [2, 1, 3, 4, 6],
            [2, 3, 1, 4, 6],
            [1, 2, 3, 4, 6]
        ]
        for arr in arrs:
            print(arr)
            tree = make_bst(arr)
            level_traverse_iterative(tree)
            for i in [1, 2, 3, 4, 6]:
                self.assertTrue(is_in_bst_iterative(tree, i))
                self.assertTrue(is_in_bst_recursive(tree, i))
            for i in [0, 1.5, 5, 7]:
                self.assertFalse(is_in_bst_iterative(tree, i))
                self.assertFalse(is_in_bst_recursive(tree, i))

    def test_parent(self):
        tree = make_bst([4, 2, 6, 1, 3, 5, 7])
        tests = [
            [tree, None],
            [tree.left, tree],
            [tree.left.left, tree.left],
            [tree.left.right, tree.left],
            [tree.right, tree],
            [tree.right.left, tree.right],
            [tree.right.right, tree.right]
        ]
        for node, parent in tests:
            with self.subTest(node=node.val):
                self.assertIs(node.parent, parent)

    def test_size(self):
        tree = make_bst([4, 2, 6, 1, 3, 5, 7, 0])
        tests = [
            [tree, 8],
            [tree.left, 4],
            [tree.left.left, 2],
            [tree.left.left.left, 1],
            [tree.left.right, 1],
            [tree.right, 3],
            [tree.right.left, 1],
            [tree.right.right, 1]
        ]
        for node, size in tests:
            with self.subTest(node=node.val):
                self.assertEqual(len(node), size)


if __name__ == "__main__":
    unittest.main()

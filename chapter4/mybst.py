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
    """Inserts val into binary search tree with root `root`"""
    if val is None:
        return
    if not root:
        root = TreeNode(val)
    elif val <= root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def delete_from_bst(root: TreeNode, val) -> None:
    """Deletes val from binary search tree with root `root`"""
    if val is None or not root:
        return None

    if val < root.val:
        root.left = delete_from_bst(root.left, val)
    elif val > root.val:
        root.right = delete_from_bst(root.right, val)
    else:   # val found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # find in-order successor, swap, and delete
            root.val = get_min(root.right)
            root.right = delete_from_bst(root.right, root.val)
    return root


def is_in_bst_iterative(root: TreeNode, val) -> bool:
    """Returns true iff `val` is in binary search tree with root `root`, iteratively"""
    while root:
        if val == root.val:
            return True
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return False


def is_in_bst_recursive(root: TreeNode, val) -> bool:
    """Returns true iff `val` is in binary search tree with root `root`, recursively"""
    if not root:
        return False
    if val == root.val:
        return True
    elif val < root.val:
        return is_in_bst_recursive(root.left, val)
    else:
        return is_in_bst_recursive(root.right, val)


def is_bst(root: TreeNode, minval: float = float("-inf"), maxval: float = float("inf")) -> bool:
    """Returns true iff root is a binary search tree with all nodes in (minval, maxval)"""
    if not root:
        return True
    if root.val <= minval or root.val > maxval:
        return False
    return is_bst(root.left, minval, root.val) and is_bst(root.right, root.val, maxval)


def get_min(root: TreeNode) -> int:
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val


class TestBST(unittest.TestCase):
    def test_bst(self):
        arrs = [
            [2, 1, 3, 4, 6],
            [2, 3, 1, 4, 6],
            [6, 3, 2, 4, 1],
            [4, 1, 3, 2, 6],
            [1, 2, 3, 4, 6],
            [6, 4, 3, 2, 1]
        ]
        for arr in arrs:
            tree = make_bst(arr)
            self.assertTrue(is_bst(tree))
            for i in [0, 1.5, 5, 7]:
                with self.subTest(arr=arr, i=i):
                    self.assertFalse(is_in_bst_iterative(tree, i))
                    self.assertFalse(is_in_bst_recursive(tree, i))
            for i in [1, 2, 3, 4, 6]:
                with self.subTest(arr=arr, i=i):
                    self.assertTrue(is_in_bst_iterative(tree, i))
                    self.assertTrue(is_in_bst_recursive(tree, i))
            for i in [1, 2, 3, 4, 6]:
                with self.subTest(arr=arr, delete=i):
                    tree = make_bst(arr)
                    tree = delete_from_bst(tree, i)
                    self.assertTrue(is_bst(tree))
                    self.assertFalse(is_in_bst_iterative(tree, i))
                    self.assertFalse(is_in_bst_recursive(tree, i))
                    for j in [1, 2, 3, 4, 6]:
                        if i != j:
                            self.assertTrue(is_in_bst_iterative(tree, j))
                            self.assertTrue(is_in_bst_recursive(tree, j))


if __name__ == "__main__":
    unittest.main()

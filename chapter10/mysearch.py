from typing import List
import unittest


def binary_search(arr: List[int], val: int, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(arr) - 1
    while True:
        if l > r:
            return False
        mid = (l+r)//2
        if val == arr[mid]:
            return True
        elif val < arr[mid]:
            r = mid-1
        else:
            l = mid+1


def binary_search_recursive(arr: List[int], val: int,
                            l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(arr) - 1
    if l > r:
        return False
    mid = (l+r)//2
    if val == arr[mid]:
        return True
    elif val < arr[mid]:
        return binary_search_recursive(arr, val, l, mid-1)
    else:
        return binary_search_recursive(arr, val, mid+1, r)


class TestSearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [-5, -3, -3, 0, 1, 2, 4, 4, 7, 8, 11]
        trues = [i for i in range(-6, 13) if i in arr]
        falses = [i for i in range(-6, 13) if i not in arr]
        for val in trues:
            self.assertTrue(binary_search(arr, val))
            self.assertTrue(binary_search_recursive(arr, val))
        for val in falses:
            self.assertFalse(binary_search(arr, val))
            self.assertFalse(binary_search_recursive(arr, val))


if __name__ == "__main__":
    unittest.main()

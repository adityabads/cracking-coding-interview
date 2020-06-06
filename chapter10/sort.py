from typing import List
from random import randint
import unittest


def bubble_sort(arr: List[int]) -> None:
    """Bubble sort `arr`"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr: List[int]) -> None:
    """Insertion sort `arr`"""
    n = len(arr)
    for i in range(1, n):
        for j in reversed(range(i)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break


def selection_sort(arr: List[int]) -> None:
    """Selection sort `arr`"""
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


def merge_sort(arr: List[int], l: int = 0, r: int = None) -> None:
    """Merge sort `arr[l...r]`"""
    if r is None:
        r = len(arr) - 1
    if l < r:
        mid = (l+r)//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        _merge(arr, l, mid, r)


def _merge(arr: List[int], l: int, mid: int, r: int) -> None:
    """Merges sorted sublists arr[l...mid] and arr[mid+1...r] in place"""
    merged = []
    lefti = l
    righti = mid+1
    while lefti <= mid or righti <= r:
        leftval = arr[lefti] if lefti <= mid else float("inf")
        rightval = arr[righti] if righti <= r else float("inf")
        if leftval <= rightval:
            merged.append(leftval)
            lefti += 1
        else:
            merged.append(rightval)
            righti += 1
    arr[l:r+1] = merged


def quick_sort(arr: List[int], l: int = 0, r: int = None) -> None:
    """Quick sort arr[l...r]"""
    if r is None:
        r = len(arr) - 1
    if l < r:
        index = _partition(arr, l, r)
        quick_sort(arr, l, index)
        quick_sort(arr, index+1, r)


def _partition(arr: List[int], l: int, r: int) -> int:
    """Partitions `arr[l...r]` by value of middle element, returns index of partition"""
    pivot = arr[l]
    i = l-1
    j = r+1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def make_tests() -> List[List[int]]:
    """Returns list of test lists to sort"""
    tests = [[], [1 for _ in range(9)], [1 for _ in range(10)]]
    tests.extend([[i for i in range(j)] for j in range(6)])
    tests.extend([[i for i in reversed(range(j))] for j in range(6)])
    tests.extend([[randint(0, 9) for j in range(randint(6, 9))]
                  for i in range(10)])
    return tests


def is_sorted(arr: List[int]) -> bool:
    """Returns true iff `arr` is sorted in ascending order"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        tests = make_tests()
        for test in tests:
            with self.subTest(test=test):
                bubble_sort(test)
                self.assertTrue(is_sorted(test))

    def test_insertion_sort(self):
        tests = make_tests()
        for test in tests:
            with self.subTest(test=test):
                insertion_sort(test)
                self.assertTrue(is_sorted(test))

    def test_selection_sort(self):
        tests = make_tests()
        for test in tests:
            with self.subTest(test=test):
                selection_sort(test)
                self.assertTrue(is_sorted(test))

    def test_merge_sort(self):
        tests = make_tests()
        for test in tests:
            with self.subTest(test=test):
                merge_sort(test)
                self.assertTrue(is_sorted(test))

    def test_quick_sort(self):
        tests = make_tests()
        for test in tests:
            with self.subTest(test=test):
                quick_sort(test)
                self.assertTrue(is_sorted(test))

    def test_radix_sort(self):
        pass


if __name__ == "__main__":
    unittest.main()

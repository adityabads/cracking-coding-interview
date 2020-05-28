# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

from collections import defaultdict

def main():
    checkeq(is_permutation("abcde", "bdeca"), True)
    checkeq(is_permutation("Abcde", "bdeca"), False)
    checkeq(is_permutation("abcde", "bdecb"), False)


def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    d = defaultdict(int)
    for c in s1:
        d[c] += 1
    for c in s2:
        d[c] -= 1
    for c in d:
        if d[c] != 0:
            return False
    return True


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

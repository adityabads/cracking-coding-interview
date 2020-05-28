# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be 
# limited to just dictionary words.
# 
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

from collections import defaultdict

def main():
    checkeq(is_palindrome_permutation("Tact Coa"), True)
    checkeq(is_palindrome_permutation("Raeccar"), True)
    checkeq(is_palindrome_permutation("aloha"), False)


def is_palindrome_permutation(s: str) -> bool:
    d = defaultdict(int)
    for c in s:
        if c.isalpha():
            d[c.lower()] += 1
    isoddcount = False
    for c in d:
        if d[c] % 2 == 1:
            if isoddcount:
                return False
            isoddcount = True
    return True


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

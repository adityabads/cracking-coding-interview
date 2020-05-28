# Is Unique
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def main():
    checkeq(all_chars_unique("Aabc"), True)
    checkeq(all_chars_unique("aabc"), False)


def all_chars_unique(s: str) -> bool:
    bitvec = 0
    for c in s:
        if in_bitvec(bitvec, ord(c)):
            return False
        bitvec = add_to_bitvec(bitvec, ord(c))
    return True


def in_bitvec(bitvec: int, ind: int) -> bool:
    return (bitvec & (1 << ind)) != 0


def add_to_bitvec(bitvec: int, ind: int) -> int:
    return bitvec | (1 << ind)


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

# Is Unique
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def main():
    print(all_chars_unique("Aabc"))
    print(all_chars_unique("aabc"))


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


if __name__ == "__main__":
    main()

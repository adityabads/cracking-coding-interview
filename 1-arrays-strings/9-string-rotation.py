# String Rotation
# Assume you have a method `isSubstring` which checks if one word is a substring
# of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a
# rotation of `s1` using only one call to isSubstring (e.g., "waterbottle"
# is a rotation of "erbottlewat").

def main():
    checkeq(is_rotated("waterbottle", "erbottlewat"), True)
    checkeq(is_rotated("waaawa", "wawaaa"), True)
    checkeq(is_rotated("waaawa", "aaawaw"), True)
    checkeq(is_rotated("aaaaaa", "aaaaaa"), True)
    checkeq(is_rotated("aawaaaw", "aaawawa"), False)
    checkeq(is_rotated("aawaaw", "aaawawa"), False)


def is_rotated(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 * 2)


def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

# One Away
# There are three types of edits that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.
#
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def main():
    checkeq(one_away("pale", "pale"), True)
    checkeq(one_away("pale", "plea"), False)
    checkeq(one_away("pale", "ple"), True)
    checkeq(one_away("pales", "pale"), True)
    checkeq(one_away("pale", "pald"), True)
    checkeq(one_away("pale", "bale"), True)
    checkeq(one_away("pale", "bake"), False)
    checkeq(one_away("pal", "pull"), False)


def one_away(s1: str, s2: str) -> bool:
    diff = len(s1) - len(s2)
    if diff < -1 or diff > 1:
        return False
    # make s1 smaller string
    if diff > 0:
        s1, s2 = s2, s1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i:] == s2[i+1:] or s1[i+1:] == s2[i+1:]
    return True


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

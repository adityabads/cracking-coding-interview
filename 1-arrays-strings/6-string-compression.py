# String Compression
# Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string aabcccccaaa
# would become a2b1c5a3. If the "compressed" string would not become smaller
# than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def main():
    checkeq(compress("aabcccccaaa"), "a2b1c5a3")
    checkeq(compress(""), "")
    checkeq(compress("aaa"), "a3")
    checkeq(compress("aa"), "aa")
    checkeq(compress("abc"), "abc")


def compress(s: str) -> str:
    if len(s) == 0:
        return ""

    compressed = []
    count = 0
    for i in range(len(s)):
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(f"{s[i - 1]}{count}")
            count = 0
        count += 1
    compressed.append(f"{s[-1]}{count}")

    result = ''.join(compressed)
    return result if len(result) < len(s) else s


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

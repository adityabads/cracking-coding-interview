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
    current = ""
    count = 0
    result = ""
    for c in s:
        if c != current:
            if count > 0:
                result += f"{current}{count}"
            current = c
            count = 1
        else:
            count += 1

    if count > 0:
        result += f"{current}{count}"
    return result if len(result) < len(s) else s


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional 
# characters, and that you are given the "true" length of the string. 
# 
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

def main():
    checkeq(urlify("abcde   ", 5), "abcde")
    checkeq(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")


def urlify(s: str, n: int):
    result = ""
    for i in range(n):
        result += s[i] if s[i] != " " else "%20"
    return result


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()

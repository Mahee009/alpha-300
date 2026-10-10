def find_the_difference(s, t):
    result = 0
    for ch in s:
        result ^= ord(ch)
    for ch in t:
        result ^= ord(ch)
    return chr(result)


print(find_the_difference("abcd", "abcde"))
print(find_the_difference("", "y"))

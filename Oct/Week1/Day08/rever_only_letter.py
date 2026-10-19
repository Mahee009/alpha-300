class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        right = len(ans) - 1
        for x in s:
            if x.isalpha():
                while not s[right].isalpha():
                    right -= 1
                ans.append(s[right])
                right -= 1
            else:
                ans.append(x)
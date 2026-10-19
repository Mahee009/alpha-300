class Solution:
    def isPalindrome(self, s):
        # find length without len()
        n = 0
        for ch in s:
            n += 1

        i = 0        # start
        j = n - 1    # end

        while i < j:
            # skip spaces, commas, etc.
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            # compare both sides (ignore caps)
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


# example
# s = "A man, a plan, a canal: Panama"
# cleaned it reads "amanaplanacanalpanama"
# same from both sides, so it returns True
# s = "race a car"
# 'e' and 'a' don't match in the middle, so it returns False
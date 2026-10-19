class Solution:
    def commonChars(self, words):
        common = {}
        first = True

        for w in words:
            count = {}
            for ch in w:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1

            if first:
                common = count
                first = False
            else:
               
                for ch in common:
                    if ch not in count:
                        common[ch] = 0
                    elif count[ch] < common[ch]:
                        common[ch] = count[ch]

        ans = []
        for ch in common:
            times = common[ch]
            while times > 0:
                ans.append(ch)
                times -= 1
        return ans
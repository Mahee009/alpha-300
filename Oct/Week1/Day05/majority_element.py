class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        count = {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
s = Solution()

print(s.majorityElement([3, 2, 3]))
class Solution:
    def missingNumber(self, nums):
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result


print(Solution().missingNumber([3, 0, 1]))
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

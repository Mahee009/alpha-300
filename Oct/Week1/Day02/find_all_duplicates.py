class Solution:
    def findDuplicates(self, nums):
        result = []
        for value in nums:
            index = abs(value) - 1
            if nums[index] < 0:
                result.append(abs(value))
            else:
                nums[index] = -nums[index]
        return result


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicates([1, 1, 2]))

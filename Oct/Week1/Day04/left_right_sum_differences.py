class Solution:
    def leftRightDifference(self, nums):
        total = 0
        for num in nums:
            total += num
        answer = []
        left = 0
        for num in nums:
            right = total - left - num
            answer.append(abs(left - right))
            left += num
        return answer


print(Solution().leftRightDifference([10, 4, 8, 3]))
print(Solution().leftRightDifference([1]))

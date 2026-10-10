class Solution:
    def buildArray(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        for i in range(n):
            nums[i] //= n
        return nums


print(Solution().buildArray([0, 2, 1, 5, 3, 4]))
print(Solution().buildArray([5, 0, 1, 2, 3, 4]))

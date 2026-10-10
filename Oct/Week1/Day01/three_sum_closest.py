class Solution:
    def threeSumClosest(self, nums, target):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        best = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return best
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest([0, 0, 0], 1))
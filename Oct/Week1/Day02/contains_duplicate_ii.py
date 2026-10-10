class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

class Solution:
    def intersection(self, nums1, nums2):
        seen = {}
        for x in nums1:
            seen[x] = True

        ans = []
        for x in nums2:
            if x in seen and seen[x]:
                ans.append(x)
                seen[x] = False  # so it doesn't get added again
        return ans
class Solution:
    def intersect(self, nums1, nums2):
        c1 = {}
        c2 = {}

        for x in nums1:
            if x in c1:
                c1[x] += 1
            else:
                c1[x] = 1

        for x in nums2:
            if x in c2:
                c2[x] += 1
            else:
                c2[x] = 1

        ans = []
        for x in nums1:
            
            if c1[x] > 0 and x in c2 and c2[x] > 0:
                ans.append(x)
                c1[x] -= 1
                c2[x] -= 1
        return ans
class Solution:
    def findDifference(self, nums1, nums2):
        first = {}
        for x in nums1:
            first[x] = True

        second = {}
        for x in nums2:
            second[x] = True

        ans1 = []
        for x in first:
            if x not in second:
                ans1.append(x)

        ans2 = []
        for x in second:
            if x not in first:
                ans2.append(x)

        return [ans1, ans2]
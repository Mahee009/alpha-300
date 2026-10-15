from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = defaultdict(int)  # keeps count of each num

        for n in nums:
            count[n] += 1  # saw this num again, so add 1

            if len(count) <= 2:
                continue  # we can have max 2 majority nums

            new_count = defaultdict(int)  # make a fresh count

            for n, c in count.items():  # check each num and its count
                if c > 1:
                    new_count[n] = c - 1  # cancel 1 count from each num

            count = new_count  # save the updated counts

        res = []  # nums that pass the final check

        for n in count:
            # check how many times this num ACTUALLY appears
            if nums.count(n) > len(nums) // 3:
                res.append(n)  # add it if count is more than n/3

        return res  # give back the final list
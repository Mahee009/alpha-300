# Day 04 - Running Sum of 1d Array

Running Sum: walk from index 1 and add the previous value into the current one, so each spot holds the total so far. O(n), done in place.
Range Sum Query builds a prefix array with a leading 0 so any range is one subtraction, Build Array from Permutation just appends nums[nums[i]], Richest Customer Wealth sums each row and keeps the max, and Left and Right Sum Differences tracks a running left sum against total - left - nums[i].

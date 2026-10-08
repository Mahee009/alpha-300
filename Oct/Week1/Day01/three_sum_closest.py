def three_sum_closest(nums, target):
    nums = sorted(nums)
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return total
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                left += 1
            else:
                right -= 1
    return closest


print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([0, 0, 0], 1))

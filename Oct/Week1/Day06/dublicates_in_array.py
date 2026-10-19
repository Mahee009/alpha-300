def findDuplicates(nums):
    result = []

    for i in nums:
        slot = abs(i) - 1

        if nums[slot] < 0:
            result.append(abs(i))
        else:
            nums[slot] = -nums[slot]

    return result
nums = [3, 1, 1, 2]
print(findDuplicates(nums))
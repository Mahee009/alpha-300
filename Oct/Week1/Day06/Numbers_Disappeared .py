def findDisappearedNumbers(nums: list[int]) -> list[int]:
    result = []
    for i in nums:
        slot = abs(i) - 1
        if nums[slot] > 0 :
            nums[slot] = -nums[slot]

    for i in range(len(nums)):
        if nums[i] > 0 :
            result.append(i)
    return result
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))

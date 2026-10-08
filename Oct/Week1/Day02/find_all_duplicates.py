def find_duplicates(nums):
    result = []
    for value in nums:
        index = abs(value) - 1
        if nums[index] < 0:
            result.append(abs(value))
        else:
            nums[index] = -nums[index]
    return result


print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_duplicates([1, 1, 2]))

def contains_nearby_duplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False


print(contains_nearby_duplicate([1, 2, 3, 1], 3))
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

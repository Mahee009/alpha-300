def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


print(two_sum_sorted([2, 7, 11, 15], 9))
print(two_sum_sorted([2, 3, 4], 6))

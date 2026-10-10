def single_number(nums):
    result = 0
    for bit in range(32):
        count = 0
        for num in nums:
            if (num >> bit) & 1:
                count += 1
        if count % 3 != 0:
            result |= 1 << bit
    if result & (1 << 31):
        result -= 1 << 32
    return result


print(single_number([2, 2, 3, 2]))
print(single_number([0, 1, 0, 1, 0, 1, -99]))

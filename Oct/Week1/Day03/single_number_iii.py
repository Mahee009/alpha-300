def single_number(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num
    lowest_bit = xor_all & -xor_all
    a = 0
    b = 0
    for num in nums:
        if num & lowest_bit:
            a ^= num
        else:
            b ^= num
    return [a, b]


print(single_number([1, 2, 1, 3, 2, 5]))
print(single_number([-1, 0]))

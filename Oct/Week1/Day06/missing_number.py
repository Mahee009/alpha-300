def missingNumber(nums):
    full = 0
    for i in range (len(nums) + 1 ):
        full += i
        actual = 0
    for i in nums:
        actual += i
    return full - actual
nums = [0, 3, 1]
print(missingNumber(nums))
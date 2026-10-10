class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(0, 2))
print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(2, 5))

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        w = len(arr) // 4  # 25% of the array

        for index in range(len(arr) - w):
            # check if same num appears again after w positions
            if arr[index] == arr[index + w]:
                return arr[index]  # found the special num

        return -1  # just in case no num is found

s = Solution()
print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
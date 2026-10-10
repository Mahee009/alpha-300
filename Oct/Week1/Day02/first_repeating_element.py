class Solution:
    def firstRepeated(self, arr):
        seen = set()
        answer = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] in seen:
                answer = i + 1
            else:
                seen.add(arr[i])
        return answer


print(Solution().firstRepeated([1, 5, 3, 4, 3, 5, 6]))
print(Solution().firstRepeated([1, 2, 3, 4]))

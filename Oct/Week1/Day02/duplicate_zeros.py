def duplicate_zeros(arr):
    n = len(arr)
    zeros = arr.count(0)
    i = n - 1
    j = n + zeros - 1
    while i < j:
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
        i -= 1
        j -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr)
print(arr)

arr = [1, 2, 3]
duplicate_zeros(arr)
print(arr)

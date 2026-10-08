def first_repeated(arr):
    seen = set()
    answer = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in seen:
            answer = i + 1
        else:
            seen.add(arr[i])
    return answer


print(first_repeated([1, 5, 3, 4, 3, 5, 6]))
print(first_repeated([1, 2, 3, 4]))

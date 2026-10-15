def degree_of_an_array(nums):
    count = {}  # how many times each num appears
    first = {}  # where each num appears first
    last = {}   # where each num appears last

    for i, n in enumerate(nums):
        count[n] = count.get(n, 0) + 1  # count the num

        if n not in first:
            first[n] = i  # save its first position

        last[n] = i  # keep updating its last position

    degree = max(count.values())  # highest frequency
    res = len(nums)  # start with the full array

    for n in count:
        if count[n] == degree:  # only check nums with highest frequency
            res = min(res, last[n] - first[n] + 1)  # shortest length

    return res
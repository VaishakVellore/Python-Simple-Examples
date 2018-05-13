def longest_ordered_subsequence(L):
    n = len(L)
    list = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if L[i] > L[j] and list[i] < list[j] + 1:
                list[i] = list[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, list[i])

    return maximum


array = [1, 7, 3, 5, 9, 4, 8]
print("Length of list is", longest_ordered_subsequence(array))

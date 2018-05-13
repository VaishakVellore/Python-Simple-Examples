def find_maximum_subarray_iterative(A):
    length = len(A)
    maxsum = A[0]
    localsum = 0
    right = 0
    left = 0
    temp_left = 0

    for i in range(0, length, 1):
        localsum = max(A[i], localsum + A[i])
        if localsum == A[i]:
            temp_left = i
        if localsum > maxsum:
            maxsum = localsum
            right = i
            left = temp_left

    return left, right, maxsum


#STOCK_PRICE_CHANGES = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7] #All Negatives
#STOCK_PRICE_CHANGES = [13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 4, 7] #All Positives
STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] #Given Test case


def test():
    left, right, sum1 = find_maximum_subarray_iterative(STOCK_PRICE_CHANGES)
    print("(", left, ",", right, ")")
    pass


if __name__ == '__main__':
    test()



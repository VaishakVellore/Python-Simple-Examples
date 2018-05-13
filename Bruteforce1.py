def maximum_subarray_brute(a):
    leftindex = 0
    rightindex = 0
    maxsum = -999
    for i in range(0, len(a), 1):
        localsum = 0
        for j in range(i, len(a), 1):
            localsum = localsum + a[j]
            if localsum >= maxsum:
                maxsum = localsum
                leftindex = i
                rightindex = j
    return leftindex, rightindex

#STOCK_PRICE_CHANGES = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7] #All Negatives
#STOCK_PRICE_CHANGES = [13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 4, 7] #All Positives
#STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] #Given Test case
#STOCK_PRICE_CHANGES = []
#STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18]
STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18, 20]


def test():
    leftindex, rightindex = maximum_subarray_brute(STOCK_PRICE_CHANGES)
    print("(", leftindex, ",", rightindex, ")")
    pass


if __name__ == '__main__':
    test()

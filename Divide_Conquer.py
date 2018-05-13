def find_maximum_subarray_recursive(a):
    assert len(a) > 0, "Array is Empty"
    return find_maximum_subarray_recursive_helper(a, 0, len(a)-1)


def find_maximum_subarray_recursive_helper(a, low, high):
    if low == high:
        return a[low], low, high
    else:
        mid = (low+high)//2
        left_sum, left_low, left_high = find_maximum_subarray_recursive_helper(a, low, mid)
        right_sum, right_low, right_high = find_maximum_subarray_recursive_helper(a, mid + 1, high)
        cross_sum, cross_low, cross_high = find_maximum_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_low, left_high
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_low, right_high
        else:
            return cross_sum, cross_low, cross_high


def find_maximum_crossing_subarray(a, low, mid, high):
    local_sum = 0
    left_sum = -999
    right_sum = -999
    i = mid
    leftpointer = i
    while i >= low:
        local_sum = local_sum+a[i]
        if local_sum > left_sum:
            left_sum = local_sum
            leftpointer = i
        i = i-1

    local_sum = 0
    j = mid+1
    rightpointer = j
    while j <= high:
        local_sum = local_sum+a[j]
        if local_sum > right_sum:
            right_sum = local_sum
            rightpointer = j
        j = j+1

    return left_sum+right_sum, leftpointer, rightpointer


#STOCK_PRICE_CHANGES = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7] #All Negatives
#STOCK_PRICE_CHANGES = [13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 4, 7] #All Positives
#STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] #Given Test case
STOCK_PRICE_CHANGES = [13, -3, -25, 20, 0, 0, 30, -3, -16, -23, 18]


def test():
    maxsum, L, R = find_maximum_subarray_recursive(STOCK_PRICE_CHANGES)
    print("(", L, ",", R, ")")
    pass


if __name__ == '__main__':
    test()

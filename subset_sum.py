def subset_sum_solver(S,n):
    maxsum = sum(S)
    number = (n * 2) - maxsum
    S.append(number)
    if partition_set_solver(S) is True:
        return True
    else:
        return False


# Driver program to test above function
S = ([1, 3, 2, 4], 8)
if subset_sum_solver(S,n) == True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

import numpy as np

# ============================== Counting Pond ================================


def count_ponds(G):
    n = len(G)
    m = len(G[0])
    pond = [['-' for i in range(m)] for j in range(n)]
    for i in range(0, n):
        index = 0
        total = G[i]
        for j in range(0, m):
            if total[index] != '#' and total[index] != '-':
                return None
            pond[i][j] = total[index]
            index = index + 1
    count = 0
    for i in range(0, n):
        for j in range(0, m):
            if pond[i][j] == '#':
                count += 1
                check(pond, i, j)
    return count


def check(pond, i, j):
    m = len(pond[0])
    n = len(pond)

    if i < 0 or i >= n or j < 0 or j >= m or pond[i][j] != '#':
        return
    pond[i][j] = 'Visited'
    check(pond, i, j - 1)
    check(pond, i, j + 1)
    check(pond, i-1, j-1)
    check(pond, i-1, j)
    check(pond, i-1, j+1)
    check(pond, i+1, j-1)
    check(pond, i+1, j)
    check(pond, i+1, j+1)


# ======================== Longest Ordered Subsequence ========================


def longest_ordered_subsequence(l):
    n = len(l)
    lists = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if l[i] > l[j] and lists[i] < lists[j] + 1:
                lists[i] = lists[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lists[i])

    return maximum

# =============================== Supermarket =================================


def supermarket(Items):
    n = len(Items)
    Items.sort(key=lambda x: -x[0])
    lists = [0] * n
    optimal_profit = 0

    for each_item in Items:
        for j in range(min(n, each_item[1]) - 1, -1, -1):
            if lists[j] == 0:
                lists[j] = each_item[0]
                optimal_profit += each_item[0]
                break

    return optimal_profit

# ============================== Reducibility =================================


def subset_sum_solver(S, n):
    maxsum = sum(S)
    number = (n * 2) - maxsum
    S.append(number)
    if partition_set_solver(S) is True:
        return True
    else:
        return False
    pass


def partition_set_solver(S):
    total = sum(S)

    if total & 1 == 1:
        return False

    total >>= 1
    n = len(S) + 1

    dp = [[False for i in range(total + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= S[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - S[i - 1]]

    return dp[n - 1][total]


# =============================== Unit tests ==================================


def test_suite():

    if count_ponds(["#--------##-", "-###-----###", "----##---##-",
                    "---------##-", "---------#--", "--#------#--",
                   "-#-#-----##-", "#-#-#-----#-", "-#-#------#-",
                    "--#-------#-"]) == 3:
        print('passed')
    else:
        print('failed')

    if longest_ordered_subsequence([1, 7, 3, 5, 9, 4, 8]) == 4:
        print('passed')
    else:
        print('failed')

    if supermarket([(50, 2), (10, 1), (20, 2), (30, 1)]) == 80:
        print('passed')
    else:
        print('failed')

    if subset_sum_solver([1, 3, 2, 4], 8) is True:
        print('passed')
    else:
        print('failed')


if __name__ == '__main__':
    test_suite()

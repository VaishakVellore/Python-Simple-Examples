def supermarket(Items):
    n = len(Items)
    Items.sort(key=lambda x: -x[0])
    lists = [0] * n
    optimal_profit = 0

    for each_item in Items:
        for j in range(min(n, each_item[1] - 1, -1, -1)):
            if lists[j] == 0:
                lists[j] = each_item[0]
                optimal_profit += each_item[0]
                break

    return optimal_profit

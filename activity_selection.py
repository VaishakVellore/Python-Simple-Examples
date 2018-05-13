def activity_scheduling(Items):
    if not Items:
        return 0

    sorted_items = sorted(Items, key=lambda x: x[0])
    sorted_items.reverse()

    deadlines = []
    for i in range(0, len(sorted_items)):
        deadlines.append(sorted_items[i][1])
    max_deadline = max(deadlines)

    # create time_slot and ignore 0th value

    time_slot = [0] * (max_deadline + 1)

    # fill the time_slot array with profit of each activity

    for i in range(0, len(sorted_items)):
        k = min(max_deadline, sorted_items[i][1])  # min(3, ith deadline)
        if k > 0:
            if time_slot[k] == 0:
                time_slot[k] = sorted_items[i][0]

            elif time_slot[k] != 0:
                for j in range(k, 0, -1):  # from k upto 1 go backwards..
                    if time_slot[j] == 0:
                        time_slot[j] = sorted_items[i][0]
                        break
            else:
                pass

    optimal_profit = 0
    for i in time_slot:
        optimal_profit += i

    return optimal_profit


activities = []
print(activity_scheduling(activities))

# [(20,2),(20,2),(20,2),(40,3)]
# [(20,1), (2,1),(10,3),(100,2), (8,2),(5,20),(50,10)]
# [(50,2), (10,1),(20,2),(30,1)]
# []
# sort activities based on profit and in descending order.

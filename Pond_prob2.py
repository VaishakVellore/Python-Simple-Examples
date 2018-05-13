def count_ponds(G):
    n = len(G)
    m = len(G[0])
    pond = [['-' for i in range(m)] for j in range(n)]
    for i in range(0, n):
        total = G[i]
        index = 0
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
    n = len(pond)
    m = len(pond[0])
    if i < 0 or i >= n or j < 0 or j >= m or pond[i][j] != '#':
        return
    pond[i][j] = 'Visited'
    check(pond, i-1, j-1)
    check(pond, i-1, j)
    check(pond, i-1, j+1)
    check(pond, i, j-1)
    check(pond, i, j+1)
    check(pond, i+1, j-1)
    check(pond, i+1, j)
    check(pond, i+1, j+1)

result = count_ponds(["#--------##-", "-###-----###", "----##---##-", "---------##-", "---------#--", "--#------#--",
                      "-#-#-----##-", "#-#-#-----#-", "-#-#------#-", "--#-------#-"])
print("No of ponds", result)

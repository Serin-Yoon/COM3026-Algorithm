def optimizeInvestments(invstmt, money):
    """ knapsack problem """
    n = len(invstmt)
    val = []
    name = []
    roi = []

    for i in invstmt:
        name.append(i[0])
        val.append(i[-1])
        roi.append(i[1])

    K = [[0 for x in range(money + 1)] for x in range(n + 1)]
    I = [[0 for x in range(money + 1)] for x in range(n + 1)]
    optimal = [[None for x in range(money + 1)] for x in range(n + 1)]
    traceback = [[False for x in range(money + 1)] for x in range(n + 1)]


    for i in range(n + 1):
        for w in range(money + 1):
            optimal[i][w] = 0
            if i == 0 or w == 0:
                K[i][w] = float(0)
                I[i][w] = ""
                optimal[i][w] = 0
                traceback[i][w] = False

            elif roi[i - 1] <= w:

                if (val[i - 1] + K[i - 1][w - roi[i - 1]] > K[i - 1][w]):
                    K[i][w] = val[i - 1] + K[i - 1][w - roi[i - 1]]
                    optimal[i][w] = val[i - 1] + optimal[i - 1][w - roi[i - 1]]
                    traceback[i][w] = True

                    if len(I[i - 1][w - roi[i - 1]]) > 0:
                        I[i][w] = name[i - 1] + " & " + I[i - 1][w - roi[i - 1]]
                    else:
                        I[i][w] = name[i - 1]

                else:
                    K[i][w] = K[i - 1][w]
                    I[i][w] = I[i - 1][w]
                    optimal[i][w] = optimal[i-1][w]
                    traceback[i][w] = False




            else:
                K[i][w] = K[i - 1][w]
                I[i][w] = I[i - 1][w]
                optimal[i][w] = optimal[i-1][w]
                traceback[i][w] = False

        print('optimal: ')
        for row in optimal:
            print(row)
        print("traceback: ")
        for row in traceback:
            print(row)
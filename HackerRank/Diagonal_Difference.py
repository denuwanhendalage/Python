def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    length = len(arr)
    for i in range(length):
        diagonal1 += arr[i][i]
        inverse = length-i-1
        diagonal2 += arr[i][inverse]

    return abs(diagonal1-diagonal2)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))  # 15

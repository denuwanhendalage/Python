def plusMinus(arr):
    count_arr = [0, 0, 0]
    length = len(arr)
    for element in arr:
        if element > 0:
            count_arr[0] += 1
        elif element < 0:
            count_arr[1] += 1
        else:
            count_arr[2] += 1
    print(count_arr[0]/length, "\n", count_arr[1] /
          length, "\n", count_arr[2]/length)


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)  # 0.500000 0.333333 0.166667

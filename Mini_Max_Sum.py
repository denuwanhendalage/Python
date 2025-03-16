def miniMaxSum(arr):
    arr.sort()
    total = 0
    arr1 = arr[:4]
    for element in arr1:
        total += element
    print(total, total+arr[4]-arr[0])


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)  # 10 14

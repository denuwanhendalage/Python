def getArraySum(arr):
    total = 0
    for element in arr:
        total += element
    return total


arr = [1, 2, 3, 4, 10, 11]
print(getArraySum(arr))  # 31

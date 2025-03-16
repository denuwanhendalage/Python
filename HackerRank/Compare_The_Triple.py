def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]


a = [5, 6, 7]
b = [3, 6, 10]
print(compareTriplets(a, b))  # [1, 1]


# def compareTriplets2(a, b):
#     rating_array = [0, 0]
#     for i, j in a, b:
#         if i > j:
#             rating_array[0] += 1
#         elif i < j:
#             rating_array[1] += 1
#     return rating_array


# a = [5, 6, 7]
# b = [3, 6, 10]
# print(compareTriplets2(a, b))  # [1, 1]

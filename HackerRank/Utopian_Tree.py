def utopianTree(n):
    starting_value = 0
    if n == 0:
        starting_value = 1
    else:
        for i in range(n+1):
            if i % 2 == 0:
                starting_value += 1
            else:
                starting_value *= 2

    return starting_value


# print(utopianTree(0))  # 1
# print(utopianTree(1))  # 2
# print(utopianTree(2))  # 3
print(utopianTree(3))  # 6

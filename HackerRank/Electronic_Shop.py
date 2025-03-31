def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()
    maximum = 0
    if (keyboards[0]+drives[0]) > b:
        maximum = -1
        return maximum
    else:
        for element1 in keyboards:
            for element2 in drives:
                if maximum < (element1+element2) <= b:
                    maximum = element1+element2
    return maximum


print(getMoneySpent([3, 1], [5, 2, 8], 10))  # 9

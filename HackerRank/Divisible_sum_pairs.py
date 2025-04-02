def divisibleSumPairs(n, k, ar):
    divisible_count = 0
    for i in range(n):
        for j in range(i+1, n):
            total = 0
            total = ar[i]+ar[j]
            if total % k == 0:
                print(total)
                divisible_count += 1
    return divisible_count
    # Write your code here


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))  # Expected output: 5

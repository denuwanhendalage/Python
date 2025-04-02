def beautifulDays(i, j, k):
    beautiful_day_count = 0
    for t in range(i, j+1):
        number_str = str(t)
        reverse_number_str = number_str[::-1]
        reverse_number = int(reverse_number_str)
        diffrence_division = int(abs(t - reverse_number) / k)
        if diffrence_division*k == abs(t - reverse_number):
            beautiful_day_count += 1
    return beautiful_day_count


beautifulDays(20, 23, 6)  # Expected output: 2

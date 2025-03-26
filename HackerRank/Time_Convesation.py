def timeConversion(s):
    # Write your code here
    first_sector = int(s[:2])
    middle_sector = s[2:8]
    end_sector = s[8:]

    if end_sector == "PM":
        if first_sector < 12:
            first_sector += 12
            s = str(first_sector)+middle_sector
        else:
            s = str(first_sector)+middle_sector
    else:
        if first_sector == 12:
            first_sector -= 12
            s = str(first_sector)+middle_sector
        else:
            s = str(first_sector)+middle_sector
    return s


print(timeConversion("07:05:45PM"))  # 19:05:45
print(timeConversion("12:05:45AM"))  # 00:05:45
print(timeConversion("12:05:45PM"))  # 12:05:45
print(timeConversion("01:05:45PM"))  # 07:05:45

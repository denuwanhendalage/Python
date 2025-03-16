def birthdayCakeCandles(candles):
    candles.sort()
    last_element = candles[-1]
    value = candles.count(last_element)
    return value


candles = [3, 2, 1, 3]
print(birthdayCakeCandles(candles))  # 2

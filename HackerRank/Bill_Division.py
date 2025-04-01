def bonAppetit(bill, k, b):
    bill.pop(k)
    total = 0
    for element in bill:
        total += element
    value = b-total/2
    if int(value) == 0:
        print("Bon Appetit")
    else:
        print(int(value))


bonAppetit([3, 10, 2, 9], 1, 12)  # Bon Appetit

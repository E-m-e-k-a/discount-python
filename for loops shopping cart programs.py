cart = [15, 42, 120, 9, 5, 380]

discount = int(input("Enter discount percentage: "))
for price in cart:
    total = 0
    total += price
    print(total-(total*(discount/100)))

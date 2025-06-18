price = 100

yosh = int(input("Enter your age:"))
if yosh <= 6:
    total_price = price * 0.5
    print(total_price)
elif 6 < yosh <= 17:
    total_price = price * 0.8
    print(total_price)
elif 60 < yosh:
    total_price = price * 0.7
    print(total_price)

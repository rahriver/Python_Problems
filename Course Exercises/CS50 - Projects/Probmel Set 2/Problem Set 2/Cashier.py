# Greedy Algorithm
# Cashier should use the fewest amount of coins possible, to give the money back to the customer. He only has 4 types of coins.

price = int(input("How Much: "))
coins = [25,10,5,1]
count = 0

# We want to make a loop that breaks every time a coin gets subtracted, because we want to check everytime from the begininng so we don't miss any price which costs like 50 cents (its 2 25 cents coin).

while price != 0:
    if price > 0:
        for i in coins:
            if price >= i:
                price -= i
                count += 1
                break
    else:
        print("Input a correct number!")
        price = int(input("How Much: "))


print(f"Count: {count}\nPrice: {price}")

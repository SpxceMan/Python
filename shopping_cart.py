#Shopping Cart Program


foods=[]
prices=[]
total=0


while True:
    foood=input("Enter a food to buy (q to quit): ")
    food=foood.capitalize()
    
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the price of a/an {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("* * * YOUR CART * * *")

for food in foods:
    print(f"{food} - ${price}")

for price in prices:
    total+=price

print(f"Your total is: ${total}")





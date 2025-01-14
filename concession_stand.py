#Concession Stand

menu = {"pizza":400,
        "burger":150,
        "fries":50,
        "coke":20,
        "chips":10,
        "cookies":90}

cart = []
total = 0

print("* * * M E N U * * *")
for key,value in menu.items():
    print(f"{key.capitalize():10}: {value:.2f}")
    print("-------------")

while True:
    food=input("Select an item (q to quit): ")

    if food.lower() == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Item not part of the menu. Enter a different Item.")    
    
if cart:
    for food in cart:
        total += menu.get(food)
        print(food.capitalize(),end=" ")
else:
    print("Cart has no Items.")


print()
print(f"Total is {total:.2f}")
print("* * * * * * * * * * * * * * * *")

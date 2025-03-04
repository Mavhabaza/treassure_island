print("Welcome to Python Pizza Deliveries!")

bill = 0
menu_on = True

while menu_on:
    size = input("What size pizza do you want? S, M or L: ").upper()
    if size == "S":
        bill = 15
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if pepperoni == "Y":
            bill += 2

    elif size == "M":
        bill = 20
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if pepperoni == "Y":
            bill += 3

    elif size == "L":
        bill = 25
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if pepperoni == "Y":
            bill += 3

    else:
        print("The size you selected is not valid!")
        break

    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
    if extra_cheese == "Y":
        bill += 1


    print(f"Your bill is: ${bill}")
    break

    

    

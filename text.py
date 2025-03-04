print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok, have a free ride on us!.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # else:
    #     bill = 0
    #     print("Midlife'Your bill is $0.'")
    
    
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        #Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")



# x = 10/2
# print(x)

#A program to check if a number is Odd or Even
"""number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")"""
    

"""When combining diffent conditions using 'and' your your answer is always false
    with "and" to get True you must combine the same conditions.
    
    - With 'or' operater if any of the conditions are true then answer is "True" 
        and if any if both the conditions are false then you get "False" 
        
    - The "not" Operator reverses the condition- if the condition is True it becomes false and is its False it becomes True
        -not False is 'True' and not True is 'False' """
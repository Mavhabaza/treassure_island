weight = 85
height = 0.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("You are under weight")
elif bmi < 25:
    print("Your weight is normal")
else:
    print("You are overweight")

print(bmi)
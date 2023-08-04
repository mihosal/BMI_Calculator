# 🚨 Don't change the code below 👇
height = float(input("enter your height in m (Please Use a '.' instead of ',' for the decimal point): "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are Underweighted")
elif bmi < 25:
    print(f"You have a normal weight")
elif bmi < 30:
    print(f"You are Slightly Overweighted")
elif bmi < 35:
    print(f"You are Obese")
else:
    print(f"You are Clinically Obese")
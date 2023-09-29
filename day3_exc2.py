# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
var_bmi =  int( round( weight / ( height * height) ) );

if var_bmi < 18.5:
    print(f'Your bmi is {var_bmi}, you are underweight.')
elif var_bmi >= 18.5 and var_bmi < 25:
    print(f'Your bmi is {var_bmi}, you have a normal weight.')
elif var_bmi >= 25 and var_bmi < 30:
    print(f'Your bmi is {var_bmi}, you are slightly overweight.')
elif var_bmi >= 30 and var_bmi < 35:
    print(f'Your bmi is {var_bmi}, you are obese.')
elif var_bmi >= 35:
    print(f'Your bmi is {var_bmi}, you are clinically obese.')
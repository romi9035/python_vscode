# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_age = 90
days_year = 365
weeks_year = 52
mon_year = 12

rem_year = max_age - int(age)

print(f"You have {int( rem_year * days_year) } days, { rem_year * weeks_year } weeks, and {rem_year * mon_year} months left.")

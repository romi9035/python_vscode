# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
var_true = ['t','r','u','e']
var_love = ['l','o','v','e']
var_name1 = name1.lower()
var_name2 = name2.lower()

i = 0
tot_true = 0
tot_love = 0
while i < len(var_true):
    tot_true += var_name1.count( var_true[i])
    tot_love += var_name1.count( var_love[i])
    tot_true += var_name2.count( var_true[i])
    tot_love += var_name2.count( var_love[i])
    i += 1

var_per = int(str(tot_true) + str(tot_love))

if var_per < 10 or var_per > 90:
    print(f"Your score is {var_per}, you go together like coke and mentos.")
elif var_per >= 40 and var_per <= 50:
    print(f"Your score is {var_per}, you are alright together.")
else:
    print(f"Your score is {var_per}")


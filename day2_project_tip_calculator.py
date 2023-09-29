#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome ot the tip calculator.")
tot_bill = float( input("What was the total bill? $") )
tip_per = int( input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

# per_head = round( ( (  tot_bill + ( tot_bill * tip_per / 100 ) )  / no_of_people ), 2 )
# print(f"Each person should pay: ${per_head}")
per_head = ( (  tot_bill + ( tot_bill * tip_per / 100 ) )  / no_of_people )
print(f"Before format: {per_head}")
per_head = "{:.2f}".format(per_head)
print(f"Each person should pay: ${per_head}")
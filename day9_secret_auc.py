import os
from art_1 import logo
print(logo)
flag = True
bidders = {}

while flag == True:
    name = input("What is your name?: ")
    price = int(input("What's your bid ?: $"))
    bidders[name] = price
    other_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bid == 'yes':
        os.system('cls')
    else:
        flag = False

high_bidprice = 0
high_bidname = ''
for bidder_name in bidders:
    bid_price = bidders[bidder_name]
    if bid_price > high_bidprice:
        high_bidprice = bid_price
        high_bidname = bidder_name

print(f"The winner is {high_bidname} with a bid of {high_bidprice}")

import os
def clear():
    os.system("clear")

from art import logo

print(logo)
print("Welcome to the Silent Auction")

users = {}
next_user_trigger = 1
current_highest_bid = 0

def bidding_process(user_name, bid_amount, next_user_value):
    current_value = {}
    current_value["name"] = user_name
    current_value["bid"] = bid_amount
    current_value["next_user"] = next_user_value
    users[name] = current_value

while  next_user_trigger == 1:
    name = input("What is your name?\n")
    bid = int(input("How much are you bidding?\n"))
    next_user = input("Is anyone bidding after you?\n").lower()
    bidding_process(name, bid, next_user)
    clear()
    if bid > current_highest_bid:
        current_highest_bid = bid
    if next_user == "no":
        next_user_trigger -= 1
    elif next_user == "yes":
        next_user_trigger = 1
    else:
        clear()
        while next_user != "yes" and next_user != "no":
            next_user = input("Is anyone bidding after you? Please type 'yes' or 'no' without any puctuation.\n").lower()
            if next_user == "no":
                next_user_trigger -= 1
            elif next_user == "yes":
                next_user_trigger = 1

for item in users:
    if current_highest_bid == users[item]["bid"]:
        winner = users[item]["name"]
        print(f"The winner is {winner} with a bid of {current_highest_bid}. Congratulations!")
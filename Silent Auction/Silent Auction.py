import os
def clear():
    os.system("clear")

from art import logo

print(logo)
print("Welcome to the Silent Auction")

next_user = 1
user_bids = []

def bidding(name_of_user, user_bid, other_user):
    current_input = {}
    list_of_bids = {}
    current_input["name_of_user"] = name_of_user
    current_input["user_bid"] = user_bid
    current_input["other_user"] = other_user
    list_of_bids[str(name)] = current_input
    user_bids.append(list_of_bids)

while next_user == 1:
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n"))
    other = input("Is anyone else bidding after you?\n").lower()
    bidding(name, bid, other)
    if other == "no":
        next_user -= 1

print(user_bids)

# TODO: compare user input values
    # TODO: call the values from each entry in the dictionary


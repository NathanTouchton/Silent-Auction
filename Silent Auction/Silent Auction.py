import os
def clear():
    os.system("clear")

from art import logo

print(logo)
print("Welcome to the Silent Auction")

next_user = 1
user_bids = {}

def bidding(name_of_user, user_bid, other_user):
    current_input = {}
    current_input["name_of_user"] = name_of_user
    current_input["user_bid"] = user_bid
    current_input["other_user"] = other_user
    user_bids[name] = current_input


while next_user == 1:
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n"))
    other = input("Is anyone else bidding after you?\n").lower()
    bidding(name, bid, other)
    clear()
    if other == "no":
        next_user -= 1

current_score = 0

for item in user_bids:
    compare = user_bids[item]["user_bid"]
    if compare > current_score:
        current_score += compare

for item in user_bids:
    compare_two = user_bids[item]["user_bid"]
    if compare_two == current_score:
        print(f"The winner of the auction is {user_bids[item]['name_of_user']} with a bid of {user_bids[item]['user_bid']}. Congratulations!")




# test = {
#     "Nathan": ["Nathan", 20, "yes"],
#     "Alison": ["Alison", 4, "yes"],
#     "Nolan": ["Nolan", 6, "no"]
# }

# for item in test:
#     test_item = test[item][1]
#     print(test_item)

# Nathan: {
#     'name_of_user': 'Nathan', 
#     'user_bid': 20.0,
#     'other_user': 'yes',
# }


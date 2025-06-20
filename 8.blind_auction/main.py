import art
print(art.logo)
print("Welcome to the secret auction program")

def highest_bidder(bid_dict):

    highest_bid = 0
    winner = ""

    for i in bid_dict:
        bid_amt = bid_dict[i]
        if bid_amt > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ₹{highest_bid} ")




info = {}
new_bids = True
while new_bids:
    name = input("What is your name: ")
    bid_amount = int(input("What is your bid?: ₹"))
    info[name] = bid_amount
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "no":
        new_bids = False
        print("\n" * 100)
        highest_bidder(info)
    elif choice == "yes":
        print("\n"*100)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

def highest_bidder(bidding_game):
    highest_bid = 0
    for key in bidding_game:
        bid_amount = bidding_game[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {key} with the bid amount of {highest_bid}")

bidding_game = {}
should_continue = True
while should_continue:
    name = input("Enter your Name:")
    amount = int(input("Enter your Bid amount: $"))
    bidding_game[name] = amount
    more_players = input("Are there any other bidders? Typer Yes or No \n").lower()
    if more_players == "no":
        highest_bidder(bidding_game)
        should_continue = False
    elif more_players  == "yes":
        print("\n" * 20)
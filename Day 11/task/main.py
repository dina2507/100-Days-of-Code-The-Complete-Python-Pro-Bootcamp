import random
from art import logo

# The deck of cards where 11 represents an Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Takes a list of cards and returns the calculated score."""
    # Check for an immediate Blackjack (Ace + 10-value card)
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # 0 represents a Blackjack in our game logic

    # If the score is over 21 and there is an Ace (11), treat it as a 1
    # Using a while loop handles multiple Aces safely
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    """Compares the user score against the computer score to determine the winner."""
    if user_score == computer_score:
        return "It's a draw! 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif user_score == 0:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over 21. You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over 21. You win! 😁"
    elif user_score > computer_score:
        return "You win! 😃"
    else:
        return "You lose! 😤"


def play_game():
    """Runs a complete round of Blackjack."""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the initial 2 cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # --- User's Turn Loop ---
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End user's turn immediately if anyone hits 21 or user busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want to hit or pass
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # --- Computer's Turn Loop ---
    # Computer keeps drawing if its score is less than 17 (and hasn't busted)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # --- Final Showdown ---
    print("\n" + "=" * 30)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("=" * 30 + "\n")


# --- Replay Engine ---
# This keeps the game runnable repeatedly and clears space between rounds
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
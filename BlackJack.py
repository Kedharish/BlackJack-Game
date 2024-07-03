
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
print(logo)
print("\nWelcome to BlackJack Game\n")

def cards_pick():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 2)
    return card

def calculate_score(cards):
    # Check for Ace and adjust if total exceeds 21
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def replay():
    while True:
        # Initialize user and computer cards
        user_cards = []
        computer_cards = []

        # Prompt user to start the game
        want_to_play_first = input("\nWould you like to play BlackJack? (y/n)\n").lower()
        if want_to_play_first != "y":
            break

        # Deal initial cards
        user_cards.extend(cards_pick())
        computer_cards.extend(cards_pick())

        # Calculate initial scores
        user_value = calculate_score(user_cards)
        computer_value = calculate_score(computer_cards)

        # Display initial cards
        print(f"\nYour cards: {user_cards}, and your value is {user_value}")
        print(f"Computer cards: [{computer_cards[0]}, 'X'], ('X' is the second card of the computer)")

        # User's turn to draw cards
        while user_value < 21:
            call_card = input("\nDo you want to pick another card? (y/n)\n").lower()
            if call_card == "y":
                user_cards.extend(random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 1))
                user_value = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, and your value is {user_value}")
            else:
                break

        # Computer's turn to draw cards
        while computer_value < 17:
            computer_cards.extend(random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 1))
            computer_value = calculate_score(computer_cards)
            print(f"Computer draws a card.")

        # Determine the winner
        if user_value > 21:
            print("\nYou lost.")
        elif computer_value > 21:
            print("\nComputer busts, you win!")
        elif user_value > computer_value:
            print("\nYou win!")
        elif computer_value > user_value:
            print("\nComputer wins!")
        else:
            print("\nIt's a draw!")

        # Display final cards and values
        print(f"\nYour cards: {user_cards}, and your value is {user_value}")
        print(f"Computer cards: {computer_cards}, and computer value is {computer_value}")

        # Ask if the user wants to play again
        do_you_want_to_play_again = input("\nDo you want to play again? (y/n)\n").lower()
        if do_you_want_to_play_again != "y":
            print("Bye Bye")
            break

# Start the game by calling replay function
replay()

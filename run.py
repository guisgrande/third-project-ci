import random
import display

# Global variables used to generate the game deck
deck_spades = ["As", "Ks", "Qs", "Js", "Ts", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s"]
deck_hearts = ["As", "Kh", "Qh", "Jh", "Th", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h"]
deck_diamonds = ["Ad", "Kd", "Qd", "Jd", "Td", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d"]
deck_clubs = ["Ac", "Kc", "Qc", "Jc", "Tc", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c"]
full_deck = deck_spades + deck_hearts + deck_diamonds + deck_clubs

deck_game = full_deck.copy()
random.shuffle(deck_game)

print("Full deck " + str(full_deck))
print("Game deck " + str(deck_game))

# Global lists, one to all cards out of deck_game and another list for the discarted cards that will be revealed.
used_deck = []
reveal_deck_game = []

# List to hold player and computer current cards
player_hand = []
computer_hand = []

# Displays the name of the game, description and rules, and the option to play or close the program.
def main_menu():
    while True:
        print("Select your action: ")
        selection = input("> ")
        if selection in ["Q", 'q']:
            print("Closing the program!")
            break
        if selection in ["P", 'p']:
            print("Starting the game! Take your seat.")
            start_game(used_deck, reveal_deck_game, player_hand, computer_hand)
            break
        if selection in ["R", "r"]:
            print('''
-----------------------------================== RULES ==================-----------------------------
    ° Each player receives 4 cards.
    ° Each turn, the player must discard a card and take another.
    ° The discarded card goes into the revealed deck.
    ° The player can buy a card from the revealed deck or the hidden deck.
    ° The object of the game is to get 3 of the same cards.
    ° If you discard the same card as the last card in the revealed deck, you win an extra round.
-----------------------------------------------------------------------------------------------------
             ''')
            continue
        if selection not in ["Q", "q", "P", "p", "R", "r"]:
            print("Wrong selection! Should be [P], [R] or [Q].")
            continue

# Close the program
def quit_program():
    pass

# Defines who will start the game, through the choice of heads or tails.
def coin_toss():
    pass

def take_card(used_deck):
    remove = deck_game.pop()
    used_deck.append(remove)

# Shuffle the cards, deal 4 cards to each player, and turn over the first card. 
def start_game(used_deck, reveal_deck_game, player_hand, computer_hand):
    print("GAME")

    player_card_one = deck_game[-1]
    take_card(used_deck)

    computer_card_one = deck_game[-1]
    take_card(used_deck)

    player_card_two = deck_game[-1]
    take_card(used_deck)

    computer_card_two = deck_game[-1]
    take_card(used_deck)

    player_card_three = deck_game[-1]
    take_card(used_deck)

    computer_card_three = deck_game[-1]
    take_card(used_deck)

    player_card_four = deck_game[-1]
    take_card(used_deck)

    computer_card_four = deck_game[-1]
    take_card(used_deck)

    # First card to start the game at revealed.
    reveal_deck_game = deck_game[-1]
    take_card(used_deck)

    player_hand = [player_card_one, player_card_two, player_card_three, player_card_four]
    computer_hand = [computer_card_one, computer_card_two, computer_card_three, computer_card_four]
    print(player_hand)
    print(computer_hand)
    print(reveal_deck_game)
    print(deck_game)
    print(used_deck)

    print(display.display_computer_hand_hiden)
    print(display.display_table)
    print(display.display_player_hand)
    selection = input("> ")

# Stops the game and returns to the main menu.
def stop_game():
    pass

# Receives the player's decision of which card to discard, and moves it to the discard deck (face revealed).
def player_discard_action(reveal_deck_game, player_hand):
    while True:
        print("Which card you wanna to discard?")
        print("[1] - [2] - [3] - [4]")
        print("[B] - Back to main menu!")
        selection = input("> ")

        if selection == "1":
            reveal_deck_game.append(player_hand[0])
            del player_hand[0]
            break
        if selection == "2":
            reveal_deck_game.append(player_hand[1])
            del player_hand[1]
            break
        if selection == "3":
            reveal_deck_game.append(player_hand[2])
            del player_hand[2]
            break
        if selection == "4":
            reveal_deck_game.append(player_hand[3])
            del player_hand[3]
            break
        if selection == "B":
            print("Ending this game! Thanks for playing.")
            main_menu()
            break
        if selection not in ["0", "1", "2", "3", "B"]:
            print("Ops! It`s not a valid selection.")
            continue

# Receives the player's decision of which card to take, and moves the card to players hand.
def player_take_action(deck_game, reveal_deck_game, player_hand):
    while True:
        print("Which deck do you want to take another card from?")
        print("- - - - - - - [H]idden - [R]eveled - - - - - - -")
        print("- - - - - - [B] - Back to main menu! - - - - - -")
        selection = input("> ")
        
        if selection in ["H", "h"]:
            player_hand.append(deck_game[-1])
            take_card(used_deck)
            break
        if selection in ["R", "r"]:
            player_hand.append(reveal_deck_game[-1])
            break
        if selection == ["B", "b"]:
            menu()
            break
        if selection not in ["H", "h", "R", "r", "B", "b"]:
            print("Ops! Its not a valid selection.")
            continue


# Check the cards in hand and purchase options and make a decision.
def computer_action():
    pass

# Check the cards in the hand
def win_check():
    pass

# Checks if you have three of a kind in your hand, does not consider suits, only value.
def extra_round_check():
    pass

print('''
======================================================================================================
 =========______=====______====______=====______=====__====___===__====___======_====_____===========
 ========|___   |===|  __  |==|   ___|===|  __  |===|  |==/  /==|  |==|  _ \===| |==|  _  \==========
 =========___|  |===| |==| |==|  |__=====| |__| |===|  |=/  /===|  |==| |=\ \==| |==| | \  \ ========
 ========|___   |===| |==| |==|   __|====|  __  |===|      <====|  |==| |==\ \=| |==| |  |  |========
 =========___|  |===| |__| |==|  |=======| |==| |===|  |=\  \===|  |==| |===\ \| |==| |_/  /=========
 ========|______|===|______|==|__|=======|_|==|_|===|__|==\__\==|__|==|_|====\___|==|_____/==========
======================================================================================================
----------------------== CHOOSE: [P] for PLAY | [R] for RULES | [Q] for QUIT ==----------------------
======================================================================================================
''')
main_menu()
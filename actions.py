from collections import Counter
import random
import display

# Global variables used to generate the game deck
deck_spades = ["As", "Ks", "Qs", "Js", "Ts", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s"]
deck_hearts = ["As", "Kh", "Qh", "Jh", "Th", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h"]
deck_diamonds = ["Ad", "Kd", "Qd", "Jd", "Td", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d"]
deck_clubs = ["Ac", "Kc", "Qc", "Jc", "Tc", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c"]
full_deck = deck_spades + deck_hearts + deck_diamonds + deck_clubs

# Global lists, one to all cards out of deck_game and another list for the discarded cards that will be revealed.
deck_game = full_deck.copy()
reveal_deck_game = []
used_deck = []

# Hand class, used to define player and computer cards

class HandCards:
    def __init__(self, card_one, card_two, card_three, card_four):
        self.card_one = [card_one[0], card_one[1]]
        self.card_two = [card_two[0], card_two[1]]
        self.card_three = [card_three[0], card_three[1]]
        self.card_four = [card_four[0], card_four[1]]

# List to hold player and computer current cards
player_hand = []
computer_hand = []

# Displays the name of the game, description and rules, and the option to play or close the program.
def main_menu():
    print(display.intro_display)
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

    random.shuffle(deck_game)

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
    table_card = deck_game[-1]
    take_card(used_deck)

    player_hand = [player_card_one, player_card_two, player_card_three, player_card_four]
    computer_hand = [computer_card_one, computer_card_two, computer_card_three, computer_card_four]
    reveal_deck_game = [table_card]

    print("PLAYER HAND")
    print(player_hand)
    print("COMPUTER HAND")
    print(computer_hand)
    print("REVEALED DECK")
    print(reveal_deck_game)
    print("GAME DECK")
    print(deck_game)
    print("USED DECK")
    print(used_deck)

    # print(display.display_computer_hand_hiden)
    # display.display_table()
    # display.display_player_hand()

    win_check(player_hand, computer_hand)
    
    player_discard_action(reveal_deck_game, player_hand)

# Stops the game and returns to the main menu.
def stop_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand):
    print(deck_game)
    print(used_deck)
    print(reveal_deck_game)
    print(player_hand)
    print(computer_hand)

    deck_game = []
    deck_game = full_deck.copy()
    used_deck = []
    reveal_deck_game = []
    player_hand = []
    computer_hand = []

    print(deck_game)
    print(used_deck)
    print(reveal_deck_game)
    print(player_hand)
    print(computer_hand)
    main_menu()

# Receives the player's decision of which card to discard, and moves it to the discard deck (face revealed).
def player_discard_action(reveal_deck_game, player_hand):
    print("PLAYER HAND")
    print(player_hand)
    print("REVEAL DECK")
    print(reveal_deck_game)
    print("COMPUTER HAND")
    print(computer_hand)
    while True:
        print("Which card you wanna to discard?")
        print("[1] - [2] - [3] - [4]")
        print("[B] - Back to main menu!")
        selection = input("> ")

        if selection == "1":
            reveal_deck_game.append(player_hand[0])
            del player_hand[0]
            player_take_action(deck_game, reveal_deck_game, player_hand)
            break
        if selection == "2":
            reveal_deck_game.append(player_hand[1])
            del player_hand[1]
            player_take_action(deck_game, reveal_deck_game, player_hand)
            break
        if selection == "3":
            reveal_deck_game.append(player_hand[2])
            del player_hand[2]
            player_take_action(deck_game, reveal_deck_game, player_hand)
            break
        if selection == "4":
            reveal_deck_game.append(player_hand[3])
            del player_hand[3]
            player_take_action(deck_game, reveal_deck_game, player_hand)
            break
        if selection in ["B", "b"]:
            print("Ending this game! Thanks for playing.")
            stop_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand)()
            break
        if selection not in ["0", "1", "2", "3", "B", "b"]:
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
            computer_action(computer_hand, reveal_deck_game, deck_game)
            break
        if selection in ["R", "r"]:
            player_hand.append(reveal_deck_game[-1])
            computer_action(computer_hand, reveal_deck_game, deck_game)
            break
        if selection == ["B", "b"]:
            stop_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand)
            break
        if selection not in ["H", "h", "R", "r", "B", "b"]:
            print("Ops! Its not a valid selection.")
            continue


# Check the cards in hand and purchase options and make a decision.
def computer_action(computer_hand, reveal_deck_game, deck_game):
    # computer cards
    cc1 = computer_hand[0][0]
    cc2 = computer_hand[1][0]
    cc3 = computer_hand[2][0]
    cc4 = computer_hand[3][0]
    ch_list = [cc1, cc2, cc3, cc4]

    # Counter used to generate a dictionary from computer cards.
    counter_list = Counter(ch_list)

    # One list to hold discard options and other to potential win, used to decide if take a card from revealed deck.
    discard_option = []
    potential_win = []

    print("COMPUTER HAND BEFORE ACTION")
    print(computer_hand)
    print(ch_list) 

    # For loop and if/else used to add single cards to discard option and pairs to potential win lists.
    for card, number in counter_list.items():
        if number == 1:
            if card not in discard_option:
                discard_option.append(card)
        elif number == 2:
            if card not in potential_win:
                potential_win.append(card)
        else:
            print("ERROR VERIFY COMPUTER ACTION")

    for card in discard_option:
        if card in ch_list:
            if card == cc1: 
                reveal_deck.append(computer_hand[0])
                del computer_hand[0]
                break
            elif card == cc2:
                reveal_deck.append(computer_hand[1])
                del computer_hand[1]
                break
            elif card == cc3:
                reveal_deck.append(computer_hand[2])
                del computer_hand[2]
                break
            else:
                reveal_deck.append(computer_hand[3])
                del computer_hand[3]
                break

    for card in potential_win:
        if card == reveal_deck[-2][0]:
            computer_hand.append(reveal_deck[-2])
            del reveal_deck[-2]
        else:
            computer_hand.append(deck_game[-1])
            del deck_game[-1]
    
    print("COMPUTER HAND BEFORE ACTION")
    print(computer_hand)
    
# Check the cards in the hand
def win_check(player_hand, computer_hand):
    print("WIN TEST CHECK START")
    # player cards
    c1 = player_hand[0][0]
    c2 = player_hand[1][0]
    c3 = player_hand[2][0]
    c4 = player_hand[3][0]
    # player hand list and check list
    ph_list = [c1, c2, c3, c4]
    ph_check = []
    for card in ph_list:
        if card not in ph_check:
            ph_check.append(card)
            
    if len(ph_check) == 2:
        print("You win! Congratulations.")

    # computer cards
    cc1 = computer_hand[0][0]
    cc2 = computer_hand[1][0]
    cc3 = computer_hand[2][0]
    cc4 = computer_hand[3][0]
    # computer hand list and check list
    ch_list = [cc1, cc2, cc3, cc4]
    ch_check = []
    for card in ch_list:
        if card not in ch_check:
            ch_check.append(card)
            
    if len(ch_check) == 2:
        print("You lose! Don't be sad, try again.")

    print(ph_list)
    print(ph_check)
    print(ch_list)
    print(ch_check)

    print("WIN TEST CHECK END")

# Checks if you have three of a kind in your hand, does not consider suits, only value.
def extra_round_check():
    last_card = reveal_deck_game[-2][0]
    discarded_card = reveal_deck_game[-1][0]

    if last_card == discarded_card:
        print("Extra round")

main_menu()
from collections import Counter
import random
import display

# Global variables used to generate the game deck
deck_spades = ["As", "Ks", "Qs", "Js", "Ts", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s"]
deck_hearts = ["Ah", "Kh", "Qh", "Jh", "Th", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h"]
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

# List to hold player and computer current cards, winner hand to recive if had a winner.
player_hand = []
computer_hand = []
winner_hand = []
player_score = 0
computer_score = 0

# Method used to display cards and table game at terminal.
def display_game():
    display.display_computer_hand_hiden()
    display.display_table()
    display.display_player_hand()

# Close the program
def quit_program():
    pass

# Defines who will start the game, through the choice of heads or tails.
def coin_toss():
    pass

# Method used to end the loop at run.py, check if some one won.
def end_loop(winner_hand):
    if "WIN" in winner_hand:
        return False
    else:
        return True

# Method to remove one card at time from deck_game and move to used_deck.
def take_card(used_deck):
    remove = deck_game.pop()
    used_deck.append(remove)

def new_deck():
    global deck_game
    deck_game = full_deck.copy()
    return deck_game

# Shuffle the cards, deal 4 cards to each player, and turn over the first card. 
def start_game(used_deck, reveal_deck_game, player_hand, computer_hand, winner_hand):
    print("########### BEGIN OF START FUNCTION #########")
    print("DECK GAME")
    print(len(deck_game))
    print(deck_game)
    # Random used to shuffle the deck_game before start the cards distribuiton.
    random.shuffle(deck_game)

    winner_hand.clear()

    # For loop give one card to player and one card to computer 4 times. Use take_card to remove from game deck.
    for card in range(4):
        player_card = deck_game[-1]
        player_hand.append(player_card)
        take_card(used_deck)
        computer_card = deck_game[-1]
        computer_hand.append(computer_card)
        take_card(used_deck)

    # First card to start the game at revealed deck.
    table_card = deck_game[-1]
    take_card(used_deck)
    reveal_deck_game.append(table_card)

    print("PLAYER HAND")
    print(player_hand)
    print("COMPUTER HAND")
    print(computer_hand)
    print("REVEALED DECK")
    print(reveal_deck_game)
    print("GAME DECK")
    print(len(deck_game))
    print(deck_game)
    print("USED DECK")
    print(used_deck)
    print("######### END OF START FUNCTION ##########")

# Stops the game and returns to the main menu.
def reset_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand):
    print("######## START OF RESET ACTION #########")
    print(deck_game)
    print(used_deck)
    print(reveal_deck_game)
    print(player_hand)
    print(computer_hand)

    deck_game.clear()
    used_deck.clear()
    reveal_deck_game.clear()
    player_hand.clear()
    computer_hand.clear()

    new_deck()

    print(f"DECK : {deck_game}")
    print(f"USED : {used_deck}")
    print(f"REVEAL : {reveal_deck_game}")
    print(f"PLAYER H : {player_hand}")
    print(f"COMPUTER H : {computer_hand}")
    print(f"WINNER H: {winner_hand}")
    print("############### END OF RESET ACTION ###########")

# Receives the player's decision of which card to discard, and moves it to the discard deck (face revealed).
def player_discard_action(reveal_deck_game, player_hand):
    print("####### START PLAYER DISCARD ACTION ##########")
    print("PLAYER HAND")
    print(player_hand)
    print("REVEAL DECK")
    print(reveal_deck_game)

    while True:
        print("Which card you wanna to discard?")
        print("---- [1] - [2] - [3] - [4] ----")
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
        if selection in ["B", "b"]:
            print("Ending this game! Thanks for playing.")
            reset_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand)
            winner_hand.append("WIN")
            break
        if selection not in ["0", "1", "2", "3", "B", "b"]:
            print("Ops! It`s not a valid selection.")
            continue

    print("PLAYER HAND AFTER DISCARD")
    print(player_hand)
    print("REVEAL DECK")
    print(reveal_deck_game)
    print("########### END OF DISCARD ACTION ##############")

# Receives the player's decision of which card to take, and moves the card to players hand.
def player_take_action(deck_game, reveal_deck_game, player_hand):
    print("############# BEGIN OF A TAKE ACTION #############")
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
            player_hand.append(reveal_deck_game[-2])
            del reveal_deck_game[-2]
            break

        if selection in ["B", "b"]:
            print("Confirm your decision first.")
            reset_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand)
            winner_hand.append("WIN")
            break

        if selection not in ["H", "h", "R", "r", "B", "b"]:
            print("Ops! Its not a valid selection.")
            continue

    print("PLAYER HAND AFTER TAKE ACTION")
    print(player_hand)
    print("############## END OF PLAYER TAKE ACTION ##########")

# Check the cards in hand and purchase options and make a decision.
def computer_action(computer_hand, reveal_deck_game, deck_game):
    print("########### BEGIN OF COMPUTER ACTION #############")
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

    # Discard action start.
    for card in discard_option:
        if card in ch_list:
            if card == cc1:
                if card != reveal_deck_game[-1][0]:
                    reveal_deck_game.append(computer_hand[0])
                    del computer_hand[0]
                    break
            elif card == cc2:
                if card != reveal_deck_game[-1][0]:
                    reveal_deck_game.append(computer_hand[1])
                    del computer_hand[1]
                    break
            elif card == cc3:
                if card != reveal_deck_game[-1][0]:
                    reveal_deck_game.append(computer_hand[2])
                    del computer_hand[2]
                    break
            else:
                if card != reveal_deck_game[-1][0]:
                    reveal_deck_game.append(computer_hand[3])
                    del computer_hand[3]
                    break
        else:
            for cards in potential_win:
                if cards not in reveal_deck_game[:][0]:
                    if cards == cc1: 
                        reveal_deck_game.append(computer_hand[0])
                        del computer_hand[0]
                        break
                    elif cards == cc2:
                        reveal_deck_game.append(computer_hand[1])
                        del computer_hand[1]
                        break
                    elif cards == cc3:
                        reveal_deck_game.append(computer_hand[2])
                        del computer_hand[2]
                        break
                    elif cards == cc4:
                        reveal_deck_game.append(computer_hand[3])
                        del computer_hand[3]
                        break
                    else:
                        reveal_deck_game.append(computer_hand[0])
                        del computer_hand[0]
                        break

    # Take a new card action
    # First check if have any potencial win, then check if the card at reveal deck match with any card at hand.
    if len(potential_win) == 0:
            if reveal_deck_game[-2][0] in ch_list:
                computer_hand.append(reveal_deck_game[-2])
                del reveal_deck_game[-2]
            else:    
                computer_hand.append(deck_game[-1])
                del deck_game[-1]
    # If have any potencial win, check if the same card was at reveal deck, if yes take it, if not take from hidden deck.
    else:
        for card in potential_win:
            try:
                if card == reveal_deck_game[-2][0]:
                    computer_hand.append(reveal_deck_game[-2])
                    del reveal_deck_game[-2]
                else:
                    computer_hand.append(deck_game[-1])
                    del deck_game[-1]
            except:
                computer_hand.append(deck_game[-1])
                del deck_game[-1]

    print("COUNTER LIST")
    print(counter_list)
    print("COMP DISCARD OPTIONS")
    print(discard_option)
    print("COMP POTENTIAL WIN")
    print(potential_win)
    print("COMPUTER HAND AFTER ACTION")
    print(computer_hand)
    print("################# END OF COMPUTER ACTION #############")

# Check if the cards in the hand (does not consider suits) are 3 of a kind, and return if had a winner.
def win_check(player_hand, computer_hand, winner_hand, player_score, computer_score):
    print("WIN TEST CHECK START")
    # player cards
    c1 = player_hand[0][0]
    c2 = player_hand[1][0]
    c3 = player_hand[2][0]
    c4 = player_hand[3][0]

    # player hand list (all cards numbers/letters) and counter list (dictionary to group the cards).
    ph_list = [c1, c2, c3, c4]
    player_counter_list = Counter(ph_list)

    # use a for loop at counter list to check if any card had 3 of the same value.
    for card, number in player_counter_list.items():
        if number == 3:
            print("You win! Congratulations.")
            winner_hand.append("WIN")
            player_score = player_score + 1
            end_loop(winner_hand)

    # computer cards
    cc1 = computer_hand[0][0]
    cc2 = computer_hand[1][0]
    cc3 = computer_hand[2][0]
    cc4 = computer_hand[3][0]

    # computer hand list (all cards numbers/letters) and counter list (dictionary to group the cards).
    ch_list = [cc1, cc2, cc3, cc4]
    computer_counter_list = Counter(ch_list)

    # use a for loop at counter list to check if any card had 3 of the same value.
    for card, number in computer_counter_list.items():
        if number == 3:
            print("You lose! Don't be sad, try again.")
            winner_hand.append("WIN")
            computer_score = computer_score + 1
            end_loop(winner_hand)

    print("PLAYER CHECK")
    print(ph_list)
    print(player_counter_list)
    print("COMPUTER CHECK")
    print(ch_list)
    print(computer_counter_list)
    print("WIN TEST CHECK END")

# Checks if the last discard of player/computer match with the last reveal card, if yes, win a extra round.
def extra_round_check():
    last_card = reveal_deck_game[-2][0]
    discarded_card = reveal_deck_game[-1][0]

    if last_card == discarded_card:
        print("Extra round")

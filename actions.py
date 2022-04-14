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

# List to hold player and computer current cards, winner hand to recive if had a winner and the score points.
player_hand = []
computer_hand = []
winner_hand = []
player_score = []
computer_score = []

def display_game():
    '''
    Method used to display cards and table game at terminal.
    '''
    display.display_computer_hand_hiden()
    display.display_table()
    display.display_player_hand()

def display_game_alternative():
    '''
    Method used to display cards and table game at terminal, after player discard action.
    '''
    display.display_computer_hand_hiden()
    display.display_table_alternative()
    display.display_player_hand()

def display_end_game():
    '''
    Method used to display cards and table game at terminal, if some one win.
    '''
    display.display_computer_hand_reveal()
    display.display_table()
    display.display_player_hand()

def end_loop(winner_hand):
    '''
    Method used to end the loop at run.py, check if some one won.
    '''
    if "WIN" in winner_hand:
        return False
    else:
        return True

def take_card(used_deck):
    '''
    Method to remove one card at time from deck_game and move to used_deck.
    '''
    remove = deck_game.pop()
    used_deck.append(remove)

def new_deck():
    '''
    Method used to reset the deck_game.
    '''
    global deck_game
    deck_game = full_deck.copy()
    return deck_game
 
def start_game(used_deck, reveal_deck_game, player_hand, computer_hand, winner_hand):
    '''
    Shuffle the cards, deal 4 cards to each player, and turn over the first card.
    First get 8 cards from deck_game, append 4 to player_hand and 4 to computer_hand,
    then get 1 more card to reveal_deck_game. Each time deals a card, remove from
    deck_game and move to used_cards.
    '''

    # Random used to shuffle the deck_game before start the cards distribuiton.
    random.shuffle(deck_game)

    # Clear the winner_hand, to star a new game.
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

def reset_game(deck_game, used_deck, reveal_deck_game, player_hand, computer_hand):
    '''
    Reset the game variables to start a new game.
    '''

    # Clear function to set all list empty.
    deck_game.clear()
    used_deck.clear()
    reveal_deck_game.clear()
    player_hand.clear()
    computer_hand.clear()

    # Method to generate a new deck_game.
    new_deck()

def player_discard_action(reveal_deck_game, player_hand):
    '''
    Receives the player's decision of which card to discard, and moves it to the discard deck (face revealed).
    '''

    # While used to run the options until get one correct selection.
    while True:
        print("Which card you wanna to discard?")
        print("---- [1] - [2] - [3] - [4] ----")
        selection = input("> \n")

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
        if selection not in ["1", "2", "3", "4"]:
            print("Ops! It`s not a valid selection.")
            continue

def player_take_action(deck_game, reveal_deck_game, player_hand):
    '''   
    Receives the player's decision of which card to take, 
    moves the card to players hand and removes from the chosen deck
    '''
    # While used to run the options until get one correct selection.
    while True:
        print("Which deck do you want to take another card from?")
        print("- - - - - - - [H]idden - [R]eveal - - - - - - -")
        print("- - - - - [B] Restart or Back to menu! - - - - -")
        selection = input("> \n")
        
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

def computer_action(computer_hand, reveal_deck_game, deck_game):
    '''
    Method to computer check the cards in hand and purchase options and make a decision.
    '''

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

    # This if run when dont have any match
    if len(computer_hand) > 4:
        reveal_deck_game.append(computer_hand[0])
        del computer_hand[0]

    # Take a new card action start.
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

def win_check(player_hand, computer_hand, winner_hand, player_score, computer_score):
    '''
    Check if the cards in the hand (does not consider suits) are 3 of a kind, 
    and return if had a winner.
    '''
    
    # player cards
    c1 = player_hand[0][0]
    c2 = player_hand[1][0]
    c3 = player_hand[2][0]
    c4 = player_hand[3][0]

    # player hand list (all cards numbers/letters) and counter list (Dictionary to group the cards).
    ph_list = [c1, c2, c3, c4]
    player_counter_list = Counter(ph_list)

    # Use a for loop at counter list to check if any card had 3 of the same value.
    for card, number in player_counter_list.items():
        if number == 3:
            display_end_game()
            print("You win! Congratulations.")
            winner_hand.append("WIN")
            player_score.append("+")
            end_loop(winner_hand)

    # computer cards
    cc1 = computer_hand[0][0]
    cc2 = computer_hand[1][0]
    cc3 = computer_hand[2][0]
    cc4 = computer_hand[3][0]

    # computer hand list (all cards numbers/letters) and counter list (Dictionary to group the cards).
    ch_list = [cc1, cc2, cc3, cc4]
    computer_counter_list = Counter(ch_list)

    # Use a for loop at counter list to check if any card had 3 of the same value.
    for card, number in computer_counter_list.items():
        if number == 3:
            display_end_game()
            print("You lose! Don't be sad, try again.")
            winner_hand.append("WIN")
            computer_score.append("+")
            end_loop(winner_hand)

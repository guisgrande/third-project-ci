import actions as act
import display as dis
import random
import os
import time

# Main python file, have access to actions.py and display.py, used to run the game.

# Global variables.
game_running = True
player_start = None

def clear():
    '''
    Method used to clear the terminal.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def change_false():
    '''
    Method used to change player_start to False.
    '''
    global player_start
    player_start = False
    return player_start

def change_true():
    '''
    Method used to change player_start to True.
    '''
    global player_start
    player_start = True
    return player_start

def game_loop(game_running):
    '''
    Run the game in a loop, until either a player wins or the user selects 
    the option to quit. When exiting the loop, executes the play_again method.
    '''
    act.start_game(act.used_deck, act.reveal_deck_game, act.player_hand, act.computer_hand, act.winner_hand)
    while game_running:
        act.display_game()
        # Computer play first if user lose at coin_flip.
        if player_start == False:
            print("- - - - - COMPUTER TURN - - - - -")
            print("Computer is deciding the move")
            print("...")
            time.sleep(5)
            print(" ▭ ⇅ ▭")
            time.sleep(2)
            clear()
            act.computer_action(act.computer_hand, act.reveal_deck_game, act.deck_game)
            act.display_game()
            change_true()
            pass
        act.win_check(act.player_hand, act.computer_hand, act.winner_hand, act.player_score, act.computer_score)
        game_running = act.end_loop(act.winner_hand)
        if not game_running:
            break
        print("- - - - - YOUR TURN - - - - -")
        act.player_discard_action(act.reveal_deck_game, act.player_hand)
        clear()
        act.display_game_alternative()
        act.player_take_action(act.deck_game, act.reveal_deck_game, act.player_hand)
        clear()
        game_running = act.end_loop(act.winner_hand)
        if not game_running:
            break
        act.display_game()
        act.win_check(act.player_hand, act.computer_hand, act.winner_hand, act.player_score, act.computer_score)
        game_running = act.end_loop(act.winner_hand)
        if not game_running:
            break
        print("- - - - - COMPUTER TURN - - - - -")
        print("Computer is deciding the move")
        print("...")
        time.sleep(4)
        print(" ▭ ⇅ ▭")
        time.sleep(1)
        clear()
        act.computer_action(act.computer_hand, act.reveal_deck_game, act.deck_game)

    play_again()

def coin_flip():
    '''
    Displays the options for the user to choose between the coin 
    flips and returns the result of who starts the game.
    '''
    clear()
    dis.choose_coin()
    option = None
    while True:
        print("Select [H] for Heads or [T] for Tails. The winner start the game!")
        selection = input("> \n")
        if selection in ["H", "h"]:
            option = 0
            break
        if selection in ["T", "t"]:
            option = 1
            break
        if selection not in ["H", "h", "T", "t"]:
            print("Ops! Wrong selection, chose a valid option.")
            continue
    result = random.randint(0, 1)

    clear()
    print("Fliping the coin...")
    time.sleep(0.5)
    print("  _")
    time.sleep(0.5)
    print("  /")
    time.sleep(0.5)
    print("  |")
    time.sleep(0.5)
    print("  \\")
    time.sleep(0.5)
    print("  _")
    print(" ")
    time.sleep(0.5)
    clear()

    if option == 0:
        if result == 0:
            dis.coin_heads()
            print("Lucky one. You start.")
            change_true()
        else:
            dis.coin_tails()
            print("No hit, you are the second to play.")
            change_false()
    if option == 1:
        if result == 1:
            dis.coin_tails()
            print("Lucky one. You start.")
            change_true()
        else:
            dis.coin_heads()
            print("No hit, you are the second to play.")
            change_false()

    time.sleep(2)
    clear()

def main_menu():
    '''
    Displays the name of the game, description and rules, 
    and the option to play or close the program.
    '''
    dis.intro_display()
    while True:
        print("Select your action: ")
        selection = input("> \n")
        if selection in ["Q", 'q']:
            print("Closing the program!")
            exit()
            break
        if selection in ["P", 'p']:
            coin_flip()
            print("Starting the game! Take your seat.")
            game_running = True
            game_loop(game_running)
            break
        if selection in ["R", "r"]:
            print('''
---------------================== RULES ==================---------------
  ° Each player receives 4 cards.
  ° Each turn, the player must discard a card and take another.
  ° The discarded card goes into the revealed deck.
  ° The player can buy a card from the revealed deck or the hidden deck.
  ° The object of the game is to get 3 of the same cards.
-------------------------------------------------------------------------
             ''')
            continue
        if selection not in ["Q", "q", "P", "p", "R", "r"]:
            print("Wrong selection! Should be [P], [R] or [Q].")
            continue

def play_again():
    '''
    Shows the user the option to play again or to return to the main menu.
    Get the selection and executes the choice.
    '''
    while True:
        print("---- Want to continue playing? ----")
        print("[Y] - Continue | [N] - Back to menu")
        selection = input("> \n")

        if selection in ["Y", "y"]:
            clear()
            print("Dealing the cards again. Good luck!")
            time.sleep(0.5)
            print(" ▭ ⇅ ▭")
            time.sleep(0.5)
            print(" ▭ ⇅ ▭")
            time.sleep(0.5)
            print(" ▭ ⇅ ▭")
            time.sleep(0.5)
            print(" ▭ ⇅ ▭")
            time.sleep(1)
            clear()
            game_running = True
            act.reset_game(act.deck_game, act.used_deck, act.reveal_deck_game, act.player_hand, act.computer_hand)
            game_loop(game_running)

        if selection in ["N", "n"]:
            clear()
            print("Thanks for playing, ending this game. Until next time!")
            act.reset_score(act.player_score, act.computer_score)
            time.sleep(2)
            game_running = False
            main_menu()

if __name__ == '__main__':
    main_menu()
import actions
import display

# Main python file.

game_running = True

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
            # start_game(used_deck, reveal_deck_game, player_hand, computer_hand)
            game_loop(game_running)
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

def game_loop(game_running):
    actions.start_game(actions.used_deck, actions.reveal_deck_game, actions.player_hand, actions.computer_hand)
    while game_running:
        actions.player_discard_action(actions.reveal_deck_game, actions.player_hand)
        actions.player_take_action(actions.deck_game, actions.reveal_deck_game, actions.player_hand)
        actions.win_check(actions.player_hand, actions.computer_hand)
        # display table and hands
        # computer action delay 3 seconds
        actions.computer_action(actions.computer_hand, actions.reveal_deck_game, actions.deck_game)
        actions.win_check(actions.player_hand, actions.computer_hand)
        # display table and hands

    # reset cards
    # actions.main_menu()

main_menu()
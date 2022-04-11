import actions as act
import display

# Main python file.
game_running = ''

def game_loop(game_running):
    game_running = True
    win = "WIN"
    act.start_game(act.used_deck, act.reveal_deck_game, act.player_hand, act.computer_hand)
    while game_running:
        act.win_check(act.player_hand, act.computer_hand, act.winner_hand)
        act.display_game()
        if win in act.winner_hand:
            break
        act.player_discard_action(act.reveal_deck_game, act.player_hand)
        act.player_take_action(act.deck_game, act.reveal_deck_game, act.player_hand)
        act.win_check(act.player_hand, act.computer_hand, act.winner_hand)
        act.display_game()
        if win in act.winner_hand:
            break
        act.computer_action(act.computer_hand, act.reveal_deck_game, act.deck_game)

    print("OUT OF LOOP")
    # reset cards
    # act.main_menu()

# Displays the name of the game, description and rules, and the option to play or close the program.
def main_menu():
    print(display.intro_display())
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

main_menu()
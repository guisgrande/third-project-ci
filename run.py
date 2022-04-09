import actions

# Main python file.

actions.main_menu()
game_running = True

def game_loop(game_running):
    actions.start_game(used_deck, reveal_deck_game, player_hand, computer_hand)
    while game_running:
        # actions.player_discard_action(reveal_deck_game, player_hand)
        # actions.player_take_action(deck_game, reveal_deck_game, player_hand)
        # actions.win_check(player_hand, computer_hand)
        # display table and hands
        # computer action delay 3 seconds
        # actions.computer_action(computer_hand, reveal_deck_game, deck_game)
        # actions.win_check(player_hand, computer_hand)
        #display table and hands

    # reset cards
    # actions.main_menu()
import actions as act

# Varibles to get ANSI characters code, used to add color.

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
# YELLOW
YW = "\033[0;33m"
# RESET
RT = "\033[0;0m"

line = '______________________________________________________________________'


def intro_display():
    '''
    Display the main menu and the options for the user.
    '''
    opt = f"{YW}CHOOSE: [P] for PLAY | [R] for RULES | [Q] for QUIT{RT}"
    d_line = '===================================='
    dl = '==========='
    print(f'''
{d_line}{d_line}
    {dl}={YW}______{RT}====={YW}______{RT}===={YW}______{RT}====={YW}______{RT}{dl}===
    {dl}{YW}|___   |{RT}==={YW}|  __  |{RT}=={YW}|   ___|{RT}==={YW}|  __  |{RT}{dl}==
    {dl}={YW}___|  |{RT}==={YW}| |{RT}=={YW}| |{RT}=={YW}|  |__{RT}====={YW}| |__| |{RT}{dl}==
    {dl}{YW}|___   |{RT}==={YW}| |{RT}=={YW}| |{RT}=={YW}|   __|{RT}===={YW}|  __  |{RT}{dl}==
    {dl}={YW}___|  |{RT}==={YW}| |__| |{RT}=={YW}|  |{RT}======={YW}| |{RT}=={YW}| |{RT}{dl}==
    {dl}{YW}|______|{RT}==={YW}|______|{RT}=={YW}|__|{RT}======={YW}|_|{RT}=={YW}|_|{RT}{dl}==
{d_line}{d_line}
    {dl}={YW}__{RT}===={YW}___{RT}==={YW}__{RT}===={YW}___{RT}======{YW}_{RT}===={YW}_____{RT}{dl}====
    {dl}{YW}|  |{RT}=={YW}/  /{RT}=={YW}|  |{RT}=={YW}|  _ \{RT}==={YW}| |{RT}=={YW}|  _  \{RT}{dl}===
    {dl}{YW}|  |{RT}={YW}/  /{RT}==={YW}|  |{RT}=={YW}| |{RT}={YW}\ \{RT}=={YW}| |{RT}=={YW}| | \  \{RT}{dl}==
    {dl}{YW}|      <{RT}===={YW}|  |{RT}=={YW}| |{RT}=={YW}\ \{RT}={YW}| |{RT}=={YW}| |  |  |{RT}{dl}=
    {dl}{YW}|  |{RT}={YW}\  \{RT}==={YW}|  |{RT}=={YW}| |{RT}==={YW}\ \| |{RT}=={YW}| |_/  /{RT}{dl}==
    {dl}{YW}|__|{RT}=={YW}\__\{RT}=={YW}|__|{RT}=={YW}|_|{RT}===={YW}\___|{RT}=={YW}|_____/{RT}{dl}===
{d_line}{d_line}''')
    print(f' ------== {opt} ==------')
    print(f'{d_line}{d_line}')


def choose_coin():
    '''
    Display the two faces of a coin for the user to choose.
    '''
    print(f'''{YW}
               __________               __________
              /          \\\           /  ______  \\\\
             /  |\_/\_/|  \\\         /  /     \\\\  \\\\
            /   |      |   \\\       /  |       ||  \\\\
            \   |______|   //       \   \     //   //
             \  --------  //         \   |___||   //
              \__________//           \__________//
                [T]ails                  [H]eads
{RT}''')


def coin_heads():
    '''
    Display the face Heads, if this was the result.
    '''
    print(f'''{YW}
               __________
              /  ______  \\\\
             /  /     \\\\  \\\\
            /  |       ||  \\\\
            \   \     //   //
             \   |___||   //
              \__________//
             The result is
                 HEADS
{RT}''')


def coin_tails():
    '''
    Display the face Tails, if this was the result.
    '''
    print(f'''{YW}
               __________
              /          \\\\
             /  |\_/\_/|  \\\\
            /   |      |   \\\\
            \   |______|   //
             \  --------  //
              \__________//
             The result is
                 TAILS
{RT}''')


def display_computer_hand_hiden():
    '''
    Display 4 hidden cards that represent the computer's cards.
    '''
    print('''
=============== COMPUTER HAND ===============================================
                _____   _____   _____   _____
               |#####| |#####| |#####| |#####|
               |#####| |#####| |#####| |#####|
               |_____| |_____| |_____| |_____|              ''')


def suits_display(suits):
    '''
    Get the character from the suit of the card and returns
    the corresponding symbol.
    '''

    # Symbols plus color
    clubs = BLUE + "♣" + RT
    hearts = RED + "♥" + RT
    spades = BLUE + "♠" + RT
    diamonds = RED + "♦" + RT

    if suits == "c":
        return clubs
    elif suits == "h":
        return hearts
    elif suits == "s":
        return spades
    elif suits == "d":
        return diamonds
    else:
        print("X")


def display_computer_hand_reveal():
    '''
    Display the cards from the computer's hand, used when someone wins.
    '''
    cc1 = act.computer_hand[0][0]
    cc2 = act.computer_hand[1][0]
    cc3 = act.computer_hand[2][0]
    cc4 = act.computer_hand[3][0]

    cs1 = suits_display(act.computer_hand[0][1])
    cs2 = suits_display(act.computer_hand[1][1])
    cs3 = suits_display(act.computer_hand[2][1])
    cs4 = suits_display(act.computer_hand[3][1])

    print(f'''
============== COMPUTER HAND =============================================
                 _____   _____   _____   _____
                | {cc1}   | | {cc2}   | | {cc3}   | | {cc4}   |
                | {cs1}   | | {cs2}   | | {cs3}   | | {cs4}   |
                |_____| |_____| |_____| |_____|
''')


def display_player_hand():
    '''
    Displays the cards in the player's hand, and shows
    the discard option under each card.
    '''

    # Try and except, used to show hand after player discard a card.
    try:
        c1 = act.player_hand[0][0]
        s1 = suits_display(act.player_hand[0][1])
    except:
        c1 = "X"
        s1 = f"{YW}#{RT}"

    try:
        c2 = act.player_hand[1][0]
        s2 = suits_display(act.player_hand[1][1])
    except:
        c2 = "X"
        s2 = f"{YW}#{RT}"

    try:
        c3 = act.player_hand[2][0]
        s3 = suits_display(act.player_hand[2][1])
    except:
        c3 = "X"
        s3 = f"{YW}#{RT}"

    try:
        c4 = act.player_hand[3][0]
        s4 = suits_display(act.player_hand[3][1])
    except:
        c4 = "X"
        s4 = f"{YW}#{RT}"

    print(f'''                _____   _____   _____   _____
               | {c1}   | | {c2}   | | {c3}   | | {c4}   |
               | {s1}   | | {s2}   | | {s3}   | | {s4}   |
               |_____| |_____| |_____| |_____|
                >[1]    >[2]    >[3]    >[4]
=============== YOUR HAND ================================================''')


def display_table():
    '''
    Display the two available decks and the corresponding option for each.
    It also shows the score points of each player, the number of cards
    in each deck, and the last 5 cards revealed.
    '''

    rc = act.reveal_deck_game[-1][0]
    rs = suits_display(act.reveal_deck_game[-1][1])

    # Try / except used to show alternative information when don't have any
    # card at respective position at reveal deck.
    try:
        rc2 = act.reveal_deck_game[-2][0]
        rs2 = suits_display(act.reveal_deck_game[-2][1])
    except:
        rc2 = "X"
        rs2 = "-"

    try:
        rc3 = act.reveal_deck_game[-3][0]
        rs3 = suits_display(act.reveal_deck_game[-3][1])
    except:
        rc3 = "X"
        rs3 = "-"

    try:
        rc4 = act.reveal_deck_game[-4][0]
        rs4 = suits_display(act.reveal_deck_game[-4][1])
    except:
        rc4 = "X"
        rs4 = "-"

    try:
        rc5 = act.reveal_deck_game[-5][0]
        rs5 = suits_display(act.reveal_deck_game[-5][1])
    except:
        rc5 = "X"
        rs5 = "-"

    # Short variable to player and computer score
    if len(act.player_score) >= 10:
        p_sc = GREEN + str(len(act.player_score)) + RT
    else:
        p_sc = GREEN + "0" + str(len(act.player_score)) + RT

    if len(act.computer_score) >= 10:
        c_sc = RED + str(len(act.computer_score)) + RT
    else:
        c_sc = RED + "0" + str(len(act.computer_score)) + RT

    # Short variabel to hidden deck and reveal deck
    if len(act.deck_game) < 10:
        hd = YW + "0" + str(len(act.deck_game)) + RT
    else:
        hd = YW + str(len(act.deck_game)) + RT

    if len(act.reveal_deck_game) < 10:
        rd = YW + "0" + str(len(act.reveal_deck_game)) + RT
    else:
        rd = YW + str(len(act.reveal_deck_game)) + RT

    table1 = f'{YW}2º{RT} {rc2} {rs2}  {YW}3º{RT} {rc3} {rs3}'
    table2 = f'{YW}4º{RT} {rc4} {rs4}  {YW}5º{RT} {rc5} {rs5}'

    print(f'''  {line}
                    _____    CPU    _____
                   |#####|   *{c_sc}   | {rc}   |         | LAST REVEAL CARDS
                   |#####|  SCORE  | {rs}   |         |   {table1}
                   |_____|   *{p_sc}   |_____|         |   {table2}
                   <{hd}>[H]   YOU   <{rd}>[R]
  {line}''')


def display_table_alternative():
    '''
    Display an alternative table, to show the take option of
    the revealed deck, the hand of the player with one card less
    and the card that will then be added to the revealed deck.
    '''

    # Short variable to reveal card / suit
    rc = act.reveal_deck_game[-2][0]
    rs = suits_display(act.reveal_deck_game[-2][1])

    # Short variabel to waitin card / suit
    wc = act.reveal_deck_game[-1][0]
    ws = suits_display(act.reveal_deck_game[-1][1])

    # Try / except used to show alternative information when don't
    # have any card at respective position at reveal deck.
    try:
        rc2 = act.reveal_deck_game[-3][0]
        rs2 = suits_display(act.reveal_deck_game[-3][1])
    except:
        rc2 = "X"
        rs2 = "-"

    try:
        rc3 = act.reveal_deck_game[-4][0]
        rs3 = suits_display(act.reveal_deck_game[-4][1])
    except:
        rc3 = "X"
        rs3 = "-"

    try:
        rc4 = act.reveal_deck_game[-5][0]
        rs4 = suits_display(act.reveal_deck_game[-5][1])
    except:
        rc4 = "X"
        rs4 = "-"

    try:
        rc5 = act.reveal_deck_game[-6][0]
        rs5 = suits_display(act.reveal_deck_game[-6][1])
    except:
        rc5 = "X"
        rs5 = "-"

    # Short variable to player and computer score
    if len(act.player_score) >= 10:
        p_sc = GREEN + str(len(act.player_score)) + RT
    else:
        p_sc = GREEN + "0" + str(len(act.player_score)) + RT

    if len(act.computer_score) >= 10:
        c_sc = RED + str(len(act.computer_score)) + RT
    else:
        c_sc = RED + "0" + str(len(act.computer_score)) + RT

    # Short variabel to hidden deck and reveal deck
    if len(act.deck_game) < 10:
        hd = YW + "0" + str(len(act.deck_game)) + RT
    else:
        hd = YW + str(len(act.deck_game)) + RT

    if len(act.reveal_deck_game) < 10:
        rd = YW + "0" + str(len(act.reveal_deck_game)) + RT
    else:
        rd = YW + str(len(act.reveal_deck_game)) + RT

    table1 = f'{YW}2º{RT} {rc2} {rs2}  {YW}3º{RT} {rc3} {rs3}'
    table2 = f'{YW}4º{RT} {rc4} {rs4}  {YW}5º{RT} {rc5} {rs5}'

    print(f'''  {line}
                    _____    CPU    _____
                   |#####|   *{c_sc}   | {rc}   |         | LAST REVEAL CARDS
                   |#####|  SCORE  | {rs}   |         |   {table1}
                   |_____|   *{p_sc}   |_____|         |   {table2}
                   <{hd}>[H]   YOU   <{rd}>[R]         # WAITING - {wc} {ws}
  {line}''')

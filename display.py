import actions as act

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0;0m"

def intro_display():
        options = f"{YELLOW}CHOOSE: [P] for PLAY | [R] for RULES | [Q] for QUIT{RESET}"
        print(f'''
==========================================================================
     ============{CYAN}______{RESET}====={CYAN}______{RESET}===={CYAN}______{RESET}====={CYAN}______{RESET}=============
     ==========={CYAN}|___   |{RESET}==={CYAN}|  __  |{RESET}=={CYAN}|   ___|{RESET}==={CYAN}|  __  |{RESET}============
     ============{CYAN}___|  |{RESET}==={CYAN}| |{RESET}=={CYAN}| |{RESET}=={CYAN}|  |__{RESET}====={CYAN}| |__| |{RESET}============
     ==========={CYAN}|___   |{RESET}==={CYAN}| |{RESET}=={CYAN}| |{RESET}=={CYAN}|   __|{RESET}===={CYAN}|  __  |{RESET}============
     ============{CYAN}___|  |{RESET}==={CYAN}| |__| |{RESET}=={CYAN}|  |{RESET}======={CYAN}| |{RESET}=={CYAN}| |{RESET}============
     ==========={CYAN}|______|{RESET}==={CYAN}|______|{RESET}=={CYAN}|__|{RESET}======={CYAN}|_|{RESET}=={CYAN}|_|{RESET}============
==========================================================================
     ============{CYAN}__{RESET}===={CYAN}___{RESET}==={CYAN}__{RESET}===={CYAN}___{RESET}======{CYAN}_{RESET}===={CYAN}_____{RESET}===============
     ==========={CYAN}|  |{RESET}=={CYAN}/  /{RESET}=={CYAN}|  |{RESET}=={CYAN}|  _ \{RESET}==={CYAN}| |{RESET}=={CYAN}|  _  \{RESET}==============
     ==========={CYAN}|  |{RESET}={CYAN}/  /{RESET}==={CYAN}|  |{RESET}=={CYAN}| |{RESET}={CYAN}\ \{RESET}=={CYAN}| |{RESET}=={CYAN}| | \  \{RESET}=============
     ==========={CYAN}|      <{RESET}===={CYAN}|  |{RESET}=={CYAN}| |{RESET}=={CYAN}\ \{RESET}={CYAN}| |{RESET}=={CYAN}| |  |  |{RESET}============
     ==========={CYAN}|  |{RESET}={CYAN}\  \{RESET}==={CYAN}|  |{RESET}=={CYAN}| |{RESET}==={CYAN}\ \| |{RESET}=={CYAN}| |_/  /{RESET}=============
     ==========={CYAN}|__|{RESET}=={CYAN}\__\{RESET}=={CYAN}|__|{RESET}=={CYAN}|_|{RESET}===={CYAN}\___|{RESET}=={CYAN}|_____/{RESET}==============
==========================================================================''')
        print(f' -------== {options} ==-------')
        print('==========================================================================')

def choose_coin():
    print(f'''{YELLOW}
          __________               __________    
         /          \\\           /  ______  \\\ 
        /  |\_/\_/|  \\\         /  /     \\\  \\\ 
       /   |      |   \\\       /  |       ||  \\\ 
       \   |______|   //       \   \     //   //
        \  --------  //         \   |___||   //
         \__________//           \__________//
           [T]ails                  [H]eads  
          
{RESET}''')

def coin_heads():
    print(f'''{YELLOW}
          __________    
         /  ______  \\\ 
        /  /     \\\  \\\ 
       /  |       ||  \\\ 
       \   \     //   //
        \   |___||   //
         \__________//
        The result is
            HEADS
{RESET}''')

def coin_tails():
    print(f'''{YELLOW}
          __________             
         /          \\\      
        /  |\_/\_/|  \\\     
       /   |      |   \\\     
       \   |______|   //     
        \  --------  //      
         \__________// 
        The result is
            TAILS
{RESET}''')

def display_computer_hand_hiden():
        print('''
================================ COMPUTER HAND ==================================
                     _______   _______   _______   _______
                    |       | |       | |       | |       |
                    |#######| |#######| |#######| |#######|
                    |#######| |#######| |#######| |#######|
                    |_______| |_______| |_______| |_______|''')

def suits_display(suits):
    clubs = BLUE + "♣" + RESET
    hearts = RED + "♥" + RESET
    spades = BLUE + "♠" + RESET
    diamonds = RED + "♦" + RESET
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

    cc1 = act.computer_hand[0][0]
    cc2 = act.computer_hand[1][0]
    cc3 = act.computer_hand[2][0]
    cc4 = act.computer_hand[3][0]
    
    cs1 = suits_display(act.computer_hand[0][1])
    cs2 = suits_display(act.computer_hand[1][1])
    cs3 = suits_display(act.computer_hand[2][1])
    cs4 = suits_display(act.computer_hand[3][1])

    print(f'''
================================ COMPUTER HAND ==================================
                     _______   _______   _______   _______
                    |       | |       | |       | |       |
                    | {cc1}     | | {cc2}     | | {cc3}     | | {cc4}     |
                    | {cs1}     | | {cs2}     | | {cs3}     | | {cs4}     |
                    |_______| |_______| |_______| |_______|
''')

def display_player_hand():
        
    c1 = act.player_hand[0][0]
    c2 = act.player_hand[1][0]
    c3 = act.player_hand[2][0]
    c4 = act.player_hand[3][0]

    s1 = suits_display(act.player_hand[0][1])
    s2 = suits_display(act.player_hand[1][1])
    s3 = suits_display(act.player_hand[2][1])
    s4 = suits_display(act.player_hand[3][1])
            
    print(f'''                     _______   _______   _______   _______
                    |       | |       | |       | |       |
                    | {c1}     | | {c2}     | | {c3}     | | {c4}     |
                    | {s1}     | | {s2}     | | {s3}     | | {s4}     |
                    |_______| |_______| |_______| |_______|
                      >[1]      >[2]      >[3]      >[4]
================================== YOUR HAND ====================================
''')

def display_table():

        rc = act.reveal_deck_game[-1][0]
        rs = suits_display(act.reveal_deck_game[-1][1])
        # Short variable to player and computer score
        if len(act.player_score) >= 10:
            p_sc = GREEN + str(len(act.player_score)) + RESET
        else:
            p_sc = GREEN + "0" + str(len(act.player_score)) + RESET

        if len(act.computer_score) >= 10:
            c_sc = RED + str(len(act.computer_score)) + RESET
        else:
            c_sc = RED + "0" + str(len(act.computer_score)) + RESET

        # Short variabel to hidden deck and reveal deck
        if len(act.deck_game) < 10:
            hd = YELLOW + "0" + str(len(act.deck_game)) + RESET
        else:
            hd = YELLOW + str(len(act.deck_game)) + RESET

        if len(act.reveal_deck_game) < 10:
            rd = YELLOW + "0" + str(len(act.reveal_deck_game)) + RESET
        else:
            rd = YELLOW + str(len(act.reveal_deck_game)) + RESET

        print(f''' _____________________________________________________________________________
                          _______               _______
                         |       |     CPU     |       |
                         |#######|     *{c_sc}     | {rc}     |
                         |#######|    SCORE    | {rs}     |
                         |_______|     *{p_sc}     |_______|
                          <{hd}>[H]      YOU      <{rd}>[R] 
  _____________________________________________________________________________''')
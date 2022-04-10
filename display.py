import actions as act

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0;0m"

def intro_display():
        options = YELLOW + "CHOOSE: [P] for PLAY | [R] for RULES | [Q] for QUIT" + RESET
        print(f'''
======================================================================================================
 ========={CYAN}______{RESET}====={CYAN}______{RESET}===={CYAN}______{RESET}====={CYAN}______{RESET}====={CYAN}__{RESET}===={CYAN}___{RESET}==={CYAN}__{RESET}===={CYAN}___{RESET}======{CYAN}_{RESET}===={CYAN}_____{RESET}===========
 ========{CYAN}|___   |{RESET}==={CYAN}|  __  |{RESET}=={CYAN}|   ___|{RESET}==={CYAN}|  __  |{RESET}==={CYAN}|  |{RESET}=={CYAN}/  /{RESET}=={CYAN}|  |{RESET}=={CYAN}|  _ \{RESET}==={CYAN}| |{RESET}=={CYAN}|  _  \{RESET}==========
 ========={CYAN}___|  |{RESET}==={CYAN}| |{RESET}=={CYAN}| |{RESET}=={CYAN}|  |__{RESET}====={CYAN}| |__| |{RESET}==={CYAN}|  |{RESET}={CYAN}/  /{RESET}==={CYAN}|  |{RESET}=={CYAN}| |{RESET}={CYAN}\ \{RESET}=={CYAN}| |{RESET}=={CYAN}| | \  \{RESET}=========
 ========{CYAN}|___   |{RESET}==={CYAN}| |{RESET}=={CYAN}| |{RESET}=={CYAN}|   __|{RESET}===={CYAN}|  __  |{RESET}==={CYAN}|      <{RESET}===={CYAN}|  |{RESET}=={CYAN}| |{RESET}=={CYAN}\ \{RESET}={CYAN}| |{RESET}=={CYAN}| |  |  |{RESET}========
 ========={CYAN}___|  |{RESET}==={CYAN}| |__| |{RESET}=={CYAN}|  |{RESET}======={CYAN}| |{RESET}=={CYAN}| |{RESET}==={CYAN}|  |{RESET}={CYAN}\  \{RESET}==={CYAN}|  |{RESET}=={CYAN}| |{RESET}==={CYAN}\ \| |{RESET}=={CYAN}| |_/  /{RESET}=========
 ========{CYAN}|______|{RESET}==={CYAN}|______|{RESET}=={CYAN}|__|{RESET}======={CYAN}|_|{RESET}=={CYAN}|_|{RESET}==={CYAN}|__|{RESET}=={CYAN}\__\{RESET}=={CYAN}|__|{RESET}=={CYAN}|_|{RESET}===={CYAN}\___|{RESET}=={CYAN}|_____/{RESET}==========
======================================================================================================''')
        print(f'----------------------== {options} ==----------------------')
        print('======================================================================================================')

choose_coin = YELLOW + '''
          __________               __________    
         /          \\\           /  ______  \\\ 
        /  |\_/\_/|  \\\         /  /     \\\  \\\ 
       /   |      |   \\\       /  |       ||  \\\ 
       \   |______|   //       \   \     //   //
        \  --------  //         \   |___||   //
         \__________//           \__________//
           [T]ails                  [H]eads  
          
''' + RESET

coin_heads = YELLOW + '''
          __________    
         /  ______  \\\ 
        /  /     \\\  \\\ 
       /  |       ||  \\\ 
       \   \     //   //
        \   |___||   //
         \__________//
           
''' + RESET

coin_tails =  YELLOW + '''
          __________             
         /          \\\      
        /  |\_/\_/|  \\\     
       /   |      |   \\\     
       \   |______|   //     
        \  --------  //      
         \__________// 

''' + RESET

def display_computer_hand_hiden():
        print('''
=========================================== COMPUTER HAND ============================================
                          __________   __________   __________   __________
                         |          | |          | |          | |          |
                         |##########| |##########| |##########| |##########|
                         |##########| |##########| |##########| |##########|
                         |##########| |##########| |##########| |##########|
                         |##########| |##########| |##########| |##########|
                         |__________| |__________| |__________| |__________|
''')

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
======================================================================================================
                         __________   __________   __________   __________
                        |          | |          | |          | |          |
                        | {cc1}        | | {cc2}        | | {cc3}        | | {cc4}        |
                        | {cs1}        | | {cs2}        | | {cs3}        | | {cs4}        |
                        |        {cs1} | |        {cs2} | |        {cs3} | |        {cs4} |
                        |        {cc1} | |        {cc2} | |        {cc3} | |        {cc4} |
                        |__________| |__________| |__________| |__________|

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
                
        print(f'''
                         __________   __________   __________   __________
                        |          | |          | |          | |          |
                        | {c1}        | | {c2}        | | {c3}        | | {c4}        |
                        | {s1}        | | {s2}        | | {s3}        | | {s4}        |
                        |        {s1} | |        {s2} | |        {s3} | |        {s4} |
                        |        {c1} | |        {c2} | |        {c3} | |        {c4} |
                        |__________| |__________| |__________| |__________|
                            >[1]         >[2]         >[3]         >[4]

============================================= YOUR HAND ==============================================
''')

def display_table():

        rc = act.reveal_deck_game[-1][0]
        rs = suits_display(act.reveal_deck_game[-1][1])

        print(f'''
  __________________________________________________________________________________________________
                                __________               __________
                               |          |             |          |
                               |##########|     *_*     | {rc}        |
                               |##########|             | {rs}        |
                               |##########|    SCORE    |        {rs} |
                               |##########|             |        {rc} |
                               |__________|     *_*     |__________|
                                 <  > [H]                 <  > [R] 
  __________________________________________________________________________________________________''')
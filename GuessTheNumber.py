"""Guess The Number Game in Python"""
from random import randint, choices
from time import sleep as wait
import os

hints = []; stop = 0; yes = ["yes", "y"]; no = ["no", "n"]; comp = None; digits = None; wrong = None; real_num = []; guess = None

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def loading(text : str, loop : int):
    for i in range(loop):
        count = 1
        for i in range(3): print(f"{text}{'.'*count}"); count+=1; wait(0.25); clear_console()

def get_hint():
    global hints, wrong, comp, digits, stop, real_num
    real_num = [str(i) for i in str(comp)]; stop_show = 0; result = []
    def find_result(stop_show, real_num, result, hints):
        for i in real_num:
            if stop_show != 1:
                if i not in hints: result.append(' _ ')
                else: result.append(f" {i} "); stop_show = 1
            else: result.append(' _ ')
    if digits <= 3 and stop <= 3:
        stop = 3
        hints.append(choices(real_num)[0])
    elif digits > 3 and digits < 11 and stop < 3:
        stop+=1
        hints.append(choices(real_num)[0])
    find_result(stop_show, real_num, result, hints)
    return ('').join(result)

def get_clue():
    global real_num, guess
    guess_nums = [str(i) for i in str(guess)]
    count = 0
    for i in guess_nums:
        if i in real_num:
            if i == real_num[count]:
                print(f"The number {i} is a correct number and in the correct placement.")
            else:
                print(f"The number {i} is a correct number but in the wrong placement.")
        count+=1

def reset_variables():
    global digits, guess, comp, real_num, stop, hints
    real_num = []; stop = 0; hints = []

def GuessTheNumberGame():
    global yes, no, hints, stop, wrong, comp, digits, guess
    clear_console()
    print(r"""

       ____ _   _ _____ ____ ____    _____ _   _ _____   _   _ _   _ __  __ ____  _____ ____  _ 
      / ___| | | | ____/ ___/ ___|  |_   _| | | | ____| | \ | | | | |  \/  | __ )| ____|  _ \| |
     | |  _| | | |  _| \___ \___ \    | | | |_| |  _|   |  \| | | | | |\/| |  _ \|  _| | |_) | |
     | |_| | |_| | |___ ___) |__) |   | | |  _  | |___  | |\  | |_| | |  | | |_) | |___|  _ <|_|
      \____|\___/|_____|____/____/    |_| |_| |_|_____| |_| \_|\___/|_|  |_|____/|_____|_| \_(_)

    """)
    input("Press Enter to continue...");
    print("\n");
    while True:
        try:
            digits = int(input("Enter how many digits the number will have(max = 10): "))
        except ValueError:
            print("Error: please put an integer-type value.\n"); continue
        if digits > 10 or digits < 1: print("Error: cannot be over maximum number or lesser than 1.\n"); wait(
            3); continue
        try:
            attempts = int(input("Enter how many attempts you want to have(max = 10): "))
        except ValueError:
            print("Error: please put an integer-type value.\n"); continue
        if attempts > 10 or digits < 1: print("Error: cannot be over maximum number or lesser than 1.\n"); wait(
            3); print("Restarting prompts..."); wait(2.5); continue
        choices = ["yes", "y", "no", "n"];
        show_hint = input("Enable hints? (eg. _ _ 7): ").lower();
        if show_hint not in choices:
            wait(1); print("Error: Say yes/y or no/n only."); wait(3); continue
        else:
            break
    wait(1);
    clear_console();
    loading("Starting Game", 5);
    clear_console();
    wait(1)
    print(r"""
       ____    _    __  __ _____   ____ _____  _    ____ _____ _ 
      / ___|  / \  |  \/  | ____| / ___|_   _|/ \  |  _ \_   _| |
     | |  _  / _ \ | |\/| |  _|   \___ \ | | / _ \ | |_) || | | |
     | |_| |/ ___ \| |  | | |___   ___) || |/ ___ \|  _ < | | |_|
      \____/_/   \_\_|  |_|_____| |____/ |_/_/   \_\_| \_\|_| (_)

    """)
    wait(3)
    clear_console(); loading("\nComputer is picking its number", 5)
    clear_console()
    comp = randint(1, int("9" * digits));
    print("\nComputer has finished picking its number!");
    wait(3)
    clear_console()
    wait(3)
    guess = None
    while guess != comp and attempts != 0:
        print(r"""
       ____ _   _ _____ ____ ____  _ 
      / ___| | | | ____/ ___/ ___|| |
     | |  _| | | |  _| \___ \___ \| |
     | |_| | |_| | |___ ___) |__) |_|
      \____|\___/|_____|____/____/(_)

        """)
        wait(3)
        print(f"YOU HAVE {attempts} ATTEMPT(S)!");
        wrong = 0
        wait(3)
        if show_hint in no:
            print(f"\nNumber : {'_' * digits}")
        elif show_hint in yes:
            res = get_hint()
            print(f"\nNumber : {res}")
        wait(3)
        while True:
            try: guess = int(input("Your Guess: "))
            except ValueError: print("Error : Please enter an integer-type value.\n"); continue
            if len(str(guess)) > digits or len(str(guess)) < digits: print(f"Error: Guess' digits cannot be lower or higher than {digits}.\n"); continue
            break
        if guess != comp: wrong = 1; attempts -= 1; print("\nWrong Guess!\n"); wait(3); get_clue(); wait(5); clear_console(); continue
    if attempts == 0: wait(1); print(r"""
       ____    _    __  __ _____    _____     _______ ____  _ 
      / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \| |
     | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | |
     | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <|_|
      \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_(_)
                                                              
    """); wait(5)
    else: wait(1); print(r"""
     __   _____  _   _  __        _____  _   _ _ 
     \ \ / / _ \| | | | \ \      / / _ \| \ | | |
      \ V / | | | | | |  \ \ /\ / / | | |  \| | |
       | || |_| | |_| |   \ V  V /| |_| | |\  |_|
       |_| \___/ \___/     \_/\_/  \___/|_| \_(_)
                                                 
    """); wait(5)


play_game = 1; pgchoices = ["yes", "y", "no", "n"]
while play_game == 1:
    GuessTheNumberGame()
    while True:
        clear_console(); play_game = input("\nWould you like to play again? (Guess The Number Game): ")
        if play_game in yes: play_game = 1; print("Great! Restarting Game..."); wait(3); break
        elif play_game in no: play_game = 0; print("Thanks for playing the game!"); wait(1); break
        else: print("Error: please say yes/y or no/n"); wait(1); continue
    reset_variables()
clear_console()
print(r"""
   ____  ___   ___  ____  ______   _______ _     ____  
  / ___|/ _ \ / _ \|  _ \| __ ) \ / / ____| |  _|  _ \ 
 | |  _| | | | | | | | | |  _ \\ V /|  _| | | (_) | | |
 | |_| | |_| | |_| | |_| | |_) || | | |___|_|  _| |_| |
  \____|\___/ \___/|____/|____/ |_| |_____(_) (_)____/ 
                                                       
""")

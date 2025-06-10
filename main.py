
from mamba.buenacifra import Buenacifra, clear_screen, show_border

from mamba.tero import  Tero, clear_screen, show_border

def menu():
    user_input = 0
    while user_input != 5:
        user_input = display_get_user_input()
        process_user_input(user_input)

def display_get_user_input():
    while True:
        clear_screen()
        show_border()
        print("\t\t\t\t\tMamba Main Menu")
        show_border()
        print("\n1. Ernesto P. Bernas III\n")
        print("2. Abrianne V. Buenacifra\n")
        print("3. Gian Rafael B. Roldan\n")
        print("4. Altheno Mari L. Tero\n")
        print("5. Exit\n")
        return int(input("Please select an option (1 - 5): "))

def process_user_input(user_input):
    match user_input:
        case 1:
            
        case 2:
            Buenacifra().show_menu()
        case 3:
            
        case 4:
            Tero().show_menu()
        case 5:
            pass
        case _:
            input("\nWrong input. Press Enter to try again.")

menu()
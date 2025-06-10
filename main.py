from mamba.bernas import Bernas
from mamba.buenacifra import Buenacifra, clear_screen, show_border
from mamba.roldan import Roldan
from mamba.tero import Tero

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
        print("\n1. Ernesto P. Bernas III")
        print("2. Abrianne V. Buenacifra")
        print("3. Gian Rafael B. Roldan")
        print("4. Altheno Mari L. Tero")
        print("5. Exit\n")
        return int(input("Please select an option (1 - 5): "))

def process_user_input(user_input):
    match user_input:
        case 1:
            Bernas().show_menu()
        case 2:
            Buenacifra().show_menu()
        case 3:
            Roldan().show_menu()
        case 4:
            Tero().show_menu()
        case 5:
            print("Exiting...")
            pass
        case _:
            input("\nInvalid input. Press Enter to try again.")
menu()
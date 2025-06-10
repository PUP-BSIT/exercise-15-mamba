import os

def show_border():
    print(
        "============================================================"
        "===================================="  
    )

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
  
def press_enter():
    input("\nPress Enter to return to menu.")

class Tero:
    def __init__ (self):
        self.name = "Altheno Mari L. Tero"
        self.course = "BSIT"
        self.year = "2"
        self.section = "1"

    def greet(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tGreetings!")
        show_border()
        print(
            f"\nHello! My name is {self.name}."
            f"\nI am from {self.course} {self.year} - {self.section}.\n"
        )
        show_border()
        press_enter()

    def show_takeaways(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tMy Takeaways")
        show_border()
        print(
            "\nI learned how to collaborate effectively with others.",
            "\nI learned the importance of being consistent with our tasks.\n"
        )
        show_border()
        press_enter()

    def show_collaborative_experience(self):
        clear_screen()
        show_border()
        print("\t\t\t\tCollaborative Experience")
        show_border()
        print(
            "\n Working with my group taught me",
            "how to communicate clearly,\n",
            "divide responsibilities fairly,",
            " and help each other troubleshoot code.\n",
            "By using GitHub it helped us track changes and",
            "avoid/solved conflicts in our codebase.\n"
        )
        show_border()
        press_enter()

    def show_skills(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tSkills")
        show_border()
        print(
            "\nThe Skills I've gained are: \n\n",
            "- Collaborating using GitHub and GitBash",
            " and managing repositories.\n",
            "- Python syntaxes and proper logic.\n",
            "- Proper Communication.\n"
        )
        show_border()
        press_enter()

    def show_about_integ(self):
        clear_screen()
        show_border()
        print("\t\t\t\tAbout Integrative Programming")
        show_border()
        print(
            "\n Course: INTE 202: Integrative Programming",
            "and Technologies 1\n",
            "Professor: Steven S. Villarosa\n",
            "Schedule: Saturday, 7:30 AM - 12:30 PM\n"
        )
        show_border()
        press_enter()

    def show_menu(self):
        user_input = 0
        while user_input != 6:
            user_input = self.display_get_user_input()
            self.process_user_input(user_input)

    def display_get_user_input(self):
        while True:
            clear_screen()
            show_border()
            print("\t\t\t\t\tTero Menu")
            show_border()
            print("\n1. Greetings")
            print("2. My Takeaways")
            print("3. Collaborative Experience")
            print("4. Skills")
            print("5. About Integrative Programming")
            print("6. Return to Main Menu\n")
            return int(input("Please select an option (1 - 6): "))

    def process_user_input(self, user_input):
        match user_input:
            case 1:
                self.greet()
            case 2:
                self.show_takeaways()
            case 3:
                self.show_collaborative_experience()
            case 4:
                self.show_skills()
            case 5:
                self.show_about_integ()
            case 6:
                pass
            case _:
                input("\nInvalid input. Press Enter to try again.")
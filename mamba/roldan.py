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

class Roldan:
    def __init__(self):
        self.name = "Gian Rafael B. Roldan"
        self.course = "BSIT"
        self.year = "2" 
        self.section = "1"

    def greet(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tGREETINGS")
        show_border()
        print(
            f"\nHi! My name is {self.name}.",
            f"\nI am from {self.course} {self.year} - {self.section}.\n"
        )
        show_border()
        press_enter()
    
    def show_takeaways(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tMY TAKEAWAYS")
        show_border()
        print(
            "\nThis course taught me how to use Python, Git, and GitHub.",
            "\nI learned that teamwork helps us grow faster.",
            "\nMistakes are normal and help me get better.",
            "\nThe best lesson is to keep learning and never give up.\n"
        )
        show_border()
        press_enter()

    def show_collaborative_experience(self):
        clear_screen()
        show_border()
        print("\t\t\t\tCOLLABORATIVE EXPERIENCE")
        show_border()
        print(
            "\nWorking with my classmates helped me learn new things.",
            "\nWe solved problems together and supported each other.",
            "\nSharing ideas made our projects better.",
            "\nollaboration taught me the value of teamwork and communication.\n"
        )
        show_border()
        press_enter()
    
    def show_skills(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tSKILLS")
        show_border()
        print(
            "\nI learned to use Git and GitHub for version control.",
            "\nI improved my Python programming skills.",
            "\nI learned to work better in a team.",
            "\nI became more confident in my coding abilities.\n"
        )
        show_border()
        press_enter()
    
    def show_about_integ(self):
        clear_screen()
        show_border()
        print("\t\t\t\tAbout Integrative Programming")
        show_border()
        print(
            "\nCourse: INTE 202: Integrative Programming and ",
            "Technologies 1",
            "\nProfessor: Steven Villarosa",
            "\nSchedule: Saturday | 7:30 - 12:30\n"
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
            print("\t\t\t\t\tROLDAN MENU")
            show_border()
            print("\n1. Greetings")
            print("2. My Takeaways") 
            print("3. Collaborative Experience")
            print("4. Skills")
            print("5. About INTE 202") 
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
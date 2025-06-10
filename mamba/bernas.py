import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def press_enter():
    input("\nPress Enter to proceed.")

def show_border():
    print(
        "============================================================"
        "===================================="
    )
    
class Bernas:
    def __init__(self):
        self.name = "Ernesto P. Bernas III"
        self.course = "BSIT"
        self.year = "2"
        self.section = "1"
    
    def greet(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tGREETINGS")
        show_border()
        print(
            f"\nHi Everyone! My name is {self.name}!",
            f"from {self.course} {self.year} - {self.section}\n",
        )
        show_border()
        press_enter()
    
    def show_takeaways(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tMY TAKEAWAYS")
        show_border()
        print(
            "\nThroughout this course, I have gained foundational "
            "knowledge, in using Python, Git, and Github," 
            "\nas well as valuable experience in collaborative"
            "development but the most important lesson I've"
            "\nlearned is 'Bilog ang Mundo' letting us know " 
            "that we are not ALWAYS at the "
            "TOP, people will"
            "\neventually LEARN MORE as they proceed in life.\n"
        )
        show_border()
        press_enter()
        
    def show_collaborative_experience(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tCOLLABORATIVE EXPERIENCE")
        show_border()
        print(
            "\n- Communication is the KEY"
            "\n- Think before you Click"
            "\n- Your Achievement is also your Team's Achievement"
            "\n- Find the BEST members that fits your LEADERSHIP"
            "\n- 50/50 in working with them again due to Time "
            "Management\n"
        )
        show_border()
        press_enter()
        
    def show_skills(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tSKILLS")
        show_border()
        print(
            "\n- Excellent Communication Skill"
            "\n- Excellent Collaboration Skill"
            "\n- Proficiency in Github/Gitbash"
            "\n- Basic Knowledge in Python"
            "\n- Good Time Management\n"
        )
        show_border()
        press_enter()
        
    def show_about_integ(self):
        clear_screen()
        show_border()
        print("\t\t\t\t\tABOUT INTE 202")
        show_border()
        print(
            "\nCourse: INTE 202: Integrative Programming and "
            "Technologies 1"
            ,"\nProfessor: Steven Villarosa"
            ,"\nSchedule: Saturday | 7:30 - 12:30\n"
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
            print("\t\t\t\t\tBernas Menu")
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
                input("\nWrong input. Press Enter to try again.")
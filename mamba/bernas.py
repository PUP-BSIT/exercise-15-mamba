import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def proceed():
    input("\nPress Enter to proceed.")

def border():
    print(
        "============================================================"
        "===================================="
    )
    
class Bernas:
    def __init__(self):
        self.name = "Ernesto P. Bernas III"
        self.course = "BS in Information Technology"
        self.year = "2"
        self.section = "1"
    
    def greet(self):
        clear_screen()
        border()
        print("\t\t\t\t\tGREETINGS")
        border()
        print(
            f"\nHi Everyone! My name is {self.name}!",
            f"from {self.course} {self.year} - {self.section}\n",
        )
        border()
    
    def show_takeaways(self):
        clear_screen()
        border()
        print("\t\t\t\t\tMY TAKEAWAYS")
        border()
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
        border()
        
    def show_collaborative_experience(self):
        clear_screen()
        border()
        print("\t\t\t\t\tCOLLABORATIVE EXPERIENCE")
        border()
        print(
            "\n- Communication is the KEY"
            "\n- Think before you Click"
            "\n- Find the BEST members that fits your LEADERSHIP\n"
        )
        border()
        
    def show_skills(self):
        clear_screen()
        border()
        print("\t\t\t\t\tSKILLS")
        border()
        print(
            "\n- Excellent Communication Skill"
            "\n- Good Collaboration Skill"
            "\n- Proficiency in Github/Gitbash"
            "\n- Good Time Management\n"
        )
        border()
        
    def show_about_integ(self):
        clear_screen()
        border()
        print("\t\t\t\t\tABOUT INTE 202")
        border()
        print(
            "\nCourse: INTE 202: Integrative Programming and "
            "Technologies 1"
            ,"\nProfessor: Steven Villarosa"
            ,"\nSchedule: Saturday | 7:30 - 12:30\n"
        )
        border()
        
    def menu(self):
        while True:
            clear_screen()
            border()
            print("\t\t\t\t\tBERNAS MENU")
            border()
            print("\n1. Greetings")
            print("2. My Takeaways")
            print("3. Collaborative Experience")
            print("4. Skills")
            print("5. About INTE 202")
            print("6. Return to Main Menu\n")
            user_input = input("Please select an option(1-6): ")
            
            match user_input:
                case "1":
                    self.greet()
                    proceed()
                    continue
                case "2":
                    self.show_takeaways()
                    proceed()
                    continue
                case "3":
                    self.show_collaborative_experience()
                    proceed()
                    continue
                case "4":
                    self.show_skills()
                    proceed()
                    continue
                case "5":
                    self.show_about_integ()
                    proceed()
                    continue
                case "6":
                    print("\nExiting...")
                    proceed()
                    break
                case _:
                    print("Invalid option, try again.")
                    
show = Bernas()
show.menu()
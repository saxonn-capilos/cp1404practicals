"""
CP1404 - Prac_07
Do-from-scratch Exercises - Project Management Program
Estimated time: 240 minutes
Actual time:
"""

import datetime
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "-(U)pdate project\n- (Q)uit")

def main():
    """Run project_management program."""
    print("Welcome to Pythonic Project Management")
    get_choice()


def retrieve_projects(in_file):
    """Return each line of projects.txt as a list of separated strings."""
    book_entries = [line.strip().split(',') for line in in_file]
    return book_entries



def get_choice():
    """Display menu and get choice from user."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("load_projects()")
        elif choice == "S":
            print("save_projects()")
        elif choice == "D":
            print("display_projects()")
        elif choice == "F":
            print("filter_projects()")
        elif choice == "A":
            print("add_new_project()")
        elif choice == "U":
            print("update_project()")
        else:
            print("Invalid menu choice.")
        choice = input(">>> ").upper()



if __name__ == "__main__":
    main()


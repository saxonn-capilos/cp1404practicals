"""
CP1404 - Prac_07
Do-from-scratch Exercises - Project Management Program
Estimated time: 240 minutes
Actual time: + 40 minutes
"""

import datetime
from project import Project


FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")


def main():
    """Run project_management program."""
    projects = retrieve_projects(FILENAME)
    total_projects = len(projects)

    display_opening_message(total_projects)
    get_choice()


def retrieve_projects(file):
    with open(file, 'r') as in_file:
        in_file.readline()
        projects = []
        for line in in_file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def display_opening_message(total_projects):
    """Display opening message"""
    print(f"Welcome to Pythonic Project Management\nLoaded {total_projects} from {FILENAME}")


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


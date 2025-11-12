"""
CP1404 - Prac_07
Do-from-scratch Exercises - Project Management Program
Estimated time: 240 minutes
Actual time:  + 72 minutes (DNF)
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
    get_choice(projects)


def retrieve_projects(file):
    """Return a list of project objects from reading the given file."""
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


def get_choice(projects):
    """Display menu and get choice from user."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("load_projects()")
        elif choice == "S":
            print("save_projects()")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("filter_projects()")
        elif choice == "A":
            print("add_new_project()")
        elif choice == "U":
            print("update_project()")
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()


def display_projects(projects):
    """Display incomplete and complete projects."""
    incomplete_projects = [project for project in projects if project.completion_percentage != '100']
    complete_projects = [project for project in projects if project.completion_percentage == '100']
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project}")


if __name__ == "__main__":
    main()


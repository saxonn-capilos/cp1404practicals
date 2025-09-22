"""
Write a complete Python program following the standard structure that uses a main and other functions.
"""


MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Displays the menu"""
    score = int(input("Enter a score between 0 and 100: "))
    print(MENU)
    get_choice(score)


def get_choice(score):
    """Get the choice from the user"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Your result is {result}")
        elif choice == "S":
            print("*" * score)
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Asks the user to enter a score between 0 and 100"""
    score = int(input("Enter a score between 0 and 100: "))
    while score < 0 or score > 100:
        result = "Invalid score"
        score = int(input("Enter score: "))
    return score


def determine_result(score):
    """Determines the result based on the score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
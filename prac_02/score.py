"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"Your result is {result}")
    random_score = random.randint(1, 100)
    print(f"Here's a random score between 0 and 100: {random_score}")
    print(f"It's result is {determine_score(random_score)}")


def determine_score(score):
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
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"Your result is {result}")


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
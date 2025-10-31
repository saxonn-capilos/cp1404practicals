"""
CP1404/CP5632 Practical
Intermediate Exercise
Estimated time: 35 minutes
Actual time: 57 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.typing == "Dynamic":
            print(language.name)


main()
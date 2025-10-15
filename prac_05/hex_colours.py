"""
CP1404/CP5632 Practical
Intermediate Exercises - hexadecimal colour code program
"""

CODE_TO_NAME = {"#FF0000": 'Red', '#0000FF': 'Blue', '#00FF00': 'Green', '#FFFF00': "Yellow", '#800080': "Purple",
                '#FFA500': "Orange", '#FFC0CB': "Pink", '#008080': "Teal", '#000080': "Navy", '#FF7F50': "Coral"}

for short_name, full_name in CODE_TO_NAME.items():
    print(f"{short_name} is {full_name}")

state_code = input("Enter hexadecimal code: ")
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid hexadecimal code")
    state_code = input("Enter hexadecimal code: ")
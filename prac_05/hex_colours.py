"""
CP1404/CP5632 Practical
Intermediate Exercises - hexadecimal colour code program
"""

COLOUR_TO_CODE = {"Red": "#FF0000", "Blue": "#0000FF", "Green": "#00FF00", "Yellow": "#FFFF00", "Purple": "#800080",
                "Orange": "#FFA500", "Pink": "#FFC0CB", "Teal": "#008080", "Navy": "#000080", "Coral": "#FF7F50"}

for name, hexadecimal_name in COLOUR_TO_CODE.items():
    print(f"{name} is {hexadecimal_name}")

colour_name = input("Enter colour: ")
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name.title()])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter colour: ")
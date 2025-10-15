"""
CP1404/CP5632 Practical
Intermediate Exercises - hexadecimal colour code program
"""

CODE_TO_NAME = {
'Red': '#FF0000',
'Blue': '#0000FF',
'Green': '#00FF00',
'Yellow': '#FFFF00',
'Purple': '#800080',
'Orange': '#FFA500',
'Pink': '#FFC0CB',
'Teal': '#008080',
'Navy': '#000080',
'Coral': '#FF7F50',
}

for colour_name, hexadecimal_name in CODE_TO_NAME.items():
    print(f"{colour_name} is {hexadecimal_name}")

colour_name = input("Enter colour: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", CODE_TO_NAME[colour_name])
    except KeyError:
        print("Invalid colour")
    state_code = input("Enter colour: ")
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
for short_name, full_name in CODE_TO_NAME.items():
    print(f"{short_name:3} is {full_name}")

state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
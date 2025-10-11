"""
CP1404 prac_04
Do-from-scratch Exercises: "Quick Pick" Lottery Ticket Generator
"""


import random

NUMBERS_PER_ROW = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
WIDTH = len(str(MAX_NUMBER))

number_quick_picks = int(input("How many quick picks? "))
for i in range(number_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_ROW:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()

    print(' '.join(f"{num:>{WIDTH}}" for num in quick_pick))
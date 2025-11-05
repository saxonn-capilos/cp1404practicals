"""
CP1404/CP5632 Prac_06
Do-From-Scratch Exercise
Estimated time: 60 minutes
Actual time: 52 minutes
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Construct a Guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        """Return Guitar in a string format."""
        return f"{self.name} ({self.year}) : ${str(self.cost)[:2]},{str(self.cost)}"


    def get_age(self):
        """Return how old the guitar is in years (e.g. in 2025 the L-5 is: 2025 - 1922 = 103)."""
        return 2025 - self.year


    def is_vintage(self):
        """Returns True if the Guitar is 50 or more years old, False otherwise."""
        return Guitar.get_age(self) >= 50
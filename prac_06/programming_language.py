"""
CP1404/CP5632 Practical
Intermediate Exercise
Estimated time: 35 minutes
Actual time: 57 minutes
"""

class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True, year=""):
        """Construct a ProgrammingLanguage from the entered values"""
        self.name = name
        self.typing = typing
        if self.is_dynamic():
            self.typing = "Dynamic"
        else:
            self.typing = "Static"
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
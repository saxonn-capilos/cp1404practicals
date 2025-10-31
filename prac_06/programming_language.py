"""
CP1404/CP5632 Practical
Intermediate Exercise
Estimated time: 35 minutes
Actual time: 57 minutes
"""

class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True, year=""):

        self.name = name
        self.typing = typing
        if self.is_dynamic():
            self.typing = "Dynamic"
        else:
            self.typing = "Static"
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        return self.typing == "Dynamic"


    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
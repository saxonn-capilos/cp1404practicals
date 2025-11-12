"""
CP1404 - Prac_07
Do-from-scratch Exercises - Project Management Program
Class Project file
"""


class Project:
    """Represent a project with [INSERT ATTRIBUTES] along with other required functions."""

    def __init__(self, name="", start_date="", priority=1, cost_estimate=0.0, completion_percentage=0.0):
        """Construct a project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")
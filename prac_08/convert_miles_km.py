"""
CP1404 - Prac 08
Do-from-scratch Exercise
Miles to Kilometres Converter
Estimated Time: 60 minutes
Actual Time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometresApp(App):
    """MilesToKilometresApp is a kivy app that converts a number of miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Enter distance in miles and press \"Convert miles to km\""
        return self.root

    def convert_miles_km(self, value):
        """Convert number of miles to kilometres."""
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, increment):
        """Increase the user input by the increment given."""
        try:
            current_value = float(self.root.ids.miles_input.text)
            self.root.ids.miles_input.text = str(current_value + increment)
        except ValueError:
            self.root.ids.miles_input.text = str(increment)


MilesToKilometresApp().run()
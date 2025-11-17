"""
CP1404 - Prac 08
Do-from-scratch Exercise
Miles to Kilometres Converter
Estimated Time: 60 minutes
Actual Time: 95 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class MilesToKilometresApp(App):
    """MilesToKilometresApp is a kivy app that converts a number of miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation from user input."""
        miles = self.convert_to_float(text)
        self.convert_miles_km(miles)

    def convert_miles_km(self, miles_input):
        """Convert number of miles to kilometres."""
        self.output_km = str(miles_input * CONVERSION_FACTOR)

    def handle_increment(self, text, increment):
        """Increase the user input by the increment given when up/down button is pressed."""
        miles = self.convert_to_float(text) + increment
        self.root.ids.input_miles.text = str(miles)


    @staticmethod
    def convert_to_float(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometresApp().run()
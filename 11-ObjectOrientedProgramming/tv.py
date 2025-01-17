# tv.py file
# Class definition
class TV:
    def __init__(self):
        self.is_on = False  # Initially, the TV is off

    def turn_on(self):
        self.is_on = True  # Turn the TV on

    def turn_off(self):
        self.is_on = False  # Turn the TV off

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")

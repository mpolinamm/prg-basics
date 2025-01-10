class Phone:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def make_call(self, contact):
        if self.battery_level > 0:
            print(f"Calling {contact} from {self.model}...")
            self.battery_level -= 5  
        else:
            print("Battery too low to make a call.")

    def send_message(self, contact, message):
        if self.battery_level > 0:
            print(f"Sending message to {contact}: {message}")
            self.battery_level -= 2  
        else:
            print("Battery too low to send a message.")

    def charge_battery(self, amount):
        if self.battery_level < 100:
            self.battery_level += amount
            if self.battery_level > 100:
                self.battery_level = 100
            print(f"Phone charged to {self.battery_level}% battery.")
        else:
            print("Battery is already full.")

    def display_info(self):
        print(f"Phone Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Level: {self.battery_level}%")

def main():
    my_phone = Phone("Apple", "iPhone 13", 69)

    my_phone.display_info()
    my_phone.make_call("Mommy")
    my_phone.send_message("Dad", "Hello, how are you?")
    my_phone.charge_battery(20)
    my_phone.display_info()

if __name__ == "__main__":
    main()

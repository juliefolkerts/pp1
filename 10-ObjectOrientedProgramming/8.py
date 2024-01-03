class Telephone:
    def __init__(self, phone_number, battery_level=100):
        self.phone_number = phone_number
        self.battery_level = battery_level
        self.in_call = False

    def dial(self, other_number):
        # Simulate the process of dialing and making a call
        print(f"Dialing {other_number}... Call connected.")
        self.in_call = True

    def send_text_message(self, other_number, message):
        # Simulate the process of sending a text message
        print(f"Sending a text message to {other_number}: {message}")

    def check_battery_level(self):
        # Check and display the remaining battery level
        print(f"Battery level: {self.battery_level}%")

# Example usage:
my_telephone = Telephone("555-1234")

# Make a call
my_telephone.dial("555-5678")

# Send a text message
my_telephone.send_text_message("555-9876", "Hello there!")

# Check battery level
my_telephone.check_battery_level()

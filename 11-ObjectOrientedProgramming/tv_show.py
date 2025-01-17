# tv_show.py file
# Main program
import tv  # Import the TV class from tv.py

def main():
    # Object creation
    my_tv = tv.TV()  # Create an instance of the TV class

    # Object usage
    print("Create TV set")
    my_tv.show_status()  # Show the current status (TV is off)

    print("Turn TV on")
    my_tv.turn_on()  # Turn the TV on
    my_tv.show_status()  # Show the current status (TV is on)

    print("Turn TV off")
    my_tv.turn_off()  # Turn the TV off
    my_tv.show_status()  # Show the current status (TV is off)

if __name__ == "__main__":
    main()  # Run the main function when this file is executed

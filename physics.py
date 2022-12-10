#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 9th, 2022
# This program asks for at least two variables, it then
# Uses those variables to calculate for either acceleration
# mass or Net Force.


# Function for calculating the variables.
def calc_forces(fnet, mass, acceleration):
    if fnet == "":
        fnet = mass * acceleration
        return fnet
    elif acceleration == "":
        acceleration = fnet / mass
        return acceleration
    elif mass == "":
        mass = fnet / acceleration
        return mass


def main():
    # Initializes the variables to nothing.
    user_mass = ""
    user_acceleration = ""
    user_fnet = ""
    # Asks the uses what variables they have.
    function_run = input(
        """Please enter a number

    1 if you have Acceleration&Mass\n
    2 if you have Fnet&Mass\n
    3 if you have Fnet&Acceleration\n
    : """
    )

    # Uses if else to see what uses has input.
    if function_run == "1":
        # Gets user input.
        user_acceleration = input("Please enter Acceleration(m/s^2): ")
        user_mass = input("Please enter Mass(kg): ")
        # Tries casting user input as a float.
        try:
            user_acceleration = float(user_acceleration)
            user_mass = float(user_mass)
        except ValueError:
            # Exception thrown if user put a string.
            print("Please enter a valid input")
            main()
        # Calls function and assigns user variables.
        fnet = calc_forces(user_fnet, user_mass, user_acceleration)
    elif function_run == "2":
        # Gets user input.
        user_fnet = input("Please enter your Net Force(N): ")
        user_mass = input("Please enter Mass(kg)")
        # Tries casting user input as a float.
        try:
            user_mass = float(user_mass)
            user_fnet = float(user_fnet)
        except ValueError:
            # Exception thrown if user put a string.
            print("Please enter a valid input: ")
            main()
        # Calls function and assigns user variables.
        acceleration = calc_forces(user_fnet, user_mass, user_acceleration)
    elif function_run == "3":
        # Gets user input.
        user_fnet = input("Please enter your Net Force(N): ")
        user_acceleration = input("Please enter Acceleration(m/s^2): ")
        # Tries casting user input as a float.
        try:
            user_acceleration = float(user_acceleration)
            user_fnet = float(user_fnet)
        except ValueError:
            # Exception thrown if user put a string.
            print("Please enter a valid input: ")
            main()
        # Calls function and assigns user variables.
        mass = calc_forces(user_fnet, user_mass, user_acceleration)
    # Exception if user did not enter a valid number.
    elif function_run != "1" or "2" or "3":
        print("Please enter a valid input")
        main()

    # Rounds and Displays the variable returning from function to the user.
    if function_run == "1":
        # Rounds to 2 Decimal placements.
        fnet_round = round(fnet, 2)
        acceleration_round = round(user_acceleration, 2)
        mass_round = round(user_mass, 2)
        # Displays variables.
        print(
            f"""
        Your Net Force is {fnet_round}N
        for an object Accelerating at {acceleration_round}m/s^2
        with a Mass of {mass_round}kg"""
        )
    elif function_run == "2":
        # Rounds to 2 Decimal placements.
        acceleration_round = round(acceleration, 2)
        fnet_round = round(user_fnet, 2)
        mass_round = round(user_mass, 2)
        # Displays variables.
        print(
            f"""
        Your Acceleration is {acceleration_round}m/s^2
        for an object with a Net Force of {fnet_round}N
        with a Mass of {mass_round}kg"""
        )
    elif function_run == "3":
        # Rounds to 2 Decimal placements.
        mass_round = round(mass, 2)
        fnet_round = round(user_fnet, 2)
        acceleration_round = round(user_acceleration, 2)
        # Displays variables.
        print(
            f"""
        Your Acceleration is {mass_round}m/s^2
        for an object with a Net Force of {fnet_round}N
        with a Acceleration of {acceleration_round}kg"""
        )

    # Gets user input for repeating the program and if its stop the program
    # stops otherwise it uses a while loop to repeat the program.
    user_repeat = input(
        """Would you like to stop the program (stop)
        to stop or any key to continue: """
    )
    repeat = user_repeat.upper()
    if repeat == "STOP":
        print("Stopping program")

    while repeat != "STOP":
        main()


if __name__ == "__main__":
    main()

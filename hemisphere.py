#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 9th, 2022
# This program asks the user for a radius and calculate volume surface
# area and 2D area of a hemisphere.


# Imports modules
import math
import colorama


# Function for calculating volume.
def calc_volume(radius):
    volume = (2 / 3) * (math.pi) * (radius * radius * radius)
    return volume


# Function for calculating surface area.
def calc_surfaceArea(radius):
    surface_area = 3 * (math.pi) * (radius * radius)
    return surface_area


# Function for calculate 2D area of shape.
def calc_area(radius):
    area = (math.pi * (radius**2)) / 2
    return area


def main():
    # Imports variable from colour module.
    from colorama import Fore

    # initializes variables.
    user_repeat = ""
    radius_user = input(
        Fore.GREEN
        + """Please enter the radius of
    the HemiSphere(cm): """
    )

    # Tries converting radius from user to a float.
    try:
        radius_user = float(radius_user)
    except ValueError:
        # Exception thrown if user enters a string.
        print(Fore.RED + "Please enter a valid number")
        main()

    # Calls all three functions to calculate surface area, area and volume.
    calc_surfaceArea(radius_user)
    surface_area = calc_surfaceArea(radius_user)
    calc_volume(radius_user)
    volume = calc_volume(radius_user)
    calc_area(radius_user)
    area = calc_area(radius_user)

    # Asks the user what type of function they would like to use.
    type_function = input(
        Fore.YELLOW
        + """Enter the type of function to run\n
        1 Surface Area\n
        2 Volume\n
        3 for 2D area\n
        4 for all\n
        Press Q to restart\n"""
    )

    # Checks the function(s) that the user has input and prints
    # the variables returning from that function.
    if type_function == "1":
        print(
            Fore.MAGENTA
            + """Your surface area is
        = {:,.2f} cm^2""".format(
                surface_area
            )
        )
    elif type_function == "2":
        print(Fore.BLUE + "Your volume is = {:,.2f} cm^3".format(volume))
    elif type_function == "3":
        print(Fore.WHITE + "Your area is = {:,.2f} cm^3".format(area))
    elif type_function == "4":
        print(
            Fore.MAGENTA
            + """Your surface area is
        = {:,.2f} cm^2""".format(
                surface_area
            )
        )
        print(
            Fore.BLUE
            + """Your volume is
        = {:,.2f} cm^3""".format(
                volume
            )
        )
        print(Fore.WHITE + "Your area is = {:,.2f} cm".format(area))
    elif type_function == "Q":
        main()
    else:
        print(Fore.RED + "Please enter a valid Number")
        main()

    # Gets user input for repeating the program and if its stop the program
    # stops otherwise it uses a while loop to repeat the program.
    user_repeat = input(
        Fore.BLACK
        + """Would you like to stop the program (stop)
        to stop or any key to continue: """
    )
    repeat = user_repeat.upper()
    if repeat == "STOP":
        print(Fore.RED + "Stopping program")

    while repeat != "STOP":
        main()


if __name__ == "__main__":
    main()

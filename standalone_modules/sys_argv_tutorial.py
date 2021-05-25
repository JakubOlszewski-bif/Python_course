# sys.argv

""" List of arguments passed to a Python script, first argument being the name of the script. """

import sys

# If passed argument is a number - print its square; otherwise just print it
for argument in sys.argv:
    try:
        argument = int(argument) # Arguments inside sys.argv are always strings
        print(f"{argument}^2 = {argument**2}")
    except ValueError:
        print(argument)

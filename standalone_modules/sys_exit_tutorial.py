# sys.exit

import sys

out_list = []

# Print square of a given number. Exit the program if a non-integer argument was passed
try:
    for argument in sys.argv[1:]:
        out_list.append(int(argument))
except ValueError:
    sys.exit("Please only include integers.")
else:
    for argument in out_list:
        print(f"{argument}^2 = {argument**2}")
finally:
    print("Finished")
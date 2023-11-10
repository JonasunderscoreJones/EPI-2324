'''EPR Übungsblatt 03'''
__author__ = "7987847, Werner"

import epr_functions

print("Welcome to the EPR Functions Console.")
print("Type 'help' for a list of commands.")
print("Type 'exit' to exit the console.")

# Main loop of the console
while True:
    command = input("> ")
    try:

        if command == "help":
            print("Commands:")
            print("help - Shows this help")
            print("exit - Exits the console")
            print("decimal_to_octal - Converts a decimal number to an octal number")
            print("decimal_to_basis - Converts a decimal number to a number with a given base")
            print("chaos_turtle - Draws a random pattern with a turtle")
        elif command == "exit":
            break
        elif command == "decimal_to_octal":
            print("Der Rechner rechnet Dezimalzahlen in Oktalzahlen um.")
            print("Geben Sie eine positive Dezimalzahl ein.")
            print(epr_functions.decimal_to_octal(int(input("Dezimalzahl: "))))
        elif command == "decimal_to_basis":
            print("Der Rechner rechnet Dezimalzahlen in Zahlen mit einer beliebigen Basis um.")
            print("Geben Sie eine positive Dezimalzahl und eine positive Basis ein.")
            print(epr_functions.decimal_to_basis(int(input("Dezimalzahl: ")), int(input("Basis: "))))
        else:
            print("Unknown command. Type 'help' for a list of commands.")
    # Catch ValueError exceptions, when the user enters invalid input
    except epr_functions.InvalidInputError:
        print("Invalid input. Please try again.")

'''EPR Übungsblatt 03, Python Modul'''
__author__ = "7987847, Werner"

import turtle
import random

class InvalidInputError(Exception):
    '''Exception for invalid input'''
    pass

def decimal_to_octal(decimal:int) -> str:
    '''Converts a decimal number to an octal number
    decimal: decimal number
    '''
    if decimal == 0:
        return "0"
    if decimal < 0:
        raise InvalidInputError("Negative numbers are not allowed")
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
        print("Octal Conversion:",decimal*8,
              "/ 8 =", decimal,
              " Rest:", decimal % 8,
              "Octal: ", octal)
    return octal

# Alternativ:
# def decimal_to_octal(decimal:int) -> str:
#     '''Converts a decimal number to an octal number
#     decimal: decimal number
#     '''
#     return decimal_to_basis(decimal, 8)

# Testfälle

# decimal_to_octal(0)
# Ausgabe: 0

# decimal_to_octal(39)
# Ausgabe: 47

# decimal_to_octal(-10)
# Ausgabe: Exception

def decimal_to_basis(decimal:int, basis:int) -> str:
    '''Converts a decimal number to a number with a given base
    decimal: decimal number
    basis: base
    '''
    if decimal == 0:
        return "0"
    if decimal < 0 or basis < 0:
        raise InvalidInputError("Negative numbers are not allowed")
    converted = ""
    while decimal != 0:
        converted = str(decimal % basis) + converted
        decimal //= basis
        print("Basis Conversion:", decimal*basis, "/",
              basis, "=", decimal,
              "Rest:", decimal % basis,
              "Converted:", converted)
    return converted

# Testfälle

# decimal_to_basis(0, 2)
# Ausgabe: 0

# decimal_to_basis(39, 2)
# Ausgabe: 100111

# decimal_to_basis(-10, 2)
# Ausgabe: Exception

def chaos_turtle(iterationen, startpunkt=(0, 0)):
    '''Draws a random triangle-like pattern with turtle
    iterationen: number of iterations
    startpunkt: start point of the turtle
    '''
    turtle.penup()
    turtle.goto(startpunkt)
    turtle.speed(0)

    punkte = [(100, -50), (-100, -50), (0, 100)]  # Eckpunkte des Dreiecks
    for _ in range(iterationen):
        zufallspunkt = random.choice(punkte)
        ziel_x = (zufallspunkt[0] + turtle.xcor()) / 2
        ziel_y = (zufallspunkt[1] + turtle.ycor()) / 2
        turtle.goto(ziel_x, ziel_y)
        turtle.dot(5)  # Punkt zeichnen

# Testfälle

# zeichne_dreieck(1000, (0, 0))
# Ausgabe: Dreieck mit 1000 Punkten

# zeichne_dreieck(1000, (100, 100))
# Ausgabe: Dreieck mit 1000 Punkten, verschoben um (100, 100)

# zeichne_dreieck(1000, (-100, -100))
# Ausgabe: Dreieck mit 1000 Punkten, verschoben um (-100, -100)

if __name__ == "__main__":
    print("Der Rechner rechnet Dezimalzahlen in Oktalzahlen um.")
    print("Geben Sie eine Dezimalzahl ein.")
    print(decimal_to_octal(int(input("Dezimalzahl: "))))

    print("Der Rechner rechnet Dezimalzahlen in Zahlen mit einer beliebigen Basis um.")
    print("Geben Sie eine Dezimalzahl und eine Basis ein.")
    print(decimal_to_basis(int(input("Decimal: ")), int(input("Basis: "))))

    print("Der Rechner zeichnet ein Chaos-Turtle.")
    print("In einem Dreieck-pattern werden Punkte gezeichnet.")
    print("Geben Sie die Anzahl der Iterationen ein.")
    chaos_turtle(int(input("Interationen: ")),
                (int(input("Startpunkt X Kooridnate: ")), int(input("Startpunkt Y Kooridnate: "))))
    input("Press Enter to close window...")

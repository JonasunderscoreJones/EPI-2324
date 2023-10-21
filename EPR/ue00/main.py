'''EPR Übungsblatt 00'''
__author__ = "7987847, Werner"


# Berechnung des harmonisches Mittel
def harmonischesMittel(a: float, b: float) -> float:
    '''
    Berechnet das harmonische Mittel zweier Zahlen
    :param a: erste Zahl
    :param b: zweite Zahl
    :return: harmonisches Mittel
    '''
    return (2*a*b)/(a+b)

# Berechnung des arithmetisches Mittel
def arithmetischesMittel(a: float, b: float) -> float:
    '''
    Berechnet das arithmetische Mittel zweier Zahlen
    :param a: erste Zahl
    :param b: zweite Zahl
    :return: arithmetisches Mittel
    '''
    return (a+b)/2


# Nutzereingaben
print("Rechner zur Berechnung des harmonischen Mittels")
print("Das harmonische Mittel der beiden Zahlen ist", harmonischesMittel(
    float(input("Bitte geben Sie die erste Zahl ein: ")),
    float(input("Bitte geben Sie die zweite Zahl ein: "))))

print("Rechner zur Berechnung des arithmetischen Mittels")
print("Das arithmetische Mittel der angegebenen Zahlen ist", arithmetischesMittel(
    float(input("Bitte geben Sie die erste Zahl ein: ")),
    float(input("Bitte geben Sie die zweite Zahl ein: "))))

# Testfälle

# Einfacher Aufruf mit 0
# arithmetischesMittel(0, 2)
# Ausgabe: 0.0

# Aufruf mit Dezimalzahlen und negativen Zahlen
# harmonischesMittel(-3.6, 3.14)
# Ausgabe: 49.14782608695653

# Aufruf mit a und b die 0 als Summe ergeben
# harmonischesMittel(3, -3)
# Das Ergebnis ist nicht definiert da durch 0 geteilt wird
# Es kommt zu einem Fehler
# Ausgabe: ZeroDivisionError: float division by zero

# Einfacher Aufruf mit 0
# arithmetischesMittel(0, 2)
# Ausgabe: 1.0

# Aufruf mit Dezimalzahlen und negativen Zahlen
# arithmetischesMitel(-3.6, 3.14)
# Ausgabe: -0.22999999999999998

# Aufruf mit falschen Datentypen
# arithmetischesMittel("a", True)
# Es kommt zu einem Fehler da die Datentypen nicht kompatibel sind
# Nur float und int sind erlaubt
# Ausgabe: ValueError: could not convert string to float: 'a'

'''EPR Übungsblatt 02'''
__author__ = "7987847, Werner"

# Aufgabe 2
# a)
def sum_range(m:int, n:int) -> int:
    '''Summe aller Zahlen von m bis n
    m: Startwert
    n: Endwert
    '''
    return sum(range(m, n+1))

print("Es wird die Summe aller Zahlen von m bis n berechnet.")
print("Geben Sie m und n ein.")
print(sum_range(int(input("m: ")), int(input("n: "))))

# Testfälle

# sum_range(0, 0)
# Ausgabe: 0

# sum_range(0, 1)
# Ausgabe: 1

# sum_range(-2, 234534634737)


# b)
def halbiere_bis_null(n:int) -> int:
    '''Anzahl der Schritte, bis n <= 1
    n: Zahl, die halbiert werden soll
    '''
    if n == 0:
        return 0
    schritte = 0
    while abs(n) >= 1:
        n /= 2
        schritte += 1
    return schritte

print("Es wird die Anzahl der Schritte berechnet, bis n <= 1 ist.")
print("Geben Sie n ein.")
print(halbiere_bis_null(int(input("n: "))))

# Testfälle

# halbiere_bis_null(0)
# Ausgabe: 0

# halbiere_bis_null(1)
# Ausgabe: 1

# halbiere_bis_null(2)
# Ausgabe: 2


# c)

def erzeuge_schachfeld(n:int, m:int):
    '''Erzeugt ein Schachfeld mit n Zeilen und m Spalten
    n: Anzahl der Zeilen
    m: Anzahl der Spalten
    '''
    for i in range(n):
        for j in range(m):
            # Wenn sowohl die Zeile als auch die Spalte gerade oder ungerade
            # ist, ist es Schwarz (1),
            # ansonsten ist es Weiß (0).
            if (i + j) % 2 == 0:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()

print("Es wird ein Schachfeld erzeugt.")
print("Geben Sie die Anzahl der Zeilen (n) und Spalten (m) ein.")
erzeuge_schachfeld(int(input("n: ")), int(input("m: ")))

# Testfälle

# erzeuge_schachfeld(0, 0)
# Ausgabe:

# erzeuge_schachfeld(1, 1)
# Ausgabe: 0

# erzeuge_schachfeld(7, 7)
# Ausgabe:
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0


# d

def catalansche_konstante_approximation(anzahl_terme:int) -> float:
    '''Approximation der catalanschen Konstante
    anzahl_terme: Anzahl der Terme, die zur Approximation verwendet werden sollen
    '''
    catalan_summe = 0.0
    for n in range(anzahl_terme):
        term = 1 / ((2 * n + 1) ** 2)
        catalan_summe += term
    return catalan_summe

print("Es wird die catalansche Konstante approximiert.")
print("Geben Sie die Anzahl der Terme ein, um die Konstante zu approximieren.")
print(catalansche_konstante_approximation(int(input("Anzahl Terme: "))))

# Testfälle

# catalansche_konstante_approximation(0)
# Ausgabe: 0.0

# catalansche_konstante_approximation(1)
# Ausgabe: 1.0

# catalansche_konstante_approximation(1000)
# Ausgabe: 1.2334505501570059


# e

def differenz_zwischen_approximationen(start:int, ende:int, schrittweite:int) -> float:
    '''Gibt die Differenz zwischen zwei Approximationen der catalanschen Konstante aus
    start: Startwert
    ende: Endwert
    schrittweite: Schrittweite
    '''
    for n in range(start, ende, schrittweite):
        erster_wert = catalansche_konstante_approximation(n)
        zweiter_wert = catalansche_konstante_approximation(n + schrittweite)
        differenz = zweiter_wert - erster_wert
        print(f"n = {n} : {erster_wert} ; n = {n + schrittweite} : {zweiter_wert}")
        print(f"Differenz: {differenz}\n")

print("Es wird die Differenz zwischen zwei Approximationen der catalanschen Konstante ausgegeben.")
print("Geben Sie den Startwert, Endwert und die Schrittweite ein.")
differenz_zwischen_approximationen(int(input("Startwert: ")),
                                   int(input("Endwert: ")),
                                   int(input("Schrittweite: ")))

# Testfälle

# differenz_zwischen_approximationen(0, 1000, 100)
# Ausgabe:
    # n = 0 : 0.0 ; n = 100 : 1.231200570968774
    # Differenz: 1.231200570968774

    # n = 100 : 1.231200570968774 ; n = 200 : 1.2324505527403138
    # Differenz: 0.0012499817715396766

    # n = 200 : 1.2324505527403138 ; n = 300 : 1.2328672175744397
    # Differenz: 0.000416664834125946

    # n = 300 : 1.2328672175744397 ; n = 400 : 1.2330755504616913
    # Differenz: 0.00020833288725152777

    # n = 400 : 1.2330755504616913 ; n = 500 : 1.2332005503028372
    # Differenz: 0.0001249998411458897

    # n = 500 : 1.2332005503028372 ; n = 600 : 1.2332838835659545
    # Differenz: 8.333326311737999e-05

    # n = 600 : 1.2332838835659545 ; n = 700 : 1.233343407339766
    # Differenz: 5.952377381146512e-05

    # n = 700 : 1.233343407339766 ; n = 800 : 1.2333880501768604
    # Differenz: 4.464283709437744e-05

    # n = 800 : 1.2333880501768604 ; n = 900 : 1.2334227723869715
    # Differenz: 3.472221011113774e-05

    # n = 900 : 1.2334227723869715 ; n = 1000 : 1.2334505501570059
    # Differenz: 2.7777770034376204e-05

# differenz_zwischen_approximationen(-3, 5, 1)
# Ausgabe:
    # n = -3 : 0.0 ; n = -2 : 0.0
    # Differenz: 0.0

    # n = -2 : 0.0 ; n = -1 : 0.0
    # Differenz: 0.0

    # n = -1 : 0.0 ; n = 0 : 0.0
    # Differenz: 0.0

    # n = 0 : 0.0 ; n = 1 : 1.0
    # Differenz: 1.0

    # n = 1 : 1.0 ; n = 2 : 1.1111111111111112
    # Differenz: 0.11111111111111116

    # n = 2 : 1.1111111111111112 ; n = 3 : 1.1511111111111112
    # Differenz: 0.040000000000000036

    # n = 3 : 1.1511111111111112 ; n = 4 : 1.1715192743764173
    # Differenz: 0.020408163265306145

    # n = 4 : 1.1715192743764173 ; n = 5 : 1.183864953388763
    # Differenz: 0.012345679012345734

# differenz_zwischen_approximationen(0, 0, 1)
# Ausgabe:

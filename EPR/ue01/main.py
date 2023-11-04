'''EPR Übungsblatt 01'''
__author__ = "7987847, Werner"

# Aufgabe 2
def bonuspunkte_rechner(bp_epr: int, bp_gpr: int, zbnp: int) -> int:
    '''
    Berechnet die Anzahl der Bonuspunkte
    :param bonuspunkte_epr: Bonuspunkte EPR
    :param bonuspunkte_gpr: Bonuspunkte GPR
    :param zbnp: Zum bestehen benötigte Punkte
    :return: Anzahl der Bonuspunkte
    '''
    # Überprüfung, ob die Werte im erlaubten Bereich liegen
    if bp_epr not in range(0, 111) or bp_gpr not in range(0, 111) or zbnp < 0:
        raise ValueError("Die Werte sind nicht im erlaubten Bereich.")
    return int(min(zbnp/4, (bp_epr+bp_gpr)/14))

print("Rechner zur Berechnung der Bonuspunkte für EPR und GPR")

epr_bp = int(input('Bitte geben Sie die Bonuspunkte EPR ein: '))
epr_bp = int(input('Bitte geben Sie die Bonuspunkte GPR ein: '))
zbnp_ = int(input('Bitte geben Sie die zum Bestehen benötigten Punkte ein: '))

bonuspunkte = bonuspunkte_rechner(epr_bp, epr_bp, zbnp_)
ergebnis_text = f"Die Anzahl der Bonuspunkte für die Klausur: {bonuspunkte}"
print(ergebnis_text)

# Testfälle

# Einfacher Aufruf mit 0
# bonuspunkte_rechner(0, 0, 0)
# Ausgabe: 0

# Aufruf mit Dezimalzahlen und negativen Zahlen
# bonuspunkte_rechner(-3.6, 3.14, 0)
# Ausgabe: ValueError: Die Werte sind nicht im erlaubten Bereich.

# Aufruf mit realen Werten
# bonuspunkte_rechner(89, 102, 50)
# Ausgabe: 12



# Aufgabe 3
def aufgabe_3(zahl_1:int, zahl_2:int) -> None:
    '''
    Prüft ob die kleinere Zahl durch 2, 4 oder 8 teilbar ist
    '''
    kleinere_zahl = min(zahl_1, zahl_2)

    ist_teilbar = False

    # Überprüfung, ob die kleinere Zahl durch 2, 4 oder 8 teilbar ist
    if kleinere_zahl % 8 == 0:
        print(f"{kleinere_zahl} ist durch 8 teilbar.")
        ist_teilbar = True
    if kleinere_zahl % 4 == 0:
        print(f"{kleinere_zahl} ist durch 4 teilbar.")
        ist_teilbar = True
    if kleinere_zahl % 2 == 0:
        print(f"{kleinere_zahl} ist durch 2 teilbar.")
        ist_teilbar = True
    if not ist_teilbar:
        print(f"{kleinere_zahl} ist weder durch 2, 4 noch 8 teilbar.")

print("Rechner zur Prüfung ob die kleinere Zahl durch 2, 4 oder 8 teilbar ist")
aufgabe_3(int(input("Bitte geben Sie die erste Zahl ein: ")),
            int(input("Bitte geben Sie die zweite Zahl ein: ")))

# Testfälle

# Einfacher Aufruf mit 0
# aufgabe_3(0, 0)
# Ausgabe: 0 ist durch 8 teilbar.
#          0 ist durch 4 teilbar.
#          0 ist durch 2 teilbar.

# Aufruf mit Dezimalzahlen und negativen Zahlen
# aufgabe_3(-3.6, 3.14)
# Ausgabe: ValueError: Es muss ein Integer übergeben werden.

# Aufruf mit natürlichen Werten
# aufgabe_3(89, 102)
# Ausgabe: 89 weder durch 2, 4 noch 8 teilbar.

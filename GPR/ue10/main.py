'''GPR Übung 10 - Reguläre Ausdrücke'''
__author__ = "7987847, Werner"

import re

def cleopatra_change_gender():
    '''
    Lies den Text aus der Datei "Kleopatra.txt" ein und ersetze alle Vorkommen von "sie" durch "er".
    Gib den modifizierten Text auf der Konsole aus.
    '''
    # Dateipfad zum Text
    dateipfad = "Kleopatra.txt"

    try:
        # Text aus der Datei lesen
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            text = datei.read()

        # Verwende die sub()-Funktion, um "sie" durch "er" zu ersetzen
        modifizierter_text = re.sub(r'\bsie\b', 'er', text, flags=re.IGNORECASE)
        modifizierter_text = re.sub(r'\bIhre\b', 'Seine', modifizierter_text, flags=re.IGNORECASE)

        # Gib den modifizierten Text auf der Konsole aus
        print(modifizierter_text)

    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")

def find_patterns_in_text():
    '''
    Lies den Text aus der Datei "Wortgitter_mitZahlen.txt" ein und finde folgende Muster:
    i) Findet das erste Vorkommen von Zeichenfolgen, die mit einer Null starten,
    gefolgt von einer Zahl und einem Buchstaben
    ii) Findet alle Vorkommen von Zeichenfolgen mit 2 oder 3 Zahlen hintereinander

    Gib die gefundenen Muster auf der Konsole aus.
    '''
    # Dateipfad zum Text
    dateipfad = "Wortgitter_mitZahlen.txt"

    try:
        # Text aus der Datei lesen
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            text = datei.read()

        # i) Findet das erste Vorkommen von Zeichenfolgen, die mit einer Null starten,
        # gefolgt von einer Zahl und einem Buchstaben
        pattern_i = re.findall(r'0[0-9][A-Za-z]', text)
        print("i. Erstes gefundenes Muster:")
        print(pattern_i[0] if len(pattern_i) > 0 else "Kein Muster gefunden.")

        # ii) Alle vorkommen aus i)
        print("\nii. Alle gefundenen Muster:")
        print(pattern_i)

        # iii) Findet alle Vorkommen von Zeichenfolgen mit 2 oder 3 Zahlen hintereinander
        pattern_iii = re.findall(r'\d{2,3}', text)
        print("\niii. Gefundene Muster:")
        print(pattern_iii)

    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")

if __name__ == "__main__":
    cleopatra_change_gender()
    find_patterns_in_text()

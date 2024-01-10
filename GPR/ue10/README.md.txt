__author__ = "7987847, Werner"

# Aufgabe 2 a) iii)

Mit Zeichenketten wie '52515' wird wie folgt umgegangen:

- Es werden die strings '52', '525', '25', '251', '51', '515' und '15' erkannt.
- Dies liegt daran, dass es keine Rolle spielt, ob vor oder nach der mehr-als-2-oder-3-stelligen Zahlenkette ein nicht numerisches Zeichen kommt. Somit enthält die Zeichenkette mehrere kürzere Zeichenketten

# Aufgabe 2 b)

Der reguläre Ausdruck stellt eine typische Email Adresse dar:

- ´^[A-Za-z0-9._%+-]+´: Beginnt mit mindestens einem alphanumerischen Zeichen oder den erlaubten Sonderzeichen (. _ % + -)
- `@`: Enthält das "@"-Symbol
- `[A-Za-z0-9.-]+`: Enthält mindestens ein alphanumerisches Zeichen oder einen Punkt zwischen "@" und der Domain
- `\.`: Enthält einen Punkt vor der Top-Level-Domain
- `[A-Z|a-z]{2,}$`: Endet mit mindestens zwei alphanumerischen Zeichen (Top-Level-Domain)

# Dokumentation *main.py*

Zur Nutzung muss eine kompatible Python version installiert sein.
Akzeptiert werden alle Python 3.x Versionen.

Das Programm kann mit dem Befehl `python3 main.py` im Ordner gestartet werden.

Nach dem Start wird die Datei `Kleopatra.txt` eingelesen und Kleopatra's weibliche Pronomen durch mänliche ausgetauscht.
Das Ergebnis wird ind er Konsole Ausgegeben.

Anschließend wird die Datei `Wortgitter_mitZahlen.txt` eingelesen und folgendes in der Konsole Ausgegeben:

i) Das Erste Vorkommen einer 0 gevolgt von einer Zahl und anschließend eines Buchstabens
ii) Alle Vorkommen aus i)
iii) Alle Zeichenfolgen aus 2 oder 3 Ziffern

author: 7987847, Werner

Aufgabe 1
---

a.

Ausgabe:

0
3
6
9
42



b.

Ausgabe:

0.1  :  1
0.2  :  1.2
0.30000000000000004  :  1.4
0.4  :  1.5999999999999999



c.

Ausgabe:

0.1  :  1
0.2  :  1.2
0.30000000000000004  :  1.4
0.4  :  1.5999999999999999
0.5  :  1.5999999999999999
0.6  :  1.5999999999999999
0.7  :  1.5999999999999999
0.7999999999999999  :  1.5999999999999999
0.8999999999999999  :  1.5999999999999999
0.9999999999999999  :  1.5999999999999999
1.0999999999999999  :  1.5999999999999999
1.2  :  1.5999999999999999
1.3  :  1.5999999999999999
1.4000000000000001  :  1.5999999999999999
1.5000000000000002  :  1.5999999999999999
1.6000000000000003  :  1.5999999999999999
B



d.

Ausgabe:

n

Die Funktion f1 wird ein mal aufgerufen und gibt None zurück, da weder die Bedingung der ersten, noch der zweiten if-Anweisung erfüllt ist. Daher gibt es kein vordefinierten return-Wert und es wird automatisch None zurückgegeben.



e.

Ausgabe:

17

Die Funktion f2 gibt den Wert von m zurück, wenn wenn n kleiner m nicht erfüllt ist. Im Code-Fragment ist n kleiner m jedoch erfüllt, da 17 < 19. Dadurch wird f2 rekursiv aufgerufen mit vertauschten Eingabewerten. Nun ist n = 19 und m = 17. Da 19 > 17 ist, wird 19 zurückgegeben und die Rekursion beendet. f2 wird insgesamt 2 mal aufgerufen.



f.

Ausgabe:

10

Die Funktion f3 wird insgesamt 1 mal aufgerufen und der Wert von a wird mit n addiert. 'a' ist bei der Definition von f3 noch nicht definiert, aber bei der Ausführung von f3 wird a initialisiert. Da n = 0 ist, wird 10 zurückgegeben.


Aufgabe 2
---

Zur Nutzung muss eine kompatible Python version installiert sein.
Akzeptiert werden alle Python 3.x Versionen.

Das Programm kann mit dem Befehl `python3 main.py` im Ordner gestartet werden.

Nach dem Aufrufen des Programms wird zunächst die Summe der Zahlen zwischen n und m berechnet. Hierzu wird der Nutzer aufgefordert die beiden Zahlen einzugeben.
Das Ergebnis wird daraufhin ausgegeben.

Als nächstes wird der Nutzer aufgefordert eine Zahl einzugeben, die so lange halbiert wird, bis sie kleiner als 1 ist. Die Anzahl der Halbierungen wird ausgegeben.

Daraufhin wird der Nutzer aufgefordert 2 Zahlen n und m einzugeben welche die Zeile und Spalten eines daraufhin ausgegebenen Schachbretts darstellen.

Folgenden wird der Nutzer aufgefordert eine Zahl anzugeben welche die Approximationsstufe der Catalanschen Konstante darstellt. Die Zahl inidziert die Anzahl der Terme der Berechnung und dadurch auch die Genauigkeit der Approximation.

Als letztes wird der Nutzer aufgefordert 3 Zahlen einzugeben. Hier wird Differenz zwischen verschiedenen Approximationen der Catalanschen Konstante berechnet. Die erste Zahl gibt die Anzahl der Terme der ersten Approximation an, die zweite Zahl die Anzahl der Terme der letzten Approximation und die dritte Zahl die Schrittweite zwischen den Approximationen. Es wird die Differenz zwischen jedem Schritt ausgegeben.

Hinweis: Es kommt in allen Eingaben zu einem Fehler, wenn kein Integer eingegeben wird. Es wird dann eine Fehlermeldung ausgegeben und das Programm beendet sich.

Nach der Ausgabe des letzten Ergebnisses wird das Programm beendet.

Testfälle
---
Im Programmcode sind zu jeder der beiden Mittel jeweils 3 Testfälle angegeben.

PEP8
---
Der Programmcode ist soweit wie möglich nach PEP8 abgestimmt.
Von der Aufgabe vorgegebene Funktions- und Variablennamen wurden beibehalten.
Diese sind nicht PEP8 konform (snake_case naming).
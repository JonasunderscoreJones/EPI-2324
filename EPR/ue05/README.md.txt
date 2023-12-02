author: 7987847, Werner


Zur Nutzung muss eine kompatible Python version installiert sein.
Akzeptiert werden alle Python 3.x Versionen.

Das Programm kann mit dem Befehl `python3 main.py` im Ordner gestartet werden.

Das Programm ist ein Kartenspiel für 3-4 Spieler. Es werden 12 Karten (1-4 in Kreuz, herz, Karo) verwendet

## Regeln wie auf dem Übungsblatt beschrieben:

Gespielt wird mit 3 – 4 Spielern.
Vorbereitung
Es gibt drei verschiedene Farben (Karo, Herz, und Kreuz). Die jeweils höchste Karte einer Farbe ist die 4, die
niedrigste eine 1. Zu Beginn des Spiels werden alle Karten vollständig an die Spieler verteilt.
Ziel des Spiels und Spielablauf
Spieler probieren Stiche zu vermeiden in denen Karten der Farbe ‚Kreuz‘ auftauchen. Jede Karte mit einem
Kreuz gibt einen Strafpunkt. Am Ende des Spiels, d.h. nachdem alle Karten gespielt wurden, werden die
EPR WiSe 2023/2024 2
Strafpunkte notiert. Der Spieler mit den wenigsten Strafpunkten gewinnt. Es können auch mehrere Spieler
gewinnen.
Stiche
Jeder Spieler spielt reihum genau eine Karte aus der Hand aus. Diese Karten bilden den Stich. In einem Spiel
werden so viele Stiche gespielt, wie Spieler Handkarten besitzen. Der beginnende Spieler kann jede Karte aus
der Hand abspielen. Die Farbe der ersten ausgespielten Karte in einem Stich ist Trumpf und muss ‚bedient‘
werden. Das heißt, hat ein Spieler die Farbe der erstgelegten Karte auf der Hand, muss er diese spielen. Kann
ein Spieler die Trumpffarbe nicht spielen, darf dieser Spieler eine andere Farbe spielen. Am Anfang jedes Stichs
wird die Trumpffarbe neu bestimmt. Die Karte mit dem höchsten Wert der Trumpffarbe gewinnt und der
Spieler, der diese Karte ausgespielt hat, bekommt alle Karten des Stichs. Karten, die eine andere Farbe als die
Trumpffarbe haben, können einen Stich nie gewinnen. Nach jedem Stich werden die Stichkarten ausgewertet
und die Strafpunkte der Spieler aufaddiert. Jede Kreuz-Karte ergibt einen Strafpunkt.

## Durchführung des Programms

Es wird zunächst nach der Anzahl an Spielern gefragt. Es können 3 oder 4 Spieler ausgewählt werden.

Dann wird nach den Namen gefragt. Gibt der Benutzer bei einem der Spieler keinen Namen ein, wird dieser Spieler 'Spieler X' genannt, wobei X die Nummer des Spielers ist.

Dann werden die Karten gemischt, an die Spieler verteilt und es geht los.
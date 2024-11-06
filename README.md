# Coding Challenge

Implementiere eine Funktion MERGE die eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von Intervallen zurückgibt.
Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein.
Alle nicht überlappenden Intervalle bleiben unberührt.

Beispiel: Input: [25,30] [2,19] [14,23] [4,8] Output: [2,23] [25,30]

## Ausführung
### Lokale Umgebung
```
pip3 install -r requirements.txt
python3 entrypoint.py [25,30] [2,19] [14,23] [4,8]
```
### Mit Docker
```
docker compose build
docker compose run-example
docker compose test
```


## Annahmen
Wie in den Tests dokumentiert wurden zwei Annahmen getroffen, die sich nicht in der Aufgabenbeschreibung finden.
1. Umgedrehte Intervalle werden als Fehler angesehen z.B. [5,3]
2. Die Reihenfolge der Intervalle in der Ausgabe muss nicht der Eingabe entsprechen

## Benötigte Zeit
5 Stunden 45 min


## Fragen
### Wie ist die Laufzeit deines Programms?
O(n log n)
Der ausschlaggebende Schritt hierfür ist das Sortieren der Liste zu Beginn.
Hier wird aktuell `Powersort` verwendet, was eine Laufzeit von O(n log n) hat.
### Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben?
Bei sehr großen Eingaben könnte das Erstellen der gesamten Liste und die Weitergabe an die `merge` Funktion zu Speicherproblemen führen.
Dieses Problem könnte behoben werden, indem immer nur das jeweils nächste Interval an die Funktion übergeben wird und dieses solange wiederholt wird bis die gesamte Eingabe abgearbeitet ist.
### Wie verhält sich der Speicherverbrauch deines Programms?
Der Speicherverbrauch wächst linear mit der Länge der Eingabe.
Durch die Verwendung einer eigenen Klasse für Intervalle wird der Speicherverbrauch zusätzlich erhöht.
Der Ansatz mit der Intervallklasse wurde dennoch gewählt um eine gute Lesbarkeit zu gewährleisten.
Falls eine Lösung mit deutlich geringerem Speicherverbrauch nötig ist, wäre eine funktionale Lösung denkbar, die lediglich auf einer Liste operiert.
Dies könnte zum Beispiel im embedded Bereich der Fall sein.
Hier sollte aber auch die Wahl der Programmiersprache Python überdacht werden.
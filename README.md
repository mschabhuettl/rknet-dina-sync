# rknet-dina-sync

## Beschreibung

**rknet-dina-sync** ist ein Python-Tool, das Daten aus einer RKnet-Personaldaten-Exportdatei („XLSX“) mit Daten aus dem DiNa-Wiki („CSV“) vergleicht und eine neue CSV-Datei erstellt. Ziel ist es, Benutzer im DiNa-Wiki auf den neuesten Stand des RKnet-Personalstands zu bringen.

Das Programm liest zwei Eingabedateien ein:

1. RKnet-Exportdatei im XLSX-Format
2. Aktueller DiNa-Wiki-Personalstand im CSV-Format

## Installation

Stelle sicher, dass Python 3 installiert ist und installiere die erforderlichen Bibliotheken:

```bash
pip install -r requirements.txt
```

## Benutzung

Das Programm kann über die Kommandozeile aufgerufen werden. Es werden Pfade zu den Eingabedateien („XLSX“ und „CSV“) sowie zur Ausgabedatei angegeben.

### Beispiel

```bash
python3 src/main.py --input-rknet=rknet_export.xlsx --input-dina=dina_users.csv --output=output.csv
```

### Optionen

- `--input-rknet`: Pfad zur RKnet-XLSX-Eingabedatei.
- `--input-dina`: Pfad zur DiNa-Wiki-CSV-Eingabedatei.
- `--output`: Pfad zur Ausgabedatei im CSV-Format.

## Funktionsweise

Das Tool führt folgende Schritte aus:

1. Liest Daten aus der RKnet-XLSX-Datei und der DiNa-Wiki-CSV-Datei.
2. Vergleicht die Benutzerdaten anhand der E-Mail-Adresse.
3. Erstellt eine neue CSV-Datei, die Benutzer enthält, die noch keinen DiNa-Wiki-Account haben.

## Ausgabedatei

Die Ausgabedatei enthält folgende Spalten:
- `Benutzername`: Generierter Benutzername im Format "v.nachname" aus der E-Mail-Adresse (gleich dem Windows-Benutzernamen)
- `Voller Name`: Vorname und Nachname zusammengefügt
- `E-Mail`: E-Mail-Adresse aus der RKnet-Datenbank
- `Gruppen`: Standardwert ist "user"

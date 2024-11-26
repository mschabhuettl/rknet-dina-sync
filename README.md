# rknet-dina-sync

## Beschreibung

**rknet-dina-sync** ist ein Python-Tool, das Daten aus einer RKnet-Personaldaten-Exportdatei („XLSX“) mit Daten aus dem DiNa-Wiki („CSV“) vergleicht und eine neue CSV-Datei erstellt. Ziel ist es, Benutzer im DiNa-Wiki auf den neuesten Stand des RKnet-Personalstands zu bringen.

Das Programm liest zwei Eingabedateien ein:

1. **RKnet-Exportdatei** im XLSX-Format, welche die aktuellen Personalinformationen enthält.
2. **Aktueller DiNa-Wiki-Personalstand** im CSV-Format, welcher die bestehenden Benutzer des DiNa-Wikis abbildet.

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
- `--check-only`: Führt nur eine Überprüfung der Diskrepanzen durch, ohne eine Ausgabedatei zu erstellen.

## Funktionsweise

Das Tool führt folgende Schritte aus:

1. **Daten einlesen**: Liest Daten aus der RKnet-XLSX-Datei und der DiNa-Wiki-CSV-Datei ein.
2. **Vergleich der Benutzerdaten**: Vergleicht die Benutzerdaten anhand der E-Mail-Adresse, um festzustellen, welche Benutzer im DiNa-Wiki fehlen oder welche Unterschiede in den vorhandenen Daten bestehen.
   - **Diskrepanzen in der E-Mail-Adresse**: E-Mail-Adressen werden unabhängig von Groß-/Kleinschreibung verglichen.
   - **Diskrepanzen im Namen**: Der zweite Vorname aus der RKnet-Datei wird ignoriert, um unnötige Unterschiede zu vermeiden.
3. **Erstellung einer neuen CSV-Datei**: Erstellt eine neue CSV-Datei, die Benutzer enthält, die noch keinen DiNa-Wiki-Account haben.
4. **Logging von Diskrepanzen**: Diskrepanzen zwischen den Daten werden im Terminal angezeigt, sodass notwendige manuelle Anpassungen vorgenommen werden können.

## Diskrepanzen

Das Tool überprüft die folgenden Diskrepanzen zwischen den RKnet- und DiNa-Wiki-Daten:

1. **E-Mail-Adressen**: Falls die E-Mail-Adressen zwischen RKnet und DiNa-Wiki nicht übereinstimmen, wird dies als Diskrepanz protokolliert.
2. **Voller Name**: Es wird geprüft, ob der vollständige Name (Vorname und Nachname) zwischen den beiden Datenquellen übereinstimmt. Der zweite Vorname aus der RKnet-Datenquelle wird jedoch ignoriert.

## Ausgabedatei

Die Ausgabedatei enthält folgende Spalten:
- `Benutzername`: Generierter Benutzername im Format "v.nachname" aus der E-Mail-Adresse (gleich dem Windows-Benutzernamen).
- `Voller Name`: Vorname und Nachname zusammengefügt.
- `E-Mail`: E-Mail-Adresse aus der RKnet-Datenbank.
- `Gruppen`: Standardwert ist "user".

## Beispiel-Use-Cases

- **Synchronisierung neuer Benutzer**: Erstelle eine Liste neuer Benutzer, die im DiNa-Wiki noch nicht vorhanden sind, basierend auf den RKnet-Daten.
- **Überprüfung von Diskrepanzen**: Finde Unterschiede zwischen den Personalinformationen in RKnet und DiNa-Wiki, um sicherzustellen, dass beide Systeme konsistente Daten haben.
- **Erstellung von Importdateien**: Generiere eine CSV-Datei, die direkt in das DiNa-Wiki importiert werden kann, um Benutzer zu synchronisieren.

## Hinweise

- Das Tool unterstützt den Vergleich und die Synchronisation nur auf Basis der vorhandenen Daten. Eventuelle Änderungen im DiNa-Wiki müssen manuell vorgenommen werden.
- Alle Diskrepanzen werden farblich hervorgehoben im Terminal ausgegeben, um die Überprüfung zu erleichtern.
- Dieses Tool wurde entwickelt, um eine möglichst einfache Synchronisation zwischen RKnet und DiNa-Wiki zu ermöglichen, jedoch bleibt eine manuelle Überprüfung der Ergebnisse notwendig, um Fehler zu vermeiden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei [LICENSE](LICENSE).

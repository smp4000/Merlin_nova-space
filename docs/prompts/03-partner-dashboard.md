# Modul-Prompt 03 – Partner-Dashboard und erste Schritte

Konsolidierte Fassung des bisherigen Dashboard-Prompts.

```text
AUFTRAG
Plane Merlin „Partner-Dashboard und erste Schritte“. Noch keinen Code schreiben
und keine bestehende Anwendung ändern. STATUS und ENTSCHEIDUNGEN lesen.

DESIGN
Freigegebener Eisblau-Petrol-Stil mit weißen Karten, Navy-Schrift, dezenten
Rahmen/Schatten, Text+Symbol-Status, klaren Aktionen, Mobile/Tablet/Desktop.
Bildreferenz docs/mockups/05-partner-dashboard.png; Fachtext hat Vorrang.

AUSGANGSLAGE
Registrierung abgeschlossen, E-Mail bestätigt, Vertragspartner/Rechnung vorhanden,
SEPA-Mandat erteilt, mindestens eine Station. Team kann noch fehlen oder Einladung
bereits versendet sein. Tatsächliche Zustände übernehmen, keine Beispieldaten im Livebetrieb.
30 Tage Trial, genauer Start folgt Registrierungsentscheidung.
Preise und automatische/manuelle Aboaktivierung bleiben offen.

KONTEXT
Organisation in Seitenleiste, aktuelle Station in Kopfzeile sichtbar trennen.
Organisationsinhaber: Gesamtübersicht und einzelne Stationen.
Stationsleitung: nur zugewiesene Stationen. Jede Zahl hat eindeutigen Stationsumfang.

ERSTER EINSTIEG
Willkommensbereich mit nächstem sinnvollem Schritt, keine erfundenen Umsätze/Alerts.
Einrichtungsfortschritt vorschlagen:
1 Erste Station angelegt.
2 Teamzugang eingerichtet.
3 Erster Schichtplan erstellt.
Aus echten Daten ableiten, nicht nur nach Buttonklick abhaken.
Team: niemand eingeladen / versendet / angenommen / Station zugewiesen.
Plan: nicht begonnen / Entwurf / veröffentlicht.
Personalakte ist nicht Benutzerkonto. Einrichtung ohne weitere Benutzer oder
Schichtplanung ermöglichen: übersprungen und erledigt verschieden kennzeichnen.

STATIONSKARTEN
Name, Anschrift, Einrichtungs-, Team-, Schichtplan- und Artikelstammstatus,
Aktion „Station öffnen“. Keine vollständigen Personenlisten.
Viele Stationen: Suche, Filter und begrenzte/paginierte Abfragen statt 100 Detailkarten.
Stationslimit serverseitig beachten. Artikelimport bezeichnet Artikelstammdaten,
keine automatische Bestandsführung.

PARTNERKONTO
Nur berechtigt: Vertragspartner, Rechnungsadresse, Mandatsstatus, Trial/Abo und
Link zur Vertragsverwaltung. Keine volle IBAN/Mandatskopie/Unterschrift im Dashboard.
Stationsleitung weder Karte noch zugrunde liegende Endpunkte freigeben.
Mandat ist kein bezahltes Abo.

TESTPHASE
Enddatum und nachvollziehbare Restzeit serverseitig berechnen.
Keine internen Planungshinweise wie „Preismodell legen wir gemeinsam fest“ in Live-UI.
Nach Ablauf operative Nutzung sperren, erlaubte Abo-/Vertrags-/Exportwege erhalten.
Nicht unmittelbar löschen. Keine automatische Verlängerung annehmen.

NAVIGATION
Vorschlag: Übersicht, Stationen, Team & Zugänge, Schichtplanung, Ware & MHD,
Kasse & Übergaben; getrennt Vertrag & Abrechnung, Einstellungen, Hilfe.
Nur verfügbare/berechtigte Module und Daten zeigen. Weitere Module später
übersichtlich ergänzen, keine unbegrenzt lange Seitenleiste.

LAUFENDER BETRIEB
Einrichtungsassistent nach Abschluss verkleinern/ausblendbar machen.
Arbeitsübersicht mit echten offenen Anträgen, Schichtbesetzungen, MHD und
Abrechnungen nur bei Modul/Recht. Kennzahldefinitionen und Zeitraum dokumentieren.
„Keine Aufgaben“, „lädt“ und „Fehler“ unterscheiden.

FEHLER/SICHERHEIT
Teilabfragen, Netzfehler, entzogene Rechte, deaktivierte Station, Trialende,
Doppelklicks und offene Einladungen behandeln. Mandanten-/Stationsrechte auch
für Cache, API, Dateien, Exporte und Jobs. Alte Kontextdaten nach Wechsel nicht zeigen.
Keine sensiblen Daten in URLs/Logs/Analyseereignissen.

ABNAHME
Einzelstation, mehrere/100 Stationen, bereits versendete Einladung, Solo-Betrieb,
Stationsleitung eine/mehrere Stationen, Vertragsdatenzugriff verweigert,
Stationswechsel, Trial aktiv/abgelaufen, leere/fehlerhafte Daten, Mobile/Tastatur.

LIEFERE
Aufbau/Priorität, Datenquellen/Statusdefinitionen, Rechte pro Karte/Aktion,
Leer-/Lade-/Fehler-/Sperrzustände, Übergang zum Betrieb, kleine Umsetzungsschritte.
Noch nicht programmieren.
```

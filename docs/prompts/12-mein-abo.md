# Modul-Prompt 12 – Mein Abo

## Phase und Quellen

Nur detailliert planen und ein Bildmockup im bestätigten Eisblau-/Weiß-/Petrol-Stil
erstellen. Keine produktive Anwendung, echte Bestellung, Rechnung oder Zahlung.
Vor späterer ausdrücklich beauftragter Umsetzung AGENTS.md, STATUS, Entscheidungen,
[MEIN-ABO](../planung/MEIN-ABO.md), Paketmodell und Prompts 10/11 lesen.

## Bestätigtes Modell

Grundpaket pro Vertragspartner mit 1 Station, weitere Stationsrechte separat,
Personal-/Einsatzplanungspaket je ausgewählter Station (Mitarbeiter, Schichten,
Abwesenheiten). Team/Zugänge und Basis inklusive, keine Kopfgebühr, zentrale Rechnung.
Monatlicher Start, Erweiterung nach Bestätigung zeitanteilig, Reduzierung zum vereinbarten
Periodenende. Beträge, genaue Vertrags-/Steuer-/Anbieterregeln bleiben offen.
30 Tage Trial, Pflicht-SEPA bei Registrierung; Mandat ist kein kostenpflichtiger Abschluss.

## Ansichten und Abläufe

Tabs Übersicht, Stationen & Module, Änderungen, Rechnungen. Vertragspartner, Status,
laufenden Zeitraum, nächstes Datum und gebuchte Mengen darstellen. Stationsstatus,
Buchungsstatus und vorgemerkte Änderung getrennt. 3 Stationen = 1 inklusive + 2 zusätzlich.
Das Inklusivkontingent nicht künstlich an die zuerst angelegte Station binden.

Stations-/Modulauswahl mit Suche, Filtern und Auswahl über Seiten hinweg. Explizite
Sammelauswahl der aktuellen Seite oder aller gefilterten Stationen. Stabile IDs und
vollständige Prüfungsliste; neue Stationen nicht automatisch nachbuchen.
Häkchen verändert nur Entwurf. Basis und Paket gemeinsam buchbar, keine verwaisten Pakete.
Geplante Module ohne Bestellaktion. Enthaltene Leistungen nicht doppelt bepreisen.

Schritte Auswahl → Prüfung → Bestätigung. Prüfung zeigt vorher/nachher je Station,
Wirkzeitpunkte, Zeitanteil, Folgesumme, Vertragsgrundlagen und Funktionsfolgen.
Sofortige Erweiterung und zukünftige Reduzierung nicht als unklare Nettomenge zeigen.
Offene Preise ausdrücklich „Preis offen“, kostenpflichtiger Abschluss gesperrt.
Preis für alte Positionen nicht durch aktuellen Neukundenpreis überschreiben.

Vorgemerkte Änderungen mit Rücknahme, Akteur und Historie. Basisende berücksichtigt
abhängige Pakete; letzte Station benötigt Gesamtvertragskündigung. Archivierung ist
keine Vertragsänderung. Paketende löscht keine Schichten, Urlaube oder Personalakten.
Historischen Lese-/Exportumfang vor Umsetzung bestätigen, nicht unbegrenzt zusagen.

## Rechte, Technik und Grenzen für später

Inhaber und ausdrücklich berechtigte Vertragsrolle, getrennte Rechte für Rechnungen,
Zahlungsprofil und Gesamtvertragskündigung. Stationsleitung/Mitarbeiter kein Abozugriff.
Organisation/Aktion auch serverseitig prüfen; kein Vertrauensschutz nur durch versteckte UI.
Rechnungen geschützt abrufbar, nur notwendige Stationsreferenzen, keine Beschäftigtendaten.

Servergeprüfte befristete Änderungsangebote, Ausgangsvertragsversion, exakte Geldwerte,
atomare Bestätigung, Wiederholungsschlüssel und eindeutige Ereignisverarbeitung.
Unbekannten Bestellstatus bei Timeout abfragen, nicht blind doppelt bestellen.
Zustände Entwurf/gültiges Angebot/abgelaufen/in Verarbeitung/vorgemerkt/wirksam/
fehlgeschlagen/zurückgenommen unterscheiden. Angebots-/Vertragskopien erhalten.
Verfügbarkeit/Preis-/Versionskonflikte vor Bestätigung erneut prüfen.
Rechnung, Zahlungsanforderung, Einzug, Eingang und Freischaltung nicht gleichsetzen.

## Ergebnisse und Abnahme

Feld-/Rechtematrix, Bildschirmzustände, Prüfregeln, Folgewirkungen, Fehlerfälle,
Zustandsmodell, Datenobjekte und offene Punkte dokumentieren. Vollständige Abnahmefälle
aus MEIN-ABO.md übernehmen, besonders Auswahl ohne Buchung, Sammelauswahl,
Abhängigkeiten, Preis-offen-Sperre, parallele Änderungen, Timeout und letzte Station.
Mockup nur mit Beispieldaten, keine Zahlenpreise. Bildabweichungen dokumentieren.
STATUS, Entscheidungen, Protokoll und Rechnerübergabe aktualisieren und auf GitHub sichern.

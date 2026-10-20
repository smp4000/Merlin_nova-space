# Modul-Prompt 11 – Grundpaket, Zusatzmodule und Abrechnung

## Phase

Nur planen. Keine Anwendung programmieren, keine Verträge aktivieren, keine echten
Rechnungen/Mandate/Einzüge erzeugen. Beträge bleiben offen. Vor späterer Umsetzung
AGENTS.md, STATUS, ENTSCHEIDUNGEN, Prompt 10 und die
[Fachspezifikation](../planung/GRUNDPAKET-UND-ZUSATZMODULE.md) lesen.
Die dortigen Empfehlungen sind ohne weitere Nutzerbestätigung keine verbindliche Preispolitik.

## Empfohlenes Modell ausarbeiten

Ein Vertrag je abonnierendem Vertragspartner/Organisation, Grundpaket mit einer Station,
zusätzliche Stationsrechte und Zusatzpakete je ausgewählter Station. Zentrale Rechnung
an Firma bzw. Einzelunternehmer; Stationsleitung ist kein Rechnungsempfänger/Besteller.
Rechtsform nicht aus Stationszahl ableiten. Getrennte Gesellschaften getrennt führen.

Grundpaket: Organisationsverwaltung, Stationsbasis, Team/Zugänge, Rollen, Basis-Dashboard,
Vertragsübersicht und notwendige Datenschutz-/Sicherheitsfunktionen.
Keine Kopfgebühren als Startempfehlung. Personalstammdaten, Schichtplanung und Abwesenheiten
als gemeinsames Zusatzpaket vorschlagen; intern getrennte Module erhalten.
Ist-Zeit und DATEV erst nach eigener Fach-/Integrationsplanung anbieten.

Vollperiodenformel: G + max(S − 1, 0) × Z + Summe(Qm × Pm).
G = Basis inklusive erster Station, S = gebuchte Stationsrechte, Z = weitere Station,
Qm = Modulstationsmenge, Pm = Modulstationspreis. Alle Beträge offen; keine Nullpreise
unterstellen. Steuer, Zeitanteile und Gutschriften getrennt. Beispiele ohne Eurozahlen.

## Zustände und Änderungen

Abrechnung aus bestätigten Vertragspositionen und gültigen Stationszuordnungen ableiten,
nicht aus Stationsstatus oder Landing-Schaltern. Entwurf nicht kostenpflichtig,
Inaktivität/Archivierung keine automatische Kündigung. Vor Archivierung laufende
Buchung anzeigen. Trial, Betriebsstatus, Vertrag, Rechnung, Zahlung und Entitlement trennen.

Empfehlung monatlicher gemeinsamer Vertragszyklus; Laufzeit/Kündigungsfrist gesondert offen.
Erweiterung nach überprüfter Angebotskopie zeitanteilig bis Periodenende, Reduzierung
zum nächsten zulässigen Periodenende. Tages-/Zeitzonen-/Rundungsregeln vor Umsetzung
bestätigen und mit Anbieter abgleichen. Abhängige Module bei Stationsabbau mitführen.
Keine automatische Neubuchung durch Mitarbeiteranlage, Einladung oder Schichtplanung.

30 Tage Test und Pflicht-SEPA bei Registrierung bleiben bestehen. Trialumfang und
bezahlter Übergang noch offen. Mandat ist kein kostenpflichtiger Aboabschluss.
Keine neue Testphase pro Station. Zahlungsprobleme brauchen einen eigenen Prozess.

## Spätere technische Leitplanken

Unveränderliche Preis-/Angebots-/Vertragsversionen und Rechnungssnapshots. Server rechnet
und prüft Rechte; Clientbeträge ablehnen. Wirksame Zeitintervalle, atomare Änderungen,
Idempotenz, Providerereignis-Deduplizierung und Audit berücksichtigen.
Keine automatischen Bestandskundenpreisanpassungen durch CMS-Veröffentlichung.
Entitlements aus bestätigten Buchungen plus persönliche Rollen-/Stationsrechte.
Partnerdaten, Rechnungsprofil, Zahlungsprofil und Arbeitgeberpersonalakte getrennt.

## Erwartetes Ergebnis und Abnahme

Paketmatrix, Mengenformeln, Vertrags-/Buchungszustände, Änderungsdialoge, Rechnungsaufbau,
Abhängigkeiten, Rechte, Fehlerfälle und offene Entscheidungen dokumentieren.
Prüfen: 1/3/100 Stationen, Modul nur an Teilmenge, Mitarbeiter an mehreren Stationen,
Archivierung ohne versteckte Kündigung, zeitanteilige Erweiterung, geplante Reduzierung,
Preisupdate ohne Änderung alter Verträge, Doppelklick/Webhook und verweigerter Leitungszugriff.
Kein echter Steuer-/Rechnungskonformitäts- oder DATEV-Erfolgsnachweis durch diesen Prompt.
Übergabe, Entscheidungen und Protokoll auf GitHub fortschreiben.

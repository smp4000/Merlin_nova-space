# Modul-Prompt 10 – Super-Admin, Landing und Preise

## Auftrag und Phase

Plane Merlin im freigegebenen Eisblau-/Weiß-/Petrol-Stil. Der Plattformbetreiber
will die gesamte Landing zentral im Super-Admin steuern, besonders Modulpreise.
Aktuell nur Planung und Mockups, keine produktive Implementierung oder Zahlung.
Bei späterem ausdrücklichen Programmierauftrag zuerst AGENTS.md, STATUS und
[Fachspezifikation](../planung/SUPER-ADMIN-LANDING-UND-PREISE.md) lesen.
Offene Entscheidungen nicht eigenmächtig als bestätigte Geschäftspolitik implementieren.

## Gewünschte Oberfläche

- Navigation: Website & Landing, Medien, Module, Tarife & Preise,
  Angebotsregeln, Veröffentlichungen, Änderungsprotokoll.
- Strukturierte Bearbeitung von Hero, Bild/Alternativtext, Navigation, Vorteilen,
  Modulübersicht, Zielgruppen, Ablauf, FAQ, Kontakt, Footer und Seitendaten.
- Abschnitte sortieren und ausblenden; sichere Bausteine statt beliebiger Skripte.
- Desktop-/Mobilvorschau, klarer Entwurfsstatus, Änderungsvergleich und Prüfbericht.
- Modultabelle mit stabilem Schlüssel, Status, Abhängigkeiten, Sichtbarkeit und Tarifzuordnung.
- Preiseditor mit expliziten Bezugsgrößen, Intervallen, Währung und Steuerprofil.
  Beträge aktuell leer/„offen“, niemals als kostenlos interpretieren.
- Veröffentlichung durch explizite Berechtigung; Speichern allein bleibt privat.
- Keine persönlichen Bank-/Mitarbeiterdaten für normale CMS-Aufgaben anzeigen.

## Fachlich strikt trennen

Landing-Sichtbarkeit, technische Modulverfügbarkeit, vertragliche Berechtigung
und persönliche Rollen-/Stationsrechte sind verschiedene Zustände.
Einzelunternehmer/Firma nicht anhand Stationsanzahl unterscheiden.
Organisation, Vertragspartner, Rechnungsprofil, Zahlungsprofil und Station getrennt halten.
Pflicht-SEPA bei Registrierung; Mandat ist kein kostenpflichtiger Vertragsabschluss.
30 Tage Test bleiben bestätigt; danach bezahlt oder stillgelegt. Automatische
Verlängerung oder ausdrückliche Aktivierung bleibt offen.

## Veröffentlichungs- und Preismodell

Plane unveränderliche Versionen für Preise, Angebotsregeln und Rechtsdokumente
sowie einen atomaren Release mit den zugehörigen Landinginhalten.
Checkout berechnet serverseitig mit gültiger Preisversion und speichert die
bestätigten Bedingungen als Angebots-/Vertragskopie. Keine Autorität für Clientbeträge.
Bei veraltetem Angebot erneute Prüfung/Bestätigung statt stiller neuer Preise.
Öffentliche Preisänderungen ändern keine bestehenden Verträge oder Rechnungen.
Bestandskundenänderung benötigt einen eigenen noch festzulegenden Prozess.
Historie und Referenzen bei Rücknahme/Archivierung erhalten.

Offene Preise blockieren bezahlten Abschluss, nicht zwingend eine Informationsseite.
Eine echte Testregistrierung braucht unabhängig davon fertige und geprüfte Abläufe.
Keine geplanten Funktionen als sofort buchbare Leistung ausgeben.
Keine unbelegten Rabatte oder erfundenen Netto-/Brutto-/Jahrespreise verwenden.

## Technische Leitplanken für eine spätere Umsetzung

Plattformrollen getrennt von Partnerrollen, serverseitige Rechte, MFA,
Versionskonfliktprüfung, Transaktionen, Cache-Invalidierung und datensparsames Audit.
Keine Entwurfspreise in öffentliche Antworten ausliefern. Vorschau geschützt.
Text-/Medienvalidierung und sichere Linkziele; keine ausführbaren Uploads oder Secrets.
Exakte Geldwerte, stabile Modulschlüssel, keine zerstörende Löschung referenzierter Preise.
Angebotskopie und Abschluss gegen Wiederholung absichern.
Bestehende Test-/Vertragsbedingungen bei neuer Regelversion erhalten.
Vier-Augen-Prinzip und zeitgesteuerte Veröffentlichungen als offene Ausbaustufen kennzeichnen.

## Erwartete Ergebnisse

Feld-/Rechtematrix, Zustandsmodell, Datenobjekte, Ansichten, Validierungen,
Fehlerfälle, Abhängigkeiten und offene Entscheidungen nachvollziehbar dokumentieren.
Mockup im bisherigen Stil, keine echten Preise/Kundendaten erfinden.
Spätere Abnahme anhand der Szenarien in der Fachspezifikation, insbesondere
Entwurfsisolation, unveränderte Bestandsverträge, manipulierter Preis,
Versionskonflikt und verweigerter Partnerzugriff.
STATUS, ENTSCHEIDUNGEN, PROTOKOLL und Übergabe fortschreiben.

# Modul-Prompt 02 – Partnerregistrierung und Ersteinrichtung

Konsolidierte Fassung des bisher im Chat erstellten Prompts einschließlich SEPA-Nachtrag.
Stand: 20.10.2026. Keine Implementierungsfreigabe.

```text
AUFTRAG
Plane Merlin „Partnerregistrierung und Ersteinrichtung“ im Detail:
Abläufe, Feldkatalog, Datenmodell, Zustände, Berechtigungen, Validierung und Abnahme.
Noch kein Code, keine Migrationen, echten Konten, Mandate oder Zahlungen.
Lies AGENTS.md und ENTSCHEIDUNGEN.md; bestätigte Anforderungen von Vorschlägen trennen.

DESIGN
Eisblau/Petrol, Weiß, dunkelblaue Typografie, klare Schrittführung, responsive.
Referenz: Mockups 02 bis 04; bei Widerspruch gilt diese Fachplanung vor Bildtext.

ZIEL UND OBJEKTE
Gewerblicher Partner als Einzelunternehmen oder Firma/Gesellschaft.
Beide Arten können 1 bis 100 Stationen führen.
Getrennt modellieren: Organisation, Vertragspartner, persönlicher Benutzer,
Rechnungsprofil, Zahlungsprofil, Station, Benutzer-/Stationszuordnung,
Einladung, Testphase und Abonnement.
Vorschlag V1: ein zentraler Vertragspartner und ein Rechnungsprofil je Organisation.
Keine getrennten Rechnungsschuldner je Station oder Multi-Org-Konten still voraussetzen.

ABLAUF
1 Konto → 2 Unternehmen → 3 Rechnung → 4 SEPA → 5 Stationen & Team → 6 Prüfen & starten.
Entwurf speichern und sicher fortsetzen; Pflichtfelder pro Schritt erklären.

SCHRITT 1 – KONTO
Vorname, Nachname, E-Mail, sicheres Passwort. E-Mail bestätigen.
Passwortmanager/Einfügen unterstützen. Keine privaten Daten ohne Zweck.
Vorhandene Konten, Fristablauf, Neuversand und Missbrauch berücksichtigen.
Nicht unnötig verraten, ob eine fremde E-Mail bereits registriert ist.
Keine automatische Werbung; Betriebskommunikation getrennt halten.

SCHRITT 2 – UNTERNEHMEN
Einzelunternehmen: rechtlicher Name des Unternehmers, Geschäftsbezeichnung falls
vorhanden, Geschäftsanschrift, gegebenenfalls zutreffender Rechtsformzusatz.
Gesellschaft: vollständiger rechtlicher Name einschließlich Rechtsform,
Rechtsform, Geschäftsanschrift und verantwortliche Ansprechperson.
Registerangaben nur wo passend; nicht jede Gesellschaft ist eingetragen.
USt-IdNr. nicht pauschal verlangen. Nicht pauschal „Firmenname laut Register“.
Ansprechperson nicht mit Vertragspartner gleichsetzen.
Berechtigung zum Handeln für den Partner bestätigen lassen; Erklärung ersetzt
keine notwendige tatsächliche Prüfung. Vertragspartnerwechsel separat protokollieren.

SCHRITT 3 – RECHNUNG
Vertragspartner/Geschäftsanschrift als Vorgabe übernehmen.
Optional abweichende Rechnungsanschrift, Rechnungs-E-Mail und Referenz.
Versandanschrift ändert nicht den rechtlichen Rechnungsschuldner.
Gesellschaft wird zentral abgerechnet, nicht Stationsleitung.
Stationsadressen getrennt halten. Spätere Rechnungen behalten den damaligen Snapshot.

SCHRITT 4 – SEPA, VERPFLICHTEND
Benutzer hat Mandat ausdrücklich während Registrierung verlangt.
Ohne erfolgreich erteiltes Mandat bleibt Einrichtung Entwurf; kein Abschluss/Trialstart.
Planen: Kontoinhaber, IBAN, erforderliche Zahleranschrift, tatsächlicher Empfänger
mit Anschrift und Gläubiger-ID, eindeutige Mandatsreferenz, Verfahren,
wiederkehrende Zahlungen, freigegebener Text, Berechtigung und Erteilungsnachweis
mit Zeitpunkt/Textversion; Mandatskopie bereitstellen.
Basis-/Firmenlastschrift explizit mit Bank/Anbieter wählen; Firma bedeutet nicht
automatisch Firmenlastschrift. Elektronisches Verfahren muss akzeptiert sein.
Checkbox oder gezeichnete Unterschrift nicht ungeprüft als ausreichend behandeln.
Abweichenden Kontoinhaber einschließlich tatsächlicher Autorisierung berücksichtigen.
IBAN-Formatprüfung beweist weder Inhaberschaft noch gültiges Mandat.
Bank/BIC nur abfragen, wenn das Verfahren es erfordert.
Zustände: Entwurf, ausstehend, erteilt, fehlgeschlagen, widerrufen, ersetzt.
Doppelklicks und wiederholte Anbieterantworten erzeugen kein Doppelmandat.
Bevorzugt nur notwendige Zahlungsreferenzen/maskierte Daten in Merlin halten;
konkrete Architektur bleibt bis Anbieterauswahl offen.
Mandat ist keine kostenpflichtige Abo-Bestellung.
Vor Live-Erteilung müssen reale Betreiberangaben, Gläubiger-ID, Anbieter und
Text/Verfahren final vorliegen. Platzhalter dürfen kein Mandat aktivieren.

SCHRITT 5 – STATIONEN & TEAM
Mindestens erste Station: Name, Straße/Hausnummer, PLZ, Ort, Land;
optional Kurzname/Marke. Weitere Fachangaben später.
Weitere Stationen bis 100; nicht alle während Registrierung erzwingen.
Ähnliche Namen als Hinweis, keine alleinige harte Duplikatsperre.
Stationsadresse nicht still aus Firmenadresse übernehmen.
Team-Einladung optional: persönliche E-Mail, Rolle, ausdrücklich gewählte Stationen.
Einladungen erst nach ausgewähltem Versand und erfolgreichem Abschluss verschicken.
Keine gemeinsamen Passwörter oder automatische Personalakte.
Befristete, widerrufbare, einmalige Links. Bestehende Konten nicht ungefragt vereinen.
Stationsleitung sieht keine fremden Stationen, Rechnungen, Bankdaten oder Mandate.
Team-&-Zugänge-Spezifikation gesondert berücksichtigen.

SCHRITT 6 – PRÜFEN
Vertragspartner, Rechnung, Kontoinhaber/maskierte IBAN, Mandatsstatus,
Stationen, Einladungen und Trialbedingungen zusammenfassen.
Gezielt korrigieren; relevante Mandatsänderung verlangt passenden neuen Prozess.
Vertragsbestätigung, Mandat und optionale Werbung getrennt darstellen.
Datenschutzhinweise bereitstellen, keine pauschale Einwilligung statt Rechtsgrundlagen.
Abschluss wiederholbar/idempotent ohne doppelte Organisation, Trial oder Einladung.

TRIAL/ABO
Bestätigt: 30 Tage kostenlos, danach Abo oder Stilllegung.
Vorschlag: einmaliger Start nach vollständig abgeschlossenem Setup inklusive
E-Mail und Mandat. Enddatum serverseitig/zeitzonengerecht anzeigen.
Wiederaufnahme setzt Frist nicht zurück.
Preise/Laufzeiten/Verlängerung sind offen. Bis zur Entscheidung kein automatisches
kostenpflichtiges Abo oder Einzug allein aufgrund vorhandenen Mandats.
Bei Trialende operative Nutzung sperren, zulässige Vertrags-/Datenwege erhalten.
Nicht unmittelbar löschen; Aufbewahrung/Export/Löschung gesondert definieren.
Widerruf eines Mandats beendet nicht automatisch den Vertrag.

DATENSCHUTZ/SICHERHEIT
Datensparsam, restriktive Rechte, nachvollziehbare Erhebung der Bankdaten vor Trial.
Keine Bankdaten/Tokens/Passwörter in Logs, Analytics oder ungeschützten Browserspeichern.
Mandantentrennung für Seiten/API/Dateien/Exporte/Jobs serverseitig prüfen.
Passwörter sicher hashen, Übertragung/Geheimnisse schützen.
Zweck, Rechtsgrundlagen, Empfänger, Dienstleister, Aufbewahrung und Löschung pro
Datenart festlegen. Keine Fristen erfinden. Betreiber/Partner/Anbieter-Verantwortung klären.
Keine absolute Sicherheit oder ungeprüfte DSGVO-Konformität behaupten.

ABNAHME
Einzelunternehmer 1/mehrere Stationen; Gesellschaft 1/100; Limitüberschreitung;
Gesellschaft ohne Register; abweichende Rechnung/Kontoinhaber; fehlendes/fehlerhaftes
Mandat; Abbruch/Wiederaufnahme; doppelte Abschlussaufrufe; Einladung abgelaufen;
bestehende Konten; Stationsleitung mehrere Stationen; Rechteentzug;
fremde Daten nicht erreichbar; Testende; keine Zahlung allein aus Mandat;
fehlende Anbieter-/Gläubigerkonfiguration; mobile und Tastaturbedienung.

LIEFERE
Fachablauf, Feldkatalog, Datenmodell/Zustände, Berechtigungsmatrix,
Mandats-/Zahlungssystemgrenzen, Datenschutzkonzept/offene Entscheidungen,
Bildschirmbeschreibungen und kleine spätere Umsetzungsschritte.
Noch keinen Code schreiben.
```

# Modul-Prompt 06 – Mitarbeiter und Mitarbeitereinladung, DATEV-orientiert

Planungsauftrag, Stand 20.10.2026. Kein Code und keine echte Übertragung.

```text
AUFTRAG
Plane Merlin „Mitarbeiter & Mitarbeitereinladung“ haarklein auf DATEV-orientierter
Grundlage. Noch keine Anwendung programmieren, keine Migrationen, Mitarbeiter,
Einladungen oder DATEV-Übertragungen erzeugen.
Lies AGENTS.md, STATUS.md, ENTSCHEIDUNGEN.md, MITARBEITER-UND-EINLADUNG.md,
TEAM-UND-ZUGAENGE.md und leitfaeden/DATEV-GRUNDLAGE.md.
Die vollständige Fachspezifikation ist Bestandteil dieses Arbeitsauftrags.

DESIGN UND ZIEL
Freigegebenes Eisblau/Weiß/Petrol, dunkelblaue Schrift, klare Karten/Tabellen,
dezent, mobil bedienbar, Status mit Text+Symbol. Referenz Mockup 08;
fachliche Regeln haben Vorrang vor generiertem Bildtext.
Arbeitgeber erfasst Grunddaten, Mitarbeiter ergänzt eigenen Personalfragebogen,
Personalstelle prüft/übernimmt und bereitet ggf. Kanzleiübergabe vor.
Nicht DATEV-Formular/Logo kopieren, keine Zertifizierung oder Integration behaupten.

ABGRENZUNG UND DATENMODELL
Person, Personalakte, Arbeitgeber, Beschäftigungsabschnitt, Stationseinsatz,
Lohnstammdaten, Fragebogen, Einladung und persönlicher Login getrennt.
Eine Beschäftigung an zwei Stationen erzeugt keine zwei Akten/Personalnummern.
V1-Arbeitgebermodell bestätigen; mehrere Gesellschaften nicht durch Stationswechsel lösen.
Merlin-Vertragspartner nicht ungeprüft als rechtlichen Arbeitgeber voraussetzen.
Keine Lohnberechnung, Überweisung, ELStAM/eAU oder Sozial-/Sofortmeldung in diesem Modul.

ANLEGEN
Grunddaten Name, persönliche Kontaktadresse für Einladung, Arbeitgeber,
geplanter Eintritt, Stamm-/weitere Einsatzstationen mit Gültigkeit.
Entwurf ohne vollständige Lohndaten erlauben. Personalnummer intern versus DATEV
unterscheiden, pro Arbeitgeber/Lohnmandant zuordnen und führende Nullen erhalten.
Vollzeit/Teilzeit, geringfügig/kurzfristig/regulär/Ausbildung, Befristung und
Vergütungsart sind unterschiedliche Dimensionen, keine einzige widersprüchliche Auswahl.
Vertrag, Arbeitszeit und Vergütung vom Arbeitgeber, nicht ungeprüft durch Mitarbeiter ändern.
Keine aktuellen gesetzlichen Grenzwerte als dauerhafte Konstanten erfinden.

FELDGRUPPEN
Persönliches/Anschrift/Geburt, notwendige melderelevante Angaben,
profilabhängige Beschäftigungsselbstauskunft, Steuer/SV/Kassenangaben,
Gehaltszahlungsziel, nötige Nachweise, Arbeitgebervertrag/Arbeitszeit/Vergütung,
DATEV-Nummern und Schlüssel nur mit abgestimmter Fachverantwortung.
Je Feld Zweck, Quelle, Datentyp, Pflicht/bedingt, Sicht-/Änderungs-/Prüfrecht,
Gültigkeit und Aufbewahrung definieren. „Unbekannt“ und „nicht zutreffend“ unterscheiden.
Keine pauschale Pflicht zu Religion/Familienstand/Ausweis-/Bankkartenkopien,
Diagnosen oder sonstigen unnötigen Daten. Anforderungen mit Lohnstelle konkretisieren.
Fehlende Kennungen/Auslandsfälle als Klärungsweg, keine Fantasiewerte.
Gehalts-IBAN ist kein SEPA-Mandat und bleibt vom Partner-Zahlungsprofil getrennt.

MITARBEITEREINLADUNG
Eigener Zweck: nur persönliche Angaben für eigene Akte erfassen.
Versand nach Empfänger-/Kontextprüfung und ausdrücklicher Bestätigung.
Mail ohne Steuer/SV/Bankdaten, Verträge oder komplette Akte.
Token zufällig/gehasht/einmalig/befristet/widerrufbar und an Vorgang gebunden.
Keine dauerhafte sensible Personalakte allein durch wiederverwendbaren Link schützen.
Vor sensibler Vorbelegung bestätigte Zieladresse und sicheren Erfassungszugang verlangen.
7 Tage Gültigkeit ist Vorschlag. Neuversand invalidiert alten Link, verhindert Doppelanlage.
Versandstatus, Annahme, Bearbeitung und Einreichung separat führen.
Ohne persönliche E-Mail sichere assistierte Erfassung statt universeller Stationen-Accounts.
QR/Papiercode nur späterer bewusst bestätigter sicherer Übergabeweg, nicht Alleinschutz.
Zusätzlicher Merlin-Login separat in Team & Zugänge prüfen/einladen/verknüpfen.

SELBSTERFASSUNG
Eigener mobiler Assistent: Persönliches → Beschäftigungsselbstauskunft →
Steuer/Sozialversicherung → Zahlungsangaben → Nachweise → Prüfen & einreichen.
Nur passende Profilfelder, Arbeitgeberwerte als schreibgeschützte Vorgabe/Rückfrage.
Serverseitiges Zwischenspeichern mit Bestätigung und sicherer Wiederaufnahme.
Keine sensiblen Offline-/localStorage-/Service-Worker-Caches, Daten in URL/Analytics/Mail/Logs.
Einreichung versioniert, nicht automatisch in Stamm-/Lohnsystem übernommen.
Keine pauschale Datenschutz-Einwilligung, Vertragsunterschrift oder SEPA-Erteilung
durch „Einreichen“ unterstellen.

PRÜFUNG
Abschnitts-/Felddifferenzen, fehlende Angaben und Rückfragen nur für Berechtigte.
Formale Prüfung, Selbstauskunft, Arbeitgeberprüfung und externe Bestätigung unterscheiden.
Gezielte Übernahme, keine unkontrollierte Vollüberschreibung vorhandener Daten.
Korrekturen/versionierte Wirkung, Konflikte und bereits exportierte Stände berücksichtigen.
Bankänderungen besonders absichern. Vier-Augen-Freigabe als offener Vorschlag.
Dokumente kategorisieren, prüfen/quarantänisieren, geschützt speichern/abrufen;
keine ungefragten externen OCR-/Signaturdienste und öffentlichen Downloadlinks.

RECHTE
Personal-/Lohnrechte feld- und vorgangsbezogen, nicht pauschal durch Inhaber-/Leitungsrolle.
Stationsleitung standardmäßig nur erforderliche Einsatz-/Planungsdaten ihrer Stationen,
keine Wohnanschrift, Vergütung, Steuer/SV/IBAN oder allgemeine Personalakte.
Mitarbeiter nur eigene angefragte Daten; kein Verzeichnis anderer Personen.
Kanzleizugriff eigener späterer begrenzter Prozess. Jeder Zugriff auch in
API/Dateien/Suche/Zähler/Export/Jobs serverseitig autorisieren.

DATEV-GRUNDLAGE
Zielprogramm LODAS oder Lohn und Gehalt wurde angefragt, bis Antwort offen.
Eigenes neutrales Stammdatenmodell planen, DATEV-Mapping als separaten Adapter.
Je Zielfeld echte Bezeichnung/Kennung, Quelle/Version, Pflicht, Code, Format,
Gültigkeit, Null-/Löschsemantik und nicht unterstützte Werte dokumentieren.
Arbeitgeber/Lohnmandant und Personalnummer mit Kanzlei abgleichen.
Keine beliebige CSV als DATEV-kompatibel bezeichnen. Ohne bestätigtes Format nur
ausdrücklich neutrale Prüfübersicht, kein aktiver „an DATEV senden“-Erfolgsweg.
Exporte nur geprüft, autorisiert, versioniert und sicher; Wiederholung/Korrektur/
Rückmeldungen ohne Doppelanlage. PDF erstellt ≠ übertragen ≠ im Ziel übernommen.
Cloud/API, Freischaltung und technische Abnahme sind ein eigener späterer Auftrag.
Keine Meldungen oder rechtliche Fristerfüllung aus Fragebogenversand ableiten.

LEBENSZYKLUS/DATENSCHUTZ
Beschäftigungsstatus, Fragebogenstatus, Login und Übergabe getrennte Zustände.
Austritt, nicht angetreten, Wiedereintritt und Arbeitgeberwechsel gesondert planen.
Kein Austritt als automatisches Löschdatum, keine Kontosperre als Vertragskündigung.
Zweck/Erforderlichkeit/Rechtsgrundlagen/sensible Felder/Empfänger/Fristen
mit Personal-/Datenschutz-/Lohnstelle prüfen. Keine Konformitätsgarantie.
Audit minimal statt voller Kennungen/Werte; keine echten Personal-/Bankdaten auf GitHub.

ABNAHME UND ERGEBNIS
Vollständige Fälle aus Fachspezifikation behandeln: Mehrstationeneinsatz,
getrennter Login, falsche/alte Einladung, eigene Datenisolation, unbekannte Kennungen,
Arbeitgeberwerte geschützt, Versionskonflikte, Bankänderung, Dokumentenquarantäne,
Stationsleitung ohne Lohneinsicht, Zielprogramm offen, Exportprüfung/Rückmeldung,
Austritt/Wiedereintritt, sicheres Fortsetzen, Mobile/Tastatur/Auslandsanschrift.
Liefere Feldkatalog, Rollenmatrix, Prozess-/Zustandsdiagramme, Screens, Mappinggerüst,
Datenschutzkonzept/offene Punkte und kleine spätere Umsetzungsschritte.
Noch keinen Code schreiben.
```

# Datenschutz und SEPA – Planungsleitfaden

Stand: 20.10.2026. Technische/fachliche Anforderungen, keine fertigen Rechtstexte
und keine Bestätigung einer absoluten oder bereits geprüften DSGVO-Konformität.

## Datenschutz von Anfang an

Datensparsamkeit, begrenzte Zugriffe und datenschutzfreundliche Voreinstellungen
in Datenmodell und Oberfläche einplanen. Nur erforderliche Angaben je Zweck erfassen.
Quelle: [EU-Kommission – Datenschutzgrundsätze](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en).

Technik und organisatorische Maßnahmen müssen von Beginn an geplant und im Betrieb
fortgeführt werden. Quelle: [EDPB – Privacy by design and by default](https://www.edpb.europa.eu/topics/ai-and-technology/privacy-by-design-and-by-default_en).

Vor Produktionsstart konkret klären:
- Verantwortlichkeiten von Merlin-Betreiber, Partner und Dienstleistern.
- Zwecke/Rechtsgrundlagen, Hinweise und erforderliche Verträge je Verarbeitung.
- Hosting, Empfänger, Unterauftragnehmer und gegebenenfalls Drittlandtransfers.
- Fristen für Entwürfe, Einladungen, Mandate, Rechnungen, Konten und Auditdaten.
- Betroffenenrechte, Datenexport, Sperre und Löschung mit Aufbewahrungspflichten.
- Technische Mandanten-/Stationsabgrenzung einschließlich Dateien/API/Exports.
- Schlüsselmanagement, sichere Authentifizierung, Backups und Vorfallprozess.

Das früh verlangte SEPA-Mandat ist ausdrücklicher Benutzerwunsch. Zweck und
Rechtsgrundlage der Bankdatenerhebung bereits vor Trial müssen nachvollziehbar geprüft
und erklärt werden. Eine optionale Werbeeinwilligung nicht mit Betrieb/Vertrag koppeln.

## SEPA

Gläubiger-ID und Mandatsreferenz identifizieren ein Mandat gemeinsam.
Quelle: [Bundesbank – Gläubiger-Identifikationsnummer](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/serviceangebot/sepa/glaeubiger-identifikationsnummer).

Für Vorabinformationen Betrag und Fälligkeit vorsehen; grundsätzlich 14 Kalendertage
vor Fälligkeit, sofern keine andere Frist vereinbart ist. Nicht still verkürzen.
Quelle: [Bundesbank – Fragen und Antworten zu SEPA](https://www.bundesbank.de/action/de/613964/bbksearch?pageNumString=1).

Noch offen:
- Tatsächlicher Zahlungsempfänger mit Anschrift und Gläubiger-ID.
- Zahlungsanbieter/Bank und akzeptierter elektronischer Nachweis.
- Basis- oder Firmenlastschrift; Gesellschaft als Kunde entscheidet das nicht automatisch.
- Freigegebener Text, Autorisierung abweichender Kontoinhaber, Mandatskopie und Widerruf.
- Speicherung beim Anbieter versus notwendige verschlüsselte lokale Daten/Referenzen.
- Zahlungs-/Fehler-/Rücklastschriftprozess und Benachrichtigungen.

IBAN-Prüfung ist keine Kontoinhaberprüfung. Checkbox ist nicht automatisch ein akzeptiertes
elektronisches Mandat. Bestehendes Mandat allein ist keine Abo-Bestellung.
Ohne tatsächliche Anbieter-/Betreiberkonfiguration keine Live-Erteilung ermöglichen.

## Öffentliche GitHub-Ablage

Nur Beispieldaten verwenden. Keine echten IBANs, Mandate, Personalakten, Kundenlisten,
Supportexporte, Passwörter oder Tokens hochladen. Screenshots vor Ablage auf solche Daten prüfen.
Planungsunterlagen dürfen offen liegen; persönliche Betriebsdaten gehören nicht in dieses Repository.

# Mein Abo – Stationsauswahl, Zusatzmodule und Buchungsänderungen

Stand: 20.10.2026. Fachplanung und Rastermockup, keine Implementierung.

## 1. Bestätigte Grundlage und neue Vorschläge

Der Benutzer bestätigt das zuletzt vorgeschlagene Modell: Grundpaket je Vertragspartner
mit einer Station, weitere Stationen separat, Zusatzpakete je ausgewählter Station,
zentrale Rechnung, keine Kopfgebühren. Stationsbasis und Team/Zugänge sind inklusive;
Personal, Schichten und Abwesenheiten bilden das Personal-/Einsatzplanungspaket.
Monatlicher Start, bestätigte Erweiterungen zeitanteilig und Reduzierungen zum
vereinbarten Periodenende bilden die bestätigte Planungsrichtung.

Konkrete Beträge, Steuer-/Rundungsregeln, Anbieter, Vertragsfristen und bezahlter Übergang
nach 30 Tagen sind weiterhin offen. Die hier ergänzten Bedienabläufe, Status und
Konfliktregeln sind Umsetzungsvorschläge. Diese Bestätigung ist keine Bestellung.

Ziel: Ein berechtigter Partner versteht jederzeit, was heute gilt, was er gerade
ausgewählt hat, was ab wann geändert wird und wie sich die Abrechnung zusammensetzt.

## 2. Zugang und Rechte

| Fähigkeit | Inhaber | Delegierte Vertragsrolle | Stationsleitung | Mitarbeiter |
|---|---|---|---|---|
| Organisationsabo lesen | Ja | Mit Leserecht | Nein als Standard | Nein |
| Auswahl entwerfen/Angebot prüfen | Ja | Mit Änderungsrecht | Nein | Nein |
| Kostenpflichtig bestellen/reduzieren | Ja | Mit explizitem Vertragsrecht | Nein | Nein |
| Rechnungen herunterladen | Ja | Separates Rechnungsrecht | Nein | Nein |
| Zahlungsprofil bearbeiten | Ja | Separates Zahlungsrecht | Nein | Nein |
| Gesamtvertrag kündigen | Ja | Eigenes Kündigungsrecht | Nein | Nein |

Delegation zunächst optional. Serverseitig Organisation, konkrete Aktion und aktuelle
Berechtigung bei jedem Abruf/Bestätigen erneut prüfen. Kein Rollenwechsel im Browser.
Vertragsrecht gibt keine Personal-/Gesundheitsdatenrechte. Super-Admin-CMS-Recht gibt
kein unbegrenztes Recht, im Namen eines Kunden kostenpflichtig zu bestellen.
Supporteingriffe später als gesonderte begründete/auditierte Befugnis planen.

## 3. Aufbau der Seite

Kopf: „Mein Abo“, Vertragspartner, Vertragsreferenz, Status, Bezugsdatum und klarer
Hinweis bei Trial, Sperre oder unvollständigem Angebot. Keine Bankdaten im Kopfbereich.

Tabs: Übersicht, Stationen & Module, Änderungen, Rechnungen; Rechnungs-/Zahlungsprofil
als gesonderte berechtigte Detailansichten. Browser-Zurück verliert keine bestätigte
Buchung, ungespeicherten Entwurf vor Verlassen kenntlich machen.

Übersichtskarten:

- Grundpaket: enthaltene Leistung, 1 Station inklusive, Preisversion.
- Stationen: aktuell gebuchte Zahl, weitere Stationen als Menge, nicht alle Entwürfe.
- Personalpaket: Anzahl aktuell freigeschalteter Stationen.
- Abrechnung: laufender Zeitraum, nächster Zyklus, wiederkehrender Betrag.
- Änderungen: heute wirksame und zukünftige Änderungen deutlich trennen.

Alle Betragsfelder in dieser Planungsansicht „Preis offen“, kein 0-Euro-Platzhalter.
Kein echter aktiver Bezahlvertrag wird behauptet. „Beispielansicht“ im Mockup kennzeichnen.

## 4. Stationsauswahl im Detail

Tabelle: Auswahl, Stationsname, Referenz/Ort, Betriebsstatus, Basisbuchung,
Zusatzpakete, geplante Wirksamkeit, Aktionen. Suche, Statusfilter, Sortierung und
seitennummerierte Ansicht für bis zu 100 Stationen vorsehen.

Vertraglicher Buchungsstatus und Betriebsstatus stehen in getrennten Spalten/Details:
„Inaktiv“ ist nicht „ungekündigt kostenlos“, „Entwurf“ ist nicht „gebucht“.
Ein erklärter Mengenzähler zeigt „3 Stationen gebucht = 1 inklusive + 2 zusätzlich“.
Die enthaltene Station ist ein Mengenkontingent; keine künstliche dauerhafte
Preisbindung an die zuerst angelegte Stations-ID. Endet eine von drei Buchungen,
bleiben eine inklusive und eine zusätzliche Station. Zuordnungswechsel ist trotzdem
ein eigener Vorgang, keine parallele Nutzung desselben Rechts an zwei Stationen.

| Zeilentyp | Anzeige/Aktion |
|---|---|
| Basis gebucht, kein Personalpaket | Personalpaket auswählen |
| Basis und Personalpaket gebucht | Paketende vormerken oder Basisende mit Folgen prüfen |
| Basis als Entwurf | Stationsbasis hinzubuchen, optional Paket zusammen auswählen |
| Ende bereits vorgemerkt | Enddatum zeigen; gesondert „Beendigung zurücknehmen“ |
| Station archiviert, Buchung läuft | Warnung und Weg zur Vertragsänderung |
| Unvollständiger Stationsentwurf | Fehlende Mindestdaten zeigen; keine ungültige Buchung |

Mindestdaten für Zuordnung: stabile Stations-ID, organisatorische Zugehörigkeit,
eindeutiger Anzeigename, vereinbarter Standortumfang; weitere Pflichtdaten mit
Stationsverwaltung abstimmen. Keine personenbezogenen Beschäftigtendaten im Selektor.

Häkchen ändern nur den Auswahlentwurf. Neue Station zuerst als Datensatz anlegen,
anschließend ausdrücklich buchen. Basis und abhängige Pakete können in einem
geprüften Änderungsvorgang aufgenommen werden; kein Paket ohne Stationsbasis.

Sammelauswahl: „Alle Treffer dieser Seite“ und „Alle N gefilterten Stationen“ explizit
unterscheiden. Auswahl mit stabilen IDs festhalten, über Seitenwechsel erhalten,
ausgefilterte ausgewählte Stationen im Zähler anzeigen. Vor Bestätigung vollständige
Liste prüfbar machen. Später neu angelegte Stationen werden nicht automatisch gewählt.
„Alle buchen“ darf niemals still den gesamten Organisationsbestand bestellen.

## 5. Zusatzmodule und Abhängigkeiten

Personal & Einsatzplanung enthält Mitarbeitergrundlage, Schichtplanung und Abwesenheiten.
Stationsbezogene Buchung und individuelle Rollenrechte bleiben getrennt. Ein Paket
an zwei Stationen erzeugt zwei Paketpositionen, keine doppelten Personalakten.
Andere Stationen können dieselben Benutzerkonten besitzen, ohne das Paket zu erhalten.

Modulkarten zeigen Inhalt, Voraussetzungen, Verfügbarkeit, ausgewählte Stationszahl
und aktuelle/neue Menge. Nur verfügbare Leistungen buchbar; Ist-Zeit und DATEV zeigen
höchstens „Geplant“, ohne Bestellaktion. Bei enthaltenen Leistungen „Im Grundpaket“
statt erneut kostenpflichtig auswählen. Paketabhängigkeiten serverseitig prüfen.
Noch nicht beauftragte Module erzeugen weder Personalakte noch Datenexport.

## 6. Änderungen in drei Schritten

### Schritt 1 – Auswahl

Aktuellen Stand als unveränderte Ausgangsbasis laden. Stations- und Paketwünsche
erfassen. Für Hinzubuchungen „Ab sofort“ oder „Ab nächstem Abrechnungszeitraum“
anbieten. Reduzierung auf nächstes vertraglich zulässiges Ende vormerken.
Genaue Wirksamkeit immer aus Vertragszyklus/-regeln bestimmen, nicht aus Browserdatum.
Bei leerem Unterschied keine Bestellung anbieten.

### Schritt 2 – Prüfung

Server erstellt versioniertes, befristetes Änderungsangebot. Anzeige:

1. Vertragspartner und Vertragsreferenz.
2. Heute bestehende Mengen/Leistungen.
3. Hinzukommende und entfallende Leistungen je Station.
4. Wirkzeitpunkte; sofortige und spätere Teile in getrennten Gruppen.
5. Einmaliger Zeitanteil im laufenden Zeitraum mit Tagesbasis.
6. Wiederkehrende Summe im nächsten Zyklus sowie weitere vorgemerkte Schritte.
7. Steuerdarstellung und Zahlungsgrundlage nach freigegebenem Modell.
8. Folgen für Funktionen und Datenzugriff, relevante Vertragsdokumentversionen.

Für gemischte Änderungen keine unverständliche Nettomenge: „Station West hinzubuchen
ab heute, Station Süd beenden zum Periodenende“ ausdrücklich auflisten. Keine sofortige
Verrechnung einer erst später endenden Leistung. Historische Bestandspositionen behalten
ihre Preisversion; Preis für neue Leistungen nach noch festzulegender Anschlussregel
ermitteln. Kunden nicht still vollständig auf aktuellen Neukundentarif umstellen.

Offene Preise/Vertragsgrundlagen: Pflichtfelder als fehlend markieren, Abschluss sperren.
Keinen „vorläufigen“ Bezahlvertrag mit nachträglich frei einsetzbarem Betrag erzeugen.

### Schritt 3 – Bestätigung und Ergebnis

Erst bei vollständigem rechts-/fachlich geprüftem Angebot darf ein eindeutig bezeichneter
kostenpflichtiger Abschluss erfolgen. Endgültige Buttontexte/Zustimmungen separat prüfen;
Mockupwortlaut ist keine freigegebene rechtliche Gestaltung. Erneut Rechte, Mandat soweit
erforderlich, Angebotsgültigkeit, Vertragsversion, Kapazität und Abhängigkeiten prüfen.

Ergebnis mit Änderungsreferenz: „Wirksam“, „Vorgemerkt“ oder „Wird verarbeitet“.
Technische Annahme nicht als verbuchter Zahlungseingang darstellen. Bei Timeout aktuellen
Status zur selben Referenz abfragen; kein erneutes blindes Bestellen.
Bestätigungsbeleg mit Leistungen/Wirksamkeit/Preisversion später abrufbar; keine echten
E-Mails in Planung, spätere Benachrichtigung separat datensparsam vorsehen.

## 7. Zustandsmodell und Konflikte

| Zustand | Bedeutung | Zulässiger nächster Schritt |
|---|---|---|
| Auswahlentwurf | Unverbindliche lokale/gespeicherte Auswahl | Prüfen oder verwerfen |
| Angebot gültig | Servergeprüfte unveränderte Angebotskopie | Bestätigen oder neu berechnen |
| Angebot abgelaufen | Frist, Vertrag oder Verfügbarkeit geändert | Erneut prüfen/akzeptieren |
| Wird verarbeitet | Bestätigung angenommen, Ergebnis noch nicht gesichert | Status laden |
| Vorgemerkt | Verbindlich erfasst, zukünftiger Zeitpunkt | Zulässige Rücknahme prüfen |
| Wirksam | Leistung zum bestätigten Zeitpunkt gültig | Neuer Änderungsvorgang |
| Fehlgeschlagen | Keine wirksame Buchung oder klar abgegrenzter Fehler | Fehler zeigen, sicher erneut prüfen |
| Zurückgenommen | Vormerkung ausdrücklich aufgehoben | Historie erhalten |

Vertragsversion und eindeutiger Wiederholungsschlüssel verhindern parallele Überschreibungen
und Doppelbuchungen. Zwei Inhaber können nicht auf derselben veralteten Ausgangsbasis
abweichende Angebote blind bestätigen. Dienstneustart darf keine Vormerkung verlieren.
Anbieterfehler und lokal angenommene Buchung abgleichen; keine widersprüchlichen
Zahlungs-/Leistungszustände mit bloßem roten Toast verbergen.

Konfliktbeispiele: Station inzwischen einer anderen Organisation zugeordnet, erreichtes
Limit, zurückgezogenes Modul, beendeter Vertrag, ausstehende Kündigung, Preis zurückgezogen.
Konkrete betroffene Station/Leistung nennen; keine fremden Organisationsdaten offenlegen.

## 8. Vorgemerkte Änderungen und Reduzierungen

Tab Änderungen zeigt geplant/wirksam/zurückgenommen/fehlgeschlagen, Datum, Akteur,
Positionen und Beleg. Keine sensiblen Zahlungsdaten im Änderungsjournal.
„Zurücknehmen“ vor Wirksamkeit nach Berechtigungs-/Fristenprüfung; neues dokumentiertes
Ereignis statt Historieneintrag löschen. Nach Wirksamkeit ist Neubuchung nötig.

Basisbeendigung muss anhängende Pakete am gleichen Ende berücksichtigen. Bei späterer
Paketaktivierung auf einer zum früheren Zeitpunkt endenden Basis Auswahl blockieren.
Neue widersprüchliche Vormerkung verlangt explizite Ersetzung mit erneutem Vergleich.
Keine doppelte Kündigung derselben Position. Zeitzone und genaues Ende sichtbar machen.

Vor Leistungsende zeigen: welche Stationen/Planer betroffen sind, bestehende Daten bleiben
erhalten, welche Schreibaktionen enden, mögliche Konflikte mit bereits geplanten Schichten.
Keine automatische Schichtlöschung oder Urlaubsstornierung durch Paketende. Vorschlag:
historische Informationen berechtigt lesbar/exportierbar halten, neue modulbezogene
Schreibaktionen ab Ende sperren. Umfang und Dauer des Nachzugriffs bleiben Datenschutz-/
Vertragsentscheidung; keine unbegrenzte kostenlose Archivfunktion zusagen.

Letzte Stationsbuchung entfernen ist Gesamtvertragskündigung, nicht Reduzierung auf
kostenloses Grundpaket. Gesonderter Ablauf mit Folgen, Frist und Bestätigung nötig.
Station archivieren ändert den Vertrag nicht; Warnung verlinkt auf genau diese Station
in Mein Abo. Vertragsänderung archiviert die Station umgekehrt nicht automatisch.

## 9. Trial und Zahlungsprobleme

Trialansicht: 30 Tage, verbindlicher Start-/Endzeitpunkt, verwendeter Angebotsstand,
Testumfang und ausgewählte künftige Leistungen getrennt. Kein erneuter Trial je Modul.
Noch offene Testmengen nicht im Mockup als unbegrenzt darstellen.
Pflicht-SEPA aus Registrierung bleibt sichtbar als Status, nicht als IBAN-Klartext.
SEPA erteilt bedeutet nicht „Abo kostenpflichtig bestätigt“ oder „Zahlung eingegangen“.
Der automatische oder ausdrücklich bestätigte bezahlte Übergang bleibt offen.

Bei stillgelegtem/gekündigtem/gesperrtem Vertrag passende schreibgeschützte Ansicht,
Statusbegründung und zulässigen Reaktivierungsweg zeigen. Keine neue Belastung per
„Erneut versuchen“, wenn Bestellstatus unbekannt ist. Mahn-/Kulanz-/Sperrregeln und
Reaktivierung nach Rücklastschrift sind separate noch offene Fachregeln.

## 10. Rechnung und Zahlung

Rechnungsliste: Nummer, Zeitraum, Datum, Rechnungsempfänger, Betrag, Rechnungsstatus,
separater Zahlungsstatus und berechtigter Download. Rechnungsvorschau ist kein echter
Beleg; ohne Rechnungsdaten leerer Zustand statt erfundener Rechnungsnummer.
Detail: Grundpaket, zusätzliche Stationen, Paketmengen, Stationsaufschlüsselung,
Zeitanteile/Korrekturen und Steuern. Historische Adress-/Preis-Snapshots erhalten.

Keine Rechnung an Stationsleitung, auch wenn sie Kostenstelle ist. Kein Mitarbeitername
oder Gesundheitsdatum auf Stationsaufschlüsselung. Downloads nur mit Rechteprüfung,
keine öffentlichen dauerhaften URLs. Bankänderung über gesondert geschützten Prozess;
ein geändertes Rechnungsprofil ersetzt kein Mandat und keinen Vertragspartnerwechsel.
Mandatsdetails/-änderung erst mit ausgewähltem Anbieter endgültig planen.

## 11. Fehlende Daten, Bedienbarkeit und Datenschutz

Ladezustand, keine Station, keine Zusatzmodule, kein Beleg, keine Änderungen und Fehler
als eigene Ansichten. Bei technischer Störung keine Beträge aus leerem Zustand als null
berechnen. Auswahl erhalten, unbekannten Bestellstatus ausdrücklich zeigen.
Tastaturbedienung, Fokusführung im Prüfdialog, beschriftete Checkboxen, Status mit Text
statt nur Farbe, Mobilansicht als Stationskarten mit angehefteter Zusammenfassung.
Zurück aus Prüfung erhält Auswahl; „Entwurf verwerfen“ ändert keine bestehende Buchung.

Zugriffs-/Änderungsprotokoll sparsam, kein Klartextmandat oder voller Zahlungsdateninhalt.
Rechte bei Export/Belegabruf ebenso prüfen wie auf der Seite. Kein Tracking der
Abrechnungsansicht durch öffentlich eingebettete Werbedienste.

## 12. Spätere Datenobjekte und Lieferreihenfolge

Subscription/Items und Stationszuordnungen aus Prompt 11 ergänzen um SelectionDraft,
ChangeQuote mit expires-at/base-version, ChangeRequest mit Wiederholungsschlüssel,
ScheduledChange und ChangeEvent. Event-/Angebotskopien unveränderlich, Entwurf löschbar
nach festgelegter Frist. Preise und Mengen nur serverseitig als Vertragsautorität.
Vormerkungsprozess muss exakt einmal wirksame Buchungen erzeugen; Abgleich mit Anbieter
wiederholbar, Fehlerqueue/Betreiberprüfung für nicht selbst auflösbare Fälle vorsehen.

Spätere Schritte: Lesemodell/Rechte → Auswahl/Abhängigkeiten → Angebotsberechnung →
Bestätigung/Vormerkung → Rechnungs-/Zahlungsanzeige mit bestätigtem Provider.
Jetzt keine Migration, Serverendpunkte, Zahlungsanbindung oder App-Komponenten erstellen.

## 13. Spätere Abnahmeszenarien

1. Drei gebuchte Stationen zeigen 1 inklusive + 2 zusätzlich; Entwürfe zählen nicht.
2. Personalpaket von 2 auf 3 Stationen wählen verändert vor Bestätigung keine Rechte.
3. Basisentwurf plus Paket wird gemeinsam geprüft; Paket allein wird abgewiesen.
4. Alle gefilterten Stationen auswählen, Seitenwechsel und Filterwechsel verlieren keine IDs.
5. Später angelegte Station wird durch frühere Sammelauswahl nicht mitgebucht.
6. Fehlender Preis blockiert Abschluss, Anzeige bleibt „offen“ statt null.
7. Ausgeblendeter Landingpreis schreibt bestehende Vertragsposition nicht um.
8. Gleichzeitige Änderung zweier Inhaber erzeugt kontrollierten Versionskonflikt.
9. Doppelklick, Timeout und wiederholtes Providerereignis erzeugen nur eine Änderung.
10. Zubuchung heute und Reduzierung später bleiben getrennte Positionen/Zeiträume.
11. Reduzierung samt abhängigen Modulen wird einmal wirksam; Rücknahme bewahrt Historie.
12. Letzte Station entfernen führt zur Gesamtvertragsprüfung statt Gratisbestand.
13. Archivierte Station mit laufender Buchung wird erklärt, nicht heimlich abbestellt.
14. Stationsleitung kann weder Seite noch Bestell-/Belegendpunkte unberechtigt nutzen.
15. Bereits geplante Schichten/Urlaube werden bei Paketende nicht gelöscht.
16. Fehlendes erforderliches Mandat und abgelaufenes Angebot werden vor Abschluss erkannt.
17. Rechnungsempfänger bleibt Vertragspartner, historische Adresse bleibt erhalten.
18. Trialende ohne gültigen Folgezustand erzeugt keine erfundene Zahlung oder Datenlöschung.

## 14. Offene Entscheidungen

Beträge, Preisregel für spätere Zubuchung bei alten Verträgen, Steuer/Rundung/Zeitzone,
Trialumfang/Übergang, genaue Kündigungsfristen, Anbieter und Zahlungsproblemregeln.
Außerdem delegierte Vertragsrechte, Detailpolitik zum Datenzugriff nach Leistungsende,
Angebotsgültigkeitsdauer und maximale Entwurfsaufbewahrung. Nicht aus Bildtexten ableiten.

[Prompt 12](../prompts/12-mein-abo.md) ·
[Mockup 13](../mockups/13-mein-abo.png) ·
[Paketmodell](GRUNDPAKET-UND-ZUSATZMODULE.md)

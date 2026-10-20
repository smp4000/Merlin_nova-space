# Stationsverwaltung – Fachspezifikation

Stand: 20.10.2026 · Planungsentwurf · Keine Implementierung.
Bestätigt sind mehrere Stationen bis 100, getrennte Rechnungs-/Standortangaben,
persönliche Stationsleitungszugänge und der Eisblau-Petrol-Stil.
Weitere fachliche Detailregeln sind Vorschläge bis zur Besprechung mit dem Benutzer.

## 1. Ziel und Abgrenzung

Der Partner verwaltet Standorte zentral, die Stationsleitung den freigegebenen
Teil ihrer zugewiesenen Standorte. Alle Fachmodule verwenden dieselbe Station,
keine eigenen parallelen Stationsstammdaten.

Station ≠ Organisation ≠ Vertragspartner ≠ Rechnungsprofil ≠ Zahlungsprofil.
Eine Adresse kann bei verschiedenen Stationen gleich sein; gemeinsame Anschrift
beweist weder Gleichheit noch Zugehörigkeit. Ein Standortwechsel ist nicht automatisch
ein Wechsel von Inhaber, Organisation oder Rechnungsschuldner.

Dieses Modul plant Stammdaten, reguläre Öffnungszeiten, Ausnahmen, Zuständigkeiten,
Ausstattungsreferenzen und Lebenszyklus. Schichtregeln, Warenbestände, echte Gerätekopplung,
Prüftermine, Zählerstände und Bankabrechnung bleiben bei ihren Fachmodulen.
Register-, Preis-, Karten- und Tankstellenverzeichnis-APIs sind kein notwendiger V1-Bestandteil.

## 2. Fachliche Grundstruktur

- Eine Organisation besitzt mehrere Stationen; eine Station gehört genau einer Organisation.
- Das Stationslimit ist serverseitig pro Organisation zu prüfen, auch bei Parallelaufrufen.
- Maximal 100 ist bestätigt; welche Zustände das Limit belegen, ist noch offen.
- Planungsvorschlag: Entwürfe, aktive und inaktive Stationen belegen Plätze;
  archivierte nicht, haben aber keinen operativen Zugriff und keine Neuanlagen unter sich.
  Wiederherstellung prüft das Limit erneut. Keine unbegrenzte Archivierung als Produktversprechen.
- Stations-ID bleibt stabil bei Umbenennung, Adressänderung oder Deaktivierung.
- Interne Fremdschlüssel nicht an Namen, Kürzel oder Straße binden.
- Rechnungsadresse, Bankverbindung und Mandat nur am zentralen Partnerkonto.
- Eine Station kann mehrere Leitungen haben, eine Leitung mehrere Stationen.
- Neue Station erzeugt keine automatische Berechtigung für bestehende Stationsleitungen.

## 3. Drei getrennte Statusachsen

### Betriebsstatus

| Zustand | Bedeutung | Vorgeschlagene Nutzung |
|---|---|---|
| Entwurf | Angelegt, noch nicht für Betrieb freigegeben | Stammdaten vorbereiten; keine operativen neuen Buchungen. |
| Aktiv | Für erlaubte Betriebsabläufe freigegeben | Fachmodule nach Rechten, Abo und Modulfreigabe nutzbar. |
| Inaktiv | Vorübergehend pausiert | Neue operative Vorgänge gesperrt; Historie berechtigt lesbar. |
| Archiviert | Dauerhaft aus laufender Übersicht genommen | Keine operative Nutzung; Historie/gezielte Wiederherstellung. |

### Einrichtungsfortschritt

Beispielsweise Pflichtangaben vollständig, Öffnungszeiten erfasst, Leitung zugewiesen,
Artikelstamm eingerichtet, Geräte gekoppelt. Nicht mit Betriebsstatus verwechseln.
Eine aktive Station kann ein unvollständiges optionales Profil haben.
„Keine Leitung“, „keine Geräte“ oder „keine Artikel“ sind keine automatische Stilllegung.

### Nutzungsberechtigung

Trial/Abo/Modulfreigabe ist eine separate, organisationsbezogene Achse.
Eine Stationspause darf nicht Trial verlängern oder Abo automatisch ändern.
Nach Ende der Organisationstestphase ist „Station aktiv“ allein keine Nutzungserlaubnis.
Limit-/Tarif-/Abrechnungsfolgen einer Archivierung sind nicht entschieden.

## 4. Feldkatalog

| Feld | Pflicht / Phase | Validierung und Zweck |
|---|---|---|
| Stationsname | Pflicht ab Entwurf | Verständliche Bezeichnung, trimmen, Länge festlegen; Name nicht als globale ID. |
| Stationskürzel | Optional, Vorschlag | Innerhalb Organisation eindeutig, normierte Groß-/Kleinschreibung; keine personenbezogene Kennung. |
| Straße/Hausnummer | Vor Aktivierung; adressabhängige Fälle berücksichtigen | Vollständige Standortanschrift; keinen deutschen Regex für alle Länder erzwingen. |
| PLZ/Ort | Vor Aktivierung, landesabhängig | PLZ als Text; führende Nullen erhalten; Ort nicht aus PLZ erraten. |
| Land | Vor Aktivierung | Definierter Länderkatalog; Deutschland ist Vorschlag als Vorgabe, kein V1-Länderumfang beschlossen. |
| Region/Bundesland | Falls für regionale Kalender nötig | Manuell bestätigte Auswahl, Feiertagsfunktion separat freigeben. |
| Marke | Optional | Katalogreferenz und gegebenenfalls freie Angabe; keine behauptete Markenanbindung. |
| Stationstelefon | Optional | Für geschäftliche Stationskommunikation; private Nummer nicht erforderlich. |
| Stations-E-Mail | Optional | Kontaktadresse, keine automatische Anmeldung oder Empfängerberechtigung. |
| Externe Standortnummer | Optional, nur bei belegtem Bedarf | Darf nicht mit interner ID/Rechnungsnummer verwechselt werden. |
| Koordinaten | Optional/später | Keine automatische Ortung; manuell/Quelle bestätigt; Anschrift bleibt führend. |
| Öffnungszeiten | Optional für Aktivierung, nötig für jeweilige Planungsautomatik | Unbekannt ≠ geschlossen; Intervalle/Ausnahmen getrennt. |
| Leitung | Optional für Aktivierung | Bestehender Zugang mit erlaubter Stationsrolle oder vorbereitete Einladung. |
| Ausstattung/Services | Optional | Strukturierte Liste; keine sensiblen Zugangscodes in Freitext. |
| Kraftstoffsorten/Zapfpunkte | Optional; Fachmodul kann Voraussetzungen verlangen | Aus Katalog, stabil referenziert, Einheiten/Zahl eindeutig. |
| Zeitzone | Sichtbar, vorgeschlagener V1-Wert aus Organisation | Keine stillschweigende stationsweise Überschreibung. |
| Interne Notiz | Optional, zweckgebunden | Keine Bank-, Gesundheits-, Ausweis- oder Sicherheitsgeheimnisse. |

Grenzlängen und tatsächlich zulässige Länder beim Feldschema festlegen und erklären,
nicht aus Beispieldaten ableiten. Keine externen Bestandsdaten ohne Bestätigung übernehmen.

## 5. Übersicht – Bildschirm A

- Überschrift, Anzahl sichtbarer Stationen, „Station anlegen“ nur mit Recht und Platz.
- Suchfeld für Name, Kürzel, Ort; Statusfilter, später Markenfilter falls nötig.
- Standard: aktive Stationen und relevante Entwürfe/inaktive; Archiv eigener Filter.
- Statuszählung bezieht sich auf denselben autorisierten Organisationsumfang.
- Tabelle/Karten: Name/Kürzel, Ort, Leitungen zusammengefasst, Betriebsstatus,
  Einrichtungsbedarf und Öffnen-Aktion.
- Lange Leitungslisten als Anzahl plus Detail, nicht sämtliche E-Mail-Adressen.
- Keine Umsatz-/Personal-/Kassenkennzahlen ohne passende Fachrechte laden.
- Bei bis 100 Stationen Suche, Sortierung und Paginierung statt riesiger Detailansicht.
- Listenstatus, Suche ohne Treffer, technische Fehler und fehlende Rechte unterscheiden.
- Karte/Zeile ist kein automatischer Wechsel der globalen Station ohne klaren Hinweis.
  Ein Profil darf zunächst angesehen werden; Wechsel in den Arbeitskontext ausdrücklich anbieten.
- Aktuelle Filter nach Rückkehr erhalten; Archiv nicht durch Suche unbemerkt offenlegen.

## 6. Station anlegen – Bildschirm B

1. Name und Standortadresse eingeben, Organisation fest sichtbar.
2. Optional Kürzel, Marke, geschäftliche Kontakte; restliche Felder später.
3. Als Entwurf speichern, dann Profil ergänzen oder gezielt aktivieren.
4. Aktivierung prüft Mindestanschrift, Recht, Limit und Nutzungsberechtigung erneut.

Ähnliche Name-/Adresskombinationen als Duplikatverdacht zeigen. Keine automatische
Zusammenführung und keine harte Sperre allein wegen gleicher Anschrift.
Import/Serienanlage nicht V1 versprechen; späterer Import muss Limit, Vorschau,
Zeilenfehler und idempotente Übernahme beachten.
Wiederholter Abschluss erzeugt keine zweite Station; Parallelaufrufe gegen Limit absichern.
Fehler während Speichern verliert nicht die gesamte Eingabe. Nicht vorgesehene
personenbezogene Daten in URL oder Browserdauerablage vermeiden.

## 7. Stationsprofil – Bildschirm C

Kopf: Name, Kürzel, Anschrift, Betriebsstatus, berechtigtes Verwaltungsmenü.
Vorgeschlagene Reiter:

1. Übersicht: Zusammenfassung und nächste tatsächlich erforderliche Aufgaben.
2. Stammdaten: Anschrift/Kontakte/Marke.
3. Öffnungszeiten: Wochenplan und Ausnahmen.
4. Team & Zugänge: sichtbare Zuordnungen, Verweis auf zuständiges Zugangsmodul.
5. Ausstattung: Services, Kraftstoffe, Zapfpunkte nach aktivierter Fachlichkeit.
6. Geräte: berechtigte Referenzen/Verbindungsstatus aus späterem Gerätemodul.

Module ohne Umsetzung als solche kennzeichnen oder Reiter ausblenden; keine leeren
funktionslosen Schaltflächen als fertige Integration darstellen.
Keine Bankdaten, Mandate oder Rechnungsempfänger in das Stationsformular kopieren.
Keine gemeinsame allgemeine „Stations-E-Mail“ als geteilter Benutzerzugang.

## 8. Öffnungszeiten – fachlich präzise

Reguläre Woche hat für jeden Wochentag ausdrücklich einen Modus:
- Unbekannt/nicht erfasst.
- Geschlossen.
- Ein oder mehrere Zeitfenster.
- 24 Stunden geöffnet.

Zeitfenster als lokale Uhrzeiten in der wirksamen Zeitzone interpretieren.
Mehrere Intervalle für geteilte Öffnung ermöglichen, Überlappungen ablehnen.
Lücken sind Schließzeiten, nicht automatisch durchgehend geöffnet.
00:00–00:00 nicht still als 24 Stunden deuten; expliziten 24h-Modus nutzen.
Übernachtöffnung z. B. Mo 22:00 bis Di 02:00 ausdrücklich mit Folgetagsmarkierung;
Normalisierung in Intervalle mit Ursprungstag, Überschneidung am Folgetag prüfen.
Erfasste Zeiten nicht beim Wechsel zwischen unbekannt/geschlossen/24h unbemerkt verlieren.

Ausnahmen an konkretem Datum ersetzen den regulären Plan dieses Datums vollständig.
Sie können geschlossen, 24h oder mehrere Zeitfenster sein; Grund optional, keine
Personaldaten erforderlich. Eindeutige Regel pro Datum; doppelte Ausnahmen bearbeiten
statt eine zufällige Rangfolge erzeugen. Vorschau des wirksamen Kalendertags zeigen.
Übernachtintervalle am Rand einer Ausnahme ausdrücklich abstimmen: vorgeschlagene
Regel ist Aufteilung nach lokalem Kalendertag; Ausnahme bestimmt sämtliche Zeitteile
des betreffenden Tages, auch solche aus der regulären Vorabendöffnung.

Priorität: konkrete Datumsausnahme > reguläre Woche; unbekannter Tag bleibt unbekannt.
Feiertag allein bedeutet weder geöffnet noch geschlossen. Automatische regionale
Feiertagsregeln/Verzeichnisimporte erst bei eigener Entscheidung/Quelle; keine Rechtsberatung
oder automatische Schlussfolgerung aus Feiertagsrecht in diesem Modul.

Zeitzone sichtbar; Vorschlag V1 erbt Station die Organisationszeitzone. Ein Wechsel dieser
Zeitzone ist ein eigener organisationsweiter Vorgang mit Wirkungsprüfung, kein Nebenfeld.
Kalender-/Uhrzeitänderungen dürfen historische Ereigniszeitpunkte nicht neu interpretieren.
Sommer-/Winterzeit mit Zeitlücken und doppelten Uhrzeiten für Planableitung berücksichtigen;
24h Öffnung bedeutet nicht automatisch 24 geleistete Arbeitsstunden an Umstellungstagen.

Öffnungszeiten dienen als Planungsgrundlage, sind keine Mitarbeiterverfügbarkeit und
keine Arbeitszeitregel. Änderungen veröffentlichen/ändern keine bestehenden Schichten
automatisch. Betroffene zukünftige Planungen als Hinweis, keine stillen Umbuchungen.
Gültig-ab-Versionierung als Vorschlag: neue Regeln gelten ab explizitem Datum;
Historie und Vorversion bleiben nachvollziehbar, keine rückwirkende Änderung gebuchter Vorgänge.
V1-Einstieg und Umfang einer Vorausplanung mit Benutzer bestätigen.

## 9. Team, Ausstattung und Geräte – Systemgrenzen

Team-Zuordnungen stammen aus Modul Team & Zugänge, kein zweites Rollenmodell.
Ein offener Einladungslink ist noch keine aktive Leitung. Relevanten Zustand zeigen.
„Leitung fehlt“ ist Einrichtungsbedarf, keine Pflicht zu einer externen Einladung.
Inhaber kann eine Station selbst betreuen, ohne zusätzliche Personalakte anzulegen.

Services wie Shop/Waschanlage sowie gepflegte Kraftstoffe/Zapfpunkte sind optional.
Fachmodul kann vor einer konkreten Aktion Voraussetzungen erklären, aber fehlende
Zapfpunktzahl nicht mit null Zapfpunkten gleichsetzen. In alten Vorgängen referenzierte
Sorten/Objekte deaktivieren, nicht durch harte Löschung unlesbar machen.

Geräte gehören zur Station; Kopplung/Tokens und Druckstellen sind eigenständige Module.
Hier nur Rechte-geprüfte Übersicht/Navigation; keine Tokens, NFC-Geheimnisse oder PINs anzeigen.
Eine Stammdatenänderung koppelt keine Geräte um. Umzug eines Geräts zwischen Stationen
verlangt gesonderten Ablauf. Inaktive Station muss operativen Gerätezugriff serverseitig sperren.

## 10. Rechtevorschlag

| Aktion | Organisationsinhaber | Zentrale Verwaltung | Stationsleitung |
|---|---|---|---|
| Station sehen | Organisation | Nur freigegebener Umfang | Zugewiesene Stationen |
| Anlegen | Ja, innerhalb Limit | Explizites zentrales Recht | Nein |
| Name/Adresse/Marke ändern | Ja | Explizites Recht | Standardmäßig nein; Änderungsbedarf melden |
| Geschäfts-Kontakt ändern | Ja | Explizites Recht | Optional eigenes Recht, noch zu bestätigen |
| Öffnungszeiten ändern | Ja, passendes Fachrecht | Explizites Recht | Optional eigenes Recht, noch zu bestätigen |
| Leitungen zuweisen | Passendes Benutzerverwaltungsrecht | Explizite Delegation | Standardmäßig nein |
| Aktivieren/pausieren/archivieren | Ja, gesicherter Ablauf | Explizites Recht | Nein |
| Ausstattung ändern | Passendes Fachrecht | Passendes Fachrecht | Optional zugewiesenes Fachrecht |
| Geräte/Token verwalten | Separates Geräterecht | Separates Geräterecht | Nicht automatisch |
| Rechnung/SEPA ändern | Zentral, nicht im Stationsprofil | Separates Recht | Nein |

Rechte für Stammdaten, Betrieb, Öffnungszeiten, Zuordnungen und sensible Administration
nicht zu einem undifferenzierten „Station bearbeiten“ bündeln.
Weder UUID noch ausgeblendeter Button ersetzt serverseitige Prüfung auf allen Endpunkten.
Änderungshistorie nur für Berechtigte; Personennamen/Änderungswerte datensparsam halten.

## 11. Pause, Archivierung, Wiederherstellung

Vorschlag V1: keine automatische zeitgesteuerte Stilllegung. Bewusste Aktion mit Vorschau.
Vor Pausierung/Archivierung prüfen und zeigen:
- Laufende Kassenschichten, unbestätigte Einwürfe/Übertragungen.
- Offene Druckaufträge, gekoppelte Geräte und noch nicht synchronisierte Vorgänge.
- Zukünftige veröffentlichte Schichten, offene Anträge/Störungen/Fristvorgänge.
- Aktive Zuordnungen und Einladungen.

Wirkungsmatrix pro Fachmodul vor Umsetzung konkretisieren. Kritische laufende Vorgänge
müssen vorher abgeschlossen oder über einen ausdrücklich berechtigten Nachbearbeitungsweg
gesichert werden; weder verwerfen noch unbegrenzt still blockieren.
Offline-Gerät kann noch Daten halten: Aktivierungsstatus beim Serverempfang erneut prüfen,
Originalvorgang erhalten und nötigenfalls in nachvollziehbare Nachbearbeitung überführen.
Keine falsche Erfolgsbestätigung für zurückgewiesene Vorgänge.

Pausierung sperrt neue Operationen, erhält Stammdaten/Historie; ändert keine Rechnung/Abo.
Archivierung nimmt Station aus Standardlisten, löscht keine Buchungen/Personalhistorie.
Einladung/Zuordnung wird nicht ungeprüft bei Wiederherstellung reaktiviert: vorhandene
Zuweisungen sichtbar prüfen, Einladungen ggf. neu ausstellen, Gerätefreigaben separat prüfen.
Wiederherstellung prüft Rechte, Limit, Abo und Abhängigkeiten erneut; keine Trialverlängerung.
Vor endgültigem Löschen eigenes Datenschutz-/Aufbewahrungsverfahren planen.
„Archiviert“ heißt nicht datenschutzrechtlich gelöscht. Keine pauschale Sofortlöschung in V1.

## 12. Änderungen, Historie und Sicherheit

Audit: Akteur, Station, Aktion, Zeit, minimal nötige geänderte Felder, optionaler Grund.
Keine Geheimnisse oder komplette unsanitierte Formulare protokollieren.
Geschäftlich historische Werte in Fachvorgängen bei Bedarf als Snapshot erhalten;
Stationsumbenennung darf alten gedruckten Bericht nicht still ändern.
Parallelbearbeitung erkennen (Versionskonflikt); keine fremden Änderungen überschreiben.
Organisation beim Anlegen aus gesichertem Kontext, nicht frei aus Request übernehmen.
Keine ungefragten externen Adressabfragen/Geolokalisierung oder Karten-Tracker.
Öffnungszeiten/geschäftliche Kontaktdaten nicht automatisch öffentlich veröffentlichen.
Datenschutz-/Aufbewahrungskonzept aus dem bestehenden Leitfaden anwenden und konkretisieren.

## 13. Konzeptionelles Datenmodell

| Objekt | Zweck |
|---|---|
| Station | organization_id, stabile ID, Name/Kürzel, Anschrift/Kontakt, Marke, Betriebsstatus, Version. |
| StationProfileCompleteness | Aus Daten abgeleitete Hinweise; keine zweite manuell widersprüchliche Wahrheit. |
| OpeningHoursVersion | Station, gültig ab, Wochenregeln, Herkunft, Änderungszeit; effektive Zeitzone. |
| WeeklyOpeningInterval | Wochentag, lokaler Beginn/Ende, Folgetagsbezug; 24h/geschlossen/unbekannt explizit. |
| OpeningDateException | Station, lokales Datum, Modus und Intervalle, ersetzt regulären Tagesplan. |
| StationLifecycleEvent | Pause/Aktivierung/Archiv/Wiederherstellung, Akteur, Wirkung und Grund. |
| StationRoleAssignment | Bestehende Referenz aus Team-Modul, nicht neu duplizieren. |
| StationService/FuelType/PumpPoint | Optionale strukturierte Ausstattung bzw. Referenzen. |
| Device/PrintTarget | Fremdmodulreferenz mit Stationsbindung, keine Token im Profil. |
| StationAuditEvent | Datenschutzgerecht minimierte Änderungshistorie. |

Nicht als fertiges Datenbankschema verstehen. Altmodelle bei späterem Implementierungsauftrag
abgleichen; keine Migrationen oder parallelen Stammdatenmodelle jetzt anlegen.

## 14. Abnahmefälle

| Fall | Erwartetes Verhalten |
|---|---|
| Organisationen A/B | Keine fremden Stationen in Liste/Suche/Zähler/API/Dateien/Jobs. |
| Leitung Station 1 | Station 2 weder lesbar noch veränderbar. |
| Neue Station | Keine automatische Leitungserweiterung oder Einladung. |
| 100 Stationen | Weitere Anlage auch parallel/über Import verweigert; Entwurfs-/Archivregel sichtbar. |
| Archiv wiederherstellen bei Limit | Kein Limitumgehen; verständlicher Hinweis. |
| Gleiche Adresse/Namen | Duplikatwarnung, keine ungewollte Zusammenführung. |
| Anschrift ändern | Rechnungsprofil, Mandat und alte Vorgangssnapshots unverändert. |
| Aktiv mit unvollständigem Optionalprofil | Als aktiv plus konkrete Einrichtungsbedarfe darstellbar. |
| Mo–Fr 06–22 | Regel pro Tag korrekt ableiten, Sammelbearbeitung erklärt. |
| Zwei Tagesintervalle | Keine Schließlücke überbrücken; Überschneidung verweigert. |
| 24h vs unbekannt vs geschlossen | Eindeutig und unterschiedlich. |
| Mo 22–Di 02, Di Ausnahme | Ausnahme des lokalen Dienstags gilt auch für Zeitteil 00–02. |
| Doppelte Datumsausnahme | Nicht still zufällig überschreiben. |
| Sommer-/Winterzeit | Öffnungskalender korrekt; nicht automatisch Arbeitsstunden berechnen. |
| Wochenregel ändern | Keine stillen Änderungen veröffentlichter Schichten oder alter Buchungen. |
| Pause mit laufender Kasse/Offline-Daten | Geordnete Blockade oder expliziter Nachbearbeitungsweg, kein Datenverlust. |
| Trial abgelaufen | Aktivstatus oder Restore hebt Sperre nicht auf. |
| Team-Einladung offen | Keine aktive Stationsleitung vortäuschen. |
| Geräte deaktivierter Station | Operativer Zugriff serverseitig gesperrt; Historie erhalten. |
| Gleichzeitige Bearbeitung | Versionskonflikt statt stiller Datenüberschreibung. |
| Mobil/Tastatur | Labels/Fokus/Fehler/Intervalle bedienbar, keine Nur-Farb-Zustände. |

## 15. Kleine spätere Umsetzungsstufen

1. Rechte, Limitzählung, Länder-/Zeitzonenmodell und Zustandsübergänge bestätigen.
2. Stationsliste, sichere Detailansicht, Such-/Filter-/Leerezustände.
3. Anlage als Entwurf, Stammdaten und minimale Aktivierung.
4. Reguläre Öffnungszeiten, Übernachtfälle und Datumsausnahmen mit Vorschau.
5. Verweise zu Team/Ausstattung/Geräten; keine heimliche Parallelverwaltung.
6. Pause/Archiv/Restore mit Wirkungsmatrix und gesicherten Nachbearbeitungswegen.
7. Historie, Berechtigungstests, Parallelfälle, mobile und barrierearme Bedienung.

**Keine dieser Stufen ist umgesetzt oder zur Programmierung freigegeben.**

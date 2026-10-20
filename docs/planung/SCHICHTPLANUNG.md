# Schichtplanung – Fachspezifikation

Stand: 20.10.2026 · Planungsentwurf, keine Implementierung.
Benutzer hat Fortsetzung mit Schichtplanung, Prompt, Mockup und übertragbarer
GitHub-Dokumentation bestätigt. Einzelregeln dieser Spezifikation sind Vorschläge,
soweit sie noch nicht ausdrücklich bestätigt wurden.

## 1. Ziel und Grenzen

Stationsleitung/Planungsverantwortliche erstellen nachvollziehbare Dienstpläne,
prüfen Besetzung und Konflikte und veröffentlichen eine feste Version.
Mitarbeiter sehen ihre eigenen veröffentlichten Einsätze über separat freigegebenen Zugang.
Ein Organisationsinhaber kann mehrere Stationen überblicken, ohne in einem unlesbaren
100-Stationen-Kalender arbeiten zu müssen.

Planung ist weder tatsächliche Zeiterfassung noch Lohnabrechnung, Abwesenheitsgenehmigung,
Vertragsänderung oder Gehaltszahlung. DATEV-Stammdaten bleiben getrennt; geplante Stunden
dürfen nicht ungeprüft als tatsächlich geleistete Arbeitszeit exportiert werden.
V1 schlägt Mitarbeiter nicht vollautomatisch verbindlich zu; Vorschläge immer prüfen/bestätigen.

## 2. Abhängigkeiten

- Organisation, Nutzungsberechtigung und aktive Station aus Partner-/Stationsmodulen.
- Wirksame Öffnungszeiten inklusive Ausnahmen und Zeitzone als Planungsgrundlage,
  nicht als gesetzliche Einsatzberechtigung oder zwingende Personalbesetzung.
- Beschäftigungsabschnitt mit Eintritt/Austritt, gültigen Einsatzstationen, nötigen
  Arbeitszeitdaten und gegebenenfalls Qualifikationen aus Mitarbeiterverwaltung.
- Persönlicher Benutzerzugang nur für Mitarbeiter-Selbstansicht/Anfragen; Personalakte
  allein darf keinen Login erzeugen. Mitarbeiter ohne Login bleiben planbar.
- Verfügbarkeiten und freigegebene Abwesenheitsintervalle über klare Datenverträge.
- Regeln aus versionierter Regelkonfiguration; keine willkürlichen Grenzwerte im UI.
- Unvollständige steuerliche Angaben blockieren nicht automatisch Planung;
  fehlende erforderliche Planungs-/Regeldaten dürfen aber nicht als geprüft gelten.

## 3. Begriffe

| Objekt | Bedeutung |
|---|---|
| Bereich | Arbeitsbereich z. B. Shop/Kasse/Waschanlage, keine Zugriffsrolle. |
| Qualifikation | Fachliche Einsatzvoraussetzung mit Gültigkeit, keine Benutzerberechtigung. |
| Schichtvorlage | Wiederverwendbare Zeiten/Bedarf; enthält keine festen Mitarbeiter. |
| Schicht | Konkrete Zeitspanne an Station/Bereich mit Personalbedarf. |
| Besetzungsposition | Ein benötigter Platz mit ggf. Qualifikationsanforderung. |
| Zuweisung | Mitarbeiterbesetzung eines Platzes mit individuellen Pausen und Prüfstand. |
| Planwoche | Bearbeitungs-/Veröffentlichungseinheit je Station, keine Grenze der Regelprüfung. |
| Veröffentlichung | Unveränderlicher sichtbarer Snapshot, nicht bloß ein Boolean am Entwurf. |
| Wunsch/Verfügbarkeit | Präferenz oder erklärte Zeitlage; keine Abwesenheitsgenehmigung. |
| Konflikt | Belegbare Regelabweichung bzw. fehlende Prüfgrundlage mit Schwere/Quelle. |

## 4. Vorlagen und Besetzungsbedarf

Vorlage: Name/Kürzel, Bereich, örtlicher Beginn/Ende mit Folgetag, optionale Wochentage,
Positionsanzahl, nötige Qualifikationen, Pausenvorgaben, Gültigkeit und Status.
Vorlage „Früh/Spät/Nacht“ frei benennen; Farbe nur ergänzend, nie einziges Erkennungsmerkmal.
Versionierung: spätere Vorlagenänderung verändert bereits erzeugte Schichten nicht still.
Vorlagen deaktivieren statt historische Referenzen zu zerstören.

„Aus Vorlagen füllen“ zeigt Zeitraum/Quelle/Vorschau, ergänzt kontrolliert und erzeugt
bei Wiederholung keine stillen Doppelungen. Bestehende Planung nicht ohne bewusste Auswahl
ersetzen; veröffentlichte Versionen niemals überschreiben. Kopieren der Vorwoche ist
eigene Vorschau, prüft neue Daten/Abwesenheiten/Vertragsstände erneut.

Öffnungszeiten können Vorschläge für Vorlagen liefern. Arbeit außerhalb der Kundenöffnung
z. B. Vorbereitung/Reinigung nicht pauschal verbieten, sondern nachvollziehbaren Bereich/Zweck
und nötige Freigabe planen. Besetzung während Pausen zeitintervallgenau prüfen;
„1 Person zugewiesen“ bedeutet nicht durchgehend 1 Person anwesend.

## 5. Schicht anlegen/bearbeiten

Erforderlich: Station, lokales Start-/Enddatum und Uhrzeit, wirksame Zeitzone, Bereich,
Positionsbedarf. Ein Mitarbeiter kann später zugeordnet werden: offene Schicht ist gültiger Entwurf.
Ende nach Beginn, Folgetag ausdrücklich anzeigen; 00:00 nicht automatisch als ganzer Tag.
Pausen als zeitlich geplante Intervalle mit sinnvoller Lage; nur Summenminuten reichen
nicht für jede Regel-/Besetzungsprüfung. Bezahlt/unbezahlt getrennt von gesetzlicher Ruhepause.
Keine automatische Pause als tatsächlich genommen verbuchen.

Arbeitsdauer, Anwesenheitsspanne, Netto-Planarbeitszeit und bezahlte Zeit unterscheiden;
für jede Zahl Definition anzeigen. Nicht auf volle/halbe Stunden runden.
Geld-/Minijobprognose braucht eigene zulässige Quelldaten und darf keine Gehaltsrechte umgehen.
Notizen nur betriebliche Übergabehinweise, keine Diagnosen, Steuerdaten oder Personaldetails.

## 6. Zeitmodell und kalenderübergreifende Prüfung

Lokale Eingabe mit IANA-Zeitzone und eindeutiger Auflösung; intern konkrete Zeitpunkte
und beabsichtigte lokale Darstellung nachvollziehbar speichern. Nicht nur „06:00–14:00“.
Sommerzeitlücke nicht still verschieben; doppelte Uhrzeit erfordert eindeutige Auswahl.
24h-Öffnung kann an Zeitumstellungstagen eine andere reale Dauer haben.
Keine Rückinterpretation alter Einsätze bei späterem Organisationszeitzonenwechsel.

Halboffene Intervalle [Beginn, Ende): direkt angrenzende Zuweisungen überlappen nicht,
können aber andere Regeln z. B. Ruhe-/Pausen-/Tagesgrenzen verletzen.
Prüfzeitraum umfasst erforderliche Nachbarwochen, Vertragsversionen, Kalendermonate,
Ausgleichszeiträume und ggf. Jahresgrenzen. Sonntag/Montag oder Mitternacht setzen
Arbeitszeit-/Ruhezeitberechnungen nicht künstlich zurück.
Mehrere Stationen derselben Person gemeinsam prüfen; keine Schichten durch neue
Personalnummer oder Wechsel des Standorts aus den Summen verlieren.
Mehrarbeitgeberdaten nur soweit bekannt/zulässig, Unvollständigkeit kennzeichnen;
keine fremden Arbeitgeberdaten automatisch abrufen oder volle Prüfdeckung behaupten.
Fahr-/Wegezeiten zwischen Einsatzorten als offener Fachfall, nicht still null setzen.

## 7. Ansichten

### A – Wochenplan einer Station

- Kopf mit Station, Woche/Datumsbereich, Zeitzone, Entwurf/Veröffentlichungsstand.
- Wechsel Woche/Monat, Datum, Bereich, veröffentlichte Version vs. aktueller Entwurf.
- Kalender nach Tagen/Bereichen; Uhrzeit, Platzbelegung, Namen und konkrete Prüfhinweise.
- Kennzahlen Schichten/offene Plätze/blockierende Konflikte/unprüfbare Regeln klar definiert.
- Panel Mitarbeiter zuordnen mit erlaubten Einsatzkandidaten, Verfügbarkeits-/Sollstundenhinweis,
  nicht privater Vergütung oder vollständiger Personalakte.
- Ziehen UND barrierearme Auswahldialoge; gleicher Serverprüfweg für jede Aktion.
- Konfliktpanel mit nächster Handlung, Quelle, Zeitpunkt, Regelversion und betroffenen Intervallen.
- Fehlende Qualifikation/Zuordnung erklären, keine automatische Rechtevergabe aus Drag-and-drop.
- Mobile alternative Tages-/Listenansicht statt sieben unbedienbar schmaler Spalten.

### B – Monats-/Organisationsübersicht

Monat zeigt verdichtete Schichten/Bedarf, Detail öffnet Tages-/Wochenansicht.
Organisationssicht zeigt Stationen mit Planstatus, offenen Plätzen, Veröffentlichungsbedarf;
Filter/Paginierung für 100 Standorte, kein gleichzeitiges Laden aller Personen/Schichten.
Nicht berechtigte Stationen erscheinen weder in Zähler noch Auswahl/Export.

### C – Prüfen und veröffentlichen

Station/Woche, Entwurfsversion, Prüfzeitpunkt, Blocker, ungeklärte Prüfungen, Warnungen,
offene Plätze, Änderungen zur letzten Version und betroffene Empfänger darstellen.
Explizite Bestätigung nur zulässiger organisatorischer Restpunkte; kein Universal-Override.
Ein Veröffentlichungsschritt erzeugt festen Snapshot und Benachrichtigungsaufträge.

### D – Eigener Plan

Nur veröffentlichte eigene Zuweisungen, Station/Anschrift/Zeit/Pausen/Version und
verständliche Änderungen seit vorherigem Stand. Keine fremden Mitarbeiterkontaktdaten,
Gesundheitsgründe oder privaten Lohnwerte. Teamplan nur bei eigener Entscheidung/Recht.
Offline-Lesen des letzten Plans allenfalls spätere eigene Funktion: Stand/Veraltetheit
klar kennzeichnen; keine Offline-Übernahme/Tausch als bestätigt darstellen.
Kenntnisnahme getrennt von Zustimmung/Vertragsannahme; keine Pflichtsignatur vortäuschen.

## 8. Regelprüfung – Ergebnisse und Änderbarkeit

Jede Regel hat stabile ID, Version/Gültigkeit, Quelle, Eingabeabhängigkeiten,
Prüfhorizont, Schweregrad und verständliche Abhilfe.
Ergebnisse: bestanden / blockierend / Warnung / Hinweis / nicht prüfbar / nicht anwendbar.
Ein Zeitablauf oder fehlender Lohnwert ist niemals automatisch „bestanden“.

| Regelgruppe | Beispiel | Vorgeschlagene Folge |
|---|---|---|
| Datenintegrität | Ende vor Beginn, doppelte Position | Speichern/Zuordnen verweigern. |
| Identität/Umfang | Fremde Organisation, Station nicht freigegeben, außerhalb Beschäftigung | Zuweisung blockieren. |
| Überlappung | Dieselbe Person gleichzeitig an zwei Stationen | Verbindliche Besetzung blockieren. |
| Abwesenheit | Genehmigtes frei oder festgestellte Nichtverfügbarkeit | Blockieren bzw. nach bestätigtem Fachtyp behandeln; kein stilles Übergehen. |
| Qualifikation | Nötige aktuelle Qualifikation fehlt | Blockieren, keine Benutzerrolle als Ersatz. |
| Arbeitszeit/Pause/Ruhe | Wirksame gesetzliche/vertragliche Regeln | Nach geprüftem Regelprofil blockieren; Ausnahme nur mit belegter Grundlage. |
| Fehlende Grundlage | Alter/Vertragszeiten/Regelprofil unklar | Nicht prüfbar; notwendige Prüfung vor Veröffentlichung klären. |
| Sollstunden/Präferenz | Unterplanung oder Wunsch nicht erfüllt | Konfigurierbare organisatorische Warnung. |
| Offene Besetzung | Ein Platz unbesetzt | Sichtbar; bewusste Veröffentlichung nur nach bestätigter Betriebsregel. |
| Entgeltprognose | Minijobprognose unvollständig/auffällig | Fachhinweis, keine automatische sozialrechtliche Einstufung. |

Firmen dürfen interne Warnschwellen ändern, aber Gesetze nicht durch UI-Override außer Kraft setzen.
Begründung allein legalisiert keine Überschreitung. Abweichende Tarif-/Ausnahmeregel
braucht passende Geltung/Nachweis/Gültigkeit und Fachprüfung.
Keine pauschale Tankstellen-Ausnahme, keine unbegrenzte „trotzdem veröffentlichen“-Schaltfläche.
Rechts-/Quellenorientierung und Grenzwerte als recherchierte Beispiele im gesonderten Leitfaden.

## 9. Mindestumfang der Prüfgruppen

- Überlappung und Ruhe zu vorherigem/nachfolgendem Einsatz über Stations-/Wochenränder.
- Nettoarbeitszeit/Schichtspanne, Pausenlage/-dauer und Ausgleichszeiträume.
- Sonn-/Feiertagsbeschäftigung mit zutreffendem Regelprofil und Ersatzruhe, nicht allein Öffnungszeiten.
- Jugendliche/Ausbildung/Berufsschule mit geprüften alters-/statusbezogenen Regeln;
  keine Ableitung „Azubi = minderjährig“ und keine fehlende Geburt als automatisch erwachsen.
- Vertragsstunden und zulässige Vereinbarungen in gültigen Zeitabschnitten; keine rückwirkende Umrechnung.
- Minijob als Prognose mit Gültigkeitswerten/regelmäßigem Entgelt, keine starre
  universelle Maximalstundenzahl. Fehlende Lohnrechte nur Ergebnis im erlaubten Umfang,
  keine Rückrechnung aus offen sichtbaren Beträgen/Prozenten auf vertraulichen Stundenlohn.
- Mutterschutz/andere Schutzprofile nur als notwendige freigegebene Einsatzrestriktion
  aus zuständiger Personalstelle; keine Diagnosen im Plan oder automatisches Profiling.
- Externe Arbeitszeiten soweit sicher und zulässig vorliegend; sonst Prüfgrenze klar anzeigen.

Eine vollständige Rechts-/Abrechnungsgarantie wird nicht behauptet. Gesetzliche Regelprofile
vor echtem Einsatz durch zuständige Fachstelle bestätigen; Datenänderungen invalidieren Prüfergebnis.

## 10. Entwurf, Prüfung und Veröffentlichung

Entwurf kann unvollständige Planung enthalten; bindende Zuweisung/Veröffentlichung nur mit
erforderlicher Prüfung. Bereits veröffentlichte Woche bleibt während Bearbeitung als letzte
gültige Version sichtbar, neue Änderungen als unveröffentlichter Entwurf gekennzeichnet.

Veröffentlichungsablauf:
1. Rechte, Station, Organisation/Trial und aktuelle Entwurfsversion prüfen.
2. Abhängigkeiten (Personen, Verträge, Abwesenheiten, Zuordnungen, Regeln, Nachbarpläne) erfassen.
3. Serverseitig alle nötigen Prüfungen ausführen; Fehler/fehlende Pflichtprüfung blockieren.
4. Zulässige Warnungen/offene Plätze gegebenenfalls ausdrücklich bestätigen und protokollieren.
5. Unveränderliche Version, Zugehörigkeiten und Ereignisse atomar festhalten.
6. Benachrichtigungen nach erfolgreichem Commit über wiederholbare Warteschlange versenden.

Erneuter Klick erzeugt keine zweite Version/Doppelmail. Gleichzeitige Veröffentlichungen
an zwei Stationen mit derselben Person gegen Konfliktrennen absichern (Versions-/Sperrkonzept).
Zwischen Prüfung und Commit geänderte Daten verlangen neue Prüfung, kein altes grünes Ergebnis.
Empfänger nur tatsächlich betroffene freigegebene Benutzer; ohne Login kein Passwortmail
oder automatische Kontoeinladung. Mail nur Änderungshinweis/geschützter Link, nicht volle Personalliste.
Mailzustand ausstehend/übergeben/fehlgeschlagen, nicht automatisch gelesen/zugestellt.
Planveröffentlichung bleibt bei Mailfehler gültig; Versand sichtbar wiederholen.

## 11. Änderungen, Absage und Nachbearbeitung

Veröffentlichte Schicht nicht einfach löschen: neue Änderungsversion mit Grund, betroffenem
Zeitpunkt und Empfängern. Mitarbeiter sieht klar neu/geändert/abgesagt im eigenen Umfang.
Eine Änderung am Sonntag prüft auch Montag in anderer Woche/Station erneut.
Regel-/Abwesenheitsänderung nach Veröffentlichung als aktueller Konflikt/Todo melden,
nicht Historie umschreiben oder automatisch Mitarbeitereinsatz versetzen.
Historische Zuordnung als Referenz für spätere Ist-/Lohnprozesse erhalten; Korrekturen nachvollziehbar.
Station pausieren/archivieren zeigt zukünftige Pläne als Abhängigkeit (Stationsmodul).
Planpause oder Schichtabsage ist keine Kündigung, Abwesenheitsgenehmigung oder Gehaltsentscheidung.

## 12. Verfügbarkeit, Schichtangebote und Tausch – Ausbaustufe

V1: eigene Verfügbarkeit/Wünsche melden, berechtigte Planung entscheidet; Abwesenheitsmodul
liefert genehmigte Intervalle, Diagnosen/Gründe nicht im Kalender.
Anfrage ist keine verbindliche Änderung des veröffentlichten Plans.

Späterer Tauschprozess: Mitarbeiter bietet eigene zukünftige veröffentlichte Zuweisung an,
berechtigter geeigneter Kollege bewirbt sich bzw. wählt Gegenschicht, Leitung prüft erneut
Rechte/Qualifikation/Verfügbarkeit/Regeln und bestätigt neue Planversion.
Original bleibt bis Bestätigung verbindlicher Stand. Mehrere Bewerbungen erzeugen keine
doppelte Besetzung; Fristablauf, Absage, Rücknahme und inzwischen geänderter Plan berücksichtigt.
Keine offenen Angebote aller Organisationen und keine Preis-/Lohnangaben in Schichtbörse.
Echte Tauschausführung ist nicht Bestandteil der ersten Kernstufe.

## 13. Aushang und Kalender

Geschützter PDF-Aushang als spätere definierte Ausgabe desselben Veröffentlichungssnapshots,
mit Station, Zeitraum, Versionsstand, Generierungsdatum und nur nötigen Personendaten.
Kein vertraulicher Konflikt-/Abwesenheitsgrund oder Gehalt im Aushang.
Wer Aushang sehen darf, ist gesonderte organisatorische Datenschutzentscheidung.
Downloads mit aktueller Berechtigung, keine dauerhaften öffentlichen Freigabelinks.
Ein persönliches iCal-Abo ist zusätzliche Option mit widerrufbarem Geheimlink und nur eigenen
Schichten; Dritt-Kalenderverarbeitung offenlegen, kein Standard ohne bewusste Aktivierung.

## 14. Rechtevorschlag

| Aktion | Inhaber/zentrale Planung mit Recht | Stationsleitung | Mitarbeiter |
|---|---|---|---|
| Plan sehen | Erlaubter Umfang | Zugewiesene Stationen | Eigene veröffentlichte Einsätze |
| Vorlagen/Entwurf bearbeiten | Eigenes Planungsrecht | Eigenes Recht, zugewiesene Station | Nein |
| Personal zuordnen | Geeignete Beschäftigte im erlaubten Umfang | Nur gültige Einsatzzuordnung, kein Recht zur Erweiterung | Nein |
| Regelkonfiguration | Gesondertes zentrales Fachrecht | Keine beliebige Gesetzesüberschreibung | Nein |
| Veröffentlichen/absagen | Gesondertes Veröffentlichungsrecht | Nur explizit zugewiesen | Nein |
| Verfügbarkeit melden | Eigene soweit Beschäftigter | Eigene soweit Beschäftigter | Eigene |
| Tausch entscheiden | Gesondertes Recht | Gesondertes Recht | Antrag, keine automatische Umbesetzung |
| Gehalt/Minijobbeträge sehen | Separates Lohnrecht | Nicht aus Planungsrecht ableiten | Kein fremdes Gehalt |
| Export/Aushang | Eigenes Exportrecht | Nur erlaubte Station/Version | Eigene freigegebene Ausgabe |

Cross-Station-Prüfung darf intern Kollision erkennen, ohne Leitung die Namen/Details fremder
Station oder dortige Personalakte offenzulegen: z. B. „anderweitig eingeplant“ plus nötiges Intervall.
Feldminimierung serverseitig auch in Livewire/API, Suche, Exports, Jobs und Benachrichtigungen.
Planerrolle ist keine Mitarbeiter-/Lohnakte-Administration.

## 15. Konzeptionelles Datenmodell

PlanPeriod/PlanningDraft (Station, Woche, Revision), ShiftTemplateVersion,
Shift (Zeitpunkte, lokale Zeitzone, Bereich), StaffingPosition, ShiftAssignment,
PlannedBreak, QualificationRequirement, AvailabilityRequest, AbsenceIntervalReference,
RuleDefinition/RuleVersion, RuleEvaluation (Abhängigkeitsversionen, Quelle, Zustand),
PublishedPlanVersion/Snapshot, PlanChangeEvent, NotificationOutbox/DeliveryAttempt,
später ShiftOffer/ExchangeRequest und CalendarSubscription.
Bestehende Station/Mitarbeiter/Vertrags-/Rechtemodelle referenzieren, keine Duplikate.
Snapshot und Entwurfsdaten fachlich trennen, historischen Lohn-/Istbezug erhalten.
Keine fertigen Tabellen/Migrationen im Planungsmodus.

## 16. Abnahmefälle

| Fall | Erwartung |
|---|---|
| Vorlagen zweimal anwenden | Keine stillen Doppelungen/Überschreibung veröffentlichter Daten. |
| Zwei Stationen, gleiche Person | Gemeinsame Überschneidungs-/Ruheprüfung, begrenzte Sichtbarkeit. |
| Sonntagabend/Montagmorgen | Nachbarwoche wird geprüft, kein Reset an Wochen-/Monatsrand. |
| Übernacht/DST | Eindeutige lokale Eingabe, korrekte reale Dauer, kein stilles Verschieben. |
| Grenze der Pausenschwelle | Genau/knapp darüber nach gültiger Regel unterscheiden. |
| Zwei Teilpausen | Dauer/Lage nach Regel, Besetzungslücken sichtbar. |
| Minderjährig/Berufsschule | Passendes geprüftes Profil, keine Erwachsenenannahme bei Unklarheit. |
| Minijob/fehlende Vergütung | Keine universelle Stundenobergrenze/keine falsche grüne Prüfung. |
| Genehmigte Abwesenheit | Neuprüfung; Gründe nicht öffentlich, keine stillen Umbuchungen. |
| Veraltete Regelprüfung | Veröffentlichung verlangt aktuellen abhängigen Stand. |
| Gleichzeitige Publikation | Kein Konfliktrennen/keine doppelte Version/Doppelbesetzung. |
| Maildienst ausgefallen | Planversion besteht, Versandfehler sichtbar/retry ohne Doppelmail. |
| Offene Position | Offener Platz bleibt sichtbar; kein vollständiger Planstatus vortäuschen. |
| Fremder Entwurf | Nicht durch Mitarbeiter/ungewählte Station lesbar. |
| Tauschbewerbung | Original bleibt bis Freigabe; Race/Frist/Absage behandelt. |
| Plan kopieren/Vertrag geändert | Neue Vertrags-/Qualifikations-/Abwesenheitsstände geprüft. |
| Station inaktiv/Trialende | Keine Veröffentlichung als Umgehung der Sperre. |
| Planstunden/DATEV | Keine ungeprüfte Übernahme als geleistete/abgerechnete Stunden. |
| Keine Personal-Logins | Planung möglich, keine ungewollte Kontoanlage oder Mailpasswörter. |
| Mobil/Tastatur | Tagesliste und Auswahl statt reiner Drag-and-drop-Pflicht. |

## 17. Kleine spätere Umsetzungsschritte

1. Daten-/Regel-/Rechteverträge mit Stations-/Mitarbeiter-/Abwesenheitsmodul bestätigen.
2. Vorlagen und Stations-Wochenentwurf mit manueller Zuordnung/Zeiten/Pausen.
3. Reine Integritäts-/Konfliktprüfung einschließlich Zeitmodell/Stationsrändern.
4. Fachlich freigegebene versionierte Regeln mit fehlender Datenlage und Nachbarzeiträumen.
5. Prüfansicht, atomare Versionierung, Veröffentlichung und wiederholbarer Benachrichtigungsweg.
6. Eigene Mitarbeiteransicht und nachvollziehbare Planänderungen.
7. Monat/Organisation, geschützter Aushang und Verfügbarkeit.
8. Erst danach Tausch/Schichtbörse, persönliche Kalenderabos und gesonderte Ist-Anbindung.

Noch nichts programmiert oder als vollständig rechtlich geprüft freigegeben.

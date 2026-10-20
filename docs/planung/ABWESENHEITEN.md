# Abwesenheiten, Urlaub, Krankheit und Verfügbarkeit – Fachspezifikation

Stand: 20.10.2026 · Planungsentwurf, keine Implementierung.
Benutzerauftrag „weiter“ bezieht sich auf den vorgeschlagenen nächsten Baustein
Abwesenheiten als Grundlage der Schichtplanung. Detailregeln sind Vorschläge bis Bestätigung.
Quellen und Grenzen: `docs/leitfaeden/RECHERCHE-ABWESENHEITEN.md`.

## 1. Ziel und fachliche Trennung

Mitarbeiter melden Wünsche, beantragen Urlaub und melden Nichtverfügbarkeit;
berechtigte Verantwortliche entscheiden über Anträge, erfassen Tatsachen und klären
Nachweise. Der Planer bekommt nur nötige Einsatzrestriktionen, keine Gesundheitsakte.

Urlaubsantrag ≠ genehmigter Urlaub ≠ Wunschfrei ≠ Krankmeldung ≠ eAU-Nachweis ≠
Verfügbarkeit ≠ tatsächliche Zeiterfassung ≠ Lohnabrechnung.
Eine Krankmeldung ist keine Bitte um Erlaubnis krank zu sein.
Antragstellung ist keine Zustimmung; Antrag per Merlin ersetzt keine tatsächlich
erforderlichen unverzüglichen betrieblichen Meldewege oder externe Abrufverfahren.

## 2. Arten und Auswirkungen

| Art | Vorgang | Planungswirkung | Urlaubskonto |
|---|---|---|---|
| Erholungsurlaub | Antrag/Entscheidung | Genehmigt verhindert kollidierenden Arbeitseinsatz | Geprüfte Buchung nach gültigem Anspruchsprofil. |
| Wunschfrei | Präferenz, optional berücksichtigt | Vor Freigabe Hinweis; bindende Wirkung nur nach ausdrücklich definierter Regel | Kein Urlaubsabzug. |
| Verfügbarkeit | Eigene Zeitlagen/Präferenzen | Keine Beschäftigungs-/Sollstundenänderung; Gewicht/Verbindlichkeit klar | Kein Abzug. |
| Krankheit/Arbeitsunfähigkeit | Meldung/Erfassung/Nachweisklärung | Notwendige Nichtverfügbarkeit ab Meldung, nicht erst bei Nachweis | Kein pauschaler Urlaubsabzug. |
| Schulung/Berufsschule | Bestätigte anderweitige Verpflichtung | Nicht für reguläre Stationsschicht verfügbar; Arbeitszeitbeitrag ggf. gesondert | Nicht einfach Urlaub. |
| Unbezahlte Freistellung | Eigener Genehmigungs-/Vertragsprozess | Nach Freigabe Restriktion; Lohnfolgen nur zuständige Stelle | Kein automatischer Ersatz für negativen Urlaubssaldo. |
| Sonstige Freistellung | Konkreter freigegebener Fachtyp | Wirkung/Recht/Nachweise je Typ | Nur falls fachlich zutreffend, kein generischer Standardabzug. |

Sonderfälle wie Kind krank, Pflege, Beschäftigungsverbote, Elternzeit und andere
Schutzfälle brauchen eigene Profile/Rechte. Kein pauschaler Dropdown-Eintrag mit
identischem Genehmigungs-/Lohnverhalten und kein Diagnose-/Gesundheitsprofiling.
V1-Kern: Urlaub, Wunschfrei, Krankmeldung und Verfügbarkeit. Weitere Arten abgegrenzt planen.

## 3. Arbeitgeber, Person und Station

Abwesenheit/Urlaub gehören zum Beschäftigungsverhältnis beim rechtlichen Arbeitgeber,
nicht zu einem isolierten Stationskonto. Eine Person an zwei Stationen hat einen
Urlaubsverbrauch für denselben freien Arbeitstag, keine doppelte Abbuchung je Standort.
Genehmigte Einschränkungen wirken an allen zulässig verknüpften Einsatzstationen.
Verschiedene rechtliche Arbeitgeber nicht durch bloße Filialzuweisung zusammenführen.

Primäre Bearbeitung über zuständige Personal-/Leitungsrolle bestimmen. Wenn eine Leitung
nicht den gesamten relevanten Beschäftigungsumfang verantwortet, Anfrage zentral oder
an berechtigte Vertretung routen; kein unberechtigter Zugriff durch eine fremde Station.
Stationsübergreifende Hinweise dürfen intern Kollisionen feststellen, aber keine
privaten Gründe oder fremden Stationsdetails an unberechtigte Leitung verraten.
Eigene Anträge niemals selbst genehmigen; Vertretung und Eskalationsweg ohne Zwang zu
automatischer Freigabe. Kein aktiver Zugang nötig, um durch Berechtigte eine Meldung zu erfassen.

## 4. Feldkatalog

| Feld | Zweck/Regel |
|---|---|
| Mitarbeiter/Beschäftigung/Arbeitgeber | Aus autorisiertem Kontext, nicht frei fremde ID auswählbar. |
| Art/Unterart | Bestimmt Workflow, Kontowirkung und Zugriffsprofil. |
| Von/bis | Lokales Datum; intern eindeutige Intervalle/Zeitzone mit passender Tagessemantik. |
| Ganztägig/zeitanteilig | V1 Urlaub als Arbeitstage; Teil-/Stundenurlaub nur nach bestätigtem Anspruchsprofil. |
| Voraussichtliches Ende | Bei Krankheit soweit bekannt; unbekannt ausdrücklich statt Fantasiedatum. |
| Anlass/Kommentar | Nur nötige betriebliche Erklärung, keine Diagnosepflicht; sichere Rückfrage statt Gesundheitsfreitext. |
| Beantragt/gemeldet von | Mitarbeiter oder berechtigte erfasste Fremdmeldung mit Herkunft/Zeitpunkt. |
| Entscheidung/Bearbeiter/Zeit | Eindeutiger Status, delegiertes Recht und gültige Revision. |
| Ablehnungsgrund | Sachliche erforderliche Erklärung, ohne private Details anderer Personen. |
| Zähltage/Arbeitstage | Berechnete Einzelpositionen aus eingefrorener Grundlage, nicht freie UI-Zahl. |
| Anspruchs-/Regelversion | Kalender, Arbeitsrhythmus, Verträge/Quellen und Gültigkeit. |
| Nachweisstatus | Getrennt vom Abwesenheits-/Antragsstatus, nur berechtigte Einsicht. |
| Betroffene Pläne | Sichere Referenzen für Neuprüfung/Vertretung, keine automatische Änderung. |
| Dokumentreferenz | Nur falls nötig, geschützt/quarantänisiert; keine Diagnosekopien als Standard. |

Wohnadresse, Steuer-/SV-ID, Kontonummer oder Vergütung nicht auf dem normalen Antragsformular.
Bei Krankheit nicht automatisch vollständige Kassen-/Lohnakte öffnen oder alles neu abfragen.

## 5. Mitarbeiter beantragt Urlaub – Bildschirm B

Eigene berechtigte Ansicht mit verfügbarem und verifiziertem Kontostand,
bereits genehmigten/zeitlich verbrauchten Tagen und offenen Anträgen getrennt.
Zeitraum auswählen, beantragte Arbeitstage mit nachvollziehbarer Tagesliste zeigen,
anwendbaren Kalender/Arbeitsrhythmus erklären. Nicht pauschal Samstag/Sonntag ausschließen:
Tankstellenpersonal kann an diesen Tagen arbeitspflichtig sein.

Konto/Berechnung unvollständig: „Noch zu prüfen“ statt 0 oder fiktiver Anspruch.
Antrag kann mit Klärungsbedarf gespeichert/eingereicht werden; finale Genehmigung
erst nach belastbarer Berechnung/Fachentscheidung, kein unbemerkter Nullverbrauch.
Arbeitsvertragliche Urlaubsansprüche nicht aus dem sichtbaren Schichtentwurf erfinden.
Optionaler Hinweis, kein Pflichtfeld „privater Reisegrund“; keine Nachweise zu Reisezielen.
Nach Einreichen eindeutig beantragt, zuständige Stelle/Status und sicherer eigener Wiederzugang.
Kein automatischer Urlaub bei Schweigen oder Versandfehlern.

## 6. Antrag, Rücknahme und Änderung – Zustände

Entwurf → beantragt → Rückfrage → erneut beantragt → genehmigt oder abgelehnt.
Offener Antrag kann ausdrücklich zurückgezogen werden. Abgelehnt/zurückgezogen
verändert kein genehmigtes Kontingent. Keine stille Statusänderung durch Fristablauf.
Wiederholte Klicks/Neuversand erzeugen keinen zweiten Antrag/keine Doppelbuchung.

Nach Genehmigung Änderung/Stornierung als neuer Antrag mit Bezug auf Original,
nicht Bearbeiten der alten Historie. Bis zur Entscheidung gelten ursprünglicher Urlaub
und Kontobuchung. Keine freie einseitige Rückholung wegen Unterbesetzung aus dem UI.
Sachliche Korrekturen durch berechtigte Personalstelle protokollieren und Auswirkungen zeigen.
Teilzeiträume/Jahresgrenzen können in einer Operation aufgeteilt werden, ohne doppelten Verbrauch.

## 7. Prüfung und Entscheidung – Bildschirm C

Zeigen: Zeitraum/Art, Kontovorher/-nachher, berechnete Arbeitstage, Antragshistorie,
berechtigte Plan-/Besetzungsauswirkungen und noch offene fachliche Klärung.
Nicht automatisch nach „zuerst geklickt“ oder KI-Bewertung entscheiden; menschliche
Zuständigkeit, relevante betriebliche Vorgaben und zulässige Kriterien separat festlegen.

Vor Genehmigung serverseitig erneut prüfen:
- Aktuelle Zuständigkeit und keine Selbstgenehmigung.
- Antrag noch offen und Revision aktuell.
- Gültiges Beschäftigungs-/Anspruchsprofil, Tage/Kalender und Kontostand.
- Andere Buchungen/Anträge und vorhandene Überschneidungen.
- Bei Cross-Station-Fall berechtigte zentrale Entscheidung/Abstimmung.

Entscheidung, Urlaubsbuchung, wirksame Abwesenheitsintervalle und Benachrichtigungsereignis
atomar festhalten. Parallelgenehmigungen dürfen denselben Restsaldo nicht doppelt nutzen.
Unterbesetzung als Prüfhinweis, keine automatische Ablehnung/Übersteuerung von Rechten.
Ablehnung mit sachlichem Grund und berechtigtem Zugriff; keine Diagnosen/Personaldaten
Dritter im Grund. Dienstfehler beim Versand nimmt die Entscheidung nicht zurück.

## 8. Urlaubsanspruch – kein pauschaler Rechner

Rechtlicher Mindestanspruch, vertraglicher Mehrurlaub, ggf. Zusatzansprüche,
Überträge und manuelle fachlich begründete Korrekturen getrennt führen.
30 Tage im Mockup sind ein Beispiel, kein Unternehmensstandard.
Anspruch hängt u. a. von Beschäftigungs-/Arbeitsrhythmus und rechtlichem Profil ab;
Teilzeit nicht einfach nach Stundenquote reduzieren, Arbeitstage/Wechselmodelle beachten.
Eintritt/Austritt/Wartezeit/Teilurlaub/Wiedereintritt und Jahresgrenzen mit gültigen Regeln,
keine pauschale monatliche 1/12-Verteilung für alle Fälle.

Vorgeschlagene Einführung in zwei fachlich getrennten Stufen:
A) Personalstelle hinterlegt geprüften Jahres-/Restanspruch samt Herkunft, Bezugsjahr,
   Regelbasis und Eröffnungsstand. Merlin bucht transparent gegen diesen Stand.
B) Erst nach Fachfreigabe automatisierte Anspruchsermittlung mit zeitabhängigen
   Vertrags-/Arbeitstageprofilen, Fällen/Rundung und nachvollziehbaren Tests.

Auch Stufe A ist keine beliebige freie Überschreibung: Änderungsrecht, Pflichtgrund,
Herkunft und Historie; bereits gebuchte/freigegebene Tage bei Änderung prüfen.
Fehlende verlässliche Daten verhindern falsche automatische Zusage, nicht das Melden eines Wunsches.

## 9. Urlaubskonto als nachvollziehbares Journal

Je Arbeitgeber/Beschäftigung und Anspruchsherkunft/Jahr eindeutige Buchungen:
Eröffnung/Zugang, genehmigte Reservierung, zeitlicher Verbrauch, Freigabe/Storno,
Übertrag, fachlich freigegebene Korrektur und separat gerechtfertigter Verfall.
Keine freie Restzahl neben einem widersprechenden Buchungsjournal pflegen.

Vorschlag: offene Anträge separat ausweisen und noch nicht vom verbindlich verfügbaren
Kontostand abziehen; bei Freigabe atomar reservieren. Keine doppelte Reservierung und
Verbrauchsbuchung für denselben Tag. Übergang reserviert → zeitlich verbraucht
ändert den Gesamtverbrauch nicht erneut. „Genommen“ ist die buchhalterische
Zuordnung verstrichener gebuchter Tage, kein biometrischer Anwesenheitsnachweis.

Beispiel ohne Übertrag/Korrektur: 30 Anspruch = 12 zeitlich verbraucht + 8 für Zukunft
genehmigt + 10 verfügbar. Offener 5-Tage-Antrag bleibt separat; nach Genehmigung:
12 verbraucht + 13 genehmigt + 5 verfügbar. Nicht 5 zweimal abziehen.

Arbeitstagezählung:
- Vertrags-/Arbeitsrhythmus, gültiger Feiertags-/Einsatzortkalender und Freistellungszweck.
- Unveröffentlichter leerer Plan ist keine Grundlage für automatisch 0 Urlaubstage.
- Maßgebliche gültige Grundlage vor Freigabe bestimmen und als Berechnungssnapshot erhalten.
- Spätere Pläne/Vertragsänderungen ändern alte Buchungen nicht still; Prüf-/Korrekturprozess.
- Mehrstationeneinsatz zählt einen betroffenen Arbeitstag nur einmal, keine Paralleljournale.
- Halbe Tage/Bruchteile/Rundung je Anspruchsprofil bestätigen; V1 kein freier Stundenurlaub
  als Ersatz für gesetzliche Tagesansprüche.
- Jahresübergreifende Anträge auf betreffende Anspruchsjahre/-töpfe aufteilen;
  Entnahmereihenfolge durch freigegebene Regel statt zufälligem Tabellenstand.

Keine pauschale Löschung am 31.12./31.03. oder allein nach 15 Monaten.
Hinweis-/Mitwirkung, Nachweise, langdauernde Krankheit und unterschiedliche Anspruchstypen
fachlich berücksichtigen. Erinnerung versandt ≠ rechtlich ausreichende Belehrung bewiesen.
Verfall nur mit geeignetem freigegebenem Regelprofil oder kontrollierter Fachentscheidung.
Abgeltung bei Ende der Beschäftigung ist eigener Lohn-/Rechtsprozess, keine direkte Zahlung aus Merlin.

## 10. Krankheit melden – eigener Workflow

Mitarbeiter bzw. Berechtigter erfasst Beginn, soweit bekannt voraussichtliches Ende,
Meldezeitpunkt/Herkunft und gegebenenfalls Hinweis „Verlängerung“. Kein Diagnosefeld,
keine Freitextpflicht „Welche Krankheit?“ und kein standardmäßiger Diagnosen-Upload.
Unbekanntes Ende ausdrücklich offen mit Nachfass-/Klärhinweis; kein geratenes Gesunddatum.
Weitergeltende Einschränkung nach Fachregel, keine automatische Freigabe allein nach
einem technischen Standarddatum. Klar anzeigen, welche zukünftigen Einsätze ungeklärt sind.

Krankmeldung wirkt als notwendige Nichtverfügbarkeit ab Eingang. Fehlender Nachweis
macht Person nicht automatisch verfügbar; Erfassung/Nachweisklärung sind unabhängig.
Zustände: gemeldet → laufend/verlängert → Ende geklärt → abgeschlossen bzw. korrigiert.
Keine Aktion „Krankheit genehmigen/ablehnen“. Falsche Meldung berechtigt berichtigen,
Historie erhalten; keine medizinische oder Entgeltentscheidung automatisch treffen.

Nachweisstatus getrennt: nicht erforderlich / zu klären / angefordert / liegt vor /
widersprüchlich, jeweils Quelle/Version. Wenn zukünftig eAU integriert wird, reale
Verfahrenszustände und Rückmeldungen übernehmen; kein Fake-„eAU bestätigt“.
V1 kein eigener eAU-Abruf, keine Lohnfortzahlungsberechnung und keine Diagnoseauswertung.
Alternative Nachweise nur falls nötig, nur Arbeitgeberfassung/erforderlicher Umfang,
geschützt/quarantänisiert; Mitarbeiter nicht pauschal zur Diagnosekopie auffordern.

Gesund-/Rückkehrmeldung klärt zukünftigen Einsatz, ist keine eigenmächtige Stornierung
historischer Nachweise. Rückkehr, Folgemeldung und nachträgliche Korrektur unterscheiden.
Technische Erfassung ersetzt nicht alle erforderlichen betrieblichen Informationswege;
im Livebetrieb klare Kontakt-/Fallback-Regel bei Ausfall festlegen.

## 11. Krankheit während Urlaub und weitere Überlappungen

Urlaub/Krankheit können sich sachlich überlagern. Nicht global „überlappende Abwesenheit
verboten“ anwenden und auch nicht doppelt als Verlust abbuchen.
Bei gemeldeter Erkrankung im Urlaub Nachweis-/Fachprüfung nach zutreffender Regel anstoßen.
Erst begründete bestätigte Korrektur der betroffenen Urlaubstage als Gegenbuchung,
nicht pauschal gesamten Urlaub erstatten oder bei bloßer Meldung endgültig ändern.
§ 9 BUrlG als Ausgangspunkt, keine automatische Verlängerung des Urlaubszeitraums.
Krankmeldung als Planrestriktion bleibt unabhängig von der Urlaubsrückbuchung wirksam.

Doppelte Meldungen/Anträge mit Hinweis behandeln; keine stille Zusammenführung,
wenn unterschiedliche Rechts-/Nachweisgrundlagen vorliegen. Zeitteile/Arbeitsrhythmus
und Jahres-/Stationsränder sorgfältig zuordnen. Pflege/Kind krank/Schulung sind keine
identischen Krankheitstypen mit automatisch gleicher Kontenwirkung.

## 12. Wunschfrei, Verfügbarkeit und anderweitige Verpflichtungen

Verfügbarkeit hat Gültigkeitszeitraum, Wochentags-/Zeitfenster oder konkrete Datumsangabe,
Art „bevorzugt/nicht bevorzugt/nicht verfügbar“ mit eindeutigem Fachstatus und optionalem Hinweis.
Vertragsdaten, gesetzliche Restriktion und genehmigte Abwesenheit haben eigene Priorität.
Mitarbeiterwunsch ändert keinen Arbeitsvertrag, keine Sollstunden und keinen veröffentlichten Plan.
Ob ausdrücklich bestätigtes Wunschfrei als bindende Planrestriktion wirkt, ist offen.
Bis Entscheidung als Wunsch anzeigen, nicht als Urlaub/Urlaubsabbuchung bezeichnen.

Schulung/Berufsschule kann für Stationsbesetzung abwesend und zugleich Arbeitszeitbeitrag sein.
Diese Stunden nicht pauschal aus Arbeitszeit-/Ruhe-/Jugendprüfung herausnehmen oder doppelt
mit Schicht zählen. Zuständiger Datenvertrag für Zeitanteile und Überschneidungen.
Weitere Freistellungsarten erst mit eigener fachlicher Entscheidung.

## 13. Auswirkungen auf Schichtplanung und Ist-Zeit

Einreichung Urlaub = Hinweis auf offenen Wunsch; Genehmigung = wirksame Restriktion.
Krankmeldung = notwendige Nichtverfügbarkeit, kein Genehmigungsvorbehalt.
Gemeinsamer Vertrag zum Planer: Person/Beschäftigung, eindeutige Intervalle/Datumsgrundlage,
Wirksamkeitsstatus, minimale Kategorie, Priorität, Version und fachlicher Zeitbeitrag.
Planungsrollen erhalten möglichst „nicht verfügbar“, nicht Gesundheitsdetails.

Bei Änderung berührte Entwürfe, Nachbarschichten/Übernacht-/Stationsgrenzen und veröffentlichte
Versionen neu prüfen; zuständige Personen bekommen erlaubten Handlungsbedarf.
Kein automatisches Löschen/Umsetzen veröffentlichter Schichten. Tatsächliche Abwesenheit
darf auch bei besetztem Plan erfasst werden; Planmangel nicht als Krankheitsablehnung lösen.
Vertretung über eigenen Planänderungs-/Veröffentlichungsprozess.
Ganztagsurlaub erzeugt technische lokale Datumsintervalle; Nachtarbeits-/Diensttagbezug
mit Fachprofil vor Freigabe prüfen, Grenzüberschneidung sichtbar statt still ignorieren.
Ist-Zeiterfassung muss Arbeit trotz gespeicherter Abwesenheit als Klärung erkennen können,
keine automatische Gehalts-/Zeitentscheidung aus Planstatus. DATEV-Schlüssel später separat mappen.

## 14. Ansichten und Rechte – Vorschlag

| Ansicht/Aktion | Mitarbeiter | Stationsplanung/Leitung | Personalverwaltung mit Fachrecht |
|---|---|---|---|
| Eigener Antrag/Kontostand | Eigener Beschäftigungsumfang | Kein automatischer Einblick fremder Konten | Erlaubter Arbeitgeberumfang |
| Antrag bearbeiten/entscheiden | Einreichen/Rücknahme, keine Selbstfreigabe | Nur ausdrücklich delegiert und zuständig | Mit Entscheidungsrecht, keine Selbstfreigabe |
| Krankheit erfassen | Eigene Meldung | Berechtigte Erfassung des nötigen Ausfalls | Mit Melde-/Nachweisrecht |
| Diagnose/medizinische Details | Nicht vorgesehen | Nicht vorgesehen | Kein Sammelzweck für Diagnosen |
| Nachweisdateien/eAU-Details | Eigene nötige Dokumente | Standardmäßig nein | Separates sensibles Nachweisrecht |
| Teamkalender | Standardmäßig keine fremden Gründe | Nötige Nichtverfügbarkeit zugewiesener Personen | Je Fachrecht/Kategorie |
| Anspruch/Journal korrigieren | Nein; Rückfrage möglich | Nicht aus Planerrolle ableiten | Eigenes Kontorecht, Grund/Historie |
| Verfügbarkeit | Eigene | Nur nötige Planungssicht | Erlaubter Umfang |
| DATEV-/Gesamtexport | Nein | Nein, standardmäßig | Eigenes Exportrecht/zulässiger Datenumfang |

Übersicht trennt Anträge, Kalender und Krankmeldungen/Nachweisklärung.
Kalenderdaten dürfen Gesundheitsdetails nicht über Farblegende, Tooltip, iCal,
PDF, Titel, URL, Suchtreffer, Badge oder API offenlegen. Auch neutrale Abwesenheit
ist personenbezogen; kein frei öffentlicher Teamkalender.
Keine zentrale Selbstgenehmigung über Zweitrolle/Vertretung. Fehlt Entscheider,
definierter Eskalationsweg statt automatischer Zustimmung.

## 15. Datenschutz, technische Zuverlässigkeit und Historie

Krankheit betrifft besonders schutzbedürftige Angaben. Zweck, Rechtsgrundlage,
erforderliche Felder, Kategorien, Rollen und Fristen mit zuständiger Stelle klären.
Keine pauschale Datenschutz-Einwilligung oder absolute Konformitätsgarantie.
Gesundheits-/Urlaubsdaten nicht in echte GitHub-Beispiele, Mailbetreff, Pushtext,
Analytics, ungeschützte Browsercaches oder vollständige Audit-Dumps.
Benachrichtigung nur notwendiger Vorgang/Handlungsbedarf plus geschützter Link.

Serverseitige Konten-/Mandanten-/Feldrechte für Web, API, Exporte, Dateien und Jobs.
Optimistische Revision/atomare Buchung gegen parallele Entscheidungen; Kontowirkung
idempotent, Ersetzungs-/Gegenbuchungen statt historischer Löschung.
Quelle, Entscheider, Zustand und Regelversion minimal nachvollziehbar protokollieren;
private Freitexte/Nachweise nicht unnötig in separate Logs kopieren.
Papier-/Telefonmeldung assistiert mit Herkunft erfassen, keine fingierte Mitarbeiter-Unterschrift.
Keine automatische irreversible Löschung beim Austritt oder bei Linkablauf.
Nachweis-, Antrags-, Konto- und Regelhistorie haben verschiedene Aufbewahrungszwecke.

## 16. Konzeptionelles Datenmodell

AbsenceType/TypePolicy, AbsenceRequest mit Revision/Entscheidungsereignissen,
EffectiveAbsenceInterval, SicknessReport/SicknessRevision, EvidenceStatus/DocumentReference,
AvailabilityPreference, EmploymentWorkPatternVersion, HolidayCalendarReference,
LeaveEntitlementBucket (Jahr/Herkunft/Regelbasis), LeaveLedgerEntry mit eindeutiger
Vorgangs-/Tagesreferenz, LeaveCalculationSnapshot, AbsenceChangeRequest,
ApprovalResponsibility/Delegation, PlanningImpactEvent und NotificationOutbox.
Bestehende Mitarbeiter-/Beschäftigungs-/Stationsobjekte referenzieren, keine Parallelakte.
Kein Tabellen-/Migrationscode und keine tatsächlich ausgeführten Übertragungen.

## 17. Abnahmefälle

- Urlaub beantragt ohne Freigabe sperrt nicht automatisch bindend wie genehmigter Urlaub.
- Krankheit wird gemeldet, nicht genehmigt; fehlender Nachweis hebt Restriktion nicht auf.
- Wunschfrei ohne Kontoabzug, eindeutig von genehmigtem Urlaub getrennt.
- Zwei Einsatzstationen, ein freier Arbeitstag: eine Kontobuchung, Restriktion für beide.
- Keine Selbstgenehmigung, auch nicht mit mehreren Rollen oder Vertretung.
- Zwei gleichzeitige Genehmigungen können Restsaldo nicht doppelt verbrauchen.
- Doppelklick/Retry erzeugt keine doppelte Reservierung, Verbrauch oder Gegenbuchung.
- Fehlendes Arbeitsrhythmus-/Feiertagsprofil ergibt „zu prüfen“, nicht null Tage.
- Teilzeit/wechselnde Tage, Feiertage und Wochenende nach tatsächlichem Profil, nicht pauschal Mo–Fr.
- Jahreswechsel/Eintritt/Austritt/Wiedereintritt/Anspruchstopf ohne pauschale 1/12-Fehlberechnung.
- Veränderte Schicht-/Vertragsdaten schreiben alte Buchungen nicht still um.
- Reserviert → verbraucht zieht nicht erneut ab; Beispiel 30=12+8+10 bleibt konsistent.
- Genehmigten Urlaub ändern/stornieren als eigener Vorgang, keine stille Neufreigabe.
- Krankheit im Urlaub mit geeignetem Nachweis/Fachprüfung: nur betroffene Tage korrigiert,
  keine automatische Reiseverlängerung oder doppelte Abwesenheitsbuchung.
- Unbekanntes Krankheitsende, Verlängerung/Rückkehr nachvollziehbar und ohne Gesunddatum-Raten.
- Schichtkonflikte nach Abwesenheit erkennbar, Veröffentlichungshistorie nicht gelöscht.
- Schulung/Berufsschule als Nichtverfügbarkeit plus ggf. Arbeitszeitbeitrag, keine Doppelzählung.
- Gesundheitsdaten nicht über Kalenderfarbe/Tooltip/Mail/PDF/API an Planer/Mitarbeiterkollegen.
- eAU nicht angeschlossen: keine erfundenen Abrufe/Bestätigungen oder gesetzliche Fristerfüllung.
- Versand-/Netz-/Sessionfehler mit sicherer Wiederaufnahme; keine ungewollte Freigabe.
- Verfall nicht allein aufgrund Kalenderdatum automatisch, Herkunft/Regel/Fachprüfung nachvollziehbar.
- Mobile/Tastatur/Fokus, eigene Datenisolation und berechtigtes Vertretungsrouting.

## 18. Kleine spätere Umsetzungsschritte

1. Arten-/Rechte-/Zustandsmatrix und Arbeitsrhythmus-/Kalendervertrag bestätigen.
2. Eigene/administrative Erfassung, Anträge, Rückfrage/Entscheidung und sichere Listen.
3. Geprüfte Eröffnungsansprüche, Tagesberechnung und idempotentes Journal (Stufe A).
4. Krankmeldung/Nachweisstatus getrennt, sensible Rechte und begrenzte Nachweise.
5. Wirksame Intervalle/Planhinweise und Benachrichtigungen mit Schichtplanung integrieren.
6. Verfügbarkeit/Wunschfrei, Änderungen, Korrektur/Überschneidung und Jahreswechsel.
7. Erst später: automatischer vollständiger Anspruchsrechner (Stufe B), eAU-Verfahren,
   weitere Schutz-/Freistellungsarten und bestätigte DATEV-/Ist-Zeit-Schnittstellen.

Keine dieser Stufen ist programmiert oder als universell rechtlich geprüft freigegeben.

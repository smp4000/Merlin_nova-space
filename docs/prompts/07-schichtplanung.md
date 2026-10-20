# Modul-Prompt 07 – Schichtplanung

Planungsauftrag, 20.10.2026. Vollständige fachliche Grundlage:
`docs/planung/SCHICHTPLANUNG.md`. Noch keine Implementierungsfreigabe.

```text
AUFTRAG
Plane Merlin „Schichtplanung“ vollständig für spätere modulweise Programmierung.
Keine Anwendung, Migration, echte Schichten oder Benachrichtigungen erzeugen.
Lies AGENTS.md, STATUS/ENTSCHEIDUNGEN, SCHICHTPLANUNG.md, RECHERCHE-SCHICHTREGELN.md,
Stations-/Mitarbeiter-/Team-Spezifikationen und Umsetzungsübergabe.

DESIGN
Eisblau/Weiß/Petrol, Navy-Typografie, klare Kalender-/Listenansichten, dezente
Statusfarben mit Text/Symbol. Mockup 09 als Stilreferenz; fachlicher Text hat Vorrang.
Desktop-Wochenplan plus bedienbare mobile Tagesliste, keine reine Drag-Pflicht.

FACHZIEL
Verantwortliche planen, prüfen und veröffentlichen Versionen je Station/Woche.
Mitarbeiter sehen nur eigene veröffentlichte Einsätze über separaten aktiven Zugang.
Bis 100 Stationen organisatorisch verdichtet statt unlesbarer globaler Planmatrix.
Planung ist keine Ist-Zeit, Abwesenheitsgenehmigung, Lohnabrechnung oder DATEV-Übergabe.

DATENVERTRÄGE
Aktive Station/Nutzungsrecht, wirksame Öffnungszeiten und Zeitzone,
gültige Beschäftigung/Einsatzzuordnung/Arbeitszeitdaten/Qualifikationen,
genehmigte Abwesenheiten, eigene Verfügbarkeit und versionierte Regeln referenzieren.
Fehlende nötige Planungsdaten als unprüfbar; keine automatische Erwachsenenannahme
oder volle Prüffähigkeit aus fehlenden Geburts-/Lohninformationen.
Keine parallelen Mitarbeiter-/Stations-/Berechtigungsmodelle.

VORLAGEN UND SCHICHTEN
Vorlage mit Bereich/Zeiten/Folgetag/Bedarf/Qualifikation/Pausenvorgaben/Gültigkeit.
Konkrete Schicht mit eindeutigen Zeitpunkten/Zeitzone, Plätzen und individuellen Zuweisungen.
Vorlagenänderung verändert keine bestehenden Schichten. Erzeugen/Kopieren mit Vorschau,
keine stillen Duplikate oder Überschreibung veröffentlichter Daten.
Öffnungszeit ist Planungsgrundlage, kein rechtlicher Einsatznachweis; Vor-/Nachbereitung zulassen.
Pausen als Intervalle, bezahlt/unbezahlt getrennt von tatsächlicher Ruhepause.
Anwesenheit, Netto-Planarbeit und bezahlte Zeit sauber definieren.
Bedarfsdeckung auch während Pausen prüfen, keine bloße Kopfzählung.

ZEITMODELL
Lokales Datum/Zeit und IANA-Zeitzone eindeutig auflösen; Übernachtöffnung anzeigen.
Sommerzeitlücke/doppelte Uhrzeit nicht still verschieben oder raten.
Nachbarwochen, Stationswechsel, Vertragsstände, Ausgleichs-/Monats-/Jahreszeiträume prüfen.
Mitternacht/Wochenrand setzt Ruhe/Arbeitsdauer nicht zurück.
Fremdarbeitgeberdaten nur soweit zulässig bekannt, Prüfgrenzen transparent.

ANSICHTEN
A Wochenplan: Station/Woche/Version, Bereichsfilter, Vorlagen, Schicht erstellen,
Zuweisungsdialog/Drag, Mitarbeiterpanel, konkrete Konflikt-/Unprüfbar-Hinweise.
B Monats-/Organisationssicht: verdichtete Zustände/offene Plätze, sichere Filter/Paginierung.
C Prüfen/Veröffentlichen: aktuelle Revision, Abhängigkeiten/Prüfstand, Blocker,
ungeklärte Pflichtprüfung, Warnungen/offene Plätze, Änderungsübersicht und Empfänger.
D Eigener Plan: nur eigene veröffentlichte Schichten, Zeit/Pausen/Ort/Version/Änderung.
Keine fremden Gehalts-/Gesundheits-/Personaldaten im Plan oder Aushang.

REGELENGINE
Version/Gültig-ab/Quelle/Prüfhorizont/Eingaben/Abhilfe pro Regel.
Ergebnisse bestanden, blockierend, Warnung, Hinweis, nicht prüfbar, nicht anwendbar.
Integrität/Umfang/Überlappung/Abwesenheit/Qualifikation und freigegebene Fachregeln prüfen.
Arbeitszeit, Pausenlage, Ruhe, Sonn-/Feiertag/Ersatzruhe, Jugend/Berufsschule,
gültige Verträge und Minijobprognose differenziert behandeln.
Keine starre universelle Minijob-Stundengrenze oder private Lohnwerte durch Prozentanzeigen verraten.
Keine pauschale Tankstellen-Ausnahme. Begründung legalisiert keine Rechtsverletzung.
Gesetzliche Vorgaben nicht als frei editierbare Firmenwarnschwelle behandeln.
Fachlich belegte Ausnahmeprofile gesondert prüfen; keine allgemeine Trotzdem-Freigabe.
Rechtsgarantie nicht behaupten. Recherchierte Beispiele nur mit Gültigkeit/Quelle übernehmen.

VERÖFFENTLICHUNG
Unvollständiger Entwurf erlaubt, erforderliche Blocker/Prüflücken vor Publikation lösen.
Letzte veröffentlichte Version bleibt während neuer Bearbeitung sichtbar.
Aktuelle Rechte/Nutzungsstatus/Revision und alle abhängigen Daten erneut prüfen.
Zulässige organisatorische Restpunkte nur bewusst bestätigen, nicht gesetzlichen Fehler.
Atomarer Snapshot und Benachrichtigungs-Outbox; Doppelklick idempotent.
Parallelveröffentlichung gleicher Person an zwei Stationen gegen Konfliktrennen sichern.
Mailfehler ändern nicht Planversion; Versand begrenzt/retrybar, keine Doppelmail.
Nur betroffene aktive Konten benachrichtigen; fehlender Login erzeugt keine Kontoeinladung.

ÄNDERUNGEN UND AUSBAU
Veröffentlichte Änderung/Absage als neue Version mit Grund/Empfängern, kein stilles Löschen.
Neue Abwesenheit/Regel-/Vertragsänderung löst passende Neuprüfung aus, keine automatische Umbesetzung.
V1 Verfügbarkeit als eigener Wunsch; Abwesenheitsmodul bleibt zuständig.
Tausch/Schichtangebot später: Original bleibt bis bestätigter, neu geprüfter Änderung,
Mehrfachbewerbungen/Rennen/Frist/Absage behandeln. Keine automatische Bindung durch Anfrage.
Aushang aus Snapshot mit minimalen Personendaten und berechtigtem Download.
iCal später optional, nur eigene Daten, widerrufbarer Link und transparenter Drittanbieterbezug.

RECHTE/SICHERHEIT
Plan ansehen/bearbeiten/veröffentlichen/Regeln verwalten/exportieren getrennte Rechte.
Stationsleitung nur zugewiesene Station, keine Personal-/Lohnrechte daraus ableiten.
Cross-Station-Konflikte intern prüfen, fremde Stations-/Personaldetails nicht offenlegen.
API/Suche/Datei/Export/Jobs/Benachrichtigungen serverseitig abgrenzen.
Trialende/Stationspause nicht über Veröffentlichung oder Kopieren umgehen.

ABNAHME
Alle Fälle aus Fachspezifikation: Vorlagenwiederholung, mehrere Stationen,
Wochenränder/Übernacht/DST, Pausengrenzen/-lage und Besetzung, Jugend/Berufsschule,
fehlende Lohndaten, Abwesenheit, veraltete Prüfung, gleichzeitige Publikation,
Mailfehler, offene Plätze, private Entwürfe, spätere Tauschanfrage, Vertragsänderung,
Nutzungsrechtssperre, kein Ist-/DATEV-Export aus Planstunden, Mobile/Tastatur.

LIEFERE
Screens/Komponenten, Feldkatalog, Rechte-/Status-/Regelmatrix, Zeitmodell,
Veröffentlichungs-/Änderungsprozess, Datenverträge, Datenschutzkonzept,
konkrete Abnahmeszenarien und kleine priorisierte Implementierungsschritte.
Noch keinen Code schreiben.
```

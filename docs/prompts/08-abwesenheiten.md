# Modul-Prompt 08 – Abwesenheiten, Urlaub, Krankheit und Verfügbarkeit

Stand 20.10.2026. Vollständige Grundlage in `docs/planung/ABWESENHEITEN.md`.
Planungsauftrag, keine Implementierungsfreigabe.

```text
AUFTRAG
Plane Merlin „Abwesenheiten“ vollständig für die spätere modulweise Programmierung.
Keine Anwendung, Migrationen, echten Anträge, Krankmeldungen, eAU-Abrufe,
Freigaben oder Benachrichtigungen erzeugen.
Lies AGENTS.md, STATUS/ENTSCHEIDUNGEN, ABWESENHEITEN.md,
RECHERCHE-ABWESENHEITEN.md und die Mitarbeiter-/Schicht-/Team-Spezifikationen.

DESIGN
Eisblau/Weiß/Petrol, Navy-Typografie, klare Listen und eigene mobile Formulare,
Status mit Text/Symbol. Mockup10 als Stilreferenz, Fachtext vor Bilddetails.
Personalansicht, nötige Planungsansicht und Mitarbeiter-Selbstansicht strikt trennen.

ZIEL UND ARTEN
Urlaubsantrag ist noch kein genehmigter Urlaub. Wunschfrei/Verfügbarkeit sind
eigene Präferenzen, Krankheit eine Meldung/Tatsache, keine Genehmigung.
Krankmeldung ≠ Nachweis/eAU, Planung ≠ Ist-Zeit/Lohnabrechnung.
Schulung/Berufsschule kann Nichtverfügbarkeit UND Arbeitszeitbeitrag sein.
Unbezahlte/sonstige Freistellung und weitere Schutzfälle haben eigene Profile,
keine pauschal gleichen Konten-/Genehmigungsregeln.
V1-Kern Urlaub/Wunschfrei/Krankmeldung/Verfügbarkeit.

PERSON UND UMFANG
Urlaubskonto/Abwesenheit gehören zum Beschäftigungsverhältnis beim rechtlichen
Arbeitgeber. Zwei Einsatzstationen erzeugen keine doppelte Urlaubsabbuchung.
Wirksame Restriktion betrifft alle passenden Einsätze. Verschiedene Arbeitgeber
nicht als bloßen Stationswechsel zusammenführen.
Zuständigkeit/Vertretung explizit, keine Selbstgenehmigung auch über Zweitrolle.
Mitarbeiter ohne Login können berechtigt assistiert erfasst werden, keine Fake-Unterschrift.

URLAUBSANTRAG
Eigener Kontostand, Zeitraum/Arbeitstage, optionale betriebliche Notiz,
berechtigte Übersicht/Entscheider und eindeutig beantragter Status.
Keine Pflicht zum privaten Reisegrund. Offene/abgelehnte/zurückgezogene Anträge
nicht als genehmigt darstellen. Kein automatischer Urlaub bei Schweigen/Mailfehler.
Entwurf → beantragt → Rückfrage → erneut beantragt → genehmigt/abgelehnt;
offene Rücknahme möglich. Genehmigte Änderung/Stornierung eigener neuer Vorgang,
Original gilt bis Entscheidung. Keine freie einseitige Rückholung aus Personalmangel.

PRÜFUNG UND KONTO
Serverseitig Revision, Rechte, zuständige Stelle, keine Selbstfreigabe,
Arbeits-/Kalenderprofil, Tage/Anspruch/Saldokollision und Planwirkung neu prüfen.
Entscheidung, Kontobuchung, wirksame Intervalle und Notification-Outbox atomar.
Parallele Freigaben/Doppelklick dürfen Restsaldo nicht doppelt verbrauchen.
Unklarer Kontostand ist „zu prüfen“, nicht null oder automatisch freigegeben.

ANSPRUCHSMODELL
Gesetzlichen/vertraglichen/Zusatzurlaub, Überträge und Korrekturen getrennt führen.
Keine pauschale 30-Tage-Vorgabe, Stundenquote für Teilzeit oder 1/12-Regel für alle.
Vorschlag StufeA: fachlich geprüfter Eröffnungsanspruch mit Quelle/Regelbasis und
transparentem Journal; StufeB erst später vollständiger fachlich geprüfter Rechner.
Arbeitstage aus gültigem Rhythmus/Feiertags-/Einsatzortkalender, nicht aus leerem
unveröffentlichtem Plan oder pauschalem Ausschluss Samstag/Sonntag.
Berechnungssnapshot, Gültigkeit, Jahresgrenzen/Töpfe und Rundung dokumentieren.
Teil-/Stundenurlaub nur nach bestätigtem Profil, keine Umgehung gesetzlicher Tage.
Reservierung, Verbrauch, Freigabe, Übertrag/Korrektur getrennt und idempotent buchen.
Vorschlag offene Anträge separat ohne verbindlichen Abzug; Reservierung erst Freigabe.
Beispiel30=12verbraucht+8genehmigt+10verfügbar; nach weiterem5-Tage-Antrag genehmigt:
12+13+5. Reserviert→verbraucht belastet nicht erneut.
Kein automatischer Verfall allein 31.12./31.03./15Monate; Voraussetzungen/Hinweise/
Krankheitsfälle/Anspruchstyp und Fachentscheidung gesondert. Abgeltung kein direkter Einzug/Zahlweg.

KRANKMELDUNG
Beginn, soweit bekannt voraussichtliches Ende, Herkunft/Zeitpunkt und Verlängerung.
Kein Diagnosefeld/-pflichtupload. Fehlender Nachweis hebt Nichtverfügbarkeit nicht auf.
Unbekanntes Ende nicht raten oder nach technischem Default automatisch gesund melden.
Meldung/laufend/verlängert/Ende geklärt/abgeschlossen/korrigiert als eigene Zustände.
Keine Genehmigen-/Ablehnen-Aktion für Krankheit. Nachweisstatus getrennt:
nicht erforderlich/zu klären/angefordert/vorliegend/widersprüchlich.
V1 kein eAU-Abruf oder Entgeltfortzahlungsrechner; keine falschen Erfolgs-Badges.
Nötige Nachweise nur passender Umfang, geschützter Upload/Quarantäne/Downloadrechte.
Livebetrieb braucht Melde-/Fallback-Regel, App ersetzt nicht alle betrieblichen Pflichten.

ÜBERLAPPUNGEN
Krankheit im Urlaub nicht pauschal verbieten oder automatisch ganze Reise erstatten.
Nach zutreffender Nachweis-/Fachprüfung nur betroffene Tage gegenbuchen,
keine automatische Urlaubsverlängerung. Planrestriktion unabhängig von Rückbuchung.
Andere Überlappungen mit typbezogener Priorität/Version behandeln, kein globales
Verbot und keine stillen Zusammenführungen verschiedener Nachweisgrundlagen.

WUNSCHFREI/VERFÜGBARKEIT
Gültige Zeitlagen/Wochentage oder konkrete Daten, Präferenz vs. verbindliche
Restriktion ausdrücklich; bestätigtes Wunschfrei als bindend ist noch offen.
Keine Vertrags-/Sollstunden-/Urlaubskontoänderung durch Mitarbeiterwunsch.
Schulung/Berufsschule mit geprüftem Zeitbeitrag nicht aus Schutz-/Arbeitszeitprüfung verlieren.

SCHICHTPLAN-DATENVERTRAG
Person/Beschäftigung, eindeutige Intervalle/Datumsgrundlage/Zeitzone,
Wirksamkeit, minimale Kategorie, Priorität, Version und Fachzeitbeitrag.
Planungsrollen erhalten nur notwendige Nichtverfügbarkeit, keine Krankheitsgründe.
Antrag Hinweis, genehmigter Urlaub Restriktion, Krankheit nötiger Ausfall ohne Freigabevorbehalt.
Betroffene Entwürfe/Publikationen über Station/Nachbar-/Übernachtgrenzen neu prüfen.
Keine automatische Löschung/Umbesetzung veröffentlichter Schichten oder Umdeutung
von Ist-Zeit/Lohn-/DATEV-Werten. Vertretung über eigenes Planänderungsverfahren.

RECHTE/DATENSCHUTZ
Mitarbeiter nur eigene Konten/Anträge; Leitung nur nötige zugewiesene Planungssicht,
Entscheidung nur delegiert. Anspruchskorrektur/Nachweise/Export separate sensible Rechte.
Krankheit nicht über Tooltip/Farbe/Kalender/URL/Mail/Push/PDF/API an Unberechtigte verraten.
Keine öffentliche Teamkalenderfreigabe oder Gesundheitsdaten in Analytics/Auditdump/GitHub.
Rechtsgrundlagen, Gesundheitsdatenumfang, Empfänger, Erforderlichkeit und Fristen
mit zuständiger Stelle klären; keine pauschale Einwilligung/Konformitätsgarantie.
Revision/atomare Buchung/geschützter Nachweis/Wiederaufnahme/Austrittsaufbewahrung planen.

ABNAHME UND ERGEBNIS
Alle Fälle aus Spezifikation behandeln: offene/genehmigte Anträge, Krankheit ohne
Freigabe, Wunsch ohne Konto, Multi-Station, Selbstfreigabe/Vertretung, parallele
Kontonutzung, Wiederholung, fehlendes Rhythmusprofil, Feiertage/Wochenende/Teilzeit,
Jahres-/Vertragswechsel, Korrekturjournal, Krankheit im Urlaub, unbekanntes Ende,
Planfolgen, Schulzeitbeitrag, Gesundheitsdatenschutz, eAU nicht angeschlossen,
Versandfehler, Verfallprüfung, Mobile/Tastatur und Datenisolation.
Liefere Feld-/Arten-/Rechte-/Zustandsmatrix, Datenmodell, Buchungsbeispiele,
Screens, Schichtdatenvertrag, Datenschutz-/Quellenkonzept, offene Entscheidungen
und kleine spätere Umsetzungsschritte. Noch keinen Code schreiben.
```

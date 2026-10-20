# Modul-Prompt 05 – Stationsverwaltung

Eigenständig nutzbarer Planungsauftrag; vollständige Fachdetails in
`docs/planung/STATIONSVERWALTUNG.md`. Stand 20.10.2026.

```text
AUFTRAG
Plane Merlin „Stationsverwaltung“ haarklein. Noch keinen Anwendungscode,
Migrationen, echten Stationsdatensätze, Einladungen oder Gerätezugänge anlegen.
Lies AGENTS.md, STATUS.md, ENTSCHEIDUNGEN.md, STATIONSVERWALTUNG.md und
TEAM-UND-ZUGAENGE.md. Bestätigte Anforderungen von Vorschlägen trennen.

ZIEL UND DESIGN
Einzelunternehmer/Gesellschaft verwaltet bis zu 100 Stationen.
Freigegebenes Eisblau/Weiß/Petrol, Navy-Typografie, klare Karten/Tabellen,
Text-und-Symbol-Status, Mobile/Tablet/Desktop. Mockup 07 als visuelle Referenz;
fachliche Spezifikation geht vor generierten Bilddetails.

OBJEKTE UND GRENZEN
Organisation, Vertragspartner, Station, Rechnungsprofil, Zahlungsprofil und
Benutzer getrennt halten. Stabile Stations-ID trotz Umbenennung/Adressänderung.
Eine Station gehört genau einer Organisation; neue Station erzeugt keine
automatische Stationsleitungsberechtigung. Rollen aus Team-Modul verwenden.
Keine Rechnung, Bankverbindung oder SEPA im Stationsprofil duplizieren.
Keine Bestandsführung, echte Gerätekopplung oder Schichtregelprüfung in dieses
Stammdatenmodul verlagern.

ZUSTÄNDE
Betriebsstatus Vorschlag: Entwurf, Aktiv, Inaktiv, Archiviert.
Einrichtungsfortschritt und organisationsbezogene Nutzungsberechtigung sind
andere Achsen. Aktiv kann unvollständiges Optionalprofil haben.
Fehlende Leitung/Artikel/Geräte blockieren Aktivierung nicht automatisch.
Limit 100 serverseitig/atomar prüfen. Vorschlag: Entwurf/Aktiv/Inaktiv zählen,
Archiv zählt nicht; Restore prüft erneut. Zähl-/Tarifregel noch nicht beschlossen.

ÜBERSICHT
Name/Kürzel, Ort, Leitungen, Betriebsstatus, Profilbedarf und Öffnen-Aktion.
Suche Name/Kürzel/Ort, Statusfilter, Archiv getrennt, Paginierung für viele Stationen.
Zähler nur aus berechtigtem Umfang; keine fremden Daten in Suche/Export/Badges.
Profil ansehen nicht unbemerkt mit globalem Stationswechsel verbinden.
Leer, lädt, ohne Treffer und technischer Fehler unterscheidbar.

ANLEGEN UND STAMMDATEN
Station als Entwurf: Name Pflicht; vollständige passende Standortanschrift vor
Aktivierung vorschlagen. Kürzel organisationsweit eindeutig, optional.
Marke, geschäftliches Telefon/E-Mail, Services und externe Nummer nur falls nötig.
Länderabhängige PLZ/Adresse, führende Nullen und Unicode berücksichtigen.
Kein Register-/Adressimport oder Standorttracking ohne gesonderte Entscheidung.
Duplikatverdacht warnen, gleiche Anschrift nicht automatisch verbieten/vereinen.
Idempotentes Speichern, Versionskonflikte und paralleles Limit berücksichtigen.

PROFIL
Vorgeschlagene Reiter: Übersicht, Stammdaten, Öffnungszeiten, Team & Zugänge,
Ausstattung, Geräte. Nur verfügbare/berechtigte Fachbereiche anbieten.
Kopf mit Name/Kürzel/Anschrift/Status; ausdrückliche Verwaltungsaktionen.
Keine geteilte Stations-E-Mail als persönlicher Login.

ÖFFNUNGSZEITEN
Pro Wochentag unbekannt, geschlossen, Intervalle oder explizit 24h.
Mehrere Intervalle, Überlappungsprüfung und Folgetagsmarkierung für Übernachtöffnung.
00:00–00:00 nicht als 24h erraten. Sammelbearbeitung Mo–Fr muss Einzelregeln klar erzeugen.
Datumsausnahmen ersetzen gesamten lokalen Kalendertag; Vorrang vor Wochenregeln.
Beispiel Mo 22–Di 02 plus Di-Ausnahme: Di-Regel gilt für alle Dienstagsteile,
auch den Anteil aus Montag. Doppelte Ausnahmen nicht zufällig überschreiben.
Wirksamen Tageskalender als Vorschau zeigen.
Feiertag allein bedeutet nicht geschlossen. Regionale Automatik ist gesondert offen.
Zeitzone sichtbar, Vorschlag V1 aus Organisation geerbt. Zeitzonenwechsel separat.
Sommer-/Winterzeitfälle berücksichtigen, keine Arbeitsstunden aus Öffnungsdauer ableiten.
Versionierung/Gültig-ab als Vorschlag erläutern. Änderungen überschreiben keine
historischen Vorgänge oder veröffentlichten Schichtpläne stillschweigend.

TEAM/AUSSTATTUNG/GERÄTE
Mehrere Leitungen je Station und umgekehrt. Offene Einladung ist kein aktiver Zugang.
Inhaber kann selbst betreuen. Bestehendes Team-Modul referenzieren.
Kraftstoffe/Zapfpunkte/Services optional strukturiert, unbekannt nicht mit null gleichsetzen.
Historisch verwendete Objekte deaktivieren statt Datenbezüge zerstören.
Gerät-/Druckstellenverwaltung nur als abgesicherte Fremdmodulreferenz;
keine Tokens/PINs zeigen, keine automatische Umkopplung durch Stammdatenänderung.

RECHTE
Organisationsinhaber zentral, Zentrale Verwaltung nur delegiert,
Stationsleitung nur zugewiesener Umfang. Anlegen/Status/Adresse zentral.
Eigene Rechte für Öffnungszeiten, Kontakte, Ausstattung und Geräte als Vorschläge.
Keine automatische Rechte-/Rechnungsfreigabe aus „Station bearbeiten“ ableiten.
Jede Seite/API/Datei/Export/Job serverseitig abgrenzen.

PAUSE/ARCHIV/RESTORE
Explizite Wirkungsvorschau: laufende Kassenschichten, Offline-Warteschlangen,
Einwürfe, Druckjobs, zukünftige Pläne, Anträge/Störungen und Einladungen.
Kritische Vorgänge vorher abschließen oder abgesicherten Nachbearbeitungsweg
planen. Keine Daten verwerfen oder falschen Erfolg melden.
Neue operative Vorgänge an inaktiver Station sperren; Historie berechtigt lesbar.
Archivierung ist keine Löschung, Pause/Restore keine Aboänderung/Trialverlängerung.
Restore prüft Limit, Rechte, Nutzungsstatus und Zuordnungen/Geräte neu;
widerrufene Rechte/Einladungen nicht ungeprüft wiederherstellen.
Keine automatische zeitgesteuerte Stilllegung in V1 ohne eigene Entscheidung.

DATENSCHUTZ/HISTORIE
Nur nötige Geschäftskontaktdaten. Keine automatischen öffentlichen Profile,
Karten-Tracker oder externen Adressabfragen. Minimale Änderungen mit Akteur/Zeit
protokollieren, keine Geheimnisse/Formularvollkopien.
Historische relevante Daten als Fachsnapshot erhalten; Versionskonflikte sichtbar.
Löschung/Aufbewahrung nach gesondertem Konzept, nicht pauschal aus Archivierung.
Keine ungeprüfte DSGVO-/Sicherheitsgarantie.

ABNAHME
Szenarien der vollständigen Spezifikation abdecken: Mandantentrennung,
100er Limit parallel/Restore, neue Station ohne automatische Rechte, Duplikate,
Adresse versus Rechnung, aktive/unvollständige Profile, mehrere/übernächtige
Intervalle, 24h/unbekannt/geschlossen, Ausnahmen und DST, Planhistorie,
laufende Kasse/Offline-Daten bei Pause, Trialende, Gerätezugriff, Parallelbearbeitung,
Tastatur und Smartphone.

LIEFERE
1. Feldkatalog mit Pflicht, Zweck, Validierung und Änderungsrecht.
2. Rechte-/Lebenszyklus-/Fachmodul-Wirkungsmatrix.
3. Datenmodell und Zustände ohne Migrationen.
4. Screens für Liste, Anlage, Profil, Öffnungszeiten, Pause/Archiv/Restore.
5. Kalenderbeispiele für Randfälle.
6. Kleine Umsetzungsschritte, Abnahmekriterien und offene Geschäftsentscheidungen.
Noch nicht programmieren.
```

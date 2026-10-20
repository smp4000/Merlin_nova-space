# Aktueller Stand

Stand: 20.10.2026, Europe/Berlin. Phase: **Lokale technische Basis eingerichtet; Fachmodule weiter in Planung**.

## Letzter Benutzerauftrag

Prompt 00 ausdrücklich ausführen: aktuelle kompatible stabile Laravel-/Filament-Versionen,
echter MySQL, Anwendung unter `application/`, getrennte Dev-/Testdatenbanken, technisches
Adminpanel, Prüfungen und Sicherung auf GitHub. Keine Landingpage, Registrierung, Abos
oder Fachmodule. Diese begrenzte technische Freigabe ersetzt den bisherigen reinen
Planungsmodus ausschließlich für die Basis.

Ergebnis: Laravel 13.38.0, Filament 5.10.2, PHP 8.4.26 und MySQL Community 9.7.2 LTS.
Asset-Build und acht Tests mit 30 Assertions erfolgreich; echter Browser-Adminlogin,
Zugriffsschutz und DB-Isolation geprüft. npm-Audit ohne Befunde. Composer-Audit durch
Cloud-Netzregel für `packagist.org` blockiert; Domain im Konfigurationsentwurf ergänzt,
nach Speichern der Netzänderung erneut prüfen. Kein bestandener Composer-Audit behauptet.
Start und lokale Secretverwaltung: [LOKALE-ENTWICKLUNG](../leitfaeden/LOKALE-ENTWICKLUNG.md).

## Vorhandene Ergebnisse

- Mein-Abo-Spezifikation/Prompt 12: Rechte, Stationsauswahl, Abhängigkeiten,
  Angebotsprüfung, Bestätigung, Vormerkung/Rücknahme, Konflikte und Abnahme.
- Prompt 00: begrenzte spätere Entwicklungsbasis, Versionsprüfung, MySQL statt MariaDB,
  getrennte Dev-/Testdatenbank, Secretschutz, Basisprüfungen und Startdokumentation.

- Grundpaket-/Zusatzmodulplanung mit Paketmatrix, Mengenformel, Beispielen,
  Stationsbuchungen, Zeitanteilen, Rechnungsaufbau und Abnahmeszenarien; Prompt 11.

- Statische Bestandsanalyse zweier alter Archive, zusammengefasst in BESTAND.md.
- Landingpage-Mockup: erster Entwurf und bestätigte Eisblau-Petrol-Richtung.
- Partnerregistrierungs-Prompt und vierteilige Ansicht.
- Ergänzung SEPA als Pflichtschritt samt eigenem Mockup.
- Partner-Dashboard-Prompt und Mockup für ersten Einstieg.
- Team-&-Zugänge-Spezifikation, Prompt und Mockup.
- Stationsverwaltungs-Spezifikation und Prompt 05: Stammdaten, Rechte,
  Öffnungszeiten/Ausnahmen, Lebenszyklus und Abhängigkeiten.
- Mitarbeiter-/Einladungsplanung mit Feldgruppen, Personal-/Lohnrechten,
  Selbsterfassung, Prüfung und begrenzter DATEV-Vorbereitung; Prompt 06.
- Offizielle DATEV-Recherche und Mapping-Gerüst ohne erfundene Schnittstellenfelder.
- Schichtplanung mit Vorlagen/Entwurf, Prüfungen, versionierter Veröffentlichung,
  Benachrichtigungen, eigener Mitarbeiteransicht und abgegrenztem Tauschausbau; Prompt 07.
- Regelrecherche mit offiziellen Quellen und Gültigkeits-/Prüfgrenzen.
- Abwesenheiten mit Arten-/Rechte-/Zustandsmatrix, Urlaubsjournal, Krankmeldung
  und getrenntem Nachweisstatus, Planwirkung und Verfügbarkeit; Prompt 08.
- Offizielle Quellen zu Urlaub, Verfall, Krankmeldung und eAU-Grenzen.
- Zwölf Bildmockups einschließlich Super-Admin für Landing, Module und Preise.
- Super-Admin-Spezifikation: CMS, Modulkatalog, Preisversionen, Veröffentlichung, Rechte
  und Trennung von öffentlichen Angeboten und bestehenden Verträgen; Prompt 10.
- Zusätzlich interaktiver HTML-Entwurf 11: Stations-/Demo-Rollenwechsel, Navigation,
  Zuordnung mit Beispiel-Überschneidungsprüfung, Antragsstatus, Station/Einladung vormerken.
- Bedienung, Grenzen und tatsächliche Browserprüfungen in DASHBOARD-INTERAKTIV.md.
- Umsetzungsübergabe für neuen Rechner mit Modulreihenfolge, offenen Voraussetzungen
  und späterem Startprompt; keine automatische Programmierfreigabe.
- Datenschutz-/SEPA-Leitfaden mit Quellen und offenen Punkten.
- Git- und Codex-Übergabeanleitung.

## Nächste sinnvolle Arbeit

1. Mein-Abo-Ansichten und neue Detailabläufe besprechen; Trialumfang, Fristen,
   Preisregel für spätere Zubuchungen und Datenzugriff nach Paketende festlegen.
   Danach Beträge und Abrechnungsgrundlagen. Die technische Basis ist eingerichtet;
   daraus folgt keine Freigabe dieser Fachmodule.
2. Als nächstes Fachmodul Ist-Zeiterfassung/Arbeitszeitkonto vorschlagen,
   damit Plan, tatsächlich geleistete Zeit, Pausen und Korrekturen getrennt bleiben.
3. Urlaubskonto Stufe A/B, Arbeitstage-/Feiertagsgrundlage, Wunschfrei-Wirkung,
   Freigabe/Vertretung und Gesundheitsdatenrechte bestätigen.
4. Schichtregel-/Tarif-/Schutzprofile, offene Plätze und Veröffentlichungsrechte klären.
5. DATEV-/Arbeitgebermodell und übrige Stations-/Rollen-/Aboentscheidungen bleiben offen.
6. Am neuen Rechner LOKALE-ENTWICKLUNG und UMSETZUNGSUEBERGABE lesen; weitere
   Implementierungsschritte ausdrücklich beauftragen.
7. Bis dahin keine produktive Anwendung implementieren; Vorschaucode separat halten.

## Noch nicht entschieden / nicht fertig

- Automatischer kostenpflichtiger Übergang oder aktive Abo-Bestätigung.
- Preise, Tarifgrenzen unterhalb von 100, konkrete Kündigungsregeln; monatlicher Start ist bestätigt.
- SEPA-Zahlungsanbieter, Basis-/Firmenlastschrift, Gläubiger-ID und freigegebener Text.
- Rechtliche Betreiberangaben, Verträge, Aufbewahrungsfristen und Hosting.
- Endgültiger Rollen-/Rechtekatalog; separate Buchhaltungsrolle optional.
- Technischer Neuaufbau versus gezielte Übernahme alter Implementierung.
- Verknüpfung eines Benutzerkontos mit mehreren Partnerorganisationen: zurückgestellt.
- Ob Entwürfe/inaktive/archivierte Stationen auf das 100er-Limit zählen und wie sich
  Archivierung auf eine spätere Abrechnung auswirkt.
- Stationsrechte für Kontakte/Öffnungszeiten/Ausstattung; genaue Pausen-Nachbearbeitung.
- Länderumfang, Stationszeitzone versus Organisationsvererbung und Gültig-ab-Regeln.
- DATEV-Zielprogramm, Version/Feldmapping, Datei-/Cloud-Übergabe und technische Freigabe.
- Rechtlicher Arbeitgeber/Lohnmandant je Akte, Personalnummern und bedingte Pflichtfelder.
- Personalfragebogenprofile, genaue Personal-/Lohnrechte und Erfassungs-Authentifizierung.
- Schichtregelprofile/Tarif-/Ausnahmegrundlagen, Planveröffentlichung mit offenen Plätzen,
  Freigaberechte, Einbeziehung von Fremdzeiten und Abwesenheits-Datenvertrag.
- Abwesenheiten sind jetzt detailliert geplant, fachliche Anspruchsprofile/Regeln und
  Automatisierungsgrad noch nicht bestätigt; Ist-Zeit und weitere Fachmodule noch offen.
- Wunschfrei-Verbindlichkeit, Schicht-/Arbeitstagekalender, Korrektur-/Verfallsprofile,
  Nachweisumfang/eAU-Anbieter und konkrete Datenaufbewahrung.

## Technischer Zustand

Planungen, zwölf Bildmockups und HTML-Vorschau unverändert erhalten. Neue technische
Laravel-/Filament-Basis unter `application/`, keine Fachressourcen oder öffentliche
Registrierung. Lokales Admin-Konto explizit begrenzt, keine produktive Rechtearchitektur.
MySQL-Dev-/Testdatenbanken getrennt und nur lokal erreichbar. Keine Zahlungs-, DATEV-
oder Versanddienste eingerichtet. APP_KEYs, Passwörter, DB-Daten und Abhängigkeiten
bleiben lokal/ignoriert. Lockdateien und wiederholbare Einrichtungshelfer versioniert.
Cloud-Start-/Installationsanleitung ist im Konfigurationsentwurf hinterlegt; dessen
Veröffentlichung und Wiederherstellung in einer neuen Aufgabe sind nicht verifiziert.
Alte Archive wurden weiterhin nicht installiert oder gestartet.

## Zu beachten

Mockups enthalten teilweise illustrative/abweichende Texte. Siehe `docs/mockups/README.md`.
Ein erteiltes Mandat ist keine bezahlte Abo-Bestellung.
Das öffentlich zugängliche Repository ist keine Ablage für echte Bank-/Personaldaten.

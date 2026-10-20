# Aktueller Stand

Stand: 20.10.2026, Europe/Berlin. Phase: **Planung und Mockups**.

## Letzter Benutzerauftrag

Super-Admin soll sämtliche Landing-Inhalte einschließlich Modulpreisen zentral steuern.
Fachspezifikation, Prompt 10 und Mockup 12 ergänzen den Planungsstand.
Keine produktive Anwendung implementiert; konkrete Preise weiterhin offen.

## Vorhandene Ergebnisse

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
- Elf Bildmockups einschließlich Super-Admin für Landing, Module und Preise.
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

1. Super-Admin-Planung besprechen: Paket/Add-ons, Preisbezugsgröße und Freigaberechte;
   danach Beträge, Intervalle und Vertrags-/Bestandskundenregeln festlegen.
2. Als nächstes Fachmodul Ist-Zeiterfassung/Arbeitszeitkonto vorschlagen,
   damit Plan, tatsächlich geleistete Zeit, Pausen und Korrekturen getrennt bleiben.
3. Urlaubskonto Stufe A/B, Arbeitstage-/Feiertagsgrundlage, Wunschfrei-Wirkung,
   Freigabe/Vertretung und Gesundheitsdatenrechte bestätigen.
4. Schichtregel-/Tarif-/Schutzprofile, offene Plätze und Veröffentlichungsrechte klären.
5. DATEV-/Arbeitgebermodell und übrige Stations-/Rollen-/Aboentscheidungen bleiben offen.
6. Für Programmierung am neuen Rechner UMSETZUNGSUEBERGABE lesen und Stack/Basis
   plus konkreten ersten Implementierungsschritt ausdrücklich beauftragen.
7. Bis dahin keine produktive Anwendung implementieren; Vorschaucode separat halten.

## Noch nicht entschieden / nicht fertig

- Automatischer kostenpflichtiger Übergang oder aktive Abo-Bestätigung.
- Preise, Tarifgrenzen unterhalb von 100, Abrechnungsturnus, Kündigungsregeln.
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

Repository enthält Planungsdateien, zehn Bilder und eine lokal interaktive HTML-Vorschau;
keine neue produktive Anwendung, Datenbank oder Backend-Authentifizierung.
Laravel und Kotlin aus Altarchiven wurden nicht installiert/gestartet und nicht getestet.
Lokale `analysis-source/`-Ordner sind ignoriert und auf dem neuen Rechner nicht vorhanden.
Es gibt keine Datenbank, keinen Zahlungsanschluss und keinen Versanddienst für den Neuaufbau.

## Zu beachten

Mockups enthalten teilweise illustrative/abweichende Texte. Siehe `docs/mockups/README.md`.
Ein erteiltes Mandat ist keine bezahlte Abo-Bestellung.
Das öffentlich zugängliche Repository ist keine Ablage für echte Bank-/Personaldaten.

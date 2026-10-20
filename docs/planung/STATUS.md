# Aktueller Stand

Stand: 20.10.2026, Europe/Berlin. Phase: **Planung und Mockups**.

## Letzter Benutzerauftrag

Mitarbeiterverwaltung mit Mitarbeitereinladung planen, Grundlage DATEV.
Fortführung der bisherigen Arbeitsweise: Fachspezifikation, Modul-Prompt,
Mockup im gleichen Stil und GitHub-Ablage mit Protokoll/Übergabe aktualisieren.
**Noch nichts programmieren.**

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
- Acht Mockups insgesamt, zuletzt Mitarbeiterübersicht, Einladung und Selbsterfassung.
- Datenschutz-/SEPA-Leitfaden mit Quellen und offenen Punkten.
- Git- und Codex-Übergabeanleitung.

## Nächste sinnvolle Arbeit

1. Antwort zur gestellten Frage nach DATEV LODAS oder Lohn und Gehalt aufnehmen;
   bis dahin kein Zielprogramm als bestätigt behandeln.
2. Mitarbeiterfelder/-profile mit Lohnstelle, Arbeitgebermodell und gewünschtem
   Übergabeweg abstimmen; keine beliebige CSV als DATEV-Import ausgeben.
3. Personal-/Lohnrechte, Bankänderungsschutz und Erfassungszugang besprechen;
   bei Bedarf Prüf-/Rückfrageansicht zusätzlich mocken.
4. Offene Stations- und Rollenregeln bestätigen (Limit, Öffnungszeiten, Einladungsfrist).
5. Als nächstes Fachmodul Schichtplanung detailliert planen, falls Benutzer zustimmt.
6. Erst auf ausdrücklichen Implementierungsauftrag Code erzeugen.

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

## Technischer Zustand

Repository enthält Planungsdateien und Bilder; keine neue ausführbare Anwendung.
Laravel und Kotlin aus Altarchiven wurden nicht installiert/gestartet und nicht getestet.
Lokale `analysis-source/`-Ordner sind ignoriert und auf dem neuen Rechner nicht vorhanden.
Es gibt keine Datenbank, keinen Zahlungsanschluss und keinen Versanddienst für den Neuaufbau.

## Zu beachten

Mockups enthalten teilweise illustrative/abweichende Texte. Siehe `docs/mockups/README.md`.
Ein erteiltes Mandat ist keine bezahlte Abo-Bestellung.
Das öffentlich zugängliche Repository ist keine Ablage für echte Bank-/Personaldaten.

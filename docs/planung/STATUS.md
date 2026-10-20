# Aktueller Stand

Stand: 20.10.2026, Europe/Berlin. Phase: **Planung und Mockups**.

## Letzter Benutzerauftrag

Stationsverwaltung haarklein planen, mit Modul-Prompt und Mockup im gleichen Stil.
Neue Ergebnisse wieder im Repository `smp4000/Merlin_nova-space` sichern und
Status/Protokoll für einen Rechnerwechsel aktualisieren.
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
- Sieben Mockups insgesamt, zuletzt Stationsübersicht und Öffnungszeitenprofil.
- Datenschutz-/SEPA-Leitfaden mit Quellen und offenen Punkten.
- Git- und Codex-Übergabeanleitung.

## Nächste sinnvolle Arbeit

1. Stationsverwaltung besprechen: Status-/Limitzählung, Leitungsrechte für
   Öffnungszeiten und Stammdaten, Pause/Archiv mit laufenden Vorgängen bestätigen.
2. Öffnungszeiten-Versionierung, Länder-/Zeitzonenmodell und Ausnahme-Randfälle prüfen.
3. Rollen und Rechteumfang für Stationsleitung sowie vorgeschlagene
   Einladungsdauer von 7 Tagen bestätigen oder ändern.
4. Als nächstes Fachmodul Schichtplanung detailliert planen, falls Benutzer zustimmt.
5. Bei Bedarf Anlage-, Archivierungs- und Stationsleitungsansichten zusätzlich mocken.
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

## Technischer Zustand

Repository enthält Planungsdateien und Bilder; keine neue ausführbare Anwendung.
Laravel und Kotlin aus Altarchiven wurden nicht installiert/gestartet und nicht getestet.
Lokale `analysis-source/`-Ordner sind ignoriert und auf dem neuen Rechner nicht vorhanden.
Es gibt keine Datenbank, keinen Zahlungsanschluss und keinen Versanddienst für den Neuaufbau.

## Zu beachten

Mockups enthalten teilweise illustrative/abweichende Texte. Siehe `docs/mockups/README.md`.
Ein erteiltes Mandat ist keine bezahlte Abo-Bestellung.
Das öffentlich zugängliche Repository ist keine Ablage für echte Bank-/Personaldaten.

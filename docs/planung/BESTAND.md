# Bestand und Ziel

## Untersuchte Anhänge

- `ats_merlin-main.zip`: Laravel-Webanwendung mit Betreiber-/Partnerpanel und Mitarbeiter-PWA.
- `ats_merlin-mde-main.zip`: native Android-App für Scanner und Stationsgeräte.
- `ATS_Petersberg.jpg`: Benutzerfoto für Landingpage.

Untersuchung war statisch und stichprobenbezogen, keine vollständige Code-/Security-Prüfung.
Kein Testlauf und keine Aussage über Produktionsreife.

## Webprojekt

Deklarierter Stack: PHP >= 8.4, Laravel 13, Filament 5, Livewire 4 laut Dokumentation,
Tailwind 4, Vite, MariaDB/MySQL, Sanctum, Pest, Larastan, Pint.
17 Module: Absences, Access, Api, Articles, Billing, Cash, Employees, Faults, FuelThefts,
Giveaways, Inventory, Meters, Printing, Pwa, Scheduling, Tenancy, Vouchers.

Ermittelte Dateizählungen: 2.436 PHP-Dateien unter app (einschließlich 125 Blade-Dateien),
368 Dateien mit Namen *Test.php im Projekt. Keine Aussage über bestandene Tests.

## Android

Kotlin, Compose, Room; Build: Version 1.28.0, Code 47, minSdk 28.
181 Kotlin-Dateien im Hauptquellcode, 112 Dateien *Test.kt.
README-Einleitung nennt einen älteren Versionsstand; Dokumentation nicht blind übernehmen.

## Erkenntnisse für die Neugestaltung

- Web zuletzt grün/petrol umgestaltet, Android noch ältere blaue Tokens.
- Modularer Aufbau, Mandanten-/Stationskontext und Rechte sind wertvolle Referenzen.
- Navigation ist stark modulorientiert; Ziel ist eine aufgabenorientierte Übersicht.
- Dashboard bisher stark auf Stations-/Mitarbeiterkarten ausgerichtet.
- Schichtplanung benötigt einen eigenen dichten, lesbaren Entwurf.
- Offline-Verhalten ist pro Vorgang verschieden: nicht pauschal „offlinefähig“ versprechen.
- Mitarbeiterakte und Login bleiben getrennte Fachobjekte.
- Produktbeschreibung nennt auch geplante Funktionen. Zeiterfassung/Lohn nicht als
  fertig implementierte Module des Altbestands behaupten.
- Windows-Druckagent ist eine weitere Systemkomponente; eigener Quellcode nicht in den zwei Archiven enthalten.

## Ziel des neuen Projekts

Schrittweises Vorgehen: Landing → Partnerregistrierung/SEPA → Partner-Dashboard →
Team & Zugänge → Stationen → weitere Fachmodule. Aktuell ausschließlich Planung.
Keine Entscheidung über komplette Backend-Neuentwicklung aus Mockups ableiten.

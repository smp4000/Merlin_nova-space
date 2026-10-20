# Lokale Entwicklungsbasis

Stand: 20.10.2026, Europe/Berlin. Prompt 00 wurde ausdrücklich ausgeführt.
Freigegeben ist ausschließlich die lokale technische Basis unter `application/`.
Planungen und Mockups bleiben erhalten. Keine Landingpage, öffentliche Registrierung,
Abos, Fachmodule, DATEV-/Zahlungsintegration oder Bereitstellung implementiert.
Die unveränderte Laravel-Willkommensseite ist eine technische Standardseite.

## Tatsächlich installierte Versionen

| Bestandteil | Version |
|---|---|
| Host | Debian GNU/Linux 13.6, x86_64 |
| Laravel Framework | 13.38.0 |
| Laravel-Skeleton | 13.11.0 |
| Filament Panel Builder | 5.10.2 |
| Livewire | 4.4.7 |
| PHP CLI | 8.4.26, offizielles Debian-Bookworm-Image |
| Composer | 2.10.3 |
| MySQL | 9.7.2 LTS, MySQL Community Server – GPL, kein MariaDB |
| Node.js / npm | 24.19.0 LTS / 11.9.0 |
| Vite / Tailwind CSS | 8.3.4 / 4.3.3 |
| Docker Engine / Compose | 28.4.0 / 2.40.3 |

Neueste stabile Laravel-/Filament-Versionen wurden über offizielle Packagist-Metadaten
und die zugehörigen Quellen geprüft und gemeinsam von Composer aufgelöst. Laravel 13
benötigt PHP >= 8.3; PHP 8.4 ist unterstützt. PHP enthält unter anderem PDO MySQL,
mbstring, intl, bcmath, GD, ZIP, DOM/XML und OpenSSL. Keine umgangenen Plattformanforderungen.
PHP lädt hier keine einzelne `php.ini`, sondern die Extension-INI-Dateien unter
`/usr/local/etc/php/conf.d/`; Kontrolle: `bin/php --ini` und `bin/php -m`.

MySQLs offizieller Docker-Katalog führt 9.7 als LTS; zum Einrichtungszeitpunkt war
9.7.2 das verfügbare LTS-Image. Ein späterer Quellstand nannte 9.7.4, dessen Image
aber noch nicht veröffentlicht war. Verwendet wird das veröffentlichte Image,
mit SHA-256-Digest fixiert, ebenso die PHP-/Composer-Basisimages.

Quellen: [Laravel-Releases](https://github.com/laravel/docs/blob/13.x/releases.md),
[Filament-Installation](https://github.com/filamentphp/filament/blob/5.x/docs/01-introduction/02-installation.md),
[Laravel-Paket](https://repo.packagist.org/p2/laravel/framework.json),
[Filament-Paket](https://repo.packagist.org/p2/filament/filament.json),
[offizieller MySQL-Imagekatalog](https://github.com/docker-library/official-images/blob/master/library/mysql).

## Start und Stopp

Auf dem Entwicklungshost im Repository:

```sh
cd application
# Nach Checkout bzw. wenn Laufzeit/Abhängigkeiten/Datenbanken fehlen:
python3 bin/setup-local.py
# Normaler Start nach Einrichtung:
docker compose up -d --wait
# Status und Logs:
docker compose ps
docker compose logs --tail=50 app mysql
# Stopp; Datenbankvolume bleibt erhalten:
docker compose stop
# Wieder starten:
docker compose up -d --wait
```

Lokale Browseradresse: `http://127.0.0.1:8000/admin`.
Laravel-Standardseite: `http://127.0.0.1:8000/`.
Diese Adressen gelten auf dem Entwicklungshost, nicht als öffentliche Cloud-Vorschau.
App-Port 8000 und MySQL-Port 3307 sind ausschließlich an 127.0.0.1 gebunden.
Innerhalb des Compose-Netzes erreicht PHP den Dienst `mysql:3306`.
Das SQL-X-Protokoll ist nicht am Host veröffentlicht.
PHPs Entwicklungsserver liefert ausschließlich `application/public/` aus.
Keine Webserver mit dem Repository-Root als DocumentRoot starten.

Voraussetzungen: bestehende Docker-Laufzeit mit Compose, Python 3 und Node 24 LTS/npm.
Für andere Linux-Benutzer vor dem Start `LOCAL_UID`/`LOCAL_GID` passend exportieren.
Die Helfer nutzen Linux-Hostnetzwerk für Downloads; für Docker Desktop ist die
Hostnetzwerk-Unterstützung vorher zu prüfen. Es wurde keine zweite Laufzeit installiert.
Jede Cloud-Aufgabe ist bereits isoliert; den vorhandenen Checkout verwenden und
keinen Git-Worktree ohne ausdrücklichen Auftrag erstellen.

## Installation, Aktualisierung und lokale Secrets

`bin/setup-local.py` führt die geprüften Schritte aus: fehlende lokale Konfiguration
anlegen, PHP-Image bauen, Composer aus der Lockdatei installieren, `npm ci`, Assets bauen,
MySQL starten, ausstehende Standardmigrationen auf Dev/Test ausführen und lokalen Admin
anlegen. Wiederholung ersetzt weder vorhandene `.env`-Dateien noch Passwörter/APP_KEYs.
Composer veröffentlicht Filament-Assets durch den registrierten Installations-Hook neu.
Es ist weder erneutes `create-project` noch `filament:install` erforderlich.

`bin/build-runtime.py` verwendet vorhandene Proxyvariablen und bindet das vorhandene
Cloud-CA-Zertifikat als Build-Secret ein. TLS-, Paket- und Imageprüfungen bleiben aktiv;
Proxyadressen und Zertifikate sind nicht im Repository gespeichert.
`bin/composer.py` führt Composer mit derselben vorhandenen Proxy-/CA-Konfiguration aus.
Für einen normalen Rechner ohne Cloudproxy sind keine zusätzlichen Einstellungen nötig.

Der API-Downloadhost war gesperrt. Daher verweisen die GitHub-Archive in `composer.lock`
direkt auf den offiziellen `codeload.github.com/.../legacy.zip/<Commit>`-Endpunkt,
auf den GitHubs API ohnehin weiterleitet. Versionen, Commit-Referenzen und erwartete
Prüfsummen wurden nicht verändert. `bin/use-codeload.py` stellt diese URL-Form nach
bewussten späteren Dependency-Updates wieder her. Kein automatisches Major-Update.
Optionale externe Fontdownloads sind deaktiviert; Laravel und Panel verwenden Systemschriften.

Lokale Secretablage, niemals versionieren oder in Chat/Logs ausgeben:

- `application/.env`: Dev-DB-Zugang und eigener zufälliger APP_KEY.
- `application/.env.testing`: ausschließlich Test-DB-Zugang und separater APP_KEY.
- `application/.local/`: zufällige Dev-/Test-/Root-/Admin-Passwörter und lokale SQL-Initialisierung.
- `.local` hat Hostmodus 0700; Umgebungs- und Passwortdateien sind grundsätzlich 0600.
  Zwei ausschließlich für den MySQL-Container bindgemountete Dateien sind 0644 innerhalb
  dieses privaten Verzeichnisses, damit MySQLs eigener Benutzer sie lesen kann.

Admin: synthetisches Konto `admin@merlin.invalid`. Das zufällige Passwort ausschließlich
lokal aus `.local/admin-password` in einem vertrauenswürdigen Editor lesen.
`bin/php artisan merlin:create-local-admin` legt ein fehlendes Konto an und erhält
bestehende Konten/Passwörter. `LOCAL_ADMIN_EMAIL` bestimmt das einzig zugelassene Konto.
Der Zugang ist zusätzlich auf `local`/`testing` und das technische `admin`-Panel begrenzt;
im Produktionsmodus wird er abgewiesen. Dies ist kein produktives Super-Admin-Rechtekonzept.
Keine öffentliche Registrierung aktiviert; E-Mail wird nur lokal protokolliert.

MySQL-Datenbanken: `merlin_nova_dev` und `merlin_nova_test`, beide utf8mb4/
utf8mb4_0900_ai_ci. Benutzer `merlin_dev` bzw. `merlin_test` haben nur Rechte auf ihre
jeweilige Datenbank. Die App verwendet niemals Root. Das Volume `merlin-nova_mysql_data`
enthält die lokalen DB-Dateien außerhalb von Git. Nicht `docker compose down -v`
verwenden, wenn diese Daten erhalten bleiben sollen. Vorhandene fremde Volumes oder
Datenbanken nicht zurücksetzen/übernehmen. Bei Zugangskonflikten erst Herkunft klären.

## Build und Prüfungen

```sh
cd application
python3 bin/composer.py validate --strict
python3 bin/composer.py check-platform-reqs
bin/php artisan --version
bin/php artisan migrate:status
bin/php artisan migrate:status --env=testing
npm ci --cache .local/npm-cache
npm run build
bin/php artisan test
python3 bin/composer.py audit
npm audit
```

Tests laden `.env.testing` und verwenden echtes MySQL, keine SQLite-Ersatzdatenbank.
Die neuen Zugriffstests prüfen den DB-Namen vor ihren Datenoperationen und rollen
angelegte Testdatensätze per Transaktion zurück. Kein `migrate:fresh` oder DB-Reset
wurde für die Einrichtung verwendet.

Tatsächlich geprüft:

- Composer-Plattformanforderungen und strikte Manifest-/Lockvalidierung erfolgreich.
- Dev-/Test-Verbindungen und je drei Laravel-Standardmigrationen erfolgreich.
- Testbenutzer kann Dev-Daten nicht lesen; getrennte Rechte im Server geprüft.
- Asset-Build erfolgreich; npm-Audit ohne bekannte Schwachstellen.
- Acht Tests mit 30 Assertions erfolgreich: Laravel-Standards plus Admin-Login,
  Abweisung gewöhnlicher Benutzer, fehlende Registrierung, Produktionssperre und DB-Isolation.
- Echter Chromium-Browser: Gast wird zum Login umgeleitet, Admin meldet sich an,
  geschütztes Panel lädt ohne JavaScript-Fehler. `.env`, `composer.json` und Planungsdateien
  sind über den Webserver nicht abrufbar (404).
- Einrichtung wiederholt und MySQL-Erstinitialisierung auf einem separaten temporären
  Prüfvolume geprüft; produktives Dev-/Testvolume blieb erhalten.

Offen: Composer-Audit wurde ausgeführt, konnte aber den Sicherheitsdienst
`https://packagist.org/api/security-advisories/` wegen HTTP 403 des Cloudproxies nicht
abfragen. Ein fehlgeschlagener Audit ist **kein** bestandener Audit. Die notwendige
Domain `packagist.org` ist im Cloud-Konfigurationsentwurf ergänzt. Nach Speichern der
Netzänderung in den Umgebungseinstellungen `python3 bin/composer.py audit` wiederholen
und Befunde bewerten. Die Veröffentlichung der Cloud-Umgebung wurde nicht vorgenommen.

## Rechnerwechsel

Nur Quellcode, Manifest-/Lockdateien, Konfiguration mit Platzhaltern und Dokumentation
über Git übertragen. Danach obige Voraussetzungen bereitstellen und
`python3 bin/setup-local.py` ausführen. Neue lokale Secrets und Datenbanken werden angelegt;
die vorhandenen Cloud-Zugangsdaten sind absichtlich nicht auf GitHub.
`vendor/`, `node_modules/`, generierte Assets, Logs, `.env*`, lokale SQL-Dateien und
Datenbankdaten bleiben unversioniert. Bestehende lokale Daten erst separat und sicher
sichern; keine Datenbankdumps oder Zugangsdaten ins öffentliche Repository laden.

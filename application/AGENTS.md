# Merlin Nova – technische Basis

Zuerst die projektweiten Vorgaben in `../AGENTS.md`, den Status und
`../docs/leitfaeden/LOKALE-ENTWICKLUNG.md` lesen. Freigegeben ist ausschließlich
die lokale Laravel-/Filament-/MySQL-Basis. Weitere Module erfordern einen neuen Auftrag.

PHP und Composer laufen im vorhandenen Docker-Image, Node 24 LTS auf dem Host.
Keine zusätzliche PHP-Installation oder Agentenwerkzeuge aus dem Skeleton nachinstallieren.

- Einrichtung: `python3 bin/setup-local.py`
- Start: `docker compose up -d --wait`
- PHP/Artisan: `bin/php artisan ...`
- Composer: `python3 bin/composer.py ...`
- Assets: `npm run build`
- Tests: `bin/php artisan test` mit `.env.testing` und `merlin_nova_test`

Secrets, Datenbankvolumes und Benutzerdateien erhalten. Keine `.env`-Dateien,
Passwörter, Dumps oder generierten Assets committen. Kein `migrate:fresh` auf Dev.
Der Composer-Audit wartet noch auf die Netzfreigabe für `packagist.org`.

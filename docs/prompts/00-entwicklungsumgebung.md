# Start-Prompt 00 – Lokale Entwicklungsumgebung einrichten

Dieser Prompt ist für einen späteren ausdrücklich gestarteten Einrichtungsauftrag.
Seine Ablage führt ihn nicht aus. Hier wurden keine Werkzeuge oder Pakete installiert.

## Kopierbarer Arbeitsauftrag

Richte jetzt ausschließlich die lokale technische Entwicklungsbasis für Merlin Nova ein.
Lies zuerst AGENTS.md, STATUS, ENTSCHEIDUNGEN und UMSETZUNGSUEBERGABE. Dieser Auftrag
erlaubt die technische Basis, aber noch keine Fachmodule, Livezahlungen oder Bereitstellung.
Erhalte sämtliche Planungen, Mockups, Git-Historie und vorhandenen Benutzeränderungen.

1. Prüfe Betriebssystem, Projektstruktur und vorhandene Installationen: PHP samt aktiver
   php.ini/Extensions, Composer, Node/npm, Git sowie tatsächlich laufenden Datenbankserver.
   Prüfe Pfade, Dienste und Ports. XAMPP-MySQL-Bezeichnung ist kein Nachweis für Oracle
   MySQL: SELECT VERSION() und Serverherkunft prüfen, MariaDB nicht still gleichsetzen.
   Vorhandene Datenbanken/Dienste nicht löschen, ersetzen oder unbemerkt aktualisieren.

2. Verifiziere vor Installation die jeweils neueste stabile Laravel- und Filament-Version
   in deren offiziellen Dokumentationen und Paketmetadaten. Keine Beta/RC/dev-Versionen.
   Nutze die neuesten miteinander kompatiblen stabilen Releases. Falls neueste Laravel-
   und Filament-Releases nicht kompatibel sind, Konflikt und konkrete Alternativen zeigen,
   bevor eine abweichende Hauptversion gewählt wird. Keine Plattformanforderungen mit
   --ignore-platform-reqs umgehen. Prüfe passende unterstützte PHP-Version und Extensions
   einschließlich PDO MySQL sowie passende Node-LTS-/Composer-Version.

3. Lege eine neue Laravel-Anwendung unter application/ in diesem Repository an, sofern
   noch keine Anwendung existiert. Bei vorhandener application/ erst Zustand prüfen,
   sinnvoll fortsetzen und nichts überschreiben. Keine create-project-Installation in
   den bereits gefüllten Repository-Root und kein zweites verschachteltes Git-Repository.
   Root-Planung und Anwendung bewusst erhalten. Composer-/npm-Lockdateien versionieren.

4. Installiere Filament Panel Builder nach der offiziellen Anleitung der verifizierten
   Version. Richte zunächst ein lokales Admin-Basispanel ein, noch keine Ressourcen für
   Partner, Stationen, Personal oder Abos. Es ist ein technisches Grundpanel, noch kein
   fertiges Super-Admin-Rechtekonzept. Keine öffentliche Selbstregistrierung aktivieren.
   Beachte PowerShell-Versionconstraints und kontrolliere die tatsächlichen Abhängigkeiten.
   Kein Starterkit, Pluginpaket oder SaaS-Template ohne konkreten Bedarf hinzufügen.

5. Verwende echten MySQL Community Server in einer aktuellen unterstützten stabilen
   LTS-Reihe mit aktuellem Patchstand. Prüfe die verfügbare Reihe und PHP/PDO-Kompatibilität
   offiziell neu. Vorhandenen kompatiblen Server wiederverwenden. Fehlt MySQL, installiere
   ihn lokal isoliert aus offizieller Quelle bzw. nutze eine bereits vorhandene geeignete
   Containerlaufzeit; keine unnötige zweite Laufzeit installieren. Bei Portkonflikt einen
   freien lokalen Port wählen und dokumentieren, bestehende Dienste weiterlaufen lassen.
   Keine vorhandene MariaDB-Installation als vermeintliches MySQL-Upgrade überschreiben.

6. Erstelle ausschließlich neue lokale Datenbanken merlin_nova_dev und merlin_nova_test
   mit utf8mb4 und geeigneter MySQL-Kollation. Existierende gleichnamige Datenbanken nicht
   leeren oder ungeprüft übernehmen. Dedizierte Datenbankbenutzer nur für die jeweilige
   Datenbank, keine globale Root-Anmeldung der App. Secrets sicher erzeugen und lokal
   hinterlegen; nicht in Git, Shell-Historie, Screenshots oder Abschlussbericht ausgeben.
   Server und Entwicklungsdienste nur lokal erreichbar machen.

7. Konfiguriere application/.env für lokale Entwicklung und MySQL, generiere APP_KEY.
   application/.env.example nur mit Platzhaltern pflegen. Prüfe verschachtelte Gitignore-
   Regeln: .env, Dumps, Datenbankdateien, vendor/, node_modules/ und Logs bleiben lokal.
   Dokumentiere nicht geheime Host-/Port-/DB-Namen. E-Mail lokal protokollieren statt
   versenden, keine echten Zahlungs-/DATEV-/Kundendaten verwenden.

8. Führe nur Laravel-Standardmigrationen auf der nachweislich eigenen neuen Dev-Datenbank
   aus. Kein migrate:fresh/reset auf vorhandenen Datenbanken. Testumgebung explizit auf
   merlin_nova_test konfigurieren, damit Tests keine Entwicklungs-/Fremddaten verändern.
   Falls ein Demo-Admin für die lokale Prüfung nötig ist, ausschließlich synthetische
   Daten und sicher lokal verwaltetes Passwort; keine Standardpasswörter im Repository.
   Begrenze Panelzugang explizit auf das autorisierte lokale Admin-Konto, nicht jeden User.

9. Installiere benötigte Frontendabhängigkeiten, baue Assets und prüfe:
   Composer-Plattformanforderungen, Laravel-Version/Start, MySQL-Verbindung und Migrationen,
   erfolgreiche Assetkompilierung, vorhandene Basistests auf getrennter Testdatenbank,
   Admin-Login und Abweisung ohne Anmeldung. Prüfe dokumentierte Zugriffsbegrenzung.
   Dependency-Audit ausführen, Befunde bewerten und dokumentieren; keine blinden
   Major-Updates/--force-Fixes. Keine Datenschutzkonformität aus erfolgreichem Login ableiten.

10. Erstelle docs/leitfaeden/LOKALE-ENTWICKLUNG.md mit tatsächlich installierten Versionen,
    Projektpfad, Start-/Stopp-/Build-/Testbefehlen, lokalen URLs, DB-Port, Secretablage-
    Verfahren ohne Secretwerte und Rechnerwechsel-Schritten. Anwendung über public/
    ausliefern, nicht den gesamten Repository-Ordner im Webserver freigeben. Keine .env-
    oder Planungsdateien durch falschen DocumentRoot öffentlich ausliefern.
    Halte STATUS/PROTOKOLL und tatsächlichen Implementierungsstand aktuell.
    Sichere ausschließlich geprüfte Quell-/Konfigurations-/Lock-/Dokumentationsdateien
    im autorisierten GitHub-Repository. Keine Secrets, Binärinstallationen oder DB-Dumps.

Arbeite notwendige reversible Einrichtungsschritte selbstständig ab. Bei fehlenden
Adminrechten oder fehlendem Secretzugang frage gezielt nach der konkreten Voraussetzung,
ohne geheime Werte im Chat anzufordern. Berichte zum Schluss tatsächliche Versionen,
lokale Startadresse, durchgeführte Prüfungen und verbleibende Hindernisse. Stoppe nach
der technischen Basis; keine Landing, Abos, Registrierung oder Fachmodule implementieren.

## Verifikationsstand und offizielle Quellen

Am 20.10.2026 geprüft: Laravel-Dokumentation führt 13.x, Filament führt 5.x.
Laravel 13 verlangt mindestens PHP 8.3; Filament nennt PHP 8.2+, Laravel 11.28+ und
Tailwind 4.1+. Die gemeinsame Laufzeit muss die strengeren tatsächlichen Paketanforderungen
erfüllen. Patchstände nicht hier einfrieren; später neu prüfen und Lockdateien sichern.
MySQL-LTS-Reihe gezielt prüfen, nicht automatisch das gerade beworbene Innovation-Release
wählen. Diese Quellenprüfung ersetzt keine Installation oder getestete Paketauflösung.

- [Laravel Releases](https://laravel.com/docs/13.x/releases)
- [Filament Installation](https://filamentphp.com/docs/5.x/introduction/installation)
- [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/)
- [MySQL Release-Modell](https://dev.mysql.com/doc/refman/9.1/en/mysql-releases.html)

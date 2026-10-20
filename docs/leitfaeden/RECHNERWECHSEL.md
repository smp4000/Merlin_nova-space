# Auf einem anderen Rechner mit Codex fortsetzen

## Erstes Mal

1. Git und Codex auf dem anderen Rechner bereitstellen.
2. Repository klonen:

   ```sh
   git clone https://github.com/smp4000/Merlin_nova-space.git
   cd Merlin_nova-space
   ```

3. Genau diesen lokalen Ordner als Projekt in Codex öffnen.
4. Als erste Nachricht verwenden:

   > Lies AGENTS.md, docs/planung/STATUS.md, ENTSCHEIDUNGEN.md und PROTOKOLL.md.
   > Wir planen Merlin Nova weiter, noch nichts programmieren.
   > Fasse den aktuellen Stand kurz zusammen und arbeite an meinem nächsten Auftrag.

AGENTS.md ist der Einstiegspunkt im Repository. Die Projektdateien stehen nach dem Klonen
zur Verfügung; ein alter Chat wird nicht automatisch als Verlauf auf einen neuen Chat übertragen.
Es ist kein automatischer Hintergrundabgleich oder geräteübergreifender Zustand eingerichtet.

Für einen späteren ausdrücklichen Programmierauftrag gibt es zusätzlich die
[Umsetzungsübergabe mit Startprompt](UMSETZUNGSUEBERGABE.md). Sie beschreibt den
tatsächlichen Stand, offene Voraussetzungen und die modulweise Entwicklungsreihenfolge.
Die Vorlage nicht als aktuelle Freigabe interpretieren; gewünschtes Modul und Stack zuerst festlegen.

## Vor jedem Rechnerwechsel

Aktuelle Ergebnisse, neue Bilder und Entscheidungen in den Dateien speichern.
Im Arbeitsverzeichnis kontrollieren:

```sh
git status
git add AGENTS.md README.md docs .gitignore
git commit -m "docs: Planungsstand aktualisieren"
git push
```

Nur vorhandene geänderte Dateien committen; keine Dateien mit Zugangsdaten aufnehmen.
Für Push braucht der andere Rechner eigenen autorisierten GitHub-Zugang; keine Tokens
aus diesem Rechner kopieren oder in das Repository schreiben.

## Bereits geklontes Repository aktualisieren

```sh
git status
git pull --ff-only
```

Erst lokale Änderungen sichern. Bei divergierter Historie nicht mit Force-Push oder Reset
überschreiben. Änderungen vergleichen und gezielt zusammenführen.
Nicht gleichzeitig auf zwei Rechnern ungeklärte Änderungen an denselben Dateien machen.

## Was mitkommt

- Prompts, Leitfäden, Mockups, Projektstatus und Entscheidungen.
- Commit-Historie als nachvollziehbare Änderungsgeschichte.

## Was nicht mitkommt

- Vollständiger Chat, lokale App-Einstellungen oder Anmeldedaten.
- Die alten ZIP-Archive und ignorierte `analysis-source/`-Kopien.
- Das separate Originalfoto ATS_Petersberg.jpg; das Motiv ist in den Landing-Mockups sichtbar.
- Eine fertige neue Anwendung; aktuell gibt es ausschließlich Planung.

Bei späterem Bedarf alte Quellen separat und sicher bereitstellen. Nicht ungeprüft öffentlich hochladen.

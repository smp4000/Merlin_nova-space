# Arbeits- und Übergabeprotokoll

## 20.10.2026 – Bestandsaufnahme und Gestaltung

1. Benutzer stellte `ats_merlin-main.zip` und `ats_merlin-mde-main.zip` bereit.
2. Statische Untersuchung von Struktur, ausgewählten Quelldateien, Dokumentation und Screenshots.
   Kein Start, kein Dependency-Install, kein Testlauf. Archive unverändert.
3. Erster Landing-Entwurf in Waldgrün/Limette erstellt; anschließend durch andere Stilrichtung ersetzt.
4. Benutzer gab ChatGPT-Stilreferenz an, die im Browser angesehen wurde:
   https://chatgpt.com/s/p_1712a53d86348191859849b5eeba390e
5. Neue Landingpage in Eisblau/Petrol mit eigenem Stationsfoto erstellt;
   Benutzer bestätigte: „Ja der Stil gefällt mir.“ Preise bleiben offen.
6. Partnerregistrierung geplant und vierteilige Bildschirmübersicht generiert.
7. Benutzer ergänzte verpflichtendes SEPA-Mandat während der Registrierung.
   Eigenes SEPA-Mockup und erweiterter Modul-Prompt erstellt.
8. Partner-Dashboard für Erstanmeldung mit einer Station geplant und generiert.
9. Benutzer fragte nach Umsetzung, korrigierte zu echter Anwendung und entschied danach
   ausdrücklich, hier nur weiterzuplanen. **Keine Anwendung wurde programmiert.**

## 20.10.2026 – Team & Zugänge und Ablage

Benutzerauftrag: Modul haarklein planen, Prompt und Mockup erstellen, alle bisherigen
Unterlagen in `https://github.com/smp4000/Merlin_nova-space.git` speichern.
GitHub-Prüfung ergab leeres **öffentliches** Repository.

Erstellt/gesichert:
- AGENTS.md als Einstieg für weitere Codex-Sitzungen.
- STATUS.md, ENTSCHEIDUNGEN.md, BESTAND.md und diese Übergabe.
- Prompts für Landing, Registrierung mit SEPA, Dashboard und Team & Zugänge.
- Ausführliche Team-Spezifikation einschließlich Rollen, Rechte, Einladungszuständen,
  Vertretung, Rechteentzug, personenbezogenen Daten und Prüfszenarien.
- Alle sechs generierten Mockups; erster Entwurf als überholt gekennzeichnet.
- Ursprüngliches Stationsfoto als lokale Gestaltungsreferenz; nicht öffentlich hochgeladen.
- Bild-Prompts als rekonstruiertes reproduzierbares Briefing dokumentiert;
  keine Behauptung, dass die automatisch erzeugten PNGs exakt reproduzierbar wären.
- Leitfäden für Rechnerwechsel, Datenschutz/SEPA und schrittweise Weiterarbeit.

Keine alten Projektarchive, Entwicklungs-Zugangsdaten oder echten Kunden-/Bankdaten
in die öffentliche Planungsablage aufgenommen. Altquellen bleiben lokal ignoriert.

Die automatische Freigabeprüfung blockierte zunächst den Push, weil er auch die separate
Originaldatei ATS_Petersberg.jpg enthalten hätte. Sichere Alternative: Originalfoto lokal
belassen, aus Index und noch unveröffentlichter Historie entfernen und nur die beauftragten
Mockups/Planungsunterlagen hochladen. Keine Änderung an der lokalen Originaldatei.

## 20.10.2026 – Stationsverwaltung

Benutzerauftrag: Stationsverwaltung haarklein mit Modul-Prompt und Mockup im
gleichen Stil planen, wieder auf GitHub speichern und Protokoll aktualisieren;
ausdrücklich noch nichts programmieren.

Vor Bearbeitung `origin/main` abgeglichen: kein Rückstand/keine fremden Änderungen.
Erstellt:
- `STATIONSVERWALTUNG.md`: Feldkatalog, drei Statusachsen, Liste/Anlage/Profil,
  reguläre/geteilte/übernächtige Öffnungszeiten, Datumsausnahmen, Zeitzone/DST,
  Team-/Geräte-/Fachmodulgrenzen, Rollenmatrix, Pause/Archiv/Restore,
  Änderungsverlauf, konzeptionelles Modell und Abnahmefälle.
- `docs/prompts/05-stationsverwaltung.md`: eigenständig nutzbarer Modulauftrag.
- Mockup 07: Stationsübersicht und Stationsprofil mit Öffnungszeiten im freigegebenen Stil.
- Bildbriefing, Galerie, Entscheidungen, Status und README ergänzt.

Detailregeln wie Limitzählung, Leitungsrechte, Zeitzonenvererbung und
Versionierung sind Vorschläge, keine stillschweigende Geschäftsfreigabe.
Bekannte Bildvereinfachungen in der Galerie festgehalten. Keine echten Stationsdaten,
Bankdaten, Originalfotodateien oder Anwendungscode in den neuen Dateien.
Lokale Markdown-Verweise/Codeblöcke und Git-Whitespace vor Veröffentlichung prüfen;
Git-Push über Remote-Commit vergleichen. Es gibt keine ausführbare neue Anwendung.

Nächster Schritt: Stationsregeln bestätigen und anschließend auf Benutzerwunsch
Schichtplanung als eigenes Modul planen. Automatische Aboverlängerung bleibt offen.

## Weiterführungsregel

Bei jedem Folgeauftrag Datum, Ergebnis, bestätigte Entscheidungen, offene Punkte
und nächste Arbeit ergänzen. Commit/Push-Status über Git prüfen, nicht aus diesem Text ableiten.
Das Protokoll ersetzt keinen vollständigen Chat-Export, enthält aber den Arbeitskontext.

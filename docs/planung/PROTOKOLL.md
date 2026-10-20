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

## 20.10.2026 – Mitarbeiter und Mitarbeitereinladung, DATEV-Grundlage

Benutzerauftrag: „mitarbeiter mit mitarbeiter einladung grundlage datev“.
Planungsmodus und autorisierte GitHub-Ablage aus den vorigen Aufträgen fortgeführt;
kein Programmierauftrag. Remote vor Arbeit geprüft: gleichauf mit lokalem main.

Offizielle DATEV-Informationen recherchiert: digitaler Personalfragebogen,
Arbeitgeber-Grunddaten, Mitarbeiter-Rücklauf/Prüfung und Übergabemöglichkeiten.
Keine aktuelle vollständige Importspezifikation festgestellt und keine tatsächliche
DATEV-Anbindung bestätigt. Asynchron gefragt, ob Kanzlei LODAS oder Lohn und Gehalt nutzt;
bis zur Antwort ausdrücklich produktneutrale Planung.

Ergebnisse:
- `MITARBEITER-UND-EINLADUNG.md`: Fachablauf, Arbeitgeber-/Beschäftigungsmodell,
  mehrstationale Einsätze, profilabhängige Feldgruppen, sichere Erfassungseinladung,
  mobile Selbstangaben, Prüfung/Übernahme, Dokumente, sensible Rechte, Austritt und
  DATEV-Vorbereitung mit Abnahmefällen.
- Prompt 06 und Leitfaden `DATEV-GRUNDLAGE.md` mit offiziellen Quellen/Mapping-Gerüst.
- Mockup 08 mit Mitarbeiterliste, Fragebogeneinladung und mobiler Selbsterfassung.
- Galerie/Bildbriefing, Entscheidungen, STATUS, README und AGENTS ergänzt.

Keine echten Identifikationsnummern, IBANs, Personaldokumente oder Passwörter veröffentlicht.
Keine geschützten DATEV-Originalformulare/-PDFs kopiert. Lohnberechnung, ELStAM/eAU,
Sofort-/SV-Meldung, Zahlungsauftrag und funktionierender DATEV-Export sind nicht umgesetzt.
Fragebogeneinladung ist keine Vergabe von Stations-/Benutzerrechten und kein Arbeitsvertrag.
Aufbewahrung/Erforderlichkeit und Zielmapping bleiben mit zuständiger Fachstelle abzustimmen.

Nächster Schritt: DATEV-Ziel und Mitarbeiterprofil/Prüfrechte klären, danach gegebenenfalls
Schichtplanung. Vor Veröffentlichung Markdown-Verweise/Fences und Git-Whitespace prüfen;
Remote-Commit nach Push mit lokalem Commit vergleichen.

## 20.10.2026 – Schichtplanung und spätere Programmierübergabe

Benutzer bestätigte Fortsetzung mit Schichtplanung, damit am anderen Rechner später
programmiert werden kann. Planungsmodus beibehalten, kein Anwendungscode angelegt.
Vor Arbeit Remote-Abgleich: lokal und origin/main gleichauf.

Erstellt:
- SCHICHTPLANUNG.md: Vorlagen, Bedarf/Positionen, Zeit-/Pausenmodell, mehrere Stationen,
  Regelzustände, versionierte Veröffentlichung, Konfliktrennen, Benachrichtigungen,
  Änderungen, eigene Mitarbeiteransicht und klar begrenzte spätere Tauschfunktion.
- Prompt 07 sowie offizieller Quellen-/Regelleitfaden mit Zeit-/Gültigkeitsgrenzen.
- Mockup 09 mit Wochenentwurf, Veröffentlichungsvorschau und eigener Mitarbeiteransicht.
- UMSETZUNGSUEBERGABE.md: tatsächlicher Repositoryinhalt, benötigte Entscheidungen,
  technische Modulreihenfolge, Definition fertig und späterer Startprompt.
- STATUS, Entscheidungen, AGENTS, README und Galerie/Bildbriefing aktualisiert.

Recherchiert wurden offizielle ArbZG-/JArbSchG- und Minijob-Zentrale-Informationen.
Keine allgemeine Tankstellen-Ausnahme, keine gesetzliche Override-Freigabe allein per
Begründung und keine Übernahme geplanter Stunden als geleistete/DATEV-Lohnstunden zugesagt.
Einige Einzelabrufe der Gesetzesseite waren technisch nicht erreichbar; Gesamtausgaben
und erreichbare Einzelregelquellen dienen der dokumentierten Orientierung.

Mockup enthält generative Vereinfachungen (siehe Galerie), insbesondere keine echte
Rechtsprüfung. Mitarbeiteransicht zeigt ein separates illustriertes Beispiel.
Offene Abo-/DATEV-/Stack- und fachliche Regelentscheidungen bleiben offen.
Noch nicht alle Fachmodule fertig geplant; sinnvoller nächster Planungsschritt ist
Abwesenheiten/Urlaub/Wunschfrei/Krankheit als Datenbasis für den Planer.

Vor GitHub-Sicherung Markdown-Verweise/Fences und Whitespace prüfen. Nach Push
lokalen/Remote-Commit vergleichen. Anwendungstests sind mangels Anwendung kein Prüfresultat.

## 20.10.2026 – Abwesenheiten, Urlaub, Krankheit und Verfügbarkeit

Benutzer sagte „weiter“ nach vorgeschlagenem Abwesenheitsmodul. Planungsmodus
und fortlaufende GitHub-Sicherung beibehalten. Remote vor Bearbeitung gleichauf.

Erstellt:
- ABWESENHEITEN.md: Arten, Rechte, Antrags-/Melde-/Nachweiszustände, Urlaubsanspruch
  Stufe A/B, Arbeitstageberechnung/Journal, Mehrstationeneinsatz, Entscheidungen,
  Krankheit/Urlaubsüberschneidung, Verfügbarkeit, Planwirkung und Abnahmefälle.
- Prompt 08 und offizieller Quellenleitfaden für Urlaub, Verfall, Anzeige/Nachweis und eAU.
- Mockup 10: Verwaltung, eigener Urlaubsantrag und Personal-Prüfansicht mit Planhinweis.
- Status, Entscheidungen, AGENTS, README, Bildbriefing und Umsetzungsübergabe aktualisiert.

Wichtige Vorschläge/Abgrenzungen: geprüfter Eröffnungsanspruch vor Vollautomatik,
ein Konto je Arbeitgeber statt doppeltem Stationsverbrauch, keine Selbstgenehmigung,
Krankheit wird gemeldet, Nachweis beeinflusst nicht automatisch Einsatzverfügbarkeit,
keine Diagnosen im Plan, kein pauschaler kalenderbasierter Urlaubsverfall.
GKV-Quellen zeigen verschiedene Gültigkeitsversionen, nicht als bereits implementierten
eAU-Abruf oder aktuelle pauschale Feldliste missverstehen. Keine Gesundheits-/Personaldaten
echter Personen ins öffentliche Repository aufgenommen. Alle Bilder verwenden Beispieldaten.

Nächster Vorschlag: Ist-Zeiterfassung/Arbeitszeitkonto. Vor Programmierung weiterhin
Stack/Basis und konkreten Implementierungsschritt autorisieren; Geschäfts-/Fachentscheidungen
nicht aus Bildern ableiten. Vor GitHub-Push Links/Fences und Whitespace prüfen,
anschließend Remote-Commit abgleichen; mangels Anwendung keine Anwendungstests behaupten.

## 20.10.2026 – Interaktives Dashboard

Benutzer: „kannst du mal ein interaktives dashboard machen“.
Begrenzten Mockup-Auftrag umgesetzt; Anwendungsmodule bleiben ungeplant/nicht implementiert
soweit bisher dokumentiert. Interaktiver Entwurf im bestätigten Eisblau-Petrol-Stil.

Ergebnisse:
- `docs/mockups/11-dashboard-interaktiv.html` als lokale Vorschauquelle.
- Übersicht, Stationen, Team, Schichtentwurf, Abwesenheiten und zentrale Vertragsansicht.
- Station-/Demo-Rollenwechsel, offene Plätze besetzen mit Beispiel-Zeitkollision,
  Urlaubs-/Wunschfrei-Status ändern, Station ergänzen, Einladung nur vormerken, Reset.
- Bedien-/Grenzen-/Prüfleitfaden, Mockup-Auftrag09 sowie Status/Galerie/Übergabe aktualisiert.

Browserprüfung: Darstellung angesehen, Dialoge geöffnet, stationsübergreifende
Kollision abgewiesen, zulässige Zuordnung mit Zähleränderung verifiziert, Rollenfilter
mit entfernter Vertragsnavigation und Beispiel-Genehmigung/Reset geprüft.
Geschützter Inline-Rahmen erlaubte keinen normalen Formsubmit; Vorschauaktionen deshalb
auf lokale Buttonhandler mit Validierung umgestellt. Kein echter Versand/Formularziel.
JavaScript-Syntax geprüft. Kein Beleg für reale Backend-Rechtesicherheit oder Fachregelvollständigkeit.

Nur fiktive Daten, keine Netzwerk-/Zahlungs-/DATEV-/E-Mailintegration. Die clientseitige
Rollenwahl ist ein Designvergleich, keine echte Anmeldung. Eingetragene Demo-E-Mails
werden nicht versandt und nicht im optionalen Hostzustand gespeichert.
Temporärer lokaler Prüfserver ist keine Bereitstellung/Produktivveröffentlichung.
Quelle für Rechnerwechsel im Repo sichern, nicht auf den lokalen Inline-Pfad verlassen.

## 20.10.2026 – Super-Admin für Landing und Modulpreise

Benutzer bestätigt zentrale Steuerung sämtlicher Landing-Inhalte inklusive Modulpreisen
im Super-Admin. Fachspezifikation SUPER-ADMIN-LANDING-UND-PREISE.md, Modul-Prompt 10
und Bildmockup 12 erstellt. Inhalte/Medien, Module/Abhängigkeiten, Tarife/Preisversionen,
Vorschau, Veröffentlichung, Plattformrechte und Audit geplant.

Vorgeschlagen: Speichern bleibt Entwurf; Veröffentlichung referenziert geprüfte Versionen.
Landing-Sichtbarkeit ist keine Kundenberechtigung. Neue Preise ändern bestehende
Verträge nicht automatisch; Preisänderungen für Bestandskunden brauchen eigenen Prozess.
Preise bleiben offen; kein bezahlter Abschluss ohne vollständiges Angebot.
30 Tage Trial und Pflicht-SEPA bleiben erhalten, Mandat ersetzt keinen Aboabschluss.
Keine Produktion programmiert, kein Zahlungs-/Kundenprozess ausgelöst.

Nächste Entscheidung: Paket-/Zusatzmodulmodell, Bezugsgröße, dann Preise/Intervalle
und Vertragsregeln. Übergabe und Indizes aktualisiert. Git-Sicherung separat prüfen.

## 20.10.2026 – Grundpaket, Zusatzmodule und Abrechnung

Auftrag: Grundpaket/Add-ons und Bezugsgröße planen, Preise offen lassen, nichts
programmieren und GitHub/Übergabe aktualisieren. Fachspezifikation GRUNDPAKET-UND-
ZUSATZMODULE.md und Modul-Prompt 11 erstellt; keine neue Bildvariante erforderlich.

Empfehlungen, noch nicht bestätigt: Grundpaket pro Vertragspartner mit einer Station,
weitere Stationsrechte und Zusatzpakete pro ausgewählter Station; zentrale Rechnung.
Personal/Schichtplanung/Abwesenheiten als Paket, Basisrechte und Schutzfunktionen inklusive.
Monatlicher Zyklus, Erweiterung zeitanteilig nach Bestätigung, Reduzierung zum zulässigen
Periodenende. Buchungszustand unabhängig von Stationsstatus/Archivierung.
Mengenbeispiele für 1/3/12/100 Stationen ohne Preise, Rechnungsaufteilung, Trial-/SEPA-
Grenzen, Datenobjekte und spätere Abnahme dokumentiert. Kein echter Vertrag/Zahlungsfluss.

Nächster Schritt: Vorschläge zu Paketumfang/Bezugsgröße/Änderungsregeln bestätigen,
danach Trialumfang und Vertrags-/Abrechnungsgrundlagen. Git-Status separat prüfen.

## 20.10.2026 – Mein Abo und erster Einrichtungsprompt

Benutzer bestätigt das zuletzt vorgestellte Paketmodell einschließlich monatlicher
Änderungsrichtung. E50–E52 und Übergabe entsprechend aktualisiert; Beträge, Detailfristen,
Trialübergang und technische Abrechnungs-/Anbieterfragen bleiben offen.
Mein-Abo-Fachspezifikation, Prompt 12 und Mockup 13 erstellt: Auswahl/Prüfung/Bestätigung,
Stations-/Paketmengen, Vormerkung/Rücknahme, Rechnungsrechte und Konflikt-/Fehlerfälle.
Auswahl verändert keine Buchung, fehlende Preise blockieren Bezahlabschluss.

Währenddessen zusätzlicher Wunsch: erster Prompt für Umgebung mit neuestem Laravel,
Filament und MySQL. Prompt 00 bereitgestellt, offizielle Quellen für Laravel 13.x,
Filament 5.x und MySQL gelesen; später tatsächliche stabile Patchstände neu verifizieren.
Keine Installation ausgeführt, keine echte DB angelegt, keine Fachmodule programmiert.
Dokumentation/Übergabe und Bildbriefing aktualisiert; Git-Sicherung separat verifizieren.

## Weiterführungsregel

Bei jedem Folgeauftrag Datum, Ergebnis, bestätigte Entscheidungen, offene Punkte
und nächste Arbeit ergänzen. Commit/Push-Status über Git prüfen, nicht aus diesem Text ableiten.
Das Protokoll ersetzt keinen vollständigen Chat-Export, enthält aber den Arbeitskontext.

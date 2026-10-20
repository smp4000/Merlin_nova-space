# Übergabe für spätere Programmierung auf einem anderen Rechner

Stand: 20.10.2026. **Aktuell weiterhin nur Planung.**
Dieser Leitfaden erlaubt nicht von sich aus den Start von Code, echten Einladungen,
Mandaten, Zahlungen, Deployment oder Datenmigration.

## 1. Was tatsächlich vorhanden ist

GitHub enthält Planungen/Prompts für Landing, Partnerregistrierung/SEPA,
Partner-Dashboard, Team/Zugänge, Stationen, Mitarbeiter/Einladung, Schichtplanung
und Abwesenheiten/Urlaubskonto. Zehn Mockups zeigen diese Bereiche. Es gibt keinen neuen Anwendungscode, keine
installierten Abhängigkeiten, Datenbank, Live-Integration oder bestandene Anwendungstests.
Alte Laravel-/Android-Archive wurden lokal statisch betrachtet, sind aber nicht auf GitHub.
Implementierungstechnologie und konkreter Übernahmeumfang sind noch offen.

Die Planungen reichen als detaillierte Arbeitsgrundlage. Sie bedeuten nicht, dass alle
Geschäfts-/Rechtsfragen oder sämtliche späteren Fachmodule abgeschlossen sind.
Ist-Zeiterfassung, DATEV-Export, Artikel/MHD/Kasse, Geräte/Druck usw. benötigen
eigene bestätigte Spezifikationen bzw. Abgrenzung. Die Abwesenheitsplanung liegt vor,
ihre Anspruchsprofile und sonstigen offenen Fachregeln müssen noch bestätigt werden.

## 2. Einstieg am neuen Rechner

Repository klonen/aktuellen Stand holen, Ordner in Codex öffnen. AGENTS.md und
STATUS/ENTSCHEIDUNGEN/PROTOKOLL lesen. Keine persönliche Wissensbasis auf altem PC voraussetzen.
Bilder unter docs/mockups prüfen; bekannte Abweichungen stehen in deren README.
Original-Stationsfoto bei nötigen neuen Fotobearbeitungen separat vom Benutzer anfordern;
öffentliche Mockups sind vorhanden, separate Originaldatei ist nicht veröffentlicht.

## 3. Vor dem ersten Implementierungsmodul entscheiden

| Thema | Warum es nötig ist | Was ohne Entscheidung möglich bleibt |
|---|---|---|
| Stack/Neuaufbau oder Bestand | Architektur/Dateistruktur/Authentifizierung | Planung/Prototyp nur nach Auftrag; keine bestehende Basis behaupten. |
| Rechtlicher Betreiber/Arbeitgeber | Vertrag, Rechnung, Personalakte | Neutrale Modelle/Beispieldaten, keine produktiven Rechtsdokumente. |
| Datenbank/Hosting | Migrationen, Mandantentrennung, Backups | Lokale isolierte Testumgebung nach Auftrag. |
| Rollen/Delegation | Sichere Zugriffsgrenzen | Restriktiver vorgeschlagener Default, Entscheidung dokumentieren. |
| Trial/Preis/Verlängerung | Vertrags-/Zahlungsfluss | Nicht kostenpflichtiger Teststatus mit klaren Grenzen; kein echter Einzug. |
| Zahlungsanbieter/Mandatsverfahren | Gültiger SEPA-Prozess | Provideradapter/Fakes, keine vermeintliche Checkbox-Live-Erteilung. |
| DATEV-Zielprofil | Feldmapping/Dateiformat/Import | Neutrale Personalstammdaten, kein bezeichneter DATEV-Export. |
| Gesetz-/Tarif-/Schutzprofile | Korrekte Planfreigabe | Integritätsprüfungen; notwendige Fachprüfung als unvollständig kennzeichnen. |
| Aufbewahrung/Empfänger | Personen-/Bank-/Dokumentschutz | Keine automatische irreversible Löschung oder Datenübermittlung. |

Offene Punkte nicht aus Bildern erfinden und nicht durch scheinbar funktionierende
Buttons kaschieren. Gleichzeitig unabhängig mögliche Entwicklungsarbeit in kleinen Schritten fortführen.

## 4. Technische Reihenfolge bei späterer ausdrücklicher Freigabe

### A – Projektbasis

Bestätigten Stack einrichten, lokale Beispieldaten/Testkonfiguration, Designsystem,
eigene Organisations-/Benutzer-/Stationskontexte und serverseitige Rechtegrenzen.
Keine echten Zugangsdaten in Repo. Lokale Tests für horizontale/vertikale Trennung.
Vorhandenen Altcode, falls bereitgestellt, zuerst gezielt abgleichen statt blind kopieren.

### B – Partner und Registrierung

Öffentliche Landing, Konto/E-Mail, Vertragspartner/Rechnung, Setup-Entwurf,
Trialzustände. SEPA nur mit bestätigtem Anbieter-Vertrag bzw. klarer Testimplementierung;
Pflichtmandat darf in Live-Registrierung nicht durch lokale „erteilt“-Fakeantwort umgangen werden.
Wiederholbarer Abschluss, kein automatischer Einzug ohne beschlossenen Vertrag.

### C – Stationen und Team

Station als Entwurf/aktive Station, sichere Liste/Detail/Grunddaten, Limit und
Wochenöffnung/Ausnahmen. Persönliche Einladungen und Annahme, konkrete Stationsrechte,
Widerruf/Sperre, Schutz des letzten Inhabers. Auslieferung in kleinen zusammenhängenden Modulen.

### D – Mitarbeiter

Personalakte/Beschäftigungsabschnitt/Einsatzstationen, profilabhängiger Fragebogen,
sicher begrenzter Erfassungszugang, Prüfübernahme und Dokumentenschutz.
Login-Verknüpfung explizit, DATEV-Integration separat. Keine automatische HR-Vollmacht für Planer.

### E – Dashboard und Schichtplanung

Dashboard aus vorhandenen echten Zuständen. Vorlagen/Entwurf/Zeiten/Pausen/Zuordnung,
Konfliktprüfung, fachlich freigegebene Regeln, Versionierung/Veröffentlichung,
Benachrichtigungs-Queue und eigene Mitarbeiteransicht.
Verträge, Abwesenheitsdaten und Zeitzonen müssen belastbar bereitstehen.
Das vorliegende Abwesenheitsmodul mit bestätigter Arten-/Rechtematrix und geprüftem
Eröffnungsanspruch/Journal (vorgeschlagene Stufe A) vor endgültiger Planintegration umsetzen.
Nicht eine Anfrage als genehmigt behandeln und Krankheit keinem Genehmigungsvorbehalt unterwerfen.
Tausch, iCal und Ist-Zeit nicht unbemerkt in erste Kernstufe einbauen.

### F – Externe/weitere Fachmodule

DATEV-Mapping und Testimport, Abo-/Zahlungsbetrieb, Zeiterfassung, Artikel/MHD/Kasse,
Scanner/Druck jeweils nach konkretem Auftrag und eigener Integrationsabnahme.
Kein Versprechen, dass Planstunden Lohnstunden oder Mockups fertige Module sind.

## 5. Definition „fertig“ pro Entwicklungsschritt

- Anforderungen/Annahmen und offene Punkte aktualisiert.
- Funktion im Browser mit realen lokalen Zuständen nachvollziehbar.
- Serverseitige Rechte und Datenisolation geprüft, keine bloßen Menüsperren.
- Relevante Prüfungen für den geänderten Fachprozess, Fehler und Wiederholungsfälle bestehen.
- Keine echten Personal-/Bankdaten, Passwörter oder Tokens im Repository/Testfixture.
- Keine erfundenen externen Erfolgszustände, klare Test-/Live-Trennung.
- Datenmigrationen/Versionsübergänge nachvollziehbar, keine unautorisierte Datenlöschung.
- STATUS/PROTOKOLL plus Start-/Testanleitung mit Commit/Git-Stand gesichert.
- Deployment, Einzug, Mail an echte Personen etc. nur als gesondert konkret autorisierte Aktion.

## 6. Späterer Startprompt – nur nach ausdrücklichem Programmierauftrag verwenden

```text
Ich möchte jetzt mit der tatsächlichen Programmierung von Merlin beginnen.
Lies AGENTS.md, STATUS.md, ENTSCHEIDUNGEN.md, PROTOKOLL.md und
docs/leitfaeden/UMSETZUNGSUEBERGABE.md sowie die betroffenen Modul-Prompts.
Die bisherigen Prompts wurden im Planungsmodus geschrieben und dienen als Anforderungen;
meine jetzige Anweisung autorisiert nur den unten genannten Implementierungsschritt.

Mein jetzt freigegebener Schritt: [KONKRETES MODUL UND UMFANG EINTRAGEN].
Bestätigter Stack/Basis: [EINTRAGEN; FALLS OFFEN ZUERST KLÄREN].

Prüfe Repository und vorhandene Änderungen. Setze nur den freigegebenen Schritt
in einer lokalen Entwicklungs-/Testumgebung um und verifiziere ihn angemessen.
Übernimm bestätigte Entscheidungen, kennzeichne Vorschläge/offene Punkte und
täusche keine DATEV-/SEPA-/Versand-Erfolge vor. Noch keine produktive Veröffentlichung,
echten Zahlungen, Einladungen oder Migration produktiver Daten durchführen.
Aktualisiere Fortschritt/Anleitung und sichere Änderungen nachvollziehbar im Repository.
```

## 7. Noch zu besprechende nächste Planung

Ist-Zeiterfassung und Arbeitszeitkonto: reale Kommen-/Gehen-/Pausenzeiten, Nachträge,
Korrekturen, Bestätigung und Abgleich mit Plan/Abwesenheit. Kein automatischer
Ist-/Lohnwert aus dem veröffentlichten Plan. Die vorliegende Abwesenheitsplanung
unterscheidet Wunsch/Antrag/Freigabe und Krankmeldung; konkrete Profile noch bestätigen.
Weitere Fachbereiche priorisieren, statt jetzt unbekannte Prozesse zu programmieren.

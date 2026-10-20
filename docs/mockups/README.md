# Mockup-Galerie

Alle Bilder sind KI-generierte Rasterentwürfe, keine funktionsfähige Software.
Status/Nummern beziehen sich auf die Planungsreihenfolge, nicht auf Implementierung.

| Datei | Status | Bedeutung |
|---|---|---|
| [01](01-landing-erster-entwurf.png) | Überholt | Erster Waldgrün/Limette-Entwurf; nicht aktuelle Stilrichtung. |
| [02](02-landing-freigegebener-stil.png) | Stil bestätigt | Eisblau/Petrol, eigenes Stationsfoto, Preise offen. |
| [03](03-partnerregistrierung-uebersicht.png) | Konzept | Vier Ansichten vor Ergänzung des verpflichtenden SEPA-Schritts. |
| [04](04-partnerregistrierung-sepa.png) | Konzept | SEPA-Pflichtschritt; Betreiberangaben und Mandatstext fehlen bewusst. |
| [05](05-partner-dashboard.png) | Konzept | Erster Einstieg als Inhaber, eine Station, leere Fachbereiche. |
| [06](06-team-und-zugaenge.png) | Konzept, neu | Zugangsübersicht und Einladung mit Stations-/Rechteumfang. |
| [07](07-stationsverwaltung.png) | Konzept | Stationsübersicht und Profil mit Öffnungszeiten/Zuständigkeiten. |
| [08](08-mitarbeiter-und-einladung.png) | Konzept | Mitarbeiterliste, Einladung zum Personalfragebogen und mobiler eigener Erfassungsbereich. |
| [09](09-schichtplanung.png) | Konzept | Wochenentwurf, Veröffentlichungsvorschau und eigene Mitarbeiteransicht. |
| [10](10-abwesenheiten.png) | Konzept, neueste Ansicht | Abwesenheitsverwaltung, eigener Urlaubsantrag und getrennte berechtigte Prüfung. |

## Bekannte Bildabweichungen – nicht als Anforderung übernehmen

- 01 ist nicht mehr aktuelle Gestaltung.
- 02 enthält „Bestände“/Bestandsübersicht: bisher kein festgelegtes Bestandsführungsmodul.
  Drei Abo-Karten sind Illustrationen, keine beschlossenen Tarife. SEPA-Pflichthinweis später ergänzen.
- 03 hat verkürzte/widersprüchliche Schrittanzeigen und „Firmenname laut Register“:
  nicht jede Gesellschaft ist eingetragen. Finaler Ablauf steht im Registrierungs-Prompt.
- 03/04 nennen keine automatische Verlängerung. Tatsächlich ist diese Geschäftsentscheidung noch offen.
- 04 zeigt kein fertiges bankakzeptiertes Mandat. Checkboxen und Platzhalter dürfen keinen
  gültigen Erteilungsprozess vortäuschen. „Keine Abbuchung“ gilt nur zum dargestellten kostenlosen Einstieg.
- 05 enthält interne Preismodell-Planung als UI-Text und „Bestände“ beim Import:
  später Enddatum/Vertragsstatus und Artikelstammdaten verwenden.
- 06 zählt im Reiter „Zugänge (3)“ eine offene Einladung mit; die Spezifikation verlangt
  getrennte Zählung, also im Beispiel 2 aktive Zugänge und 1 offene Einladung.
  In der unteren Ansicht ist Schritt 1 markiert, obwohl Stationen/Rechte sichtbar sind:
  später konsistente Schritte oder eine einheitliche Formularansicht wählen.
  „Einladung senden“ ist die ausdrückliche Versandbestätigung, kein zusätzlicher unklarer Folgeschritt.
  Rechte-Checkboxen sind beispielhaft, noch kein bestätigtes Rollenpaket.
- Logos unterscheiden sich leicht zwischen Bildern. Ein endgültiges Logo/Icon-System ist noch nicht festgelegt.
- 07 fasst Montag–Freitag für die Darstellung zusammen. Fachlich sind es Tagesregeln;
  der 24h-Modus gehört je Tag/Zeitplan, nicht als unklarer globaler Schalter unter alle Tage.
  Reguläre Woche und Ausnahmen sind gleichzeitig gezeigt, obwohl oben Reiter sichtbar sind:
  später entweder getrennte Reiter oder ausdrücklich eine gemeinsame Zusammenfassung wählen.
  „Vollständig“ bezieht sich auf das definierte Stationsprofil, nicht sämtliche Geräte-/Fachmodule.
  Kleine Stationsbilder sind generierte Platzhalter, keine echten Standortfotos.
  Einbindung von Stationsbildern ist noch keine beschlossene V1-Funktion.
  Inaktiv ist ein neutraler Betriebszustand, kein pauschaler roter Fehlerstatus.
- 08 zeigt eine verkürzte mobile Schrittfolge. Steuer/Sozialversicherung und nötige
  Nachweise fehlen als eigene Schritte im Bild, sind aber in der Fachspezifikation enthalten.
  Beschäftigungsspalte ist eine Zusammenfassung mehrerer Merkmale; Vollzeit/Teilzeit,
  Minijobprofil und Eintrittsstatus bleiben separate Datenfelder.
  Der Personalausschnitt ist eine berechtigte Personalverwaltungsansicht, nicht die
  Standardansicht jeder Stationsleitung. Ein Organisationsinhaber wird nicht automatisch
  als Beschäftigter angelegt; „Alex Beispiel“ ist nur ein frei gewählter Beispieldatensatz.
  „Geprüft“ heißt keine von DATEV bestätigte Übernahme. Separate Login-Vormerkung
  erzeugt keinen Zugang. 7 Tage Einladungsdauer bleiben Vorschlag.
  Der mobile Menüknopf darf nur eigene Erfassungsfunktionen, keine Administration öffnen.
- 09 enthält generierte Portrait-Platzhalter, keine echten Beschäftigtenfotos;
  eine Fotopflicht oder Personalbildfunktion ist nicht beschlossen.
  Die veröffentlichte Mitarbeiteransicht ist ein eigenes Beispiel und passt nicht
  positionsgenau zur oberen Entwurfsbelegung; keine Datenübernahme daraus ableiten.
  Der Satz unter der Bestätigung des offenen Platzes nennt den Plan versehentlich
  „vollständig“: fachlich bleibt der Platz offen und wird so berichtet. Bestätigung
  erlaubt nur nach beschlossener Betriebsregel Veröffentlichung, keine Behauptung voller Besetzung.
  Grün in der Prüfansicht bedeutet nur das dargestellte freigegebene Prüfergebnis,
  keine umfassende Rechtsgarantie; reale Pflichtregeln/Daten müssen zuvor stimmen.
  Die eigene Ansicht übernimmt im Bild Organisations-Avatar/Kopf vereinfacht;
  tatsächlicher Zugang und Navigation müssen ausschließlich den eigenen Umfang zeigen.
  Pausensummen im Bild ersetzen nicht das fachlich nötige Intervall-/Besetzungsmodell.
- 10 stellt eigene Mitarbeiteransicht und Genehmigungsansicht nebeneinander dar,
  aber sie gehören verschiedenen berechtigten Akteuren. Keine Selbstgenehmigung.
  30 Anspruchstage und die Vorschau von 5 Tagen sind ausdrücklich Beispieldaten,
  kein Standardanspruch oder allgemein gültige Mo–Fr-Berechnung.
  Vor Genehmigung muss Berechnung belastbar geprüft sein, nicht nur ein hübsches
  Vorschau-Badge. Das Feld Ablehnungsgrund ist nur bei Ablehnung Pflicht.
  Die Krankmeldungszahl ist ausschließlich für entsprechende Personalberechtigte;
  Planer-/Kollegenansicht erhält keine Gesundheitsübersicht oder Diagnosen.
  Noch keine eigene Krankheitserfassungsansicht oder eAU-Integration im Bild umgesetzt.

## Vorschauen

### Aktuelle Landing-Richtung

![Landing](02-landing-freigegebener-stil.png)

### Registrierung

![Registrierung](03-partnerregistrierung-uebersicht.png)

### SEPA-Schritt

![SEPA](04-partnerregistrierung-sepa.png)

### Partner-Dashboard

![Dashboard](05-partner-dashboard.png)

### Team & Zugänge

![Team](06-team-und-zugaenge.png)

### Stationsverwaltung

![Stationsübersicht und Öffnungszeiten](07-stationsverwaltung.png)

### Mitarbeiter & Mitarbeitereinladung

![Mitarbeiterübersicht, Personalfragebogeneinladung und Selbsterfassung](08-mitarbeiter-und-einladung.png)

### Schichtplanung

![Wochenentwurf, Prüfen und eigene Mitarbeiteransicht](09-schichtplanung.png)

### Abwesenheiten

![Verwaltung, eigener Urlaub und Freigabeprüfung](10-abwesenheiten.png)

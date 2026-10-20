# Super-Admin: Landing, Module und Preise

Stand: 20.10.2026. Planung, keine produktive Implementierung.

## 1. Auftrag und Grenzen

Bestätigt: Der Plattformbetreiber soll im Super-Admin die gesamte Landing steuern
können, einschließlich Modulpreisen. Das folgende Bedien-, Rechte- und Versionsmodell
ist ein Vorschlag zur Umsetzung dieser Anforderung. Konkrete Preise bleiben offen.
Der Super-Admin gehört zur Plattform; der Partner-Inhaber verwaltet seine Organisation.
Diese Rollen dürfen nicht durch denselben frei wählbaren Organisationsschalter entstehen.

## 2. Navigation und Arbeitsablauf

Bereiche: Website & Landing, Medien, Module, Tarife & Preise, Angebotsregeln,
Veröffentlichungen und Änderungsprotokoll. Partnerverwaltung bleibt ein eigener Bereich.

1. Aktuell veröffentlichten Stand und eigenen Entwurf sehen.
2. Texte, Medien oder Angebot bearbeiten; automatisch gespeicherten Entwurf kennzeichnen.
3. Desktop-/Mobilvorschau mit denselben strukturierten Daten wie die öffentliche Seite öffnen.
4. Unterschiede zur veröffentlichten Version prüfen.
5. Pflichtangaben, Modulabhängigkeiten und Abschlussfähigkeit prüfen.
6. Berechtigter Publisher veröffentlicht eine geprüfte Version.
7. Veröffentlichung, Bearbeiter und Zeitpunkt nachvollziehen; Rücknahme gezielt vorbereiten.

Speichern veröffentlicht nichts. Eine Vorschau ist nicht öffentlich indexierbar und
nicht über erratbare öffentliche Entwurfskennungen zugänglich. Unveröffentlichte Preise
gehören nicht in öffentliche APIs, HTML-Quelltexte oder Suchindizes.

## 3. Landing vollständig verwalten

| Bereich | Einstellbare Inhalte | Prüfung |
|---|---|---|
| Kopfzeile | Logo, Navigation, Reihenfolge, Login-/Registrierungslink | Nur existierende freigegebene Ziele |
| Hero | Überschrift, Kurztext, Bild, Alternativtext, Haupt-/Nebenaktion | Pflichttexte, Bildrechte, gültige Ziele |
| Vorteile | Titel, Beschreibung, Symbol, Reihenfolge, sichtbar/verborgen | Keine unbelegten Leistungsversprechen |
| Modulübersicht | Modulreferenz, Beschreibung, Bild, Status, Reihenfolge | Verbindung mit echtem Modulkatalog |
| Zielgruppen | Einzelunternehmer/Firma, mehrere Stationen erläutern | Rechtsform nicht aus Stationszahl ableiten |
| Ablauf | Registrierung, Einrichtung, Testphase | Mit tatsächlicher Angebotsregel abgleichen |
| Preise | Tarifkarten, Vergleich, enthaltene Module, Zusatzmodule | Beträge aus freigegebener Preisversion |
| FAQ | Frage/Antwort, Kategorie, Reihenfolge, Sichtbarkeit | Widerspruchsprüfung zu Preis/Trial |
| Kontakt | Ansprechpartner/Funktionsadresse, freigegebene Links | Keine erfundenen Kontaktdaten |
| Fußzeile | Navigation und versionierte Rechtsdokumente | Betreiber-/Rechtsprüfung vor Livebetrieb |
| Seitendaten | Titel, Beschreibung, Vorschaubild | Kein Entwurf als öffentliche Vorschau |

Neue Abschnitte zunächst aus freigegebenen Bausteinen hinzufügen. Kein beliebiges
HTML, JavaScript oder Tracking-Skript im Texteditor. Rich Text serverseitig bereinigen;
keine Geheimnisse oder technischen Zugangsdaten in Inhaltseinstellungen.
Medien mit Format-/Größenprüfung, sicheren Dateinamen und Metadatenprüfung behandeln.
SVG nur nach eigener sicherer Aufbereitung, alternativ zunächst Rasterbilder.
Das echte Stationsfoto nicht ohne gesonderte Freigabe als Original öffentlich hochladen.

## 4. Modulkatalog

Ein Modul hat einen stabilen technischen Schlüssel und einen veränderbaren Anzeigenamen.
Geplante Beispiele: Stationen, Team & Zugänge, Mitarbeiter, Schichtplanung, Abwesenheiten.
Diese Liste ist keine Bestätigung, dass bereits Funktionen implementiert sind.

Felder: Schlüssel, Titel, Kurz-/Langbeschreibung, Bild/Symbol, Sortierung,
Landing-Sichtbarkeit, fachlicher Status (geplant/beta/verfügbar/zurückgezogen),
Abhängigkeiten, erlaubte Tarife und Referenzen auf Preisversionen.

Vier unabhängige Fragen:

- Soll das Modul auf der Landing sichtbar sein?
- Ist die Funktion technisch und fachlich verfügbar?
- Gehört sie zum gebuchten Angebot?
- Darf der aktuelle Benutzer sie innerhalb seiner Stationen verwenden?

Ein Schalter „Landing sichtbar“ aktiviert keine Kundenfunktion. Ein Preis aktiviert
kein Modul. Entitlements werden später serverseitig aus dem gültigen Vertrag ermittelt,
danach greifen die persönlichen Rollen- und Stationsrechte.
Geplante Module dürfen als Ausblick erscheinen, aber nicht als sofort verfügbare
bezahlte Leistung angeboten werden. Zyklische Abhängigkeiten verhindern.

## 5. Tarife und Modulpreise

Tarif = Paket mit enthaltenen Modulen; Zusatzmodul = separat hinzubuchbare Leistung.
Ob es überhaupt mehrere Pakete oder nur ein Grundpaket mit Zusatzmodulen gibt, ist offen.

| Eigenschaft | Vorgesehenes Modell | Entscheidung |
|---|---|---|
| Betrag | Exakter Geldwert mit Währung, keine Gleitkommaabrechnung | Zahlen offen |
| Bezugsgröße | Organisation oder abrechenbare Station | Noch festzulegen |
| Intervall | Monat/Jahr nur nach bestätigtem Angebot | Offen |
| Steuerdarstellung | Explizites Preis-/Steuerprofil | Zielkunden/Steuerregeln prüfen |
| Enthaltene Leistung | Referenzen auf Module und Grenzen | Offen |
| Zusatzmodule | Kompatibilität und Voraussetzungen | Offen |
| Gültigkeit | Freigabestatus und gültig-ab, unveränderliche Preisversion | Vorschlag |
| Trial | Aktuell bestätigte 30 Tage | Kein Zahlungsabschluss durch Mandat |

„Offen“ ist kein Nullpreis. Kein automatisch erfundener Rabatt oder durchgestrichener
Vergleichspreis. Jahressummen und Monatsäquivalente nur mit eindeutiger Bezugsgröße,
gleicher Steuergrundlage und transparentem tatsächlichen Zahlungsintervall anzeigen.
Bei Stationspreisen erst klären, welche Status zählen und wie Zu-/Abgänge abgerechnet
werden. Keine stille Gleichsetzung von 100 möglichen und 100 kostenpflichtigen Stationen.
Mitarbeiterpreise, Staffelpreise, Gutscheine und individuelle Angebote sind spätere
optionale Erweiterungen, keine beschlossenen Geschäftsmodelle.

## 6. Angebotsregeln und Registrierung

Die Landing bezieht Testdauer und Angebotsaussagen aus derselben freigegebenen
Regelversion wie die Registrierung. Ausgangswert bleibt 30 Tage. Spätere Änderungen
solcher Geschäftsregeln benötigen eigene berechtigte Bearbeitung, Prüfung und
Gültigkeit für neue Abschlüsse; laufende Testphasen behalten ihren vereinbarten Stand.
Ein Texteditor darf nicht durch Änderung einer Überschrift die Testdauer verändern.

Registrierung: Vertragspartner, Rechnungsprofil, Zahlungsprofil und Pflicht-SEPA bleiben
getrennt. Ohne erforderliches Mandat kein regulärer Abschluss des registrierten Setups.
Das Mandat ersetzt weder eine Preisfreigabe noch den kostenpflichtigen Vertragsabschluss.
Nach Testende bezahlt oder stillgelegt; automatische kostenpflichtige Verlängerung
gegenüber ausdrücklicher Aktivierung ist weiterhin eine offene Entscheidung.

Solange Preise oder Vertragsgrundlagen fehlen, darf es eine öffentliche Informationsseite
geben. Bezahlter Abschluss bleibt gesperrt. Ob eine echte kostenlose Registrierung schon
freigeschaltet werden kann, hängt zusätzlich vom fertig geprüften Registrierungs-/SEPA-
und Datenschutzprozess ab. Ein fertiger Werbetext allein gibt diesen Prozess nicht frei.

## 7. Veröffentlichung und Checkout

Vorgeschlagene Zustände: Entwurf → zur Prüfung → freigegeben → veröffentlicht → ersetzt.
Ein Release referenziert die geprüften Inhalts-, Katalog-, Preis-, Regel- und
Rechtsdokumentversionen. Es gibt genau einen wirksamen aktuellen öffentlichen Stand
je vorgesehenem Geltungsbereich. Terminierte Veröffentlichung ist ein späterer Ausbau.

Vor Veröffentlichung prüfen:

- Pflichtinhalte, Medien und Links vorhanden; mobile Vorschau nutzbar.
- Sichtbare Modulstatus stimmen; keine nicht verfügbare Leistung als buchbar markiert.
- Preisbezugsgrößen, Intervall, Steuerdarstellung und Vertragsgrundlagen vollständig,
  falls bezahlter Abschluss aktiviert werden soll.
- Trial-/Registrierungsaussagen passen zur tatsächlichen Regelversion.
- Änderungen an Rechtsdokumenten haben die nötige fachliche Freigabe.
- Kein konkurrierender Entwurf hat die Ausgangsversion inzwischen ersetzt.

Veröffentlichung atomar umschalten; Cache/CDN-Invalidierung berücksichtigen. Öffentliche
Seite und Registrierung dürfen nicht unabhängig willkürliche „neueste“ Preise mischen.
Checkout rechnet serverseitig, validiert die angebotene Version und erzeugt eine
unveränderliche Angebots-/Vertragskopie mit Positionen, Mengen, Preisen und Dokumenten.
Clientwerte sind keine Preisautorität. Wird ein geöffnetes Angebot ungültig, aktualisierte
Bedingungen vor Abschluss anzeigen und erneut bestätigen lassen; keine stille Ersetzung.
Auch doppelte Abschlussversuche dürfen keinen doppelten Vertrag oder Einzug auslösen.

## 8. Bestehende Verträge und Rücknahme

Eine öffentliche Preisänderung ändert nicht automatisch vorhandene Verträge,
Rechnungen oder bereits bestätigte Angebote. Für Bestandskunden braucht es einen
separaten, noch festzulegenden Änderungsprozess mit fachlicher/rechtlicher Prüfung,
gegebenenfalls Information/Zustimmung und Zahlungsanbieterabgleich.
Keine pauschale Funktion „alle Kunden sofort auf neuen Preis umstellen“ planen.

Inhalt zurücksetzen: frühere Inhalte als neuen geprüften Entwurf übernehmen.
Preise zurücksetzen: historische Beträge nicht verändern, neue freigegebene Version
erzeugen oder eine weiterhin gültige Version ausdrücklich referenzieren.
Zurückgezogene Angebote nicht versehentlich wieder buchbar machen.
Vertrags- und Rechnungshistorie bleiben nachvollziehbar; Aufbewahrung separat klären.

## 9. Rollen, Datenschutz und Protokoll

| Plattformrolle als Vorschlag | Inhalte | Preise | Veröffentlichen | Kundendaten |
|---|---|---|---|---|
| Redaktion | Entwurf bearbeiten | Lesen nach Bedarf | Nein | Kein Standardzugriff |
| Angebotsverwaltung | Lesen | Entwurf bearbeiten | Nein | Kein Bank-/Personalzugriff |
| Publisher | Prüfen | Prüfen | Eigene explizite Berechtigung | Kein Standardzugriff |
| Plattformadministration | Berechtigungen verwalten | Nach expliziter Zuweisung | Nach expliziter Zuweisung | Getrennte Befugnisse |

Zum Start dürfen Rollen kombiniert werden; Berechtigungen trotzdem getrennt modellieren.
MFA für Plattformkonten vor Livebetrieb vorsehen, erneute Bestätigung kritischer Aktionen.
Vier-Augen-Freigabe optional nach Betreiberentscheidung; nicht als bereits beschlossen ausgeben.
Partnerkonten erhalten keinen Zugriff auf dieses CMS, auch nicht über direkte URLs/APIs.

Protokoll: Akteur, Zeitpunkt, Aktion, Objekt/Version, vorher/nachher und Prüfgrund.
Keine Bankdaten, Diagnosen, Zugangstoken oder vollständigen sensiblen Formulare ins Log.
Lese-/Schreibrechte und Aufbewahrung des Protokolls festlegen. Kein unbegrenztes
Kundentracking durch CMS-Funktion; Analyse-/Consent-System wäre ein eigener Auftrag.
Rechtsdokumentbearbeitung beweist keine DSGVO-Konformität.

## 10. Vorgeschlagene Datenobjekte

LandingPage, LandingRevision, Section, MediaAsset, ModuleDefinition, ModuleDependency,
PlanDefinition, PlanModule, PriceVersion, OfferPolicyVersion, LegalDocumentVersion,
PublicationRelease, Approval und AuditEvent. Später Subscription/SubscriptionItem,
OfferSnapshot und Entitlement getrennt ergänzen. Keine Datenbankmigration beauftragt.
Stabile IDs, Referenzintegrität, Versionskonflikte und serverseitige Rechte vorsehen.
Verwendete Module/Preise nicht hart löschen; archivieren und Referenzen erhalten.

## 11. Abnahmeszenarien für spätere Umsetzung

1. Redaktion speichert neuen Hero; öffentliche Landing bleibt unverändert.
2. Vorschau zeigt Entwurf; unangemeldeter Aufruf erhält keine Entwurfsdaten.
3. Publisher veröffentlicht geprüfte Inhalte; Desktop/Mobil liefern denselben Release.
4. Offener Preis erscheint als offen, bezahlter Abschluss ist serverseitig gesperrt.
5. Modul ausblenden entfernt seine Landingkarte, aber keine vorhandenen Kundenrechte.
6. Nicht verfügbares Modul kann nicht als sofort nutzbares Add-on abgeschlossen werden.
7. Preisänderung betrifft neue Angebote; bestehende Vertragskopie bleibt unverändert.
8. Manipulierter Browserpreis wird verworfen; Server verwendet gültige Preisversion.
9. Veralteter Checkout verlangt Prüfung der aktualisierten Bedingungen.
10. Zwei Publisher kollidieren kontrolliert; kein gemischter öffentlicher Stand.
11. Rücknahme verändert keine alte Rechnung und aktiviert kein gesperrtes Angebot.
12. Partner-Inhaber und Stationsleitung werden von sämtlichen Admin-Endpunkten abgewiesen.
13. Fehlender Pflicht-SEPA-Schritt wird nicht durch eine Landingänderung umgangen.
14. Neue Trialregel verändert keine laufende Testphase rückwirkend.

## 12. Nächste Entscheidungen

Zuerst Paket-/Zusatzmodulstruktur und Bezugsgröße, danach konkrete Preise,
Zahlungsintervall, Steuerdarstellung und Bestandskundenstrategie festlegen.
Außerdem Betreiberrollen, Freigabeprinzip und gewünschte Startabschnitte bestätigen.
Vor späterem Checkout: Trialende, Vertrag, Zahlungsanbieter und SEPA-Verfahren klären.
Umsetzungsreihenfolge: Plattformrechte → Katalog/Versionen → CMS/Vorschau → Landing →
Registrierung/Angebotskopie → ausdrücklich freigegebener Zahlungsprozess.

Mockup: [Super-Admin](../mockups/12-super-admin-landing-und-preise.png).
Arbeitsauftrag: [Modul-Prompt 10](../prompts/10-super-admin-landing-und-preise.md).

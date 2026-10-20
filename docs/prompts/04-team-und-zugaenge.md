# Modul-Prompt 04 – Team & Zugänge

```text
AUFTRAG
Plane Merlin „Team & Zugänge“ detailliert. Keine Implementierung, echten Benutzer,
Einladungsmails, Datenbankänderungen oder Zahlungen anlegen.
Lies AGENTS.md, docs/planung/STATUS.md, ENTSCHEIDUNGEN.md und
docs/planung/TEAM-UND-ZUGAENGE.md als vollständige fachliche Grundlage.

ZIEL
Ein Partner lädt persönliche Benutzer ein und vergibt nachvollziehbare Rollen
und Stationen. Eine Stationsleitung verwaltet eine oder mehrere ausdrücklich
zugewiesene Stationen. Eine Station kann mehrere Leitungen besitzen.
Keine gemeinsamen Accounts oder per E-Mail verschickten Passwörter.
Benutzerkonto und Personalakte bleiben getrennt.

DESIGN
Freigegebenes Eisblau/Weiß/Petrol mit dunkelblauer Schrift, dezenten Rahmen,
klaren Hauptaktionen, Status mit Text und Symbol und responsiven Ansichten.
Mockup 06 ist die visuelle Referenz; die Spezifikation geht vor Bildtexten.

FACHLICHE OBJEKTE
Persönliches Konto, Organisationsmitgliedschaft, Stationszuordnung,
Fachrolle/Recht, Einladung, Versandversuch, optionale Personalaktenverknüpfung
und minimale Zugriffshistorie konzeptionell trennen.
Keine automatische Mehrorganisationsfähigkeit voraussetzen.
Bestehenden Benutzer einer fremden Organisation nicht ungefragt übernehmen.

ROLLEN
Organisationsinhaber: zentrale Verwaltung, Stationen, berechtigte Benutzerverwaltung
und Vertrags-/Zahlungsverwaltung; sensible Personaldaten nur nach Fachrecht.
Stationsleitung: nur zugewiesene Stationen und explizite Fachrechte.
Kein Abo, keine Rechnungen, keine Bankdaten, kein SEPA, kein Inhaberwechsel.
Keine Benutzer-/Rechteverwaltung standardmäßig für Stationsleitung.
Mitarbeiter: nur eigenes Profil und ausdrücklich freigegebene Fachfunktionen.
Zentrale Verwaltung/Buchhaltung sind optionale, noch zu bestätigende Rollen.
Endgültige Rechtepakete als Vorschlag darstellen, nicht als bereits freigegeben.

ÜBERSICHT
Reiter Zugänge, Einladungen und Rollen. Suche Name/E-Mail, Filter Rolle/Station/Status.
Person, Rolle, Stationsumfang, Status und zulässige Aktionen darstellen.
Aktive Mitglieder und offene Einladungen getrennt zählen.
Paginierung für viele Benutzer und bis zu 100 Stationen.
Keine fremden Kollegen/Stationen über Suchtreffer oder Zähler verraten.

EINLADUNG
E-Mail Pflicht, Name optional; keine privaten Daten ohne Bedarf.
Rolle und mindestens eine Station für Stationsrollen ausdrücklich auswählen.
Mehrere Stationen mit unterschiedlichen Rollen/Rechten ermöglichen oder den
V1-Schnitt ausdrücklich als offen markieren.
Prüfansicht nennt Zieladresse, Stationen, Rechte und Ausschlüsse.
Versand nur nach bestätigter Aktion, Abbrechen versendet nichts.
7 Tage Gültigkeit ist Vorschlag, kein beschlossener Produktwert.
Neue Stationen werden nicht automatisch zugewiesen.

ZUSTÄNDE
Einladung: Entwurf, offen, angenommen, abgelaufen, widerrufen, ersetzt.
Versand getrennt: ausstehend, an Dienst übergeben, fehlgeschlagen.
Offene Einladung ist kein aktiver Zugang; gesendete Mail ist keine bewiesene Zustellung.
Token zufällig, gehasht gespeichert, einmalig, befristet und widerrufbar.
Neuversand invalidiert alten Link, begrenzt gegen Mailflut.
Passende bestätigte Zieladresse bei Annahme verlangen.
Neuer Benutzer setzt eigenes Passwort; vorhandener meldet sich selbst an.
Rechte, Stationen und Delegationsgrundlage bei Annahme erneut prüfen.
Wiederholte Annahme darf keine doppelten Konten/Mitgliedschaften erzeugen.
Versandfehler wiederholbar ohne Doppelanlage behandeln.

VERWALTUNG UND WIDERRUF
Rollen/Stationen mit Wirkungsübersicht ändern; Zugang sperren/entsperren,
Einladung widerrufen, Mitgliedschaft geordnet beenden.
Eigene Rechte nicht erhöhen und letzten aktiven Inhaber nicht entfernen.
Inhaberübergabe als gesicherten separaten Ablauf planen.
Aktuelle Berechtigung für Seiten, API, Dateien, Exporte und Jobs durchsetzen.
Rechteentzug invalidiert Caches/Sessions und relevante Tokens; keine Umgehung
über alte Exporte oder vor dem Entzug gestartete Jobs.
Gleichzeitige Bearbeitung darf entzogene Rechte nicht wiederherstellen.
Historische Urheberschaft behalten; Sperre ist keine Personalaktenlöschung.

DATENSCHUTZ
Nur nötige Kontaktdaten, restriktive Standardrechte, minimale Auditdaten.
Keine Bank-/Personaldaten im allgemeinen Zugangsverzeichnis.
Keine Klartextpasswörter, Tokens in Logs, Tracking in Einladungslinks
oder ungeprüfte dauerhafte Geräte-/IP-Protokollierung.
Aufbewahrung und Rechtsgrundlagen zweckbezogen definieren; keine Fristen erfinden.
MFA für privilegierte Konten als begründeten Vorschlag ausweisen.
Keine pauschale DSGVO-/Sicherheitsgarantie.

ABNAHME
Alle Szenarien aus der Spezifikation planen: horizontale Zugriffstrennung,
mehrere Leitungen/Stationen, neue Station ohne automatische Zuweisung,
Widerruf/Neuversand, falsches Konto, doppelte Annahme, entzogene Delegation,
deaktivierte Station, letzter Inhaber, konkurrierende Änderungen, API/Export,
Trial-Sperre, getrennte Personalakte, Mobile und Tastaturbedienung.

LIEFERE
1. Vollständige Rollen-/Berechtigungsmatrix.
2. Feldkatalog und Zustandsdiagramme.
3. Screens: Übersicht, Einladung, Prüfansicht, Zugang verwalten, Sperre/Entzug.
4. Konzeptionelles Datenmodell und Abgleichbedarf zum Altprojekt.
5. Datenschutz-/Protokollierungs-/Löschkonzept mit offenen Punkten.
6. Kleine spätere Implementierungsschritte mit prüfbaren Abnahmen.
Noch keinen Code schreiben.
```

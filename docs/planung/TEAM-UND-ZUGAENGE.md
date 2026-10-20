# Team & Zugänge – Fachspezifikation

Stand: 20.10.2026 · Planungsentwurf, keine Implementierung.
Zielbild: Persönliche Konten, verständliche Zuständigkeiten, kein unbeabsichtigter Datenzugriff.
Die folgende Matrix ist ein zu prüfender Vorschlag; nicht bereits als Benutzerfreigabe behandeln.

## 1. Begriffe und Grenzen

| Begriff | Bedeutung |
|---|---|
| Benutzerkonto | Persönliche Identität mit eigenem Anmeldeverfahren und bestätigter E-Mail. |
| Organisationsmitgliedschaft | Verbindung zwischen Benutzer und einem Partnerkonto mit eigenem Status. |
| Stationszuordnung | Ausdrücklich ausgewählte Stationen innerhalb derselben Organisation. |
| Rolle | Benanntes Bündel von Fachberechtigungen; zusätzlich immer Geltungsbereich prüfen. |
| Personalakte | Beschäftigungs-/Vertrags-/Personaldaten; kein Synonym für Benutzerkonto. |
| Einladung | Befristete, widerrufbare Aufforderung, eine Mitgliedschaft anzunehmen. |
| Inhaber | Verantwortlicher Kontoverwalter; nicht automatisch Alleingesellschafter oder Vertragspartner. |

Eine Person kann mehrere Stationen verwalten. Eine Station kann mehrere Leitungen haben.
V1 unterstützt nicht automatisch mehrere voneinander unabhängige Partnerorganisationen je Konto.
Bei Anmeldung mit bestehendem Konto einer anderen Organisation keine fremde Mitgliedschaft offenlegen.
Stattdessen ein kontrolliertes Klärungsverfahren anbieten. Organisationswechsel/Multi-Org ist gesondert zu planen.

## 2. Rollenmatrix – Vorschlag

| Tätigkeit | Organisationsinhaber | Zentrale Verwaltung (optional) | Stationsleitung | Mitarbeiter |
|---|---|---|---|---|
| Stationen sehen | Alle | Ausdrücklich freigegeben | Nur zugewiesene | Nur nötiger eigener Kontext |
| Neue Station anlegen | Ja, bis Limit | Nur explizites Recht | Nein | Nein |
| Partner-Stammdaten ändern | Ja | Nur explizites Recht | Nein | Nein |
| Rechnungen/Abo sehen oder ändern | Ja | Nein, standardmäßig | Nein | Nein |
| Bankdaten/Mandate verwalten | Ja, besonders geschützt | Nein, standardmäßig | Nein | Nein |
| Benutzer einladen | Ja | Nur explizites Recht | Nein, standardmäßig | Nein |
| Rechte/Stationen vergeben | Ja | Nur delegierbare Rechte im eigenen Bereich | Nein | Nein |
| Schichtplan bearbeiten | Bei Modulfreigabe | Bei Modulfreigabe/Recht | Bei Modulfreigabe/Recht, zugewiesene Station | Nein; eigene Pläne nur lesen |
| MHD bearbeiten | Bei Modulfreigabe | Bei Modulfreigabe/Recht | Bei Modulfreigabe/Recht, zugewiesene Station | Nur separat erteiltes Fachrecht |
| Personalakte sehen/ändern | Nur mit passendem Fachrecht | Nur mit passendem Fachrecht | Kein pauschaler Vollzugriff | Nur freigegebene eigene Angaben |
| Lohn/Bank/Dokumente von Mitarbeitern | Eigenes sensibles Fachrecht | Eigenes sensibles Fachrecht | Standardmäßig nein | Kein fremder Zugriff |
| Inhaberwechsel auslösen | Gesonderter gesicherter Vorgang | Nein | Nein | Nein |

Organisationsweite Verwaltung ersetzt keine notwendigen sensiblen Fachrechte.
Das Bild ist ein Einladungsbeispiel, keine allgemeine Freigabe für jede Stationsleitung.
„Zentrale Verwaltung“ und getrennte Buchhaltung sind optionale Ausbaustufen.

## 3. Berechtigungsmodell

Effektiver Zugriff = aktive Organisation und Mitgliedschaft + zugelassenes Modul +
erforderliches Fachrecht + passende Stationszuordnung + gegebenenfalls eigener Datensatz.

- Rechte serverseitig für Seiten, einzelne Datensätze, API, Suchtreffer, Dateien,
  Downloads, Exporte und Hintergrundaufträge prüfen.
- Unzugewiesene Stationen auch nicht in Zählern, Autovervollständigung oder Fehlertexten verraten.
- Stationsrollen nur mit nichtleerer Stationszuordnung aktivieren.
- Neue Stationen nicht automatisch an Stationsleitungen vergeben.
- Administrative Rollen nicht versehentlich durch Vereinigung mehrerer Stationsrollen erhalten.
- Mehrere Fachrollen nur nach explizit dokumentierter Vereinigungsregel; keine impliziten Deny-Regeln.
- Wer delegiert, darf weder fremde Stationen noch Rechte oberhalb der eigenen Delegationsgrenze zuweisen.
- Nutzer kann eigene Rechte und eigenen Inhaberstatus nicht erweitern.
- Änderungen an Rollen müssen Folgen für alle betroffenen Personen vor Bestätigung anzeigen.
- Kein eigenständiger frei formulierbarer Rollenbaukasten in V1, solange Katalog nicht beschlossen ist.

## 4. Bildschirm A – Übersicht

Kopf: „Team & Zugänge“, Organisation und aktuelle Stationsauswahl.
Primäraktion „Person einladen“ nur mit entsprechender Berechtigung.
Reiter: Zugänge, Einladungen, Rollen (letzterer zunächst erklärend, kein zugesagter Editor).

Tabelle:
- Person und geschäftliche Konto-E-Mail.
- Rolle bzw. unterschiedliche Rollen je Station zusammengefasst.
- Zugewiesene Stationen; lange Listen als Anzahl plus zugängliche Detailansicht.
- Status.
- Aktionen abhängig von Recht, eigenem Konto und Zielperson.

Suche nach Name/E-Mail und Filter nach Rolle, Station, Status.
Paginierung und serverseitig begrenzte Abfragen für 100 Stationen und viele Benutzer.
Zähler beziehen sich auf denselben gefilterten/berechtigten Umfang wie die Tabelle.
„Zugänge“ und „Einladungen“ getrennt zählen: offene Einladung ist noch kein aktives Konto.

Leere Ansicht: „Noch keine weiteren Zugänge. Laden Sie Ihre Stationsleitung ein.“
Suchen ohne Treffer, technische Ladefehler und fehlende Rechte jeweils unterscheidbar.
Stationengebundene Teamübersicht enthält ausschließlich zulässige Kollegen und nötige Kontaktdaten.

## 5. Bildschirm B – Einladung vorbereiten

1. Person: E-Mail Pflicht; Name optional. Whitespace entfernen, Adresse geeignet prüfen,
   keine providerabhängigen Plus-/Punkt-Umschreibungen. Anrede/Geburtsdatum unnötig.
2. Rolle und Stationen ausdrücklich wählen. Bei Stationsleitung mindestens eine Station.
   Suchbare Mehrfachauswahl, „Alle sichtbaren“ darf keine automatische Zukunftszuordnung erzeugen.
3. Rechte je Station zeigen; nur delegierbare Rechte anbieten. Unterschiede sichtbar machen.
4. Prüfansicht: Zieladresse, Stationsliste, Rolle, erlaubte Bereiche und ausdrückliche Ausschlüsse.
5. Versand erst nach bewusstem „Einladung senden“. Zurück/Abbrechen versendet nichts.

Einladungsdauer 7 Tage ist **Vorschlag**, konfigurierbar zu planen. Kein bereits entschiedener Wert.
Entwürfe optional serverseitig speichern; unbestätigte Eingaben erzeugen keinen Zugang.
Noch fehlende Module nicht als verfügbare Rechte versprechen.

## 6. Einladung, Versand und Annahme

Zustandsachsen trennen:
- Einladung: Entwurf → offen → angenommen / abgelaufen / widerrufen / ersetzt.
- Versand: ausstehend → an Versanddienst übergeben / fehlgeschlagen.
„An Versanddienst übergeben“ bedeutet nicht „gelesen“ oder zuverlässig „zugestellt“.

Vorgehen:
- Kryptografisch zufälliges einmaliges Token; serverseitig nicht im Klartext speichern.
- Link nur an bestätigte Zieladresse senden; Token nicht in Tracking, Logs oder Referer an Dritte geben.
- Mail: Absenderorganisation, Einladender soweit nötig, Rolle, Stationen, Frist, Annahmelink,
  Kontakt bei unerwarteter Einladung. Keine Personalakte/Passwörter/Bankdaten mitsenden.
- Token-Gültigkeit, Zieladresse und erlaubte Mitgliedschaft bei Anzeige und Annahme prüfen.
- Annahme mit passender bestätigter E-Mail: neuer Benutzer setzt eigenes Passwort;
  bestehender Benutzer meldet sich selbst an. Falsche Sitzung bekommt einen sicheren Kontowechselweg.
- Kein automatisches Zusammenführen anhand von Name, E-Mail-Ähnlichkeit oder Personalnummer.
- Rechte und Stationen bei Annahme erneut gegen aktuellen Zustand/Einladenden prüfen;
  gespeicherte alte Berechtigungen niemals ungeprüft aktivieren.
- Wiederholte Annahme ist idempotent und erzeugt keine zweite Mitgliedschaft.
- Bei Versandfehler Einladung sichtbar halten und Wiederholung anbieten.
- Neuversand ersetzt altes Token; alter Link verliert Gültigkeit. Rate-Limit gegen Mailflut.
- Duplikate innerhalb derselben Organisation zusammenführen oder verständlich anzeigen.
- Bei bereits aktivem Mitglied keine unnötige zweite Einladung; Verwalten-Aktion anbieten.
- Ausstehende Einladung nach Rechteänderung neu ausstellen, damit angezeigte Zusage und Inhalt stimmen.
- Erst Link-Annahme erzeugt/aktiviert Zugang; Bearbeiten im Admin kann Annahme nicht vortäuschen.

## 7. Bildschirm C – Zugang verwalten

Zeigen: Mitgliedschaftsstatus, sichtbare Stationszuordnungen, aktuelle Rollen/Rechte,
zulässige Stammdaten und relevante Änderungshistorie. Anmeldung/letzte Aktivität nur bei
nachgewiesenem Zweck und passender Berechtigung, nicht als pauschale Leistungsüberwachung.

Aktionen:
- Station hinzufügen/entfernen.
- Rolle/Fachrechte ändern.
- Zugang sperren/entsperren.
- Mitgliedschaft beenden (eigener Vorgang, keine sofortige Personaldatenlöschung).
- Offene Einladung erneut versenden oder widerrufen.
- Persönlichen Passwort-Reset-Link auslösen, niemals fremdes Passwort anzeigen/festlegen.

Vor Entzug klare Auswirkung zeigen: „Der Zugriff auf Station X endet sofort.“
Bei letzter Stationszuordnung entweder sperren oder Wechsel zu gültiger Rolle verlangen.
Keine aktive Stationsleitung ohne Geltungsbereich entstehen lassen.

## 8. Rechteentzug, Vertretung und Kontinuität

- Rechteänderung wirkt ab erfolgreichem Speichern auf den nächsten geschützten Zugriff.
- Veraltete Sessions/Berechtigungscaches invalidieren; mobile/API-Token berücksichtigen.
- Länger laufende Jobs, Exporte und Download-Links müssen aktuelle Berechtigung prüfen,
  damit Widerruf nicht über alte Downloads umgangen wird.
- Sperre einer Mitgliedschaft betrifft diese Organisation, nicht automatisch jede persönliche Identität.
- Gespeicherte Vorgänge behalten nachvollziehbare Urheberschaft; Austritt löscht nicht die Historie.
- Kein Verlust bereits gebuchter Fachvorgänge durch Sperre.
- Vertretung für mehrere Stationen nur explizit und bei Bedarf befristet; Ende automatisch prüfen.
- Gleichzeitige Bearbeitung erkennen, damit eine alte Maske entzogene Rechte nicht wiederherstellt.
- Letzten aktiven Organisationsinhaber nicht entfernen/sperren/demoten lassen.
- Inhaberübergabe mit erneuter Authentifizierung, Annahme der Zielperson und Protokoll planen.
- Plattform-Support ist kein heimlicher Organisationsinhaber. Gesonderter, begrenzter Zugriff später planen.

## 9. Personalakte und Gerät

Kontozugang allein legt keine Personalakte an. Verknüpfung ist optional, explizit und
innerhalb derselben Organisation eindeutig. Eine Leitung kann extern sein; Mitarbeiter kann
ohne Webzugang existieren. Keine automatische Verknüpfung über gleiche Namen.

MDE/PIN/NFC sind spätere, getrennte Anmeldewege mit eigenen Freigaben.
Eine Stationszuordnung darf nicht automatisch Bankdatenfreigabe oder universelle Geräte-PIN erzeugen.
Wenn Alt-API später übernommen wird, alle dort wirksamen Token bei Rechteentzug berücksichtigen.

## 10. Konzeptionelles Datenmodell

| Objekt | Wesentliche Attribute/Beziehungen |
|---|---|
| User | Persönliche Identität, verifizierte E-Mail, Authentifizierungsdaten. |
| OrganizationMembership | organization_id, user_id, Status, zentrale Rolle, Version. |
| StationRoleAssignment | membership_id, station_id, Rolle, optionale Gültigkeit. |
| Permission/Role | stabiler Katalog, delegierbare und sensible Rechte; keine Freitextrechte. |
| Invitation | organization_id, Zieladresse, Einladender, Token-Hash, Zustand, Ablauf, angenommene Mitgliedschaft. |
| InvitationGrant | vorgeschlagene Rolle/Rechte/Stationen, überprüfbarer Snapshot. |
| DeliveryAttempt | Status und sichere Fehlerklasse, Zeit; kein Token-/Mailbody-Klartext im Log. |
| EmployeeUserLink | explizite Verbindung zur Personalakte, gleicher Mandant, Eindeutigkeitsregel. |
| AccessAuditEvent | Akteur, Ziel, Art, minimaler Vorher-/Nachher-Rechteumfang, Zeitpunkt. |

Nur konzeptionell: bestehende Laravel-Modelle erst bei späterem Implementierungsauftrag
abgleichen. Nicht parallel unbemerkt zweites Rechte-/Mandantenmodell einführen.
IDs nach außen nicht erratbar; UUID allein ist keine Berechtigungsprüfung.

## 11. Datenschutz und Sicherheit

Datensparsame Felder, keine privaten Angaben ohne Zweck. Listen nicht als öffentlicher
Personalstamm gestalten. Unnötige Sichtbarkeit von anderen Beschäftigten vermeiden.
Passwörter nur sicher gehasht; Übertragung schützen. Für privilegierte Konten MFA und
erneute Authentifizierung bei sensiblen Änderungen als Entscheidungsvorschlag ausweisen.

Kein Pauschalversprechen „DSGVO-konform“. Verantwortliche, Zweck, Rechtsgrundlage,
Empfänger/Dienstleister, Fristen und Betroffenenrechte im Datenschutzkonzept konkretisieren.
Einladungen sind Betriebskommunikation, keine Newsletter-Einwilligung.
Aufbewahrung von Einladungen und Auditlogs nach Zweck festlegen; 7 Tage Linkgültigkeit
ist keine automatische Löschfrist für alle Daten. Keine dauerhafte Sammlung voller IPs
oder Geräte-Fingerabdrücke ohne dokumentierten Sicherheitszweck.

## 12. Benötigte Abnahmeszenarien

| Fall | Erwartung |
|---|---|
| Leitung nur an A | B weder in Suche, Zähler, Link, API, Datei noch Export erreichbar. |
| Leitung an A und B | Nur passende Rechte je Station, keine zentrale Administration. |
| Neue Station C | Kein automatischer Zugriff für bestehende Stationsleitungen. |
| Rollenänderung | Sofort wirksam; Vorschau und Audit vorhanden. |
| Geöffnete alte Maske | Kein Wiederherstellen zwischenzeitlich entzogener Rechte. |
| Falsche E-Mail-Sitzung | Einladung nicht mit anderem Konto annehmbar. |
| Einladung doppelt angenommen | Eine Mitgliedschaft, keine doppelten Zuweisungen. |
| Widerruf/Neuversand | Alter Link ungültig. |
| Station vor Annahme deaktiviert | Kein Zugriff über veraltete Einladung. |
| Einladender verliert Recht | Annahme prüft aktuelle Delegationsgrundlage; verweigert oder neu freigeben. |
| Versanddienst ausgefallen | Verständlicher Status, wiederholbar ohne Doppelzugang. |
| Fremde bestehende Organisation | Keine Offenlegung/Zwangszusammenführung fremder Konten. |
| Letzter Inhaber entfernt | Verweigert; Übergabeweg anbieten. |
| Personalakte ohne Konto | Besteht unabhängig weiter. |
| Konto gesperrt | Kein weiterer geschützter Zugriff/Export; Historie erhalten. |
| Trial abgelaufen | Kein Einladungsweg als Umgehung; erlaubte Vertragswege bleiben. |
| 100 Stationen, viele Personen | Suchbare, paginierte Ansichten statt riesiger Checkbox-/Tabellenliste. |
| Tastatur/Smartphone | Fokusführung, Labels, Fehlerzuordnung, kein ausschließlicher Farbstatus. |

## 13. Kleine spätere Umsetzungsschritte

1. Bestandsschema und Rechtekatalog abgleichen, offene Rollenentscheidungen bestätigen.
2. Serverseitige Leseberechtigungen und Zugangsübersicht.
3. Einladung als Entwurf mit Prüfmaske, noch ohne Versand.
4. Sicherer Versand/Annahme mit echten Zuständen und Wiederholbarkeit.
5. Rollen-/Stationsverwaltung, Sperre und Widerruf einschließlich API/Jobs.
6. Letzter-Inhaber-Schutz und Übergabe.
7. Mobile/Barrierefreiheit, Datenschutzprüfung und passende Integrationsprüfungen.

Keine dieser Stufen ist bereits implementiert.

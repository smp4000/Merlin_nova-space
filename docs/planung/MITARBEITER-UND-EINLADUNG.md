# Mitarbeiter und Mitarbeitereinladung – Fachspezifikation

Stand: 20.10.2026 · Planung, keine Implementierung.
Benutzerwunsch: Mitarbeiterverwaltung mit Mitarbeitereinladung, Grundlage DATEV.
DATEV-Zielprodukt wurde angefragt, ist bis zur Antwort offen. Nicht aus Altcode ableiten.

## 1. Was „Grundlage DATEV“ hier bedeutet

Der Personalprozess und die lohnrelevanten Feldgruppen werden DATEV-orientiert geplant.
Es entsteht ein eigener Merlin-Personalfragebogen, keine Kopie eines geschützten Formulars.
Keine DATEV-Partnerschaft, Zertifizierung, funktionierende Schnittstelle oder Importfähigkeit
behaupten. LODAS und Lohn und Gehalt als unterschiedliche Zielprofile behandeln.
Offizielle Recherche und Grenzen: `docs/leitfaeden/DATEV-GRUNDLAGE.md`.

Vorgeschlagener Ablauf: Arbeitgeber legt Mitarbeitergrunddaten an → fordert Angaben
an → Mitarbeiter bestätigt Zugang und ergänzt eigene Angaben → berechtigte Personalstelle
prüft → übernimmt explizit in die Personalakte → bereitet gegebenenfalls Übergabe an Lohnbüro vor.
Merlin rechnet keinen Lohn ab, ruft nicht automatisch ELStAM/eAU ab, erstellt keine
Sozialversicherungs-/Sofortmeldung und überweist kein Gehalt in diesem Modul.

## 2. Begriffe und Arbeitgebergrenze

- Person: identifizierbarer Mensch, keine Stationsrolle.
- Personalakte: zweckgebundene Beschäftigtenunterlagen eines Arbeitgebers.
- Beschäftigungsverhältnis: Arbeitgeber, Eintritt, Austritt, Vertrags-/Arbeitszeitregeln.
- Stationseinsatz: gültige Zuordnung für den Arbeitsort, nicht automatisch rechtlicher Arbeitgeber.
- Persönliches Benutzerkonto: Zugang zu Merlin-Funktionen, separat einzuladen/zu verknüpfen.
- Erfassungszugang: zeitlich begrenzt nur für eigenen Fragebogen; kein Stationszugriff.
- Lohnstammdaten: lohnrelevante geprüfte Angaben, eingeschränkter Zugriff.
- DATEV-Zuordnung: konkreter Lohnmandant/Arbeitgeber und Personalnummer im bestätigten Zielsystem.

100 Stationen bedeuten nicht 100 Arbeitgeber. Beschäftigung an mehreren Stationen desselben
Arbeitgebers darf nicht mehrere Personalakten oder Personalnummern erzeugen.
V1-Vorschlag: ein rechtlicher Arbeitgeber innerhalb des Partnerkontos. Nicht ungeprüft aus
Merlin-Vertragspartner oder Stationsanschrift ableiten. Konzern/mehrere Gesellschaften als
Arbeitgeber braucht eigenen Schnitt; nicht mit Filialzuweisung vortäuschen.
Wechsel zu einem anderen rechtlichen Arbeitgeber ist kein einfacher Stationswechsel.

## 3. Drei unabhängige Zustandsgruppen

### Beschäftigung

Entwurf → Eintritt geplant → beschäftigt → ausgeschieden; Storno vor Eintritt gesondert.
Datum allein darf keinen ungeprüften Vertrag erzeugen. Wiedereintritt als neuer
Beschäftigungsabschnitt mit Historie, keine stille Wiederbelebung alter Konditionen.

### Fragebogen

Nicht angefordert → Entwurf → eingeladen → in Bearbeitung → eingereicht →
Rückfrage/erneute Bearbeitung → geprüft/übernommen → abgeschlossen bzw. storniert.
Jede Einreichung hat Version und Zeitpunkt. Link abgelaufen ≠ Daten gelöscht.
Versand ausstehend/übergeben/fehlgeschlagen als eigene Achse, nicht mit Annahme verwechseln.

### Systemzugang und Übergabe

Merlin-Zugang: keiner / separat eingeladen / aktiv / gesperrt; unabhängig von Beschäftigung.
DATEV-Vorbereitung: Ziel offen / Zuordnung fehlt / Prüfung offen / freigegeben /
Datei erstellt / übergeben / mit belastbarer Rückmeldung übernommen / abgelehnt.
Diese Übergabestatus nur anbieten, wenn entsprechender tatsächlich implementierter Weg existiert.
„PDF erstellt“, „Datei heruntergeladen“ und „in DATEV übernommen“ sind verschiedene Aussagen.

## 4. Arbeitgeber legt an – Bildschirm A/B

Minimal für Einladung:
- Vorname, Nachname.
- Persönliche Kontakt-E-Mail oder ausdrücklich gewählter alternativer Erfassungsweg.
- Rechtlicher Arbeitgeber fest aus autorisiertem Kontext bzw. ausdrücklich bestätigt.
- Geplanter Eintritt, soweit bekannt.
- Stammstation sowie weitere Einsatzstationen, mit gültig-ab und später gültig-bis.
- Beschäftigungsprofil nur sofern Arbeitgeber es bereits kennt; keine sozialeinstufende Automatik.

Entwurf ohne Steuer-/SV-/Bankangaben erlauben. Kein Zwang, schon alle Lohndaten zu kennen.
Interne Personalnummer unabhängig von DATEV-Personalnummer, abgestimmte Eindeutigkeit pro
Arbeitgeber/Lohnmandant. Nummern als Text behandeln, führende Nullen erhalten, nie recyceln
ohne ausdrücklich geklärte Regel. Abgleich mit Kanzlei vor finaler DATEV-Zuordnung.

Beschäftigungsmerkmale in getrennten Feldern:
- Arbeitszeitmodell Vollzeit/Teilzeit/variabel.
- Abrechnungs-/Beschäftigungsprofil regulär/geringfügig/kurzfristig/Ausbildung/weiterer Fachfall.
- Befristet/unbefristet und geplantes Ende.
- Stundenlohn/Gehalt und wirksame Vergütungsvereinbarung.
Nicht „Teilzeit“ und „Minijob“ als sich zwingend ausschließende Dimensionen modellieren.
Abrechnungsrechtliche Klassifikation und aktuelle Grenzwerte durch Lohnstelle/Regelmodul,
nicht allein aus Mitarbeiterantwort oder einem Jahres-Fixwert ableiten.

## 5. Feldkatalog – Kandidaten und Verantwortlichkeiten

Die folgende Auswahl ist eine Merlin-Planungsstruktur, keine verbindliche vollständige DATEV-Feldliste.
Pflicht ergibt sich aus Zweck, Beschäftigungsfall, aktuellem Zielprofil und Prüfung der Lohnstelle.
„Nicht bekannt“, „nicht vorhanden“ und „nicht zutreffend“ getrennt von leerem Feld behandeln.

| Bereich/Felder | Wer liefert? | Pflicht/Validierung und Sichtbarkeit |
|---|---|---|
| Vorname/Nachname, gegebenenfalls abweichender Geburtsname | Mitarbeiter, Arbeitgeber als Vorbelegung | Namen nicht auf ASCII beschränken; offizielle und bevorzugte Anrede trennen. |
| Wohnanschrift, Adresszusatz, Land/PLZ/Ort | Mitarbeiter | Für erforderliche Beschäftigungs-/Lohnzwecke; kein Wohnort im normalen Stationsverzeichnis. |
| Geburtsdatum | Mitarbeiter | Datum prüfen, kein öffentliches Such-/Geheimmerkmal; für notwendige Lohnprozesse. |
| Geburtsort/-land | Mitarbeiter, falls erforderlich | Nur wenn konkreter Melde-/Abrechnungsprozess es benötigt. |
| Staatsangehörigkeit(en), melderelevantes Geschlechtsmerkmal | Mitarbeiter/Fachstelle | Nur rechtlich/fachlich erforderliche Form; Codes aus aktuellem Zielprofil, keine erfundenen Optionen. |
| Persönliche E-Mail, optional Telefon | Mitarbeiter | Versand-/Rückfragezweck; private Telefonnummer nicht pauschal verpflichtend. |
| Steuer-ID | Mitarbeiter | Text/geeignete Formatprüfung; unbekannt als Klärungsfall, nie Fake-ID einsetzen. |
| Haupt-/Nebenbeschäftigung für Lohnzwecke | Mitarbeiter, geprüft durch Lohnstelle | Von Arbeitsort und Arbeitszeitmodell unabhängig. |
| Steuerliche weitere Merkmale | Lohnstelle bzw. bedarfsabhängige Erhebung | Keine automatische ELStAM-Abfrage oder Selbstangabe als verifiziert darstellen. |
| Sozialversicherungsnummer | Mitarbeiter/Fachstelle | Formatprüfung soweit belegt; unbekannt nicht pauschal Eintritt blockieren. |
| Versicherungs-/Kassenangaben | Mitarbeiter, Lohnstelle prüft | Keine Diagnose/Behandlungsdaten; nur notwendiger Abrechnungsumfang. |
| Weitere Beschäftigungen/Status, z. B. Studium | Mitarbeiter | Profilabhängig, keine pauschale Sammlung sämtlicher fremder Arbeitgeberdetails. |
| Pflegeversicherungs-/Kinderangaben | Nur falls erforderlich | Eigener sensibler Abschnitt, benötigten Nachweis/Feldumfang durch Fachstelle klären. |
| Zahlungsart, Kontoinhaber, IBAN | Mitarbeiter | Gehaltszielkonto, keine SEPA-Erteilung; maskierte Darstellung, sichere Änderung. |
| Abweichender Kontoinhaber | Mitarbeiter/Fachstelle | Ausdrücklich prüfen, keine automatische Kontoinhaberbestätigung aus IBAN ableiten. |
| Arbeitgeber, Eintritt/Austritt, Vertragsart | Arbeitgeber | Mitarbeiter sieht relevante Vorbelegung, Änderung als Rückfrage statt eigenmächtige Vertragsänderung. |
| Wochenstunden, Arbeitstage, Soll-/Arbeitszeitmodell | Arbeitgeber | Gültig-ab und Historie, keine stillen Änderungen veröffentlichter Schichten. |
| Vergütung, Gültigkeit, ggf. Zuschlagsvereinbarung | Arbeitgeber/berechtigte Personalstelle | Nicht aus frei eingetragenen Mitarbeiterwerten übernehmen; keine Gehaltsliste für Stationsleitung. |
| Tätigkeit/Ausbildung/abrechnungsrelevante Schlüssel | Arbeitgeber/Lohnstelle | Fachkataloge mit Quelle/Version, keine automatische Eingruppierung durch KI. |
| Befristung, Probezeit, erforderliche Dokumente | Arbeitgeber/Fachstelle | Vertragliche Tatsachen, keine automatische Erstellung/Unterzeichnung durch Fragebogenabschluss. |
| Interne Nummer und DATEV-Nummer | Arbeitgeber/Kanzlei | Getrennte IDs, festes Zuordnungsprofil pro Arbeitgeber, keine Vergabe allein aus Name. |
| Beschäftigungsfallabhängige Erklärungen | Mitarbeiter/Fachstelle | Nur freigegebene Texte, freiwillige/rechtlich nötige Erklärungen getrennt, keine generische Gesamtzustimmung. |

Keine pauschalen Pflichtfelder Religion, Familienstand, Ausweis-/Bankkartenkopie,
vollständige Gesundheitsakte oder Notfallkontakt. Falls ein entsprechendes Merkmal im
konkreten Abrechnungsfall erforderlich ist, Umfang/Rechtsgrundlage/Zugriff separat freigeben.
Notfallkontakte eigener optionaler Zweck, kein DATEV-Standard aus bloßer Vermutung.
Auslandsfälle/fehlende deutsche Kennungen als Klärungsweg, keine Fantasienummer erzeugen.

## 6. Mitarbeitereinladung – eigener, eng begrenzter Vorgang

Der Arbeitgeber wählt Mitarbeiterakte und Empfänger, prüft Adresse, Arbeitgeberkontext,
Fragebogenprofil und Zuständigkeit, bestätigt dann Versand. Mail enthält nur notwendige
Information und einen geschützten Einstieg; keine Steuer-ID, IBAN, Verträge oder Lohndaten.
Kein automatischer zusätzlicher Benutzerzugang. Optionaler Wunsch „Merlin-Zugang später
einrichten“ ist lediglich vorgemerkt und muss separat geprüft/eingeladen werden.

Sicherheit:
- Token zufällig, gehasht gespeichert, befristet, widerrufbar, nur ein Mitarbeiter/ein Vorgang.
- Erste Token-Nutzung bindet einen sicheren Erfassungszugang; erneute Sitzungen über
  bestätigte E-Mail/geeignetes Anmeldeverfahren. Link allein nicht als dauerhaftes Archivpasswort.
- Vor Anzeige sensibler Vorbelegungen Empfänger bestätigen. Bestehendes verifiziertes Konto
  nur nach passender, ausdrücklich geprüfter Zuordnung nutzen, keine Namensähnlichkeit.
- Keine fremden Mitarbeiter/Stationen oder Partneradministration im Erfassungsbereich.
- Neuversand invalidiert alten Link; Ablauf beendet Zugang, verwirft aber keinen gespeicherten Entwurf.
- Wiederholte Aufrufe/Einreichungen idempotent; parallele Versionen nicht unbemerkt überschreiben.
- Frist 7 Tage ist Vorschlag; Erinnerungen nur mit freigegebenem Plan, begrenzter Frequenz,
  ohne vollständige Personaldaten in Mail/Inhalt/Logs.
- Versanddienst-Annahme nicht mit zugestellter oder gelesener Mail gleichsetzen.

Ohne persönliche E-Mail: beaufsichtigte Erfassung durch berechtigte Personalstelle als
V1-Alternative planen. QR/Papiercode nur eigener später zu bestätigender gesicherter
Übergabeweg; keine frei fotografierbaren öffentlichen QR-Codes als Alleinschutz für Personalakte.
Geburtsdatum ist kein Passwort. Kein Versand gemeinsamer Passwörter.

## 7. Mitarbeiter füllt selbst aus – Bildschirm C

Mobil gut bedienbarer eigener Assistent, kein komplettes Verwaltungsmenü:
1 Persönliche Angaben → 2 Beschäftigungsbezogene Selbstauskunft →
3 Steuer/Sozialversicherung, soweit erforderlich → 4 Zahlungsangaben →
5 nötige Nachweise → 6 Prüfen & einreichen.

Nur zum Beschäftigungsprofil passende Felder zeigen. Arbeitgeber-Vorbelegung als solche
kennzeichnen. Keine Arbeitgeberfestlegung von Stunden/Lohn durch Selbstbedienung ändern.
Speichern pro Abschnitt mit bestätigtem Serverstatus; nicht aus Browseranzeige Erfolg ableiten.
Kein Offline-Cache/Service-Worker-Cache sensibler Antworten oder ungeschütztes localStorage.
„Später fortsetzen“ mit sicherem Wiederzugang, Sessionablauf und Schutz geteilter Geräte.
Dokumente/Steuer-/Bankangaben nicht in URL, Analytics, Mailtext oder Fehlerbericht ausgeben.
Am Ende eigene Zusammenfassung, offene Punkte sichtbar, Erklärung der Richtigkeit eigener
Angaben ohne pauschale DSGVO-Einwilligung oder stillen Vertrags-/Mandatsabschluss.
Einreichung erzeugt eine festgehaltene Version zur Prüfung, keine automatische DATEV-Übernahme.

## 8. Prüfung und kontrollierte Übernahme – Bildschirm D

Prüfliste zeigt eingereichte Abschnitte, fehlende Angaben und berechtigte Feldunterschiede
gegen bereits übernommene Daten. Nur Personal-/Lohnberechtigte sehen volle Details.
Abschnitte gezielt akzeptieren oder mit konkreter Rückfrage zurückgeben; keine allgemeine
Schaltfläche, die unbemerkt unklare Steuer-/SV-/Bankdaten als bestätigt markiert.

Unterscheiden: formale Gültigkeit, Vollständigkeit, Erklärung des Mitarbeiters,
fachliche Prüfung durch Arbeitgeber/Lohnstelle, externe Bestätigung. Keine Stufe vortäuschen.
Bereits verwendete Daten nicht durch eine neu eingegangene ungeprüfte Antwort überschreiben.
Nach Übernahme wirkende Änderungen mit Gültig-ab und nachvollziehbarer Version.
Neue Bankverbindung besonders absichern: erneute Authentifizierung, Prüfung und
Benachrichtigung über Änderung ohne volle IBAN; keine alleinige Änderung durch beliebigen Mail-Link.
Nach Übergabe Korrekturen als neuen Stand/Delta, Export-Snapshot nie nachträglich verändern.
Ohne erforderliche Rechte darf ein Prüfer nicht eigene Änderungen selbst durch den Exportweg freigeben.
Vier-Augen-Freigabe für Zahlung/Export als offener Vorschlag, nicht als bereits beschlossene Pflicht.

## 9. Dokumente und Personalakte

Kategorien statt unkontrollierter Sammelablage: Vertrag, profilbedingt erforderliche
Nachweise/Erklärungen, sonstige ausdrücklich benötigte Unterlagen.
Keine Pflicht zum Upload sämtlicher Ausweise, Bankkarten oder Gesundheitsunterlagen.
Dateityp/Größe, Malwareprüfung, Quarantäne bis Prüfung, geschützte Speicherung und
kurzlebige Downloads mit aktueller Berechtigungsprüfung planen.
Keine öffentlich erreichbaren Dateipfade, keine fremden Dokumente in OCR/externen Diensten
ohne eigene Entscheidung/Vertrags-/Datenschutzprüfung. Signatur-/OCR-Funktion nicht V1 voraussetzen.
Ein digital bestätigter Fragebogen ist kein automatisch rechtswirksam unterschriebener Arbeitsvertrag.
Aufbewahrung je Dokument/Zweck durch Fachstelle festlegen; keine pauschalen Jahresfristen erfinden.

## 10. Mitarbeiterübersicht und Profil

Übersicht: Name, interne Personalnummer, erlaubte Einsatzstationen, Beschäftigungsstatus,
Fragebogen-/Prüfbedarf, zulässige Aktion. Filter Station, Beschäftigungsprofil,
Eintritt/Austritt und Erfassungsstatus, serverseitig paginiert.
Keine Wohnanschrift, Geburtsdaten, IBAN, Steuer-/SV-ID, Gehalt oder Diagnose in Standardliste.
Ein Mitarbeiter an zwei Stationen erscheint als eine Personalakte, nicht doppelt.
Ausgeschiedene/Entwürfe getrennt filterbar; Berechtigungen auch in Zählern/Exporten.

Profilreiter-Vorschlag: Überblick, Persönliches, Beschäftigung, Stationseinsätze,
Lohndaten (spezielle Berechtigung), Dokumente, Fragebögen, Benutzerverknüpfung, Historie.
Beschäftigung vor Eintritt planen dürfen, wenn nötige Planungsdaten vorhanden;
ungeklärte Lohnfelder nicht pauschal mit Einsatzfreigabe gleichsetzen. Tatsächlich
erforderliche Beschäftigungsnachweise/Freigaben separat als Fachentscheidung behandeln.
Keine Bewerberbewertung, automatische Einstellungsentscheidung oder Leistungsüberwachung.

## 11. Rechte- und Sichtbarkeitsmatrix – Vorschlag

| Vorgang | Personal-/Lohnverwaltung mit Recht | Stationsleitung | Mitarbeiter-Selbsterfassung |
|---|---|---|---|
| Personalakte anlegen | Im eigenen Arbeitgeberkontext | Nur gesondert delegiertes Grunddatenrecht | Nein |
| Mitarbeiterliste | Erlaubter Organisationsumfang | Nur nötige Einsatz-/Planungsdaten zugewiesener Station | Kein Verzeichnis |
| Fragebogen einladen | Spezifisches Einladungsrecht | Standardmäßig nein; delegierte Einladung ohne volle Lohneinsicht denkbar | Nein |
| Persönliche Anschrift/Kennungen | Nur passende Feldrechte | Standardmäßig nein | Nur eigene nötige Angaben |
| Vergütung/Steuer/SV/IBAN | Separate sensible Rechte | Standardmäßig nein | Eigene angefragte Angaben; Arbeitgeberwerte nicht ändern |
| Beschäftigung/Stammstation festlegen | Mit passendem Fachrecht | Nur ausdrücklich delegierter Bereich | Lesen/Rückfrage |
| Eingang übernehmen | Mit passendem Prüf-/Feldrecht | Nicht allein wegen Stationsrolle | Einreichen, nicht Arbeitgeberfreigabe |
| DATEV-Datei/PDF erstellen/übergeben | Eigenes Exportrecht und geprüfter Umfang | Nein | Nein |
| Dokumente lesen | Kategorie-/Arbeitgeberrecht | Nur ausdrücklich erlaubte Kategorie | Nur eigene freigegebene Unterlagen |
| Merlin-Zugang verknüpfen | Separates Benutzerverwaltungsrecht | Nicht automatisch | Annahme eigener Einladung |

Organisationsinhaberstatus ersetzt nicht automatisch sensible Personal-/Lohnrechte.
Steuerbürozugang eigener späterer begrenzter Rollen-/Empfängerprozess, keine universelle Adminrolle.
Serverseitige Feldauswahl, nicht nur CSS/ausgeblendete Reiter, auch für API/Suche/Dateien/Jobs/Logs.
Mitarbeiter an mehreren Stationen verrät einer Leitung nicht automatisch alle anderen Einsätze.

## 12. DATEV-Vorbereitung und spätere Übergabe

Zunächst neutraler geprüfter Personalstamm mit möglicher Kanzlei-Prüfübersicht.
PDF/CSV darf nur „Prüfübersicht“ heißen, solange keine bestätigte Formatspezifikation
und Importprüfung vorliegt. Nicht beliebige CSV als DATEV-Export bewerben.

Vor Implementierung eines Exports festlegen:
- DATEV LODAS oder Lohn und Gehalt und konkrete Version/Spezifikation.
- Rechtlicher Arbeitgeber, DATEV-Lohnmandant, eventuell Berater-/Mandantennummer
  nur soweit das Verfahren erfordert; Stationskürzel ist keine Mandantennummer.
- Personalnummern-Zuordnung mit Kanzlei abstimmen, führende Nullen erhalten.
- Pro Feld Quellwert, Zielbezeichnung/-kennung, Datentyp, Pflicht/bedingt, Codekatalog,
  erlaubte Werte, Gültigkeit, Leer-/Löschbedeutung und Quelle/Version dokumentieren.
- Unterschied keine Änderung / Wert löschen / unbekannt; kein leeres Feld versehentlich als Löschbefehl.
- Encoding, Struktur, Dateikopf, Datums-/Zahlenformate und Codewerte anhand offizieller
  aktueller Vorgabe, keine zufälligen ASCII-/CSV-Details erfinden.
- Neuaufnahme versus Änderung, Storno/Wiedereintritt, nicht unterstützte Felder und
  ergänzende Dokumente ausdrücklich behandeln; stille Abschneidung/Ersetzung vermeiden.
- Export enthält nur geprüfte freigegebene Daten eines erlaubten Arbeitgeber-/Zeitraums.
- Snapshot, Quellversion, Ersteller, Empfänger, Prüfer, Formatversion und sichere Protokollierung.
- Dateien sicher bereitstellen, keine dauerhaften öffentlichen Links und keine Mailanhänge als Standard.
- Erneute Übergabe/Dubletten, Rückmeldungen/Fehler und Korrekturläufe planen.

Cloud-/API-Anbindung ist eigener späterer Auftrag mit Voraussetzungen/Authentifizierung/
DATEV-Freischaltung/technischer Abnahme. Kein ungeprüftes „Synchronisiert“-Badge.
Eine mögliche Sofortmeldung ist ein eigenständiger externer Meldeprozess mit Verantwortlichem,
Fristüberwachung und Empfangsnachweis. Fragebogenversand erfüllt keine Meldepflicht.
Kein tatsächlicher Meldeumfang oder rechtliche Frist aus dieser Planung ableiten.

## 13. Datenschutz, Historie, Austritt

Beschäftigtendaten je Zweck und Erforderlichkeit bewerten; Rechtsgrundlage/Informationen
und sensible Feldgruppen mit Personal-/Datenschutzstelle klären. Keine generische
Einwilligung als pauschale Grundlage aller Verarbeitungen. Siehe DATEV-Leitfaden/§ 26 BDSG.
Personaldaten verschlüsselt angemessen schützen, Schlüssel/Backups getrennt planen,
Passwörter/Token sicher, Audits minimal. Keine echten Personaldaten ins öffentliche GitHub.
Keine vollständigen sensiblen Vorher-/Nachherwerte in Auditlogs; Metadaten plus sicherer
Fachversionsspeicher statt Logkopie der gesamten Akte.

Austritt: geplante Einsätze/Einladungen/Zugänge prüfen, Rechte zum passenden Zeitpunkt
gezielt entziehen. Weder Kontosperre automatisch als Vertragskündigung noch Austrittsdatum
als Löschdatum behandeln. Vorhandene Fachhistorie und berechtigte Dokumentenwege getrennt
von operativem Zugang regeln. Archiv, Auskunft, Berichtigung und Löschung nach Kategorie
mit Aufbewahrungsanforderungen planen. Genaue Fristen noch offen.
Nicht angetretene Beschäftigung, stornierter Entwurf, Wiedereintritt und Arbeitgeberwechsel
als eigene Fälle; keine Weitergabe an andere Arbeitgeber durch bloßes Kopieren der Akte.

## 14. Konzeptionelles Datenmodell

| Objekt | Zweck |
|---|---|
| Employee | Stabile Personalakten-ID, Organisation/Arbeitgeber, interne Nummer, Identität. |
| EmploymentPeriod | Eintritt/Austritt, Profil, Arbeitszeit/Vergütung mit wirksamen Versionen. |
| EmployeeStationAssignment | Stamm-/weitere Einsatzstation, Gültigkeit; keine Loginrechte. |
| PayrollIdentity/Profile | Vertrauliche Lohndaten, DATEV-Zielprofil/Nummer getrennt. |
| EmployeeQuestionnaire | Anlass, Profil-/Fragebogenversion, Mitarbeiter, Bearbeitungszustand. |
| QuestionnaireInvitation | Zieladresse, sichere Tokenbindung/Frist, Versandzustand. |
| QuestionnaireSubmission | Unveränderlicher eingereichter Stand, Freigabe/Rückfrage, Quellversion. |
| EmployeeChangeRequest | Änderung eigener Daten mit Prüf-/Wirksamkeitsweg. |
| PersonnelDocument | Kategorie, sichere Dateireferenz, Schutz-/Prüfstatus, Fristen. |
| EmployeeUserLink | Explizite Organisations-/Personenzuordnung zu optionalem Benutzerkonto. |
| PayrollExportBatch | Nur später: geprüfte Snapshots, Zielversion/Empfänger, Status/Rückmeldung. |
| PersonnelAuditEvent | Minimale administrative Ereignisse, kein Geheimwertdump. |

Keine fertige Migration; Altprojektmodelle und bestehendes Rechtekonzept später abgleichen.

## 15. Abnahmefälle

- Mitarbeiter ohne Login, Login ohne Personalakte, explizite eigene Verknüpfung.
- Eine Beschäftigung/zwei Stationen ohne doppelte Akte/Personalnummer.
- Mehrere Arbeitgeber nicht als bloßer Stationswechsel behandelt.
- Einladung falsche Adresse, falsche Sitzung, Link abgelaufen/widerrufen/neuversendet.
- Token/Session kann keine anderen Personalakten, Dateien oder Arbeitgeberdaten lesen.
- Kein Versand vor ausdrücklicher Bestätigung; Dienstfehler ohne Doppelakte wiederholbar.
- Fragebogen profilabhängig; unbekannte Steuer-/SV-ID mit Klärungsweg, keine Fakewerte.
- Mitarbeiter ändert Arbeitgeberstunden/Lohn nicht; Rückfrage statt stiller Vertragsänderung.
- Eingereichte/übernommene/neue Änderungen unterscheidbar, Konflikte nicht überschrieben.
- Bankänderung geschützt; kein Mitarbeiter-SEPA-Mandat aus Gehaltskonto erzeugt.
- Upload gesperrt bis Prüfung, keine öffentlichen Links/QR-Alleinzugriffe.
- Leitung erhält keine private Anschrift, Steuer/SV/IBAN/Vergütung aus Liste/API/Export.
- Export bei Ziel offen gesperrt bzw. nur ausdrücklich neutrale Prüfübersicht.
- DATEV-Dateiprüfung und Testimport erst nach Formatwahl; kein falsches Übernahme-Badge.
- Wiederholung/Korrektur/Storno/Wiedereintritt/fehlende Zielwerte ohne Doppelanlage.
- Austritt sperrt nur vorgesehene Zugänge, keine automatische Datenlöschung.
- Offline/Sessionablauf verliert nicht bestätigten Serverstand; keine lokale sensible Dauerablage.
- Mobile, Tastatur, Fehlerrückmeldungen, mehrsprachige Namen und Auslandsanschriften.

## 16. Kleine spätere Umsetzungsschritte

1. Arbeitgeber-/DATEV-Zielmodell, Feld-/Rechtekatalog und Fragebogenprofile mit Lohnstelle abstimmen.
2. Personalaktenliste, Grunddaten, Beschäftigungsabschnitte und Stationseinsätze.
3. Mitarbeitereinladung und eng begrenzte sichere Erfassungsoberfläche.
4. Profilabhängige Felder, Zwischenspeichern und versionierte Einreichung.
5. Prüfung/Rückfrage/Übernahme, Dokumentenschutz und sensible Änderungswege.
6. Optionale Benutzerverknüpfung, Austritt und Wiederaufnahme mit Historie.
7. Erst separat: bestätigtes DATEV-Mapping, Formatprüfung/Testimport, sichere Übergabe.

Keine Implementierungsfreigabe; keine echte Einladung, Personalakte oder Übertragung erzeugt.

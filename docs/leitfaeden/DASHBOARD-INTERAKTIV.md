# Interaktives Dashboard – Bedienung und Grenzen

Stand: 20.10.2026. Visuelle interaktive Vorschau, **keine implementierte Merlin-Anwendung**.
Der Benutzer hat ausdrücklich ein interaktives Dashboard angefragt. Dieser begrenzte
Mockup-Auftrag ändert nicht den bisherigen Planungsmodus für Backend/Fachmodule.

## Quelle und Öffnen

Die eigenständige Vorschauquelle liegt unter
[11-dashboard-interaktiv.html](../mockups/11-dashboard-interaktiv.html).
Sie ist ein HTML-Fragment für die interaktive Ansicht in Codex, mit eigenen Styles
und lokalem JavaScript. Nach Klonen/Herunterladen kann sie auch direkt im Browser
geöffnet werden; die GitHub-Dateiseite selbst führt die Interaktion nicht aus.
Kein npm, Laravel, PHP, Datenbank oder Zahlungsanbieter erforderlich.
Die ursprüngliche Inline-Datei im Chatverzeichnis ist keine geräteübergreifende Adresse;
auf dem anderen Rechner immer die Repositorykopie verwenden.

## Enthaltene Ansichten

- Übersicht mit abgeleiteten Aufgaben und Tagesbesetzung.
- Stationen mit Profilansicht und Beispielanlage.
- Team & Zugänge mit Einladungsvormerkung.
- Schichtentwurf für 20.–21.10.2026 und lokale Zuordnung.
- Urlaubs-/Wunschfrei-Anträge mit Demo-Statusänderung.
- Zentrales Partnerkonto ausschließlich in der Inhaberansicht.

## Ausprobieren

1. In der Kopfzeile Station wechseln: Zähler, Personen, Anträge und Schichten filtern mit.
2. Demo-Rolle „Stationsleitung“: nur Musterstadt, keine Partner-/Vertragsverwaltung.
   Die Inhaberrolle zeigt wieder alle Beispieldaten. Das ist ein Designvergleich,
   keine echte Anmeldung oder serverseitige Sicherheitsgrenze.
3. Bei offenem Schichtplatz „Besetzen“ wählen. Beispiel: Sam ist am 20.10.14–22 bereits
   in Beispielort eingeplant und kann nicht gleichzeitig Musterstadt besetzen.
   Robin kann den freien Beispielplatz ohne Zeitüberschneidung übernehmen.
4. Abwesenheiten öffnen, Robins Antrag ansehen und als Inhaber „In Demo genehmigen“:
   Status und Übersicht ändern sich. Kein echtes Urlaubskonto wird gebucht.
5. Station anlegen: Beispieldatensatz mit Entwurfsprofil, keine Datenbankänderung.
6. Einladung vorbereiten: nur .invalid-Beispieladresse, Vormerkung ohne Mailversand.
7. Demo zurücksetzen stellt die Ausgangsdaten wieder her.

## Daten und Grenzen

Zwei fiktive Stationen, vier fiktive Teamzugänge, acht Beispielschichten und drei
Beispielanträge. Die Daten haben ein festes Beispieldatum, sind kein Live-Betrieb.
Status wie „Mandat erteilt“ beruht ausdrücklich auf Beispieldaten, keiner tatsächlichen Erteilung.
Neue Stationen/Vormerkungen bleiben nur im aktuellen Vorschau-Lauf; nicht als dauerhaft
gespeicherte Datensätze darstellen. Codex kann Navigationswahl und einige Demo-Zustände
als Vorschauzustand halten, ohne echte Formulardaten oder E-Mail-Adressen zu übertragen.

Nicht umgesetzt: Backend-Authentifizierung, reale Berechtigungsprüfung,
Arbeitszeit-/Pausen-/Vertragsregelengine, Planveröffentlichung, Urlaubsjournal,
Registrierung, SEPA, Abo, E-Mailversand oder DATEV-Integration.
Die clientseitig eingeschränkte Stationsansicht ist ausschließlich eine Darstellung,
keine Sicherheitsarchitektur. Produktiv keine Rollenumschaltung zur Rechteerhöhung anbieten.

Keine Netzaufrufe, externen Schrift-/Bildabrufe oder Datenbankverbindung aus dem Fragment.
Optionale Codex-Funktionen speichern nur Demo-Auswahl/-Kennungen und bieten Gestaltungsregler.
Ohne Codex funktionieren lokale Bedienung und Gestaltung weiter; hostbereitgestellte
Linienicons und Gestaltungsregler können fehlen. Texte/Schaltflächen bleiben nutzbar.

## Bedienbarkeit und technische Ausführung

Native Buttons/Selects/Inputs, beschriftete Dialoge, Escape zum Schließen,
Fokusbegrenzung im Dialog und deaktivierter Hintergrund während offenem Dialog.
Layoutregeln für schmale Ansichten, Tabellen bei Bedarf seitlich scrollbar.
Keine Prüfung in echten Geräten/allen Browsern zugesagt.
Lokale Formularaktionen bewusst ohne tatsächliche Formularnavigation/Versand,
damit auch der geschützte Inline-Rahmen reine Vorschauaktionen ausführen kann.

## Durchgeführte Prüfung

- JavaScript-Syntax mit Node geprüft.
- Desktopdarstellung mit Browser-Screenshot angesehen.
- Navigation und Schichtdialog im Browser geöffnet.
- Stationsübergreifende Zeitüberschneidung im Beispiel abgewiesen.
- Zulässige Besetzung übernommen und offene Plätze von 3 auf 2 aktualisiert.
- Rollenwechsel: nur Musterstadt und keine Vertragsnavigation in Leitungsansicht.
- Beispielurlaubsantrag geöffnet und Demo-Genehmigung sichtbar übernommen.
- Reset auf Ausgangsdaten geprüft.

Weitere Prüfungen und Auffälligkeiten bei Folgebearbeitung hier ergänzen.
Dies sind Interaktionsprüfungen am Mockup, keine Tests der zukünftigen Anwendung.

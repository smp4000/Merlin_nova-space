# DATEV als Grundlage – Recherche und Übergabegrenzen

Recherche: 20.10.2026. Nur offizielle DATEV-Informationen für Produktaussagen verwendet.
Kein kompletter aktueller Import-Feldkatalog festgestellt. Keine Integrationsprüfung erfolgt.
Die Merlin-Feldliste ist ein **eigener Vorschlag**, keine zugesagte exakte DATEV-Spezifikation.

## Offizielle Orientierung

| Quelle | Verwendete Aussage / Grenze |
|---|---|
| [DATEV Personal – Informationen für Unternehmen](https://www.datev.de/web/de/unternehmen/loesungen/lohn-und-personal/datev-personal-kampagnenseite) | DATEV beschreibt digitale Erfassung neuer Mitarbeiter sowie Personalfragebögen und Stammdatenänderungen. Das ist Produktkontext, keine Bestätigung einer Merlin-Anbindung. |
| [DATEV Students – Personaldaten](https://www.datev.de/students/course/view.php?id=1481) | Beschreibt Grunddatenanlage, Versand an Mitarbeiter, Rücklauf/Übernahme und Ergänzung vor Freigabe an die Kanzlei. Daraus wird ein eigener Merlin-Prüfprozess abgeleitet. |
| [DATEV MyUpdates – Oktober 2026](https://apps.datev.de/myupdates/product-change/details/rel.1051520.productversion_535655180758939) | Veröffentlicht Mitarbeiterneuanlage und Personalfragebögen für geringfügig und sozialversicherungspflichtig Beschäftigte ab 07.10.2026. Nicht pauschal auf alle Profile/Programme übertragbar. |
| [DATEV Lohnimportdatenservice](https://www.datev.de/web/de/shop/produkt-details/datev-lohnimportdatenservice-93006) | Ein Datenaustausch erfordert eine entsprechende Schnittstelle und Einrichtung; daraus folgt kein automatischer Zugang für jedes Drittsystem. |
| [DATEV – Daten aus Partnerlösungen](https://www.datev.de/web/de/steuerberatung/loesungen/komplett-digital-im-lohn/daten-und-dokumente-von-mandanten-erhalten/daten-aus-partner-software-erhalten/daten-fuer-die-lohn-und-gehaltsabrechnung-aus-partnerloesungen-erhalten) | Nennt LODAS und Lohn und Gehalt als empfangende Programme. Übertragbarer Umfang hängt vom Vorsystem ab. |
| [DATEV Developer – Schnittstellenvorgaben](https://developer.datev.de/de/guides/interface-requirements) | Für Lohnimportdatenservice sind Dienst- und Dateiformatvorgaben maßgeblich. Aktuelle technische Dokumentation vor Implementierung beschaffen. |
| [DATEV Wissensplattform, Dok. 1051138](https://wissensplattform.apps.datev.de/help/document/1051138) | Gefundenes Dokument zu Mitarbeiteranlage und Fragebogen. Öffentlich nur Gliederung/Metadaten auswertbar; keinen vollständigen Feld-/API-Inhalt behaupten. |

Die ältere offizielle Broschüre „Lohn lohnt sich“ wurde als historische Orientierung
gefunden, aber nicht als aktueller verbindlicher Feld- oder Schnittstellenstandard verwendet:
[DATEV-Broschüre](https://www.datev.de/content/dam/markenassets/themen-und-produktgruppen/neu--nichtmitglieder/lohn-lohnt-sich.pdf).
Keine PDFs oder geschützten Originalfragebögen ins öffentliche Repository kopiert.

## Noch zu klären

1. Nutzt die Kanzlei DATEV LODAS oder DATEV Lohn und Gehalt?
2. Reicht strukturierte Datenerfassung mit Kanzlei-Prüfübersicht oder wird später
   ein geprüfter Dateiimport bzw. Cloud-Datenservice benötigt?
3. Welcher rechtliche Arbeitgeber und DATEV-Lohnmandant gelten pro Personalakte?
4. Wer legt Personalnummern und Abrechnungs-/Meldeschlüssel verbindlich fest?
5. Welche aktuellen Beschäftigungsprofile/Felder fordert die Lohnstelle tatsächlich?
6. Welche Zugriffsrechte, Einwilligungen soweit nötig, Betreiber-/Dienstleisterverträge
   und sichere Übergabewege sind erforderlich?

Die Frage nach dem Zielprogramm wurde im Chat gestellt. Bis zur Antwort bleibt die
Planung produktneutral. Keine konkrete Feldkennung, Codes oder Formatanforderungen erfinden.

## Feldmapping-Gerüst (noch keine DATEV-Zielfelder)

Für jedes freigegebene Feld später ausfüllen:

| Eigenschaft | Zu dokumentierender Inhalt |
|---|---|
| Merlin-Feld | Eindeutiger Fachbegriff und Herkunft: Mitarbeiter/Arbeitgeber/Lohnstelle. |
| Zweck und Zugriff | Nötiger Beschäftigungszweck, Feld-/Export-/Prüfrecht. |
| Zielprofil | LODAS oder Lohn und Gehalt mit konkreter Spezifikationsversion. |
| DATEV-Feld | Belegte Kennung und Bezeichnung, keine erfundene Universalspalte. |
| Pflicht/bedingt | Regel je Beschäftigungsfall und Vorgang Neuaufnahme/Änderung. |
| Format/Katalog | Typ, Länge, Codes, Zahlen/Datum/Encoding aus bestätigter Vorgabe. |
| Leer-/Löschsemantik | Keine Änderung, unbekannt, Wert löschen ausdrücklich unterscheiden. |
| Gültigkeit | Ab wann wirksam, Behandlung von Historie und Korrektur. |
| Übertragbarkeit | Unterstützt / nicht unterstützt / ergänzender Nachweis. |
| Prüfung | Formale/Fachprüfung und Testimport mit synthetischen Daten. |
| Rückmeldung | Datei erstellt, übermittelt, vom Ziel angenommen/abgelehnt getrennt. |
| Quelle | Offizielles Dokument, Version und Abrufdatum. |

## Beschäftigtendatenschutz

Für Beschäftigtendaten ist eine zweck- und erforderlichkeitsspezifische Beurteilung nötig.
Eine pauschale Einwilligung ersetzt diese Prüfung nicht. Die genaue Rechtsgrundlage und
besondere sensible Feldgruppen sind mit der zuständigen Fach-/Datenschutzstelle zu klären.
Primärquelle: [§ 26 BDSG – Datenverarbeitung für Zwecke des Beschäftigungsverhältnisses](https://www.gesetze-im-internet.de/bdsg_2018/__26.html).

Keine Diagnoseinformationen, unnötigen Ausweiskopien oder kompletten Lohnakten für
Stationsleitungen. Zugriff, Prüferrollen, Bankänderungsschutz, Dokumentenkategorien,
Aufbewahrung und sichere Kanzleiübergabe im konkreten System planen.
Keine rechtliche Frist oder Gehalts-/Minijob-Grenze aus älteren Broschüren übernehmen.

## Sprachregelung

Zulässig im jetzigen Entwurf: „DATEV-orientierte Stammdaten“, „Zur Personalprüfung“,
„Zielprogramm noch offen“, „Prüfübersicht“.
Noch nicht belegt: „DATEV-kompatibel“, „DATEV-zertifiziert“, „automatisch synchronisiert“,
„Sofortmeldung erledigt“, „in DATEV übernommen“ oder „alle Felder vollständig unterstützt“.

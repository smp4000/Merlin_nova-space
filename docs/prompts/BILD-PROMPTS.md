# Bild-Prompts und Referenzen

Diese Briefings sind **rekonstruierte, konsolidierte Fassungen** der im Chat verwendeten
Bildaufträge. Sie sichern Motiv, Inhalt und Gestaltungsabsicht, nicht den vollständigen
wortgetreuen Tool-Input oder eine pixelgenaue Reproduzierbarkeit. Die PNGs selbst sind
die erhaltenen Originalergebnisse. Keine Seed-/Modell-Reproduzierbarkeit zugesagt.

Referenzfoto bei Bildern 01/02: lokal `docs/referenzen/ATS_Petersberg.jpg`.
Die separate Originaldatei ist nicht Bestandteil des öffentlichen Repositorys.
Für neue Fotovarianten auf einem anderen Rechner muss der Benutzer sie erneut bereitstellen.
Stilreferenz des Benutzers: https://chatgpt.com/s/p_1712a53d86348191859849b5eeba390e

## 01 – Erster Landing-Entwurf, überholt

```text
Create a high-fidelity full-page German MERLIN petrol station SaaS landing page,
flat desktop website screenshot, portrait composition, no device frame.
Use the supplied real ATS Petersberg photo as the large hero insert, preserve station.
Warm ivory, near-black forest-green typography, sparing electric lime accents,
generous whitespace, bold clean sans-serif, refined rounded cards.
Header merlin, Funktionen, Für wen, Preise, Anmelden, Kostenlos testen.
Hero: „Deine Stationen. Ein klarer Überblick.“ / 30 Tage kostenlos testen.
Floating „Heute im Blick“ software preview, feature bento Team/Ware/Alltag.
Audience: Einzelunternehmen and Firma & Stationsnetz, up to 100 stations.
Pricing: 30 Tage testen, 0 €, and Dein Abo / Preise folgen.
Mention active subscription required after trial, access suspended without one.
Privacy treated as a design requirement, no certification or hosting claims.
Footer imprint/privacy/contact and concept label. No fake testimonials or revenue.
```

## 02 – Bestätigte Landing-Stilrichtung

```text
Create a polished full-page flat German MERLIN SaaS landing mockup, desktop width
in portrait composition, crisp legible German text. Airy white and pale ice-blue,
dark navy bold sans-serif headings, petrol/teal CTA, thin cool-gray borders,
subtle shadows, modest rounded corners. No lime, beige or forest green.
Use the actual ATS Petersberg photo as panoramic hero with white fade on left,
preserving architecture/trees/blue canopy. Right floating white Merlin app window
with station list, compact sidebar, small status pills. Left headline:
„Deine Stationen. Dein Team. Alles im Blick.“ CTA „30 Tage kostenlos testen“.
Header: Funktionen, So funktioniert’s, Preise, Kontakt, Anmelden.
Three-step ribbon: Kostenlos registrieren / Stationen anlegen / Mitarbeiter zuordnen.
Features: Team & Schichten, Kasse & Übergaben, MHD & Artikel, Berichte & Überblick.
Audience: Einzelunternehmen and Firma & Stationsnetz, central company invoice,
personal station-manager access, one to 100 stations.
Three illustrative pricing cards Einzelstation / Mehrere Stationen / Stationsnetz,
all „Preis folgt“. No numeric price. Note active subscription after 30 days,
otherwise access suspended. Privacy planned, no fake certification or customers.
Footer „Mockup · Preise und Inhalte in Planung“.
```

## 03 – Registrierung, ursprüngliche Übersicht

```text
High-fidelity UX presentation board, four German Merlin registration screens in 2x2
grid, flat desktop mockups. White/ice-blue, navy type, petrol buttons, cool borders.
Screen 1: „Dein Unternehmen bei Merlin“, selectable Einzelunternehmen and Firma /
Gesellschaft, company fields, note station count does not decide company type.
Screen 2: central invoice address, street/PLZ/city/country, optional different billing
address, invoice email and VAT number, station addresses separate.
Screen 3: first station, add further stations, up to 100 without filling all now.
Screen 4: invite station manager, personal email, role and station multi-select,
no access to subscription/invoices, optional sending after completed setup.
Synthetic company Beispiel Stationen GmbH and .invalid email addresses.
Show progress and calm summaries, no real user data or legal certifications.
Footer concept only, no implementation.
```

Current correction: Six-step flow including mandatory SEPA supersedes this original board.
Some generated step labels and register-name labels are inaccurate; see mockup notes.

## 04 – Mandatory SEPA step

```text
Premium flat desktop German Merlin registration UI, white/ice-blue/navy/petrol,
main form plus partner summary. Six-step indicator Konto / Unternehmen / Rechnung /
SEPA-Mandat / Stationen / Prüfen; fourth step active.
Headline „SEPA-Mandat direkt hinterlegen.“ Fields account holder and empty IBAN,
optional different account holder. No real bank number. Mandate preview has
pending creditor details, creditor ID, reference to be generated, recurring payments.
Explicitly show that mandate text/electronic procedure must be agreed with provider.
Separate unticked authorization and mandate checkboxes; no invented legal text.
Summary company, billing address, 30 days trial, price not set.
Note no debit today, mandate does not replace subscription order, station managers
cannot access bank data. Back link and „Mandat erteilen und weiter“ CTA.
Footer concept only, not a valid mandate; no implementation/compliance guarantee.
```

## 05 – Partner-Dashboard, first login

```text
Exceptionally polished flat desktop Merlin SaaS dashboard, 1600x1100-ish landscape,
ice-blue background, white cards, navy bold modern typography, petrol actions,
cool borders and subtle shadows. Sidebar organization Beispiel Stationen GmbH;
overview active, Stationen, Team & Zugänge, Schichtplanung, Ware & MHD, Kasse &
Übergaben, separate Vertrag & Abrechnung, Einstellungen, Hilfe.
Top station selector Alle Stationen, one station, avatar Alex Beispiel.
Welcome header and add-station action. Trial banner, no paid subscription claimed.
Main onboarding card one of three complete: first station created / invite team /
create first shift plan, one prominent teal invite action.
Account summary organization, invoice address, mandate Erteilt, free trial;
never show IBAN. Station Musterstadt card with no invitations, no plan, no imported
articles. Explicit empty states, no fabricated operational or revenue metrics.
Explanation station managers see only assigned stations. Next actions add station,
import article master data, complete station profile. Responsive-minded layout.
Tiny concept/examples/no-implementation footer.
```

## 06 – Team & Zugänge, current module

```text
Create a high-fidelity German Merlin SaaS UX board with two large desktop screens
stacked vertically. White/ice-blue, dark navy sans-serif, petrol selected states,
crisp outline icons, cool-gray borders and subtle shadows, rounded white cards.
Only sample names and .invalid email addresses, no devices or perspective.
Screen 1 organization view: sidebar organization, Team & Zugänge active, top station
selector. Title „Dein Team. Klare Zuständigkeiten.“ and „Person einladen“ CTA.
Tabs Zugänge / Einladungen / Rollen; counters 2 active users, 1 pending invitation,
2 stations. Search name/email, role/station/status filters. Table Alex Beispiel
organizational owner all stations active; Kim Muster manager at Musterstadt and
Beispielort active; Robin Demo manager Musterstadt invitation open.
Note login account and personnel file are separate; rights assigned per station.
Screen 2 invite panel: personal email robin@beispiel.invalid, optional name,
Stationsleitung role; Musterstadt checked, Beispielort unchecked.
New stations not automatically assigned. Rights preview shifts/MHD checked,
personnel and access administration unchecked. Right summary allowed scope and
explicit exclusions: other stations, invoices/subscription, bank/SEPA, role management.
7-day validity clearly marked proposal. Recipient sets own password, no password
sent. Cancel, save draft, send invitation buttons. Concept/no-implementation footer.
```

The first generated board incorrectly counts pending invitation in the access tab;
final spec requires separate counts. Rights listed are examples, not approved defaults.

## 07 – Stationsverwaltung, aktuelle Planung

```text
Create a premium high-fidelity German Merlin UX board with two complete desktop
screens stacked vertically. Flat screenshots, no perspective/devices. Approved
white/ice-blue, dark navy sans-serif, petrol buttons/active states, cool thin borders,
restrained shadows, 12px white cards, crisp outline icons, legible German text.
No real data, original photo, bank information or legal certification.
Upper view: organization sidebar, Stationen active, station selector, title
„Deine Stationen. Zentral organisiert.“ and teal „Station anlegen“.
Counters 2 active, 1 draft, 1 inactive. Search name/code/city and status filter.
Table four synthetic stations Musterstadt MST, Beispielort BSP, Nord NRD, West WST;
columns station/city/manager/status/profile/action. Two active, one draft, one
inactive. Kim Muster manages first two, others no manager. Show incomplete
opening hours separately from active status; draft still needs address.
Note company billing address is separate from each station address.
Lower view: Station Musterstadt profile, stable code, sample address and active
badge, Station verwalten button. Tabs overview/master data/opening hours/team/
equipment/devices. Opening hours selected. Weekly schedule Mon–Fri 06–22,
Sat 07–22, Sun 08–20, add time window, explicit 24h and closed controls,
visible Europe/Berlin timezone, overnight helper. Exception 24.12.2026 08–14.
Right cards manager Kim Muster, status/profile/device setup separately, no
device coupled; missing device/article import does not block activation.
Bank data and invoices not part of station profile. Save/discard actions.
Footer concept, examples, no implementation. No fabricated revenue or map APIs.
```

See gallery notes for simplified per-day controls, simultaneous week/exception
views and illustrative generated thumbnails. Model/business rules take precedence.

## 08 – Mitarbeiter und Mitarbeitereinladung, DATEV-orientiert

```text
Create a premium high-fidelity German Merlin UX board with three views: a wide
employee-management desktop on top, employer invitation panel bottom left and
mobile self-service bottom right. Flat screenshots, approved ice-blue/white/navy/
petrol, subtle cool borders/shadows and rounded cards. No actual sensitive values,
DATEV logo, certification, real bank/tax/social IDs or working integration claims.
Top screen: organization sidebar, Mitarbeiter active, headline „Deine Mitarbeiter.
Sauber erfasst.“, create-employee action, counters 4 personal files, 1 invitation,
1 submission for review. Tabs employees/questionnaires/review, search and filters.
Four synthetic records Kim Muster, Alex Beispiel, Robin Demo, Sam Beispiel;
two active/verified, Robin planned minijob/invitation pending, Sam planned part-time/
review pending and two stations. No private or payroll values in list.
Note personal file and login separate, invitation grants no station permissions.
Employer panel: „Personalfragebogen senden“, Robin Demo, robin@beispiel.invalid,
planned entry 01.12.2026, profile Minijob, Station Musterstadt. Optional unchecked
later Merlin-login reminder, no automatic access. 7-day link duration marked proposal.
Recipient verifies email, only own questionnaire; cancel and send buttons.
Self-service: own employee form, first/last name Robin Demo, empty birth date and
home-address placeholders, employer start data read-only. Save/continue and resume
later. No complete tax/bank values or health data. Text says only self and authorized
personnel see answers. Compact step display is illustrative, further sections follow.
Footer „Gestaltungsentwurf · Beispieldaten · Keine DATEV-Anbindung umgesetzt“ and
„DATEV-orientierte Stammdaten · Zielprogramm noch offen“.
```

Full field/profile/review rules live in the specification. The picture's shortened
steps do not remove tax/social insurance or necessary evidence from the plan.

## 09 – Schichtplanung und Veröffentlichung

```text
Create a premium high-fidelity German Merlin UX board with two desktop sections
stacked vertically. Flat screenshots, approved ice-blue/white/navy/petrol, crisp
outline icons, cool thin borders, subtle shadows and 12px rounded cards.
Top full screen: organization sidebar, Schichtplanung selected, station Musterstadt.
Title „Dein Team. Klar geplant.“, KW44 26 October–1 November2026, Entwurf badge.
Actions fill templates / add shift / check plan. Counters 14 shifts, 1 open position,
1 blocking conflict. Week/month toolbar, date controls and area filter.
Seven-day grid with two shifts per day: early06–14 and late14–22. Synthetic staff
Kim Muster, Sam Beispiel, Robin Demo, Alex Beispiel, Jamie Muster, Taylor Demo.
Tuesday early Sam shows overlap; Sunday late dashed open slot. No universal green
legal-compliance badge. Right conflict panel and one open-slot note; planning is
not time recording. Bottom employee assignment chips with drag OR select helper.
Lower section two panels: publication check and own employee plan.
Left explicitly separate example after conflict fixed, current checks complete,
no blocker, one open Sunday slot; explicit unchecked acknowledgment, notification
scope affected active users, back to draft / publish. Creates fixed plan version.
Right own published plan for Robin, version1, station/address, Monday late14–22,
Wednesday early06–14, planned30min break. Only own plan, availability action and
offer-shift later-stage badge. No real private/payroll data or legal certification.
Footer design concept, examples, no implementation.
```

See gallery caveats: generated open-slot helper incorrectly calls it complete;
own assignments are separate examples and break sums do not replace actual intervals.

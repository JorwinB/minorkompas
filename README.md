# MinorKompas
De applicatie MinorKompas voor hackathon 4.

Repository: https://github.com/JorwinB/minorkompas

Demo: https://minorkompas-jorwin.navycrumb3.chatgpt.site (toegang afhankelijk van de deelinstellingen).

Architectuurschets: [ARCHITECTUUR.md](ARCHITECTUUR.md).

Nederlandstalige, regelgestuurde AI-keuzehulp voor minoren. Gratis runtime, geen API-sleutel, geen generatief taalmodel.

## Start lokaal (Windows, macOS, Linux)
Installeer Python 3. Open een terminal in de uitgepakte map:

    python -m http.server 8000 --directory dist

Open http://localhost:8000. Op Windows kan `py` nodig zijn in plaats van `python`.
Open de HTML niet als los bestand: JSON en modules hebben een webserver nodig.

## Spraak
De app gebruikt SpeechRecognition/webkitSpeechRecognition en speechSynthesis van de browser. Beschikbaarheid verschilt per browser, OS en privacybeleid. Test op de computer voor de demo. Microfoon vereist HTTPS of localhost en toestemming. Herkende tekst wordt eerst getoond en pas na bevestiging verzonden aan de lokale logica. Voor Nederlands voorlezen is een lokale Nederlandse systeemstem nodig. Installeer die via de taal-/spraakinstellingen van het OS indien afwezig; heropen daarna de browser. Typen blijft mogelijk bij fouten, maar telt niet als geslaagde spraaktest.

## Gegevens: belangrijke open eis
11 echte minortitels met bron-URL en korte geparafraseerde inhoud, verzameld uit de zoekmachine-index van Kies op Maat op 15 oktober 2026. Dit is NIET live gescrapet: de website gaf HTTP 401/anti-botblokkade. Geen datums of toelating gefingeerd. Niet claimen dat de scrape-eis afgerond is.

    python scrape.py

Het script gebruikt robots.txt, beperkte snelheid en stops bij toegangsblokkades. Het levert pas een kandidatenbestand op als alle bekende pagina's correct verwerkt zijn. Het overschrijft de app niet; controleer inhoud en labels, vervang daarna bewust dist/minors.json en werk de bronmelding in app/index bij. Vraag bij een blokkade toegestane toegang/export aan Kies op Maat. Geen omzeiling. Het script verzamelt de bekende selectie, geen volledige landelijke catalogus.

## Tests
Node.js is alleen nodig voor de automatische tests:

    node test.mjs

Of kies Testlab in de app. Zie dist/TESTPLAN.md voor de vier handmatige spraaktests. Echte gebruikerstests, foto's en presentatiefeedback moeten jullie zelf uitvoeren.

## Architectuur
Browsermicrofoon → browser-spraakdienst (mogelijk extern, opt-in) → gecontroleerd tekstveld → lokaal gespreksmodel (engine.mjs) → lokale onderwerpdetectie → minors.json → brongebonden antwoord → lokale Nederlandse spraaksynthese.
Geen applicatiebackend, database, tracking of gespreksopslag. Hosting kan technische toegangslogs verwerken. UI gebruikt textContent voor gebruikersinvoer en brondata (geen HTML-injectie).

## Matchen en eerlijkheid
Trefwoorden koppelen interesses aan handmatig aangebrachte onderwerplabels. Meerdere onderwerp-overeenkomsten krijgen voorrang; daarna alfabetische volgorde. Studie, leeftijd, geslacht en afkomst tellen niet mee in ranking. Dat voorkomt geen alle bias: de beperkte bronselectie, labels en taalherkenning kunnen benadelen. De opleiding blijft alleen in het profiel voor gesprek/context. Verdiepen/verbreden wordt uitgevraagd maar is geen toelatingsfilter. De inhoudelijke vervolgvraag kan extra interessecategorieën toevoegen; nuances binnen dezelfde categorie wijzigen niet altijd de ranking. Geen matchpercentages of geschiktheidsgaranties.

## Privacy en AVG
Geen persoonsgegevens nodig. Alle antwoorden tijdelijk in werkgeheugen; vernieuwen/reset/sluiten verwijdert ze. Geen localStorage, cookies of eigen audiologging. Browserleverancier kan spraak verwerken; dit wordt vooraf uitgelegd met aparte keuze. Bewaartermijnen daarvan zijn niet geverifieerd. Geen algemene AVG-conformiteitsclaim: verantwoordelijke, hostingvoorwaarden, spraakverwerker en eventuele doorgifte moeten voor echt gebruik worden beoordeeld. Standaard teksten zijn bruikbaar zonder externe spraakdienst.

## Bestanden
- dist/index.html / style.css: interface
- dist/app.mjs: UI, spraak, profiel en feedback
- dist/engine.mjs: lokale gesprekstoestanden en retrieval
- dist/minors.json: beperkte bronlijst
- dist/tests.mjs, test.mjs: checks
- scrape.py: reproduceerbare scraper
- PROMPT_CHARTER.md: gedragsregels en AI-verantwoording

## Opleverstatus
Werkende code voor gesprek, retrieval, bronuitleg en browser-spraakbediening. Automatische testresultaten: zie uitvoering. Live scrape geblokkeerd; end-to-end spraak op doelcomputer en drie studenttests nog niet geverifieerd. Vrijgegeven als PoC, niet productierijp.

# MinorKompas — vier testcases

Automatisch: `node test.mjs`, of open Testlab in de app. De automatische controles bewijzen GEEN werkende microfoon of verstaanbaarheid.

## Handmatig, voor alle vier
1. Open de app via HTTPS of localhost. Kies Geluid aan. Er moet een lokale Nederlandse systeemstem beschikbaar zijn.
2. Klik de microfoon, lees de spraakuitleg en kies alleen bij akkoord voor inschakelen. Sta microfoontoegang in de browser toe.
3. Spreek ieder antwoord in. Controleer de transcriptie en verstuur met de pijl.
4. Controleer dat de agent zijn vragen en aanbevelingen in het Nederlands voorleest.
5. Noteer werkelijk resultaat, geslaagd/niet geslaagd en verbeteractie. Vul geen succesvolle resultaten in zonder uitvoering.

| Test | Gesproken antwoorden | Verwacht |
|---|---|---|
| 1. Verdieping | HBO-ICT → cybersecurity → verdiepen → organisaties beschermen | Vervolgvraag over beveiliging; uitsluitend bestaande cyberminoren uit de bronlijst; inhoudelijke uitleg en werkende bronlinks. |
| 2. Verbreding | Verpleegkunde → eigen bedrijf starten → verbreden → ondernemen verkennen | Ondernemerschap wordt aanbevolen ondanks zorgachtergrond; dezelfde interesses geven dezelfde ranking bij andere studie of geslacht. |
| 3. Nog onzeker | Journalistiek → ik weet het niet → creatief ontwerpen → verbreden → ontwerpen maken | Agent vraagt eerst door. Daarna een creatieve minor met uitleg. |
| 4. Buiten aanbod | Technische natuurkunde → interstellaire teleportatie | Geen verzonnen minor; beperking van de verzameling en verwijzing naar studieadviseur. |

Aanvullend controleren: weigeren microfoontoegang, ontbrekende Nederlandse stem, netwerkfout, opnieuw beginnen wist profiel en resultaten, vraag naar toelating/deadline geeft onzekerheidsmelding.

## Werkelijk uitgevoerde verificatie tijdens bouw
- De vier geautomatiseerde gesprekstests en bronintegriteit/reset worden met `node test.mjs` gecontroleerd.
- Echte spraak, visuele browserbediening en drie niet-ICT-gebruikers: nog uit te voeren door het team.

## Feedback vastleggen
Tester (zonder naam), studierichting, mondelinge toestemming foto en opname in Canvas, testresultaat en foto. Overzicht: feedback → besluit → aanpassing. Gebruik uitsluitend werkelijk ontvangen feedback.

# Prompt Charter — MinorKompas

## Doel
Studenten helpen interesses te verkennen en bestaande minoren te vinden. De gebruiker beslist zelf, met de studieadviseur als menselijk vangnet.

## Agent en implementatie
Regelgestuurd expertsysteem, geen LLM tijdens gebruik. Dit charter is vertaald naar code, vaste Nederlandse vraagteksten en een beperkte bronlijst; het is geen verstuurde systeemprompt.

## Gedragsregels
- Stel je voor als AI-keuzehulp, geen menselijke adviseur.
- Vraag alleen opleiding, interesses, ontwikkelrichting en inhoudelijke voorkeur.
- Vraag door bij onzekerheid of een te breed antwoord.
- Noem uitsluitend titels en inhoud uit minors.json. Geef per resultaat een bronlink.
- Verzin geen toelating, EC, startdata of beschikbaarheid.
- Maak duidelijk dat afwezigheid in deze verzameling niet betekent dat een minor niet bestaat.
- Rangschik op interesses; gebruik geen afkomst, leeftijd of geslacht. Sluit studenten niet uit op studierichting.
- Geef bij ontbrekende kennis een onzekerheidsmelding en verwijs naar de studieadviseur van de eigen opleiding. Geen fictieve contactpersoon.
- Bewaar geen gesprekken of audio. Vraag afzonderlijk akkoord voor externe browser-spraakherkenning.

## AI-tools tijdens de bouw
ChatGPT/Codex is gebruikt voor implementatie, vormgeving, trefwoordregels, testcode en documentatie. Webzoektools hielpen bestaande Kies op Maat-vermeldingen te vinden. Direct HTTP-ophalen is geprobeerd en gaf HTTP 401; de app meldt dat de actuele dataset uit de index komt. AI-output is gecontroleerd via vier automatische gesprekstests, bronintegriteit en codecontroles. Browser-spraak en gebruikersfeedback zijn niet automatisch bewezen.

## Beperkingen en menselijke controle
Handmatige controle op doelcomputer, actualiteit/toelating controleren bij bronsite, dataset en labels op representativiteit beoordelen, drie niet-ICT-studenttests uitvoeren. Voor productie zijn gegevensverwerking en verwerkersafspraken nog te beoordelen.

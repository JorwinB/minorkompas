# Architectuurschets MinorKompas

```mermaid
flowchart TB
  Student[Student] -->|Spreken of typen| UI
  subgraph Browser[Browser van de student]
    UI[Interface en gecontroleerd tekstveld]
    STT[Nederlandse spraakherkenning]
    Agent[Regelgestuurde agent en tijdelijk profiel]
    Zoek[Onderwerpen herkennen en minoren rangschikken]
    Data[minors.json: 11 bronvermeldingen]
    Antwoord[Uitleg met bronlink of verwijzing naar studieadviseur]
    TTS[Lokale Nederlandse stem]
    UI -->|Audio na toestemming| STT
    STT -->|Transcript ter controle| UI
    UI -->|Bevestigd antwoord| Agent
    Agent -->|Vervolgvraag| UI
    Agent -->|Interesses| Zoek
    Data --> Zoek
    Zoek --> Antwoord
    Antwoord --> UI
    UI -->|Voorlezen indien ingeschakeld| TTS
  end
  TTS --> Student
  STT <-->|Afhankelijk van browser| Spraakdienst[Externe browser-spraakdienst]
  Hosting[Sites-hosting] -->|HTML, CSS, JavaScript en JSON| UI
  UI -->|Bronlink openen| KOM[Kies op Maat]
```

## Dataverzameling
De huidige dataset is handmatig gestructureerd uit geïndexeerde Kies op Maat-pagina's. Een rechtstreekse scrape gaf HTTP 401. Het meegeleverde scrape.py controleert robots.txt en stopt bij blokkades. Een succesvolle uitvoering levert een kandidatenbestand voor handmatige beoordeling; het wijzigt de app niet automatisch.

## Grenzen
Geen eigen backend of database voor gesprekken. Profiel en antwoorden bestaan alleen in het tabbladgeheugen. Spraakherkenning kan audio extern verwerken, na afzonderlijke keuze. Voorlezen gebruikt uitsluitend een lokale Nederlandse stem. Hosting kan technische toegangslogs verwerken.

De agent is een expertsysteem met vaste vragen en trefwoorden, geen generatief taalmodel. Studieachtergrond is context, geen rankingfilter. Aanbevelingen worden alleen uit de dataset opgebouwd. Beschikbaarheid en toelating zijn niet bevestigd. Echte spraaktests en AVG-beoordeling voor productie blijven nodig.

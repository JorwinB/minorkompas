import json
from pathlib import Path
rows=[
('143574','Cyber Security: Weerbaar tegen cybercrime','Avans Hogeschool','avans/ATIX/143574',['cyber'],'Onderzoekt hoe je jezelf en organisaties tegen cybercriminaliteit beschermt.'),
('142678','Cyber Security','Hogeschool Inholland','Inholland/TOI/142678',['cyber'],'Verbindt technische kennis van cybersecurity met de samenwerking tussen technische medewerkers en management.'),
('139439','Ondernemerschap','Hogeschool Utrecht','hu/IMC/139439',['ondernemen'],'Richt zich op ondernemende studenten die actief aan hun toekomst willen werken.'),
('9021','Ondernemerschap','Fontys','fontys/-/9021',['ondernemen'],'Je ontwikkelt een eigen idee of bedrijf met begeleiding van ervaren ondernemers.'),
('145365','Ondernemerschap','Hogeschool van Amsterdam','hva/FBE/145365',['ondernemen'],'Je start vanuit een eigen idee met een klein team een onderneming.'),
('141498','Creatief denken en ontwerpen','HZ University of Applied Sciences','hzee/HEW/141498',['creatief'],'Je verkent nieuwe mogelijkheden en oplossingen door creatief te denken en te ontwerpen.'),
('141501','De herstelgerichte professional','HZ University of Applied Sciences','hzee/HEW/141501',['zorg'],'Richt zich op ondersteuning van mensen met psychische problemen, een verstandelijke beperking of hersenletsel.'),
('143448','Minor Aarde en duurzaamheid','Open Universiteit','ou/Beta/143448',['duurzaam'],'Je onderzoekt klimaat, biodiversiteit en de invloed van mensen op het milieu.'),
('140217','Circulaire Economie (locatie Enschede)','Saxion','saxion/SFIB/140217',['duurzaam','ondernemen'],'Je werkt aan circulaire bedrijfsmodellen, materiaalgebruik en het organiseren van duurzame oplossingen.'),
('141429','Business Analytics deel 1','HZ University of Applied Sciences','hzee/AvEM/141429',['data'],'Je leert hoe organisaties gegevens analyseren en benutten bij beslissingen.'),
('141802','Business Management Analytics','Hogeschool Utrecht','hu/IIBS/141802',['data'],'Je ontwikkelt vaardigheden in bedrijfsdata, business intelligence en analyse.')]
data={'collected_at':'2026-10-15','method':'Handmatig gestructureerd uit zoekmachine-index van Kies op Maat. Directe scrape geblokkeerd (HTTP 401).','live_verified':False,'minors':[dict(id=i,title=t,institution=school,url='https://www.kiesopmaat.nl/modules/'+p+'/',tags=tags,summary=s,admission=None) for i,t,school,p,tags,s in rows]}
Path('dist/minors.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))

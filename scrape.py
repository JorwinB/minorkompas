"""Haal de bekende Kies op Maat-pagina's op. Omzeilt geen blokkades.
python scrape.py
Uitvoer: scraped-candidates.json; beoordeel dit vóór vervanging van dist/minors.json.
Standaardbibliotheek, geen installatie nodig.
"""
import json, time, urllib.request, urllib.error, urllib.robotparser
from html.parser import HTMLParser
from datetime import datetime, timezone
from pathlib import Path
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.h=0; self.p=0; self.title=[]; self.paragraphs=[]; self.current=[]
    def handle_starttag(self, tag, attrs):
        if tag=='h1': self.h+=1
        if tag=='p': self.p+=1; self.current=[]
    def handle_data(self, text):
        if self.h: self.title.append(text)
        if self.p: self.current.append(text)
    def handle_endtag(self, tag):
        if tag=='h1': self.h=max(0,self.h-1)
        if tag=='p':
            self.p=max(0,self.p-1); text=' '.join(' '.join(self.current).split())
            if len(text)>70: self.paragraphs.append(text)

def main():
    seed=json.loads(Path('dist/minors.json').read_text())
    ua='MinorKompas-EducationPoC/1.0'
    robots=urllib.robotparser.RobotFileParser('https://www.kiesopmaat.nl/robots.txt')
    try:
        with urllib.request.urlopen(robots.url,timeout=20) as r: robots.parse(r.read().decode().splitlines())
    except Exception as e: raise SystemExit('Robotscontrole mislukt; geen scrape gestart: '+str(e))
    rows=[]
    for item in seed['minors']:
        if not robots.can_fetch(ua,item['url']): raise SystemExit('Niet toegestaan door robots.txt: '+item['url'])
        try:
            req=urllib.request.Request(item['url'],headers={'User-Agent':ua})
            with urllib.request.urlopen(req,timeout=20) as r: html=r.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            raise SystemExit(f'Gestopt: HTTP {e.code}. Geen blokkades omzeild. Bestaande gegevens ongewijzigd. Vraag de beheerder om toegestane toegang of een export.')
        except Exception as e: raise SystemExit('Ophalen mislukt; bestaande gegevens ongewijzigd: '+str(e))
        page=Page(); page.feed(html)
        if not page.title or not page.paragraphs: raise SystemExit('Onverwachte pagina-indeling; handmatige controle nodig: '+item['url'])
        title=' '.join(' '.join(page.title).split())
        if ' '.join(title.lower().split())!=' '.join(item['title'].lower().split()): raise SystemExit('Titel wijkt af van bekende minor; controleer pagina: '+item['url'])
        rows.append({**item,'title':title,'summary':page.paragraphs[0][:600],'source_method':'direct HTML scrape','review_required':True})
        time.sleep(1)
    out={**seed,'collected_at':datetime.now(timezone.utc).isoformat(),'method':'Direct HTML scrape; inhoud en labels handmatig controleren','live_verified':True,'minors':rows}
    Path('scraped-candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print(f'{len(rows)} kandidaten in scraped-candidates.json. Controleer inhoud, labels en privacy voordat je deze publiceert. De app is nog niet gewijzigd.')
if __name__=='__main__':main()

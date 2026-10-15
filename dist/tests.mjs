import {createSession,respond,rank} from './engine.mjs';
export function runTests(data){
 const run=answers=>{const s=createSession();let r;const turns=[];for(const a of answers){r=respond(s,a,data);turns.push(r);}return {s,r,turns};};
 const a=run(['HBO-ICT','Cybersecurity','Verdiepen','Organisaties beschermen']);
 const b=run(['Verpleegkunde','Eigen bedrijf starten','Verbreden','Ondernemen verkennen']);
 const c=run(['Journalistiek','Ik weet het niet','Creatief ontwerpen','Verbreden','Ontwerpen maken']);
 const d=run(['Technische natuurkunde','Interstellaire teleportatie']);
 return [
 {name:'1. ICT-student zoekt cybersecurity',pass:a.r.results?.length>0&&a.r.results.every(m=>m.tags.includes('cyber')&&data.some(x=>x.id===m.id)),detail:'Doorvragen, brongebonden resultaten en cybersecurity-match.'},
 {name:'2. Zorgstudent verkent ondernemen',pass:b.r.results?.length>0&&b.r.results.every(m=>m.tags.includes('ondernemen'))&&JSON.stringify(rank(data,{...b.s,study:'HBO-ICT, man'}).map(m=>m.id))===JSON.stringify(rank(data,{...b.s,study:'Verpleegkunde, vrouw'}).map(m=>m.id)),detail:'Interesse bepaalt de matches; opleiding en geslacht veranderen de rangschikking niet.'},
 {name:'3. Student weet nog niet wat die wil',pass:!c.turns[1].results&&c.turns[1].text.includes('Wat doe je graag')&&c.r.results?.some(m=>m.tags.includes('creatief')),detail:'Eerst verduidelijken, daarna een aanbeveling met een bron.'},
 {name:'4. Geen passende gegevens',pass:d.r.handoff===true&&!d.r.results&&/studieadviseur/.test(d.r.text),detail:'Geen fictieve minor, beperking benoemd en menselijk vangnet.'}
 ];
}

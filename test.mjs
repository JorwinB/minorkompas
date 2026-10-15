import assert from 'node:assert/strict';
import fs from 'node:fs';
import {runTests} from './dist/tests.mjs';
import {detect,createSession,respond} from './dist/engine.mjs';
const data=JSON.parse(fs.readFileSync('dist/minors.json')).minors;
for(const t of runTests(data)){console.log((t.pass?'PASS':'FAIL')+' '+t.name);assert.ok(t.pass,t.name);}
assert.equal(new Set(data.map(m=>m.id)).size,data.length);
assert.ok(data.every(m=>new URL(m.url).hostname==='www.kiesopmaat.nl'));
assert.ok(!detect('Ik wil geen cybersecurity, wel ondernemen').includes('cyber'));
const s=createSession();respond(s,'ICT',data);respond(s,'cybersecurity',data);respond(s,'verdiepen',data);respond(s,'beveiliging',data);
assert.ok(respond(s,'Wat is de deadline?',data).handoff);
respond(s,'opnieuw',data);assert.equal(s.study,'');assert.deepEqual(s.topics,[]);
console.log('PASS bronintegriteit, negatieve interesse, onzekerheid en reset');

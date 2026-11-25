#!/usr/bin/env python3
"""Löst jedes Deutsch-Paket mit der App (headless Chrome): validatePack, jede Aufgabe mit der Musterlösung (muss volle Punkte geben),
mit einer falschen Antwort (darf nicht voll geben) und prüft die Punkte gegen punkte_von.

Aufruf:  python3 tools/deutsch_test.py deutsch_p1a deutsch_p1b ...   (Modulnamen mit build())
     oder python3 tools/deutsch_test.py --json pakete/joel-dario/deutscharbeit-02.12.2026/*.json
"""
import importlib
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from playwright.sync_api import sync_playwright   # noqa: E402

JS = r"""
(packs) => packs.map(p => {
  const out = {id: p.id, valid: validatePack(p), loes: [], falsch: [], punkte: 0};
  p.aufgaben.forEach((t, i) => {
    const n = i + 1;
    let ok = [], bad = [];
    switch (t.typ) {
      case 'mc': ok = [[].concat(t.richtig)]; {
        const r = [].concat(t.richtig);
        const wrong = t.antworten.map((_, k) => k).filter(k => !r.includes(k));
        bad = wrong.map(k => [k]); } break;
      case 'tf': ok = [t.richtig]; bad = [!t.richtig]; break;
      case 'kurz': ok = [].concat(t.richtig).map(String); bad = ['xqzv']; break;
      case 'luecke': {
        const g = gapsOf(t);
        ok = [g.map(x => x.ans[0])];
        // alle erlaubten Alternativen einzeln
        g.forEach((x, gi) => x.ans.slice(1).forEach(alt => { const a = g.map(y => y.ans[0]); a[gi] = alt; ok.push(a); }));
        bad = [g.map(() => 'xqzv')];
        if (t.gross) {   // Groß/klein vertauscht muss falsch sein
          g.forEach((x, gi) => { const w = x.ans[0]; const f = (w[0] === w[0].toUpperCase() ? w[0].toLowerCase() : w[0].toUpperCase()) + w.slice(1);
            if (!x.ans.includes(f)) { const a = g.map(y => y.ans[0]); a[gi] = f; bad.push(a); } });
        }
        if (t.auswahl) {   // jede andere Auswahl an der Stelle ist falsch, wenn sie keine erlaubte Antwort ist
          g.forEach((x, gi) => t.auswahl.filter(o => !x.ans.includes(o)).forEach(o => { const a = g.map(y => y.ans[0]); a[gi] = o; bad.push(a); }));
        }
      } break;
      case 'zuordnen': ok = [t.paare.map(x => x[1])]; {
        const rs = t.paare.map(x => x[1]);
        const anders = [...new Set(rs.concat(t.extra || []))];
        if (anders.length > 1) bad = [rs.map(r => anders.find(a => a !== r))]; } break;
      case 'reihenfolge': ok = [t.schritte.map((_, k) => k)]; bad = [t.schritte.map((_, k) => t.schritte.length - 1 - k)]; break;
      case 'frei': out.punkte += t.punkte; return;
    }
    const max = maxPoints(t); out.punkte += max;
    ok.forEach(a => { const r = evaluate(t, a, true); if (Math.abs(r.got - max) > 1e-9) out.loes.push([n, t.typ, JSON.stringify(a), r.got + '/' + max]); });
    bad.forEach(a => { const r = evaluate(t, a, true); if (Math.abs(r.got - max) < 1e-9) out.falsch.push([n, t.typ, JSON.stringify(a)]); });
  });
  return out;
})
"""


def laden(args):
    packs = []
    if args and args[0] == "--json":
        for f in args[1:]:
            packs.append(json.load(open(f, encoding="utf-8")))
    else:
        for m in args:
            packs += importlib.import_module(m).build()
    return json.loads(json.dumps(packs, ensure_ascii=False))


def main(args):
    packs = laden(args)
    schlecht = 0
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = br.new_page()
        pg.goto("file://" + os.path.abspath(os.path.join(HIER, "..", "index.html")))
        res = pg.evaluate(JS, packs)
        br.close()
    from deutsch_lib import punkte_von
    for p, r in zip(packs, res):
        py = sum(punkte_von(t) for t in p["aufgaben"])
        status = "OK " if not (r["valid"] or r["loes"] or r["falsch"]) and py == r["punkte"] else "FEHLER"
        print(f"{status} {r['id']:42s} {len(p['aufgaben']):3d} Aufgaben, {r['punkte']:3d} Punkte (Python {py})")
        for k in ("valid", "loes", "falsch"):
            for x in r[k][:12]:
                print("   ", k, x)
                schlecht += 1
        if py != r["punkte"]:
            schlecht += 1
    return 1 if schlecht else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

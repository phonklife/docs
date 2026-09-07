from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'PIENHS/00_SYSTEM/status.md').read_text(encoding='utf-8')
rows=[]
for sec in re.split(r'(?=## M\d )',text):
    m=re.match(r'## (M\d) (.+)',sec)
    if not m: continue
    checks=re.findall(r'- \[( |x|X)\]',sec)
    done=sum(c.lower()=='x' for c in checks); total=len(checks)
    pct=round(done/total*100) if total else 0
    rows.append((m.group(1),m.group(2).strip(),done,total,pct))
out=['# PIENHS STATUS DASHBOARD','','| Milestone | Name | Done | Progress |','|---|---|---:|---:|']
out += [f'| {m} | {n} | {d}/{t} | {p}% |' for m,n,d,t,p in rows]
(ROOT/'PIENHS/00_SYSTEM/STATUS_DASHBOARD.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('Dashboard generated')

from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'PIENHS/00_SYSTEM/status.md').read_text(encoding='utf-8')
m=re.search(r'## M7 RELEASE(.*?)(?:\n## |\Z)',text,re.S)
if not m:
    print('M7 missing'); sys.exit(1)
unresolved=re.findall(r'- \[ \] (.+)',m.group(1))
if unresolved:
    print('RELEASE BLOCKED')
    for x in unresolved: print('- '+x)
    sys.exit(1)
print('RELEASE GATE PASS')

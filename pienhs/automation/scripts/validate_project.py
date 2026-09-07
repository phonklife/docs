from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'pienhs.config.json').read_text(encoding='utf-8'))
errors=[]
for f in ['PIENHS/00_SYSTEM/status.md','pienhs.config.json']:
    if not (ROOT/f).exists(): errors.append('Missing: '+f)
status=ROOT/'PIENHS/00_SYSTEM/status.md'
if status.exists():
    text=status.read_text(encoding='utf-8')
    m=re.search(r'current_milestone:\s*(M\d+)',text)
    if not m: errors.append('Missing current_milestone')
    elif m.group(1) not in cfg['milestones']: errors.append('Invalid milestone: '+m.group(1))
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: PIENHS automation state valid')

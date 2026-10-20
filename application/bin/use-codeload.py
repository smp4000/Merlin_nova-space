#!/usr/bin/env python3
"""Use GitHub's official archive destination directly on restricted networks.

Versions, commit references and expected archive checksums are preserved.
The API zipball endpoint normally redirects to this same legacy.zip URL.
Run again after an intentional Composer dependency update if needed.
"""
import json, os, re
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[1])
p=Path('composer.lock');data=json.loads(p.read_text());count=0
for package in data['packages']+data.get('packages-dev',[]):
    dist=package.get('dist',{})
    match=re.fullmatch(r'https://api\.github\.com/repos/([^/]+/[^/]+)/zipball/([0-9a-f]{40})',dist.get('url',''))
    if match:
        dist['url']=f'https://codeload.github.com/{match[1]}/legacy.zip/{match[2]}'
        count+=1
if count:p.write_text(json.dumps(data,indent=4,ensure_ascii=False)+'\n')
print(f'{count} official GitHub archive URLs normalized; versions and checksums unchanged.')

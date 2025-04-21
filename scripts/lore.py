import json
import os
import re
from globalFunctions import hexRename
loreList = os.listdir('lore\\files')
with open('log.md','a',encoding='utf-8') as f:
    f.write(f'## Lore Books:\n')
for file in loreList:
    output = ''
    with open(f'lore/files/{file}','r',encoding='utf-8') as f:
        lore = json.load(f)
    for i in lore['entries']:
        if i['enabled'] == True:
            output += f'> # {i['name']}\n> {i['entry']}\n\n'
    with open(f'lore/md/{hexRename(re.sub(r'^(.*)\.json$',r'\1.md',file))}','w',encoding='utf-8') as f:
        f.write(output)
    with open('log.md','a',encoding='utf-8') as f:
        f.write(f'- Created: `{f'lore/md/{hexRename(re.sub(r'^(.*)\.json$',r'\1.md',file))}'}`\n    - From: `{f'lore/files/{file}'}`\n')
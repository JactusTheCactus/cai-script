import json
import os
import re
from globalFunctions import enigmaRename
loreList = os.listdir(os.path.join('lore','files'))
with open('log.md','a',encoding='utf-8') as f:
    f.write(f'# Lore Books:\n')
for file in loreList:
    inputFile = os.path.join('lore','files',file)
    outputFile = os.path.join('lore','md',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.md',file)))
    output = ''
    with open(inputFile,'r',encoding='utf-8') as f:
        lore = json.load(f)
    for i in lore['entries']:
        if i['enabled'] == True:
            output += f'> # {i['name']}\n> {i['entry']}\n\n'
    with open(outputFile,'w',encoding='utf-8') as f:
        f.write(output)
    with open('log.md','a',encoding='utf-8') as f:
        f.write(f'- created `{re.sub(r'lore\\md\\(.*)',r'\1',outputFile)}` from `{re.sub(r'lore\\files\\(.*)',r'\1',inputFile)}`\n')
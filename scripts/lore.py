def lore():
    import json
    import os
    import re
    from config import enigmaRename, log
    #from script import log
    print('Generating Lore Books...')
    loreList = os.listdir(os.path.join('lore','files'))
    with open(log,'a',encoding='utf-8') as f:
        f.write(f'# Lore Books:\n')
    for file in loreList:
        inputFile = os.path.join('lore','files',file)
        outputFile = os.path.join('lore','md',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.md',file)))
        output = ''
        outputName = re.sub(r'lore\\md\\(.*)',r'\1',outputFile)
        inputName = re.sub(r'lore\\files\\(.*)',r'\1',inputFile)
        with open(inputFile,'r',encoding='utf-8') as f:
            lore = json.load(f)
        for i in lore['entries']:
            if i['enabled'] == True:
                output += f"> # {i['name']}\n> {i['entry']}\n\n"
        with open(outputFile,'w',encoding='utf-8') as f:
            f.write(output)
        with open('log.md','a',encoding='utf-8') as f:
            f.write(f'- created `{outputName}` from `{inputName}`\n')
        print(f'Generating {outputName}...')
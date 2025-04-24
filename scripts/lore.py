def lore():
    import json
    import os
    import re
    from config import enigmaRename, logFormat
    from config import log as textLog
    print('Generating Lore Books...')
    loreList = os.listdir(os.path.join('lore','source'))
    with open(textLog,'a',encoding='utf-8') as f:
        f.write(f'Lore Books:\n')
    for file in loreList:
        inputFile = os.path.join('lore','source',file)
        outputMd = os.path.join('lore','readable','md',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.md',file)))
        outputHtml = os.path.join('lore','readable','html',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.html',file)))
        mdOutput = ''
        htmlOutput = ''
        mdName = re.sub(r'lore\\readable\\md\\(.*)',r'\1',outputMd)
        htmlName = re.sub(r'lore\\readable\\html\\(.*)',r'\1',outputHtml)
        inputName = re.sub(r'lore\\source\\(.*)',r'\1',inputFile)
        with open(inputFile,'r',encoding='utf-8') as f:
            lore = json.load(f)
        for i in lore['entries']:
            if i['enabled'] == True:
                mdOutput += f"> # {i['name']}\n> {i['entry']}\n\n"
                htmlOutput += f"<blockquote><h1>{i['name']}</h1></blockquote>\n<blockquote>{i['entry']}</blockquote>\n\n"
        with open(outputMd,'w',encoding='utf-8') as f:
            f.write(mdOutput)
        with open(outputHtml,'w',encoding='utf-8') as f:
            f.write(htmlOutput)
        with open(textLog,'a',encoding='utf-8') as f:
            f.write(f'{logFormat(inputName,mdName)}\n')
            f.write(f'{logFormat(inputName,htmlName)}\n')
        print(f'    {mdName[17:]}...')
        print(f'    {htmlName[19:]}...')
    print('Lore Books Generated Successfully')
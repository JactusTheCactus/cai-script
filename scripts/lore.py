def lore():
    import json
    import os
    import re
    from config import enigmaRename, logFormat, log as textLog, toHTML
    print('Generating Lore Books...')
    loreList = os.listdir(os.path.join('lore','source'))
    with open(textLog,'a',encoding='utf-8') as f:
        f.write(f'''Lore Books:
''')
    for file in loreList:
        inputFile = os.path.join('lore','source',file)
        outputMd = os.path.join('lore','formatted','md',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.md',file)))
        outputHtml = os.path.join('lore','formatted','html',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.html',file)))
        mdName = re.sub(r'lore\\formatted\\md\\(.*)',r'\1',outputMd)
        htmlName = re.sub(r'lore\\formatted\\html\\(.*)',r'\1',outputHtml)
        inputName = re.sub(r'lore\\source\\(.*)',r'\1',inputFile)
        with open(inputFile,'r',encoding='utf-8') as f:
            lore = json.load(f)
        mdOutput = f'''# {lore["name"]}
'''
        htmlOutput = f'<h1>{lore["name"]}</h1>'
        if lore["description"]:
            mdOutput += lore['description'] + """
"""
            htmlOutput += "<p>" + lore['description'] + "</p>"
        for i in lore['entries']:
            if i['enabled'] == True:
                mdOutput += "## " + i['name'] + """
""" + i['entry'] + """
"""
                htmlOutput += f"<blockquote><h2>{i['name']}</h3></blockquote><blockquote>{i['entry']}</blockquote>"
        with open(outputMd,'w',encoding='utf-8') as f:
            f.write(mdOutput)
        with open(outputHtml,'w',encoding='utf-8') as f:
            f.write(toHTML(htmlOutput))
        with open(textLog,'a',encoding='utf-8') as f:
            f.write(f'''    {logFormat(inputName,mdName)}
''')
            f.write(f'''    {logFormat(inputName,htmlName)}
''')
            if mdName[18:-3] == htmlName[20:-5]:
                print(f'    {mdName[18:-3]}')
    print()
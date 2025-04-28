def loreFunction():
    import json
    import os
    import re
    from config import enigmaRename, toHTML
    loreList = os.listdir(os.path.join('lore','source','agnaistic'))
    skipList = [
        'agnaistic',
        'cai'
    ]
    for i in skipList:
        if i in loreList:
            loreList.remove(i)
    for file in loreList:
        inputFile = os.path.join('lore','source','agnaistic',file)
        outputMd = os.path.join('lore','formatted','md',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.md',file)))
        outputHtml = os.path.join('lore','formatted','html',enigmaRename(re.sub(r'^(.*)\.json$',r'\1.html',file)))
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
""" + i['entry'].replace('\n','\n\n') + """
"""
                htmlOutput += f"<blockquote><h2>{i['name']}</h3></blockquote><blockquote>{i['entry']}</blockquote>"
        with open(outputMd,'w',encoding='utf-8') as f:
            f.write(mdOutput)
        with open(outputHtml,'w',encoding='utf-8') as f:
            f.write(toHTML(htmlOutput))
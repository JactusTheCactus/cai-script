def chat():
    import re
    import json
    import os
    from config import log as textLog
    from config import enigmaRename, logFormat
    def entryHtmlFormat(md):
        html = f"> # {md[0]}:\n{re.sub(r'^(.*?)$',r'> \1',md[1],flags=re.M)}"
        html = re.sub(r'# (.*?):',r'<h1>\1</h1>',html)
        html = re.sub(r'(_|\*){2}(.*?)\1{2}',r'<b>\2</b>',html)
        html = re.sub(r'(_|\*)(.*?)\1',r'<i>\2</i>',html)
        html = re.sub(r'OOC: (.*)',r'<code>\1</code>',html)
        #html = re.sub(r'\n',r'',html)
        return html
    print('Generating Chat Logs...')
    with open('charId.json','r',encoding='utf-8') as f:
        charIdDict = json.load(f)
    chatLogs = os.listdir(os.path.join('chats','source'))
    def getNames(file):
        capList = []
        basename = os.path.splitext(file)[0]
        lowerList = basename.split("&")
        for name in lowerList:
            capList.append(name.capitalize())
        return capList
    with open(textLog,'a',encoding='utf-8') as f:
        f.write(f'Chats:\n')
    def logChat(file):
        names = getNames(file)
        user = names[0]
        character = names[1]
        def fileMatch(file, extension):
            pattern = r'.*\.(' + extension + r')$'
            return bool(re.match(pattern, file))
        input = os.path.join('chats','source',file)
        outputMd = os.path.join('chats','readable','md',enigmaRename(re.sub(r'^(.*)\..*$',r'\1.md',file)))
        outputMdFile = re.sub(r'chats\\readable\\md\\(.*)',r'\1',outputMd)
        outputHtml = os.path.join('chats','readable','html',enigmaRename(re.sub(r'^(.*)\..*$',r'\1.html',file)))
        outputHtmlFile = re.sub(r'chats\\readable\\html\\(.*)',r'\1',outputHtml)
        inputFile = re.sub(r'chats\\source\\(.*)',r'\1',input)
        if fileMatch(file,'jsonl'):
            with open(input, "r", encoding="utf-8") as f:
                data = [json.loads(line) for line in f if line.strip()]
            extracted_data = [
                [entry.get('name'), entry.get('mes')] 
                for entry in data if next(iter(entry)) != 'user_name'
            ]
            for i in extracted_data:
                if i[0] == 'You':
                    i[0] = user
                elif i[0] == 'Character':
                    i[0] = character
            with open(outputMd,'w') as f:
                for i in extracted_data:
                    f.write(f"> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n")
            with open(outputHtml,'w') as f:
                for i in extracted_data:
                    f.write(entryHtmlFormat(i))
        elif fileMatch(file,'json'):
            with open(input, "r", encoding="utf-8") as f:
                data = json.load(f)
            log = []
            for i in data["messages"]:
                name = None
                if i.get('handle'):
                    name = i["handle"]
                else:
                    name = charIdDict[i["characterId"]]
                log.append([name,i['msg']])
            with open(outputMd,'w') as f:
                for i in log:
                    f.write(f"> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n")
            with open(outputHtml,'w') as f:
                for i in log:
                    f.write(entryHtmlFormat(i))
        with open(textLog,'a',encoding='utf-8') as f:
            f.write(f'    {logFormat(input,outputMd)}\n')
            f.write(f'    {logFormat(input,outputHtml)}\n')
        print(f'    {outputMdFile[18:]}...')
        print(f'    {outputHtmlFile[18:]}...')
    for i in chatLogs:
        logChat(i)
    print('Chat Logs Generated Successfully')
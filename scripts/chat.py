def chatFunction():
    import re
    import json
    import os
    from config import toHTML
    from config import enigmaRename
    def insertSubDir(file, subDir):
        dir, filename = os.path.split(file)
        return os.path.join(dir, subDir, filename)
    def entryHtmlFormat(input):
        input[1] = re.sub(r'^(.*?)$',r'\1',input[1],flags=re.M)
        html = f"<h1>{input[0]}:</h1>{input[1]}"
        html = re.sub(r'(_|\*){2}(.*?)\1{2}',r'<b>\2</b>',html)
        html = re.sub(r'(_|\*)(.*?)\1',r'<i>\2</i>',html)
        html = re.sub(r'OOC: (.*)',r'<code>\1</code>',html)
        html = re.sub(r'`(.*)`',r'<code>\1</code>',html)
        html = re.sub(r'```\n(.*)\n```',r'<pre><code>\1</code></pre>',html)
        html = re.sub(r'\n',r'<br>',html)
        return toHTML(html)
    def entryMdFormat(input):
        md = f"# {input[0]}:\n{re.sub(r'^',r'',input[1],flags=re.M)}\n"
        md = re.sub(r'\\n',r'\n',md)
        return md
    with open('data/charId.json','r',encoding='utf-8') as f:
        charIdDict = json.load(f)
    chatLogs = []
    source = os.path.join('chats', 'source')
    for folder in os.listdir(source):
        folder_path = os.path.join(source, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                chatLogs.append(f"{folder} => {file}")
    def getNames(file):
        file = re.sub(r'.* => (.*?)',r'\1',file)
        capList = []
        basename = os.path.splitext(file)[0]
        lowerList = basename.split("&")
        for name in lowerList:
            capList.append(name.capitalize())
        return capList
    def logChat(file):
        format = re.sub(r'(.*) \=\> .*',r'\1',file)
        file = re.sub(r'.*? => (.*?)',r'\1',file)
        names = getNames(file)
        user = names[0]
        character = names[1]
        input = os.path.join('chats','source',file)
        outputMd = os.path.join('chats','formatted','md',enigmaRename(re.sub(r'^(.*)\..*$',r'\1.md',file)))
        outputHtml = os.path.join('chats','formatted','html',enigmaRename(re.sub(r'^(.*)\..*$',r'\1.html',file)))
        if format == 'cai':
            with open(insertSubDir(input, format), "r", encoding="utf-8") as f:
                data = [json.loads(line) for line in f if line.strip()]
            extracted_data = [
                [entry.get('name'), entry.get('mes')] 
                for entry in data if next(iter(entry)) != 'user_name'
            ]
            for i in extracted_data:
                print(i)
                if i[0] == 'You':
                    i[0] = user
                else:
                    i[0] = character
            with open(outputMd,'w') as f:
                for i in extracted_data:
                    f.write(entryMdFormat(i))
            with open(outputHtml,'w') as f:
                for i in extracted_data:
                    f.write(entryHtmlFormat(i))
        elif format == 'agnaistic':
            with open(insertSubDir(input, format), "r", encoding="utf-8") as f:
                data = json.load(f)
            log = []
            for i in data["messages"]:
                name = None
                if i.get('name') and i.get('name') != 'JactusTheCactus':
                    name = i["name"]
                elif i.get('handle'):
                    name = i["handle"]
                elif i["characterId"] in charIdDict:
                    name = charIdDict[i["characterId"]]
                else:
                    name = "None"
                    if i.get('characterId'):
                        print(f"missing name for characterId: {i.get('characterId')}")
                log.append([name,i['msg']])
            with open(outputMd,'w') as f:
                for i in log:
                    f.write(entryMdFormat(i))
            with open(outputHtml,'w') as f:
                for i in log:
                    f.write(entryHtmlFormat(i))
    for i in chatLogs:
        logChat(i)

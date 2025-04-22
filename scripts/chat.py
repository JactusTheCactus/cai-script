import re
import json
import os
from globalFunctions import enigmaRename, seedString
with open('charId.json','r',encoding='utf-8') as f:
    charIdDict = json.load(f)
chatLogs = os.listdir(os.path.join('chats','files'))
def getNames(file):
    capList = []
    basename = os.path.splitext(file)[0]
    lowerList = basename.split("&")
    for name in lowerList:
        capList.append(name.capitalize())
    return capList
with open('log.md','a',encoding='utf-8') as f:
    f.write(f'# Chats:\n')
def logChat(file):
    names = getNames(file)
    user = names[0]
    character = names[1]
    def fileMatch(file, extension):
        pattern = r'.*\.(' + extension + r')$'
        return bool(re.match(pattern, file))
    input = os.path.join('chats','files',file)
    output = os.path.join('chats','md',enigmaRename(re.sub(r'^(.*)\..*$',r'\1.md',file)))
    outputFile = re.sub(r'chats\\md\\(.*)',r'\1',output)
    inputFile = re.sub(r'chats\\files\\(.*)',r'\1',input)
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
        with open(output,'w') as f:
            for i in extracted_data:
                f.write(f"> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n")
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
        with open(output,'w') as f:
            for i in log:
                f.write(f"> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n")
    with open('log.md','a',encoding='utf-8') as f:
        f.write(f'- created `{outputFile}` from `{inputFile}`\n')
    print(f'Generating {outputFile}...')
for i in chatLogs:
    logChat(i)

import re
import json
import os
from globalFunctions import hexRename
chatLogs = [
    'devin&kristina-01.jsonl',
    'devin&kristina-02.jsonl',
    'sadie&typh.jsonl',
    'devin&sadie.json',
    'rory&leila.json'
]
def getNames(file):
    capList = []
    basename = os.path.splitext(file)[0]
    lowerList = basename.split("&")
    for name in lowerList:
        capList.append(name.capitalize())
    return capList
def logChat(file):
    names = getNames(file)
    user = names[0]
    character = names[1]
    def fileMatch(file, extension):
        pattern = r'.*\.(' + extension + r')$'
        return bool(re.match(pattern, file))
    input = f'chats/files/{file}'
    output = f'chats/md/{hexRename(re.sub(r'^(.*)\..*$',r'\1.md',file))}'
    if fileMatch(file,'jsonl'):
        # Read the JSONL file
        with open(input, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f if line.strip()]

        # Filter and extract 'name' and 'mes' fields
        extracted_data = [
            [entry.get('name'), entry.get('mes')] 
            for entry in data if next(iter(entry)) != 'user_name'
        ]
        for i in extracted_data:
            if i[0] == 'You':
                i[0] = user
            elif i[0] == 'Character':
                i[0] = character

        # Get the result
        with open(output,'w') as f:
            for i in extracted_data:
                f.write(f'> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n')
    elif fileMatch(file,'json'):
        charIdDict = {
            '6b3b0be9-4bbf-449a-a281-0d9298b8bf49': 'Devin',
            'temp-4ca0ebff-931f-4c0d-a67e-b7a7c344d298_841893a3': 'Sadie',
            'temp-4ca0ebff-931f-4c0d-a67e-b7a7c344d298_2bad48e7': 'Leila',
            'temp-4ca0ebff-931f-4c0d-a67e-b7a7c344d298_9158f623': 'Rory'
        }
        # Read the JSON file
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
                f.write(f'> # {i[0]}:\n{re.sub(r'^',r'> ',i[1],flags=re.M)}\n\n')

for i in chatLogs:
    logChat(i)
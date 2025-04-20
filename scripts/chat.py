import re
import json
chatLogs = [
    ['Kristina_tavern_Chat_01.jsonl','Devin','Kristina'],
    ['Kristina_tavern_Chat_02.jsonl','Devin','Kristina'],
    ['Typh_tavern_Chat.jsonl','Sadie','Typh'],
    ['chat-0759.json','Devin','Sadie']
]
def logChat(file, user, character):
    def fileMatch(file, extension):
        pattern = r'.*\.(' + extension + r')$'
        return bool(re.match(pattern, file))
    input = f'chats/files/{file}'
    output = f'chats/md/{re.sub(r'^(.*)\..*$',r'\1.md',file)}'
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
                f.write(f'# {i[0]}:\n{i[1]}\n\n---\n')
    elif fileMatch(file,'json'):
        charIdDict = {
            '6b3b0be9-4bbf-449a-a281-0d9298b8bf49': 'Devin',
            'temp-4ca0ebff-931f-4c0d-a67e-b7a7c344d298_841893a3': 'Sadie'
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
                f.write(f'# {i[0]}:\n{i[1]}\n\n---\n')

for i in chatLogs:
    if not i[0]:
        print('file identifier missing')
    elif not i[1]:
        print('user missing')
    elif not i[2]:
        print('character missing')
    logChat(i[0],i[1],i[2])
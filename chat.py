import re
import json
import os

chatLogs = [
    ['tavern','Kristina_tavern_Chat_01.jsonl','Devin'],
    ['tavern','Kristina_tavern_Chat_02.jsonl','Devin'],
    ['tavern','Typh_tavern_Chat_01.jsonl','Sadie','> You weren\'t supposed to follow her. But you did.\n>\n> Now you\'re standing at the edge of a garden no one talks about. The trees don\'t rustle. The air smells like jasmine and something metallic beneath it.\n>\n> She\'s kneeling at the altar ahead, lit by the dim glow of red lanterns. There\'s blood on her hands. And when she turns to face you, you finally see her for what she is.\n>\n> The fangs. The eyes that glow just slightly in the dark.\n>\n> Typh is a vampire.\n>\n> You weren\'t meant to know. But now you do.'],
    ['agnaistic','chat-0759.json','','',{"6b3b0be9-4bbf-449a-a281-0d9298b8bf49":"Devin","temp-4ca0ebff-931f-4c0d-a67e-b7a7c344d298_841893a3":"Sadie",}]
]
structure = {
    'chats': {
        'files': {},
        'md': {},
    },
    'lore': {
        'files': {},
        'md': {},
    }
}
def create_dirs(base, tree):
    for name, subtree in tree.items():
        path = os.path.join(base, name)
        os.makedirs(path, exist_ok=True)
        create_dirs(path, subtree)
create_dirs('.', structure)
def logChat(format,chatLog,user=None,prologue=None,charIdList=None):
    with open(f'logs/files/{chatLog}','r',encoding='utf-8') as f:
        log = f.read()
    if format == 'tavern':
        if prologue:
            log = re.sub(r'(\{"user_.*\})',r'\1\n## Narrator: \n' + prologue + r'\n',log)
        def regex(item,match,replace):
            return re.sub(match,replace,item)
        regexList = [
            [r'("(?:user_)?name":")You(")',r'\1' + user + r'\2'],
            [r'\\"',r'"'],
            [r'\{"user_name":"(.*?)","character_name":"(.*?)".*?\}',r'# Chat Between \1 & \2:\n'],
            [r'\{"name":"(.*?)","is_user":.*?,"is_name":.*?,"send_date":.*?,"mes":"(.*?)"\}',r'## \1:\n\2\n'],
            [r'\\n',r'\n']
        ]
        for i in regexList:
            output = regex(log,i[0],i[1])
    elif format == 'agnaistic':
        output = '***'
        chat = []
        file = json.loads(log)
        for i in file["messages"]:
            if i["characterId"] in charIdList:
                name = charIdList[i["characterId"]]
            elif i["handle"]:
                name = i["handle"]
            else:
                name = 'Narrator'
            if i["msg"]:
                message = i["msg"]
            chat.append([name,message])
        for i in chat:
            output += f'\n\n# {i[0]}:\n{i[1]}\n\n***'
    mdLog = re.sub(r'(.*?)\..*',r'\1.md',chatLog)
    print(chatLog + f' => {mdLog}')
    with open(f'chats/md/{mdLog}','w',encoding='utf-8') as f:
        f.write(output)
print()
for i in chatLogs:
    while len(i) < 5:
        i.append('')
    logChat(i[0],i[1],i[2],i[3],i[4])
import re

chatLogs = [
    ['Devin','Kristina_tavern_Chat_01.jsonl'],
    ['Devin','Kristina_tavern_Chat_02.jsonl'],
]
def logChat(chatLog,user):
    with open(f'logs/{chatLog}','r',encoding='utf-8') as f:
        log = f.read()
    def regex(item,match,replace):
        return re.sub(match,replace,item)
    regexList = [
        [r'("(?:user_)?name":")You(")',r'\1' + user + r'\2'],
        [r'\\"',r'"'],
        [r'\{"user_name":"(.*?)","character_name":"(.*?)".*?\}',r'# Chat Between \1 & \2:\n'],
        [r'\{"name":"(.*?)","is_user":.*?,"is_name":.*?,"send_date":.*?,"mes":"(.*?)"\}',r'## \1:\n\2\n'],
        [r'\\n',r'\n'],
        [r'OOC: __(.*?)__',r'\1']
    ]
    for i in regexList:
        log = regex(log,i[0],i[1])
    log = re.sub(r'',r'',log)
    logName = re.sub(r'(.*)_tavern_Chat(.*?).jsonl',r'\1\2',chatLog)
    print(f'{logName}.jsonl => {logName}.md')
    with open(f'chats/{logName}.md','w',encoding='utf-8') as f:
        f.write(log)
print()
for i in chatLogs:
    logChat(i[1],i[0])
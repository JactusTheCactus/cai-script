import re

chatLog = 'logs/Kristina_tavern_Chat.jsonl'
user = r'Devin'

with open(chatLog,'r',encoding='utf-8') as f:
    log = f.read()

def regex(item,match,replace):
    return re.sub(match,replace,item)

regexList = [
    [r'("(?:user_)?name":")You(")',r'\1' + user + r'\2'],
    [r'\{"user_name":"(.*?)","character_name":"(.*?)".*?\}',r'# Chat Between `\1` & `\2`:'],
    [r'\{"name":"(.*?)","is_user":.*?,"is_name":.*?,"send_date":.*?,"mes":"(.*?)"\}',r'## `\1`:\n\2\n\n---\n'],
    [r'\\n',r'\n'],
    [r'OOC: __(.*?)__',r'\1'],
    [r'',r''],
    [r'',r''],
    [r'',r''],
]

for i in regexList:
    log = regex(log,i[0],i[1])

log = re.sub(r'',r'',log)

logName = re.sub(r'(.*)_tavern_Chat.jsonl',r'\1',chatLog)

print(logName)

with open(f'{re.sub(r'logs/',r'chats/',logName)}.md','w',encoding='utf-8') as f:
    f.write(log)
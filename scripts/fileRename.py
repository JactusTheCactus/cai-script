import re
lettersDict = {
    'a': '61',
    'b': '62',
    'c': '63',
    'd': '64',
    'e': '65',
    'f': '66',
    'g': '67',
    'h': '68',
    'i': '69',
    'j': '6a',
    'k': '6b',
    'l': '6c',
    'm': '6d',
    'n': '6e',
    'o': '6f',
    'p': '70',
    'q': '71',
    'r': '72',
    's': '73',
    't': '74',
    'u': '75',
    'v': '76',
    'w': '77',
    'x': '78',
    'y': '79',
    'z': '7a',
    '&': '+',
}
lettersArr = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '.md',
    '.json',
    '.jsonl'
]
input = str(input("""
User's Name and Characters' Name. List by order of importance. join with '&'. end with '#XX', in order of age.
Or
Lore book topic.

Example A:
>> User & Character1 & Character2 #01
>> 75736572+6368617261637465721+6368617261637465722-01.json
Example B:
>> lorebook.json
>> 6c6f7265626f6f6b.json

""")).lower()
outputList = []
for i in input:
    if i == '.':
        outputList.append(re.sub(r'(?:.*)\.(.*)',r'.\1',input))
        break
    if i in lettersDict:
        outputList.append(lettersDict[i])
    elif i in lettersArr:
        outputList.append(i)
    else:
        outputList.append('-')
output = ''.join(outputList)
output = re.sub(r'-?\+-?',r'+',output)
output = re.sub(r'(-|\+)\1',r'\1',output)
output = re.sub(r'^[-+]+|[-+]+$',r'',output)
print()
print(output)
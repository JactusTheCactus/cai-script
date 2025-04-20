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
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}
print()
input = str(input("User's Name and Characters' Name (list by order of importance. join with '&'. end with '#XX', in order of age):\nor\nlore book topic:\n")).lower()
outputList = []
for i in input:
    if i in lettersDict:
        outputList.append(lettersDict[i])
    else:
        outputList.append('-')
output = ''.join(outputList)
output = re.sub(r'-?\+-?',r'+',output)
output = re.sub(r'(-|\+)\1',r'\1',output)
output = re.sub(r'^[-+]+|[-+]+$',r'',output)
print()
print(output)
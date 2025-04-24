import re
import os
from datetime import datetime
now = datetime.now()
seed = [
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
]
seedList = []
def toHTML(input):
    output = re.sub(r'',r'',input)
    output = f"<!DOCTYPE html><head></head><link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-dark.css\" integrity=\"sha512-XNBMUjy86G874D+6YN8vaBJpEut/Q0IafwiWxO5CoZDyaVXxbzyzacBpA55GPYhetzeLhxUbgdETrigRIVeNqQ==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\" /><style>.markdown-body{{margin:0 auto;padding:45px;}}@media(max-width:767px){{.markdown-body{{padding:15px;}}}}</style><body class=\"markdown-body\">{output}</body>"
    return output
for s in seed:
    s = str(s)
    if len(s) < 2:
        s = f'0{s}'
    if len(s) > 2:
        s = s[2:]
    seedList.append(s)
seedString = '.'.join(str(strSeed) for strSeed in seedList)
log = os.path.join('logs',f'{seedString}.html')
def enigmaRename(userInput):
    import random
    def generate_rotor(seed):
        """Create a monoalphabetic substitution from a–z → shuffled a–z."""
        random.seed(seed)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        shuffled = alphabet.copy()
        random.shuffle(shuffled)
        return dict(zip(alphabet, shuffled))
    userInput = userInput.lower()
    output = []
    # Pre-generate rotors base on seeds list
    # (we'll re-seed/step each on every character)
    num_rotors = len(seed)
    for idx, ch in enumerate(userInput):
        # Preserve digits & the ampersand
        if ch.isdigit() or ch == '&':
            output.append(ch)
            continue
        # On hitting the dot, append extension and stop
        if ch == '.':
            output.append(userInput[idx:])
            break
        # Non‑alphabetic → dash
        if ch not in 'abcdefghijklmnopqrstuvwxyz':
            output.append('-')
            continue
        # Step & apply each rotor in sequence
        c = ch
        for r, base_seed in enumerate(seed):
            # step: reseed rotor with base_seed + position
            rotor_map = generate_rotor(base_seed + idx)
            c = rotor_map[c]
        output.append(c)
    return ''.join(output)
def logFormat(logInput,logOutput):
    return f'{logInput} => {logOutput}'
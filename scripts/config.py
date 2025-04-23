
import os
from datetime import datetime
now = datetime.now()
seed = []
seed.append(now.year)
seed.append(now.month)
seed.append(now.day)
seed.append(now.hour)
seed.append(now.minute)
seed.append(now.second)
seedList = []
for s in seed:
    s = str(s)
    if len(s) < 2:
        s = f'0{s}'
    if len(s) > 2:
        s = s[2:]
    seedList.append(s)
seedString = '.'.join(str(strSeed) for strSeed in seedList)
log = os.path.join('logs',f'{seedString}.txt')
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
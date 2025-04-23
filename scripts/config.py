
import os
from datetime import datetime
now = datetime.now()
tz = int(now.astimezone().utcoffset().total_seconds() // 3600)
seed = [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, tz]
for i in range(len(seed)):
    if len(f'{seed[i]}') < 2:
        seed[i] = f'0{seed[i]}'
    print(seed[i])
seedString = '.'.join(str(strSeed) for strSeed in seed)
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
    """
    userInput : str
    seeds     : list[int]  — one seed per rotor
    """
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

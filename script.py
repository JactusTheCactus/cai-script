import os
import subprocess
import shutil
from scripts.globalFunctions import seed
seedString = '.'.join(str(strSeed) for strSeed in seed)
structure = {
    'chats': {
        'files': {},
        'md': {},
    },
    'lore': {
        'files': {},
        'md': {},
    },
    'NotebookLM': {},
    'logs': {}
}
scripts = [
    'chat',
    'lore'
]
def create_dirs(base, tree):
    for name, subtree in tree.items():
        path = os.path.join(base, name)
        os.makedirs(path, exist_ok=True)
        create_dirs(path, subtree)
def clearDirectory(path):
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
emptyDirectories = [
    os.path.join('chats','md'),
    os.path.join('lore','md'),
    os.path.join('NotebookLM')
]
log = os.path.join('logs',f'{seed}.md')
for dir in emptyDirectories:
    clearDirectory(dir)
create_dirs('.', structure)
with open(log,'w',encoding='utf-8') as f:
    f.write(f'# Seed:\n- `{seedString}`\n')
scripts_dir = 'scripts'
print(f'\nseed:\n{seedString}\n')
for file in os.listdir(scripts_dir):
    if file.endswith('.py'):
        full_path = os.path.join(scripts_dir, file)
        if file == scripts[0] + '.py':
            print('Generating Chat Logs...')
        elif file == scripts[1] + '.py':
            print('Generating Lore Books...')
        subprocess.run(['python', full_path])
README = """# Instructions
1. Run `script.py` to build readable versions of Chat Logs & Lore Books.
1. file names follow a specific format:
    - `Chats`: 
        - `User&MainCharacter-##*optional.json/jsonl`
        - example: `Johnny&Jessica-03.json`
    - `Lore Books`:
        - `topic.json`
        - example: `Lakedaimon.json`"""
print("Generating README.md")
with open('README.md','w',encoding='utf-8') as f:
    f.write(README)
print(f"Generating {log}")
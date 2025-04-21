import os
import subprocess
structure = {
    'chats': {
        'files': {},
        'md': {},
    },
    'lore': {
        'files': {},
        'md': {},
    },
    'NotebookLM': {}
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
create_dirs('.', structure)
scripts_dir = 'scripts'
for file in os.listdir(scripts_dir):
    if file.endswith('.py') and not file.startswith('fileRename'):
        full_path = os.path.join(scripts_dir, file)
        if file == scripts[0] + '.py':
            print('Generating Chat Logs...')
        elif file == scripts[1] + '.py':
            print('Generating Lore Books...')
        subprocess.run(['python', full_path])
README = """# NOTICE
1. Run `script.py` to build readable versions of Chat Logs & Lore Books.
1. file names follow a specific format:
    1. `Chats`: 
        1. `User&MainCharacter-##*optional.json/jsonl`
        1. example: `Johnny&Jessica-03.json`
    1. `Lore Books`:
        1. `topic.json`
        1. example: `Lakedaimon.json`"""
print("Generating README.md")
with open('README.md','w',encoding='utf-8') as f:
    f.write(README)
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

1. Run `script.py` to build readable versions of chat logs/lore books.
1. when adding new files in `chats/files/` or `lore/files/`, use `scripts/fileRename.py` to generate new names.
    > User's Name and Characters' Name. List by order of importance. join with `&`. end with `#XX`, in order of age.
    >
    > Or
    >
    > Lore book topic.

    > Example A:
    >> `User & Character1 & Character2 #01`
    >>
    >> `75736572+6368617261637465721+6368617261637465722-01.json`
    >
    > Example B:
    >> `lorebook.json`
    >>
    >> `6c6f7265626f6f6b.json`"""
print('Generating `README.md`')
with open('README.md','w',encoding='utf-8') as f:
    f.write(README)
print('use scripts/fileRename.py to create hex file names')

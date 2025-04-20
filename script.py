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
    }
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
    if file.endswith('.py'):
        full_path = os.path.join(scripts_dir, file)
        if file == scripts[0] + '.py':
            print('Generating Chat Logs...')
        elif file == scripts[1] + '.py':
            print('Generating Lore Books...')
        subprocess.run(['python', full_path])
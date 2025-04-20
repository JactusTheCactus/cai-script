import os
import subprocess

# Step 1: Directory structure creation
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

def create_dirs(base, tree):
    for name, subtree in tree.items():
        path = os.path.join(base, name)
        os.makedirs(path, exist_ok=True)
        create_dirs(path, subtree)

create_dirs('.', structure)

# Step 2: Run all scripts in the `scripts/` directory
scripts_dir = 'scripts'

for file in os.listdir(scripts_dir):
    if file.endswith('.py'):
        full_path = os.path.join(scripts_dir, file)
        print(f"Running {full_path}...")
        subprocess.run(['python', full_path])
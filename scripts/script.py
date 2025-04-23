def main():
    import os
    import shutil
    from config import log
    from chat import chat
    from lore import lore
    from genPage import genPage
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
    for dir in emptyDirectories:
        clearDirectory(dir)
    create_dirs('.', structure)
    with open(log,'w',encoding='utf-8') as f:
        f.write('')
    scripts_dir = 'scripts'
    chat()
    lore()
    mdLinks = {
        "Agnaistic": "[Agnaistic](https://agnai.chat)",
        "C.AI": "[Character.AI](https://character.ai)",
        "C.AI Tools": "[CAI Tools](https://chromewebstore.google.com/detail/cai-tools/nbhhncgkhacdaaccjbbadkpdiljedlje?hl=en&pli=1)"
    }
    README = f"""# Instructions
## File names follow a specific format:
- ### Chats: 
    - `User&MainChar-##.file`
    - example: `Johnny&Jessica-03.json`
    - `-##` is optional
        - only use if there are duplicates
    - accepted file formats:
        - `.json`
            - via {mdLinks['Agnaistic']}
        - `.jsonl`
            - via {mdLinks['C.AI Tools']} for {mdLinks['C.AI']}
- ### Lore Books:
    - `topic.json`
    - example: `Lakedaimon.json`
    - source: {mdLinks['Agnaistic']}
"""
    print("Generating README.md")
    with open('README.md','w',encoding='utf-8') as f:
        f.write(README)
    print(f"Generating {log}...")
    genPage()
if __name__ == "__main__":
    main()
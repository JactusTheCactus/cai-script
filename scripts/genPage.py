import os
from pathlib import Path

# Get the root of the repo (one level up from the script)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Define folders relative to repo root
targets = {
    "chats/md": ".md",
    "lore/md": ".md",
    "logs": ".txt"
}

def genPage():
    lines = ['<html>', '<head><title>Index</title></head>', '<body>', '<h1>Repository Index</h1>']

    for folder, extension in targets.items():
        if folder == 'chats/md':
            head = 'Chats'
        elif folder == 'lore/md':
            head = 'Lore Books'
        elif folder == 'logs':
            head = 'Logs'
        lines.append(f"<details><summary>{head}</summary>")
        lines.append("<ul>")
        folder_path = REPO_ROOT / folder

        if not folder_path.exists():
            lines.append(f"<li><em>{folder} not found</em></li>")
            continue

        for file in sorted(folder_path.glob(f'*{extension}')):
            rel_path = file.relative_to(REPO_ROOT).as_posix()
            lines.append(f'<li><a href="{rel_path}">{file.name}</a></li>')

        lines.append("</ul></details>")

    lines.append('</body></html>')

    index_path = REPO_ROOT / "index.html"
    with index_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"{index_path} generated successfully.")

if __name__ == "__main__":
    genPage()
import os
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
targets = {
    os.path.join('chats','formatted','html'): ".html",
    os.path.join('lore','formatted','html'): ".html"
}
def genPage():
    lines = [
        '<html>',
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-dark.css" integrity="sha512-XNBMUjy86G874D+6YN8vaBJpEut/Q0IafwiWxO5CoZDyaVXxbzyzacBpA55GPYhetzeLhxUbgdETrigRIVeNqQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />',
        '<style>.markdown-body{margin:0 auto;padding:45px;font-size:30px;}@media(max-width:767px){.markdown-body{padding:15px;}}</style>',
        '<head><title>Index</title></head>',
        '<body class="markdown-body">',
        '<!--<h1>Header</h1>-->'
    ]
    for folder, extension in targets.items():
        if folder == os.path.join('chats','formatted','html'):
            head = 'Chats'
        elif folder == os.path.join('lore','formatted','html'):
            head = 'Lore Books'
        lines.append(f"<h2>{head}</h2>")
        lines.append("<ul>")
        folder_path = REPO_ROOT / folder
        if not folder_path.exists():
            lines.append(f"<li><i>{folder} not found</i></li>")
            continue
        for file in sorted(folder_path.glob(f'*{extension}')):
            rel_path = file.relative_to(REPO_ROOT).as_posix()
            lines.append(f'<li><a href="{rel_path.replace("formatted/html/","")}" target="_blank">{file.name.replace(".html","").upper()}</a></li>')
        lines.append("</ul></details>")
    lines.append('</body></html>')
    index_path = REPO_ROOT / "index.html"
    with index_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))
if __name__ == "__main__":
    genPage()

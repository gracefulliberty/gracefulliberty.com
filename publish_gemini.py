import sys
import os
from pathlib import Path
from md2gemini import md2gemini
import subprocess

subprocess.run(["mkdir", "-p", "public_gemini/gemlog/"])

mapping = {
    "_index.md": "index.gmi",
    "blog/_index.md": "gemlog/index.gmi",
}

for path in Path('.').glob('content/blog/*.md'):
    if path.name != '_index.md':
        mapping[f"blog/{path.name}"] = f"gemlog/{path.name}"

for source, dest in mapping.items():
    print(f"Writing content/{source} to public_gemini/{dest}")
    
    with open(f"content/{source}", "r") as f:
        gemini = md2gemini(f.read())

    with open(f"public_gemini/{dest}", "w") as f:
        f.write(gemini)

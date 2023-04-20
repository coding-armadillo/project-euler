import json
import pickle
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

parser = ArgumentParser(
    prog="UpdateDocs",
    description="A helper script to update docs",
)
parser.add_argument("-f", "--force", action="store_true")
args, _ = parser.parse_known_args()
force = args.force

try:
    with open("docs/.cache", "rb") as f:
        cache = pickle.load(f)
except:
    cache = {}

files = list(Path(".").glob("id*.py"))

solutions = {}
problem_ids = sorted([int(file.stem[2:]) for file in files])

if not force and set(solutions.keys()) < set(cache.keys()):
    print(f"⛔ Skipped: no update needed")
    sys.exit()

try:
    subprocess.call(
        [
            "black",
            ".",
        ]
    )
except:
    pass

prompt = "📖 Refreshing Docs"
text = """---
hide:
  - toc
---

<figure markdown>
![Logo](https://projecteuler.net/images/clipart/euler_portrait.png){ width="100" }
</figure>

# Project Euler

Solutions to [Project Euler](https://projecteuler.net)
"""
for problem_id in tqdm(problem_ids, prompt):
    url = f"https://projecteuler.net/problem={problem_id}"
    if problem_id in cache:
        name = cache[problem_id]
    else:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        name = soup.find("h2").text
        cache[problem_id] = name

    text += f"""
## Problem {problem_id} - [{name}]({url})

??? success "Solution"

    === "Python"

        ```py linenums="1"
        --8<-- "id{problem_id}.py"
        ```
"""

with open(".all-contributorsrc") as f:
    data = json.load(f)
    num_contributors = len(data["contributors"])

text += f"""!!! note ""

    Thanks to all {num_contributors} [contributors](https://github.com/coding-armadillo/project-euler#contributors-).
"""

with open("docs/index.md", "w") as f:
    f.write(text)

with open("docs/.cache", "wb") as f:
    pickle.dump(cache, f)

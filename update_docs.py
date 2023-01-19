import json
import pickle
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

try:
    with open("docs/.cache", "rb") as f:
        cache = pickle.load(f)
except:
    cache = {}

files = list(Path(".").glob("id*.py"))

solutions = {}
problem_ids = sorted([int(file.stem[2:]) for file in files])


prompt = "📖 Refreshing Docs"
text = """# Project Euler
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
## [{name}]({url})

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

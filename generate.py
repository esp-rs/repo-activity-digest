#!/usr/bin/env python

from datetime import datetime

import yaml


INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Repo activity digests for esp-rs</title>

    <style>
      body {
        font-family: sans-serif;
        max-width: 60em;
        margin: auto;
      }
      ul {
        padding-left: 0;
        list-style-type: none;
      }
      li {
        margin-top: 0.5em;
      }
      a {
        color: inherit;
      }
      a:hover {
        text-decoration: none;
        color: #0969da;
      }
    </style>
  </head>
  <body>
    <h1>Repo activity digests for esp-rs</h1>
    <ul>%s</ul>
  </body>
</html>
"""


def main():
    def build_digest(repo):
        name = repo.split("/")[-1]
        return {"digest": f"{name}.html", "since": "1 week", "items": [repo]}

    def build_list_item(repo):
        name = repo.split("/")[-1]
        return f'<li><a href="{name}.html">{name}</a></li>'

    now = datetime.utcnow()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open("repositories.yml", "r") as f:
        repos = yaml.safe_load(f)

    with open("config.yml", "w") as f:
        f.write(f"# Generated on {date} at {time} UTC\n\n")
        yaml.dump({"digests": [build_digest(repo) for repo in repos]}, f)

    with open("index.html", "w") as f:
        list_items = [build_list_item(repo) for repo in repos]
        f.write(INDEX_TEMPLATE % "\n".join(list_items))


if __name__ == "__main__":
    main()

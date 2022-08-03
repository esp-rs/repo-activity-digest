#!/usr/bin/env python

from datetime import datetime

import yaml


def main():
    with open("repositories.yml", "r") as f:
        repos = yaml.safe_load(f)

    now = datetime.utcnow()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    def build_digest(repo):
        name = repo.split("/")[-1]
        return {"digest": f"{name}.html", "since": "1 week", "items": [repo]}

    with open("config.yml", "w") as f:
        f.write(f"# Generated on {date} at {time} UTC\n\n")
        yaml.dump({"digests": [build_digest(repo) for repo in repos]}, f)


if __name__ == "__main__":
    main()

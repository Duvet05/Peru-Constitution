#!/usr/bin/env python3
import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(args, cwd, env=None):
    subprocess.run(args, cwd=cwd, env=env, check=True)


def main():
    if len(sys.argv) != 3:
        print("uso: build_history.py reformas.csv output_dir", file=sys.stderr)
        return 2

    manifest = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    root = manifest.parent

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    run(["git", "init"], output)
    run(["git", "config", "user.name", "Constitucion Peru Bot"], output)
    run(["git", "config", "user.email", "constitucion-peru@example.invalid"], output)

    with manifest.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    for row in rows:
        snapshot = root / row["snapshot"]
        if not snapshot.exists():
            raise FileNotFoundError(snapshot)

        shutil.copyfile(snapshot, output / "constitucion.md")
        run(["git", "add", "constitucion.md"], output)

        message = f"{row['law']}\n\n{row['message']}\n\nFuente: {row['source']}"
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{row['date']}T12:00:00-05:00"
        env["GIT_COMMITTER_DATE"] = env["GIT_AUTHOR_DATE"]
        run(["git", "commit", "-m", message], output, env=env)

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


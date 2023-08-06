from pathlib import Path

import typer

from .git import clone
from .parser import InvalidGitUrl, parse

home = str(Path.home())

app = typer.Typer(
    name='get-repo',
    add_completion=False,
    help='Helps you clone git repos in an organized way.',
)


@app.command()
def get(url: str) -> None:
    """Clones a git repository"""
    try:
        target_directory = Path.home() / 'source' / parse(url)
        clone(url, str(target_directory))
    except InvalidGitUrl as exception:
        print(exception)


def main() -> None:
    app()

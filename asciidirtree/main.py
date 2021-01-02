import sys
import os
from pathlib import Path
import click
sys.path.append(str(Path(__file__).parents[1]))
from lib.folder import Folder
from typing import Final, Dict, List


def build_tree(target: str, base: str = None) -> Folder:
    if base is not None:
        target_path: Path = Path(base) / target
    else:
        target_path: Path = Path(os.path.abspath(path=target))
    dir_list = os.listdir(str(target_path))
    base: Folder = Folder(os.path.basename(str(target_path)))
    for elem in dir_list:
        if elem in [".venv", ".idea", ".git"]:
            continue
        dir_elem_path: Path = target_path / elem
        if os.path.isdir(str(dir_elem_path)):
            base.append(build_tree(target=elem, base=str(target_path)))
        elif os.path.isfile(str(dir_elem_path)):
            base.append(elem)
    return base


@click.command()
@click.option('--target', '-t', default='.')
def cmd(target):
    hoge: Folder = build_tree(target=target)
    hoge.dir()


if __name__ == "__main__":
    cmd()

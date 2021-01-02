# AsciiDirTree

指定したディレクトリの内部構造をAsciiArtでprintするツール

## install

1. install poetry
```bash
$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
$ poetry --version
# > Poetry version 1.0.10
```
2. install require packages
```
$ cd AsciiDirTree
$ poetry install
```

- click: コマンドライン引数をパースする

## run

```
$ python AsciiDirTree/asciidirtree/main.py --target [target path]
```
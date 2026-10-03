# sh3bang

A small personal command-line toolkit, built with Typer and Rich and published on [PyPI](https://pypi.org/project/sh3bang/).

```bash
pip install sh3bang
```

| Command | What it does |
|---|---|
| `sh3bang files rename <folder> [--prefix] [--dry-run]` | Tidy filenames (replace spaces, add a prefix) |
| `sh3bang files convert <in> <out>` | Convert PDF ↔ DOCX |
| `sh3bang clip watch / save / show / copy / clear` | Clipboard history |
| `sh3bang imgtool resize / convert / info` | Resize, convert or inspect images |

Run `sh3bang --help` or `sh3bang <group> --help` for options.

Python 3.10+ · MIT License

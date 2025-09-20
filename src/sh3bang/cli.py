import typer

from sh3bang.clipboard_manager.cli import app as clip_app
from sh3bang.files.cli import app as files_app

app = typer.Typer(help="sh3bang - personal CLI")

# Register subcommands
app.add_typer(files_app, name="files")
app.add_typer(clip_app, name="clip")

if __name__ == "__main__":
    app()

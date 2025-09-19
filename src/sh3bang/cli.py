import typer

from sh3bang.files.cli import app as files_app

app = typer.Typer(help="sh3bang - personal CLI")

# Register subcommands
app.add_typer(files_app, name="files")

if __name__ == "__main__":
    app()

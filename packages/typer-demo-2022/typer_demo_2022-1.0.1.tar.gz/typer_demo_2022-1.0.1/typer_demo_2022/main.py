import typer

app = typer.Typer()


@app.command()
def main():
    """
    Hola Mundo
    """
    typer.echo("Hola mundo!")

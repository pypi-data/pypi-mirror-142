import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    La pistola de Rick
    """


@app.command()
def shoot():
    """
    Disparar portal
    """
    typer.echo("pyum pyum")


@app.command()
def load():
    """
    Recargar portal
    """
    typer.echo("Recargar portal!")

import os
import typer
from cmd.manager import manager_app

app = typer.Typer()

# add
app.add_typer(manager_app, name="manager", help="Todo manager")


@app.command()
def location():
    print(os.getcwd())


def main():
    print("TODO-MANAGER STARTED")


if __name__ == "__main__":
    app()

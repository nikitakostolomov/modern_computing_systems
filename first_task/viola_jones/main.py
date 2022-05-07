import click
from viola_jones import run_viola_jones


@click.command()
@click.argument("image")
def viola_jones(image):
    run_viola_jones(image)


if __name__ == "__main__":
    viola_jones()

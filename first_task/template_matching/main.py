import click
from temp_match import run_template_matching_methods


@click.command()
@click.argument("image")
@click.argument("template")
def template_matching(image, template):
    run_template_matching_methods(image, template)


if __name__ == "__main__":
    template_matching()

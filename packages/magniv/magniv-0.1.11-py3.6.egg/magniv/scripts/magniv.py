import click
from magniv.build import build as m_build
from magniv.export import export as m_export
from magniv.run import run as m_run


@click.group()
def cli():
    pass


@cli.command()
def build():
    return m_build()


@cli.command()
def export():
    return m_export()


@cli.command()
@click.argument("filepath")
@click.argument("function_name")
def run(filepath, function_name):
    return m_run(filepath, function_name)

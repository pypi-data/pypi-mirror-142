"""
Module that contains the command line app.

"""
import click
import yaml
from cerberus import Validator, SchemaError
from os import environ


class scheckcli(object):
    def __init__(self, schema_file_path, input_file_path=None):
        self.schema_file_path = schema_file_path
        self.input_file_path = input_file_path or {}
        self._load_input = None
        self._load_schema = None

    def yaml_load(self, filePath=None):
        with open(filePath, "r") as self.stream:
            try:
                return yaml.load(self.stream, Loader=yaml.SafeLoader)
            except yaml.YAMLError as exception:
                print(
                    "The file does not have a valid structure: ",
                    exception,
                )

    def load_schema(self):
        '''loads the schema file'''
        if self._load_schema is None:
            self._load_schema = self.yaml_load(
                filePath=self.schema_file_path
            )
            try:
                self.v = Validator(self._load_schema)
                return (self._load_schema, self.v)
            except TypeError as exception:
                print("Invalid Schema file Exception: ", exception)
                exception

    def load_input(self):
        '''loads the input file'''
        if self._load_input is None:
            self._load_input = self.yaml_load(
                filePath=self.input_file_path
            )

    def check(self):
        if self.load_schema():
            print("The Schema file has valid syntax.")

    def compare(self):
        self.load_schema()
        self.load_input()
        try:
            if self.v.validate(self._load_input):
                return print(f'Input file has a valid schema.'), 0
            raise Exception(self.v.errors)
        except SchemaError as exception:
            raise exception


@click.group()
def cli1():
    pass


@cli1.command(
    'compare',
    no_args_is_help=True,
    short_help="Compare schema of the input file against a schema file.",
    help="""\b
    Compare schema of the input file against a schema file.
    
    EXAMPLES:

        scheckcli compare -sfp ./schema.yaml -ifp./input.yaml
    
        scheckcli compare -sfp ./schema.json -ifp ./input.json
    """,
)
@click.option(
    '--schema-file-path',
    '-sfp',
    required=True,
    help="The file path to the schema file. Configurable with SCHECK_SCHEMA_PATH environmental Variable",
    default=lambda: environ.get("SCHECK_SCHEMA_PATH"),
    type=click.Path(exists=True, file_okay=True),
)
@click.option(
    '--input-file-path',
    '-ifp',
    required=True,
    help="The file path to the input file to compare.  Configurable with SCHECK_INPUT_PATH environmental variable.",
    default=lambda: environ.get("SCHECK_INPUT_PATH"),
    type=click.Path(exists=True, file_okay=True),
)
def compare_cmd(schema_file_path, input_file_path):
    comp = scheckcli(schema_file_path, input_file_path)
    comp.compare()


@click.group()
def cli2():
    pass


@cli2.command(
    'check',
    no_args_is_help=True,
    short_help="Checks the provided schema file for valid syntax.",
    help="""\b
    Checks the provided schema file for valid syntax. Both json or yaml are accepted file types.
    
    EXAMPLES:
    
        scheckcli check ./schema.yaml

        scheckcli check ./schema.json

        scheckcli check --sfp ./schema.yaml

        scheckcli check --sfp ./schema.json
    """,
)
@click.option(
    '--schema-file-path',
    '-sfp',
    required=True,
    help="The file path to the schema file. Configurable with SCHECK_SCHEMA_PATH environmental Variable",
    default=lambda: environ.get("SCHECK_SCHEMA_PATH"),
    type=click.Path(exists=True, file_okay=True),
)
def check_command(schema_file_path):
    comp = scheckcli(schema_file_path)
    comp.check()


main = click.CommandCollection(
    sources=[cli1, cli2],
    help="""
        Compare given input file with given schema file. Check's the provided schema file for valid schema syntax.
        """,
)

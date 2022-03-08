"""Module for collecting argument definitions"""
from parse.definitions.consts import DESCRIPTION, EPILOG
from parse.definitions.loader import DefinitionLoader


def get_parser_kwargs():
    """Collects parser arguments"""

    parser_kwargs = dict(
        description=DESCRIPTION,
        epilog=EPILOG
    )
    return parser_kwargs


def get_definitions():
    """Collects argument definitions"""

    loader = DefinitionLoader()
    loader.load_definitions()
    definitions = loader.get_definitions()
    return definitions

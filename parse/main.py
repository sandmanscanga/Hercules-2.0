"""Module for parsing and validating raw arguments"""
from parse.define import Definition
from parse.validate import Validation
from parse.parser import Parser


def get_args(argparse):
    """Parse and validate raw arguments"""

    arg_parser = Definition()
    arg_parser.build_parser(argparse)
    arg_parser.add_arguments()
    raw_args = arg_parser.parse_args()

    valid_args = Validation(raw_args)
    valid_args.validate()

    args = Parser(valid_args)

    return args

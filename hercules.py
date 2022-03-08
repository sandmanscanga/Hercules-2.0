"""Module for running the Hercules attack script"""
from parse.main import get_args


def main(args):
    args.display_final()


if __name__ == "__main__":
    import argparse

    args = get_args(argparse)
    main(args)

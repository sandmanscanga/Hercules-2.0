"""Module for running the Hercules attack script"""
from parse.main import get_browser


def main(browser):
    browser.display_final()


if __name__ == "__main__":
    import argparse

    browser = get_browser(argparse)
    main(browser)

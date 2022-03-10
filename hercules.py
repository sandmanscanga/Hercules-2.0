"""Module for running the Hercules attack script"""
from parse.main import get_browser
from threader.main import Threader


def main(browser):
    browser.display_final()
    total_threads = browser.threads
    attack_function = browser.attack_function
    result_function = browser.handle_result
    threader = Threader(total_threads, attack_function, result_function)


if __name__ == "__main__":
    import argparse

    browser = get_browser(argparse)
    main(browser)

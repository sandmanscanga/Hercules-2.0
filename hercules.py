"""Module for running the Hercules attack script"""
from parse.main import get_browser
from threader.main import Threader
from attack.main import attack_dir, attack_brute


def main(browser):
    """Runs the main process"""

    total_threads = browser.threads
    if browser.runmode == "BRUTE":
        attack = attack_brute
        handle_result = browser.handle_brute_result
    else:
        attack = attack_dir
        handle_result = browser.handle_dir_result

    threader = Threader(total_threads, attack, handle_result)
    threader.start_threads()

    if browser.runmode == "BRUTE":
        if browser.userfile is not None:
            for username in browser.gen_wordlist(browser.userfile):
                if browser.passfile is not None:
                    for password in browser.gen_wordlist(browser.passfile):
                        data = (browser, username, password)
                        threader.add_job(data)
                else:
                    data = (browser, username, browser.password)
                    threader.add_job(data)
        else:
            if browser.passfile is not None:
                for password in browser.gen_wordlist(browser.passfile):
                    data = (browser, browser.username, password)
                    threader.add_job(data)
            else:
                data = (browser, browser.username, browser.password)
                threader.add_job(data)

    else:
        for directory in browser.gen_wordlist(browser.wordlist):
            data = (browser, directory)
            threader.add_job(data)

    exit_signal = threader.join_threads()
    if exit_signal is False:
        print("\n[!] Killed prematurely")
    
    if browser.verbose is True:
        if browser.runmode == "BRUTE":
            browser.display_found_creds()
        else:
            browser.display_found_dirs()
    else:
        print("[*] Finished" + " "*90)


if __name__ == "__main__":
    import argparse

    browser = get_browser(argparse)
    main(browser)

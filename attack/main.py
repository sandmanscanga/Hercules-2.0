"""Module containing the attack functionality"""


def attack_dir(data):
    """Runs the attack in DIR mode"""

    browser, directory = data
    browser_kwargs = browser.build_browser_kwargs(directory)
    response = browser.driver(**browser_kwargs)
    result = browser.check_dir_response(response)

    return result


def attack_brute(data):
    """Runs the attack in BRUTE mode"""

    browser, username, password = data
    browser_kwargs = browser.build_browser_kwargs(username, password)
    response = browser.driver(**browser_kwargs)
    result = browser.check_brute_response(response)

    return result

"""Module containing the attack functionality"""


def attack(data):
    """Runs the attack"""

    browser, username, password = data
    browser_kwargs = browser.build_browser_kwargs(username, password)
    response = browser.driver(**browser_kwargs)
    result = browser.check_response(response)

    return result

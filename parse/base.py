"""Module for handling the Browser base class"""
from copy import deepcopy
import requests


class BrowserBase:
    """Class for supporting the Browser class"""

    def get_driver(self):
        """Gets the browser driver and keyword"""

        driver, data_key = None, None
        if self.method == "POST":
            driver = requests.post
            data_key = "data"
        else:
            driver = requests.get
            data_key = "params"

        return driver, data_key

    def get_payload_keys(self):
        """Gets the payload username and password key"""

        user_key, pass_key = None, None
        for key, value in self.payload.items():
            if value == "^USER^":
                user_key = key
            if value == "^PASS^":
                pass_key = key

        return user_key, pass_key

    def get_total_usernames(self):
        """Get the total usernames to be looped through"""

        total_usernames = 1
        if self.userfile is not None:
            total_usernames = self.get_total_words(self.userfile)

        return total_usernames

    def get_total_passwords(self):
        """Get the total passwords to be looped through"""

        total_passwords = 1
        if self.passfile is not None:
            total_passwords = self.get_total_words(self.passfile)

        return total_passwords

    def build_payload(self, username, password):
        """Injects payload with username and password"""

        payload = deepcopy(self.payload)
        payload[self.user_key] = username
        payload[self.pass_key] = password
        return payload

    def build_browser_kwargs(self, username, password):
        """Builds browser keyword argument dictionary"""

        payload = self.build_payload(username, password)
        browser_kwargs = {
            "url": self.url,
            "headers": {
                "User-agent": self.agent
            },
            "cookies": self.cookies,
            self.data_key: payload
        }
        return deepcopy(browser_kwargs)

    def check_response(self, response):
        """Checks response against success/failure signals"""

        if self.success_msg is not None:
            if self.success_msg in response.text:
                return True
        elif self.success_code is not None:
            if self.success_code == response.status_code:
                return True
        elif self.failure_msg is not None:
            if self.failure_msg in response.text:
                return True
        else:
            if self.failure_code == response.status_code:
                return True

        return False

    def handle_result(self, data, result):
        """Handles the operations to be performed given a result"""

        pass

    @staticmethod
    def get_total_words(wordlist):
        """Gets the total number of words in a wordlist"""

        total_words = None
        with open(wordlist, "r") as file:
            total = max(index for index, line in enumerate(file))
        total_words = total + 1

        return total_words

    @staticmethod
    def gen_wordlist(wordlist):
        """Generates words from wordlist"""

        with open(wordlist, "r") as file:
            while True:
                line = file.readline()
                if line:
                    yield line.strip()
                else:
                    break

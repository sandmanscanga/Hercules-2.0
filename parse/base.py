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

        if self.payload is None:
            return user_key, pass_key

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

    def get_total_directories(self):
        """Get the total directories to be looped through"""

        total_directories = 1
        if self.wordlist is not None:
            total_directories = self.get_total_words(self.wordlist)

        return total_directories

    def build_payload(self, username, password):
        """Injects payload with username and password"""

        payload = deepcopy(self.payload)
        payload[self.user_key] = username
        payload[self.pass_key] = password
        return payload

    def build_browser_kwargs(self, *args):
        """Builds browser keyword argument dictionary"""

        if self.runmode == "BRUTE":
            username, password = args
            payload = self.build_payload(username, password)
            browser_kwargs = {
                "url": self.url,
                "headers": {
                    "User-agent": self.agent
                },
                "cookies": self.cookie,
                "allow_redirects": False,
                self.data_key: payload
            }
        else:
            directory = args[0]
            new_url = self.url + directory
            browser_kwargs = {
                "url": new_url,
                "headers": {
                    "User-agent": self.agent
                },
                "cookies": self.cookie,
                "allow_redirects": False
            }

        return deepcopy(browser_kwargs)

    def check_brute_response(self, response):
        """Checks response against success/failure signals"""

        signal = False
        if self.success_msg is not None:
            if self.success_msg in response.text:
                signal = True
        elif self.success_code is not None:
            if self.success_code == response.status_code:
                signal = True
        elif self.failure_msg is not None:
            if self.failure_msg not in response.text:
                signal = True
        else:
            if self.failure_code != response.status_code:
                signal = True

        return signal

    def check_dir_response(self, response):
        """Gets the response status code"""

        return response.status_code, len(response.text)

    def handle_brute_result(self, args):
        """Handles the operations to be performed given a brute result"""

        data, result, child_id, current = args

        _, username, password = data
        progress = self.calc_brute_progress(current)

        creds_msg = f"{username}:{password}"
        child_msg = f"(child {str(child_id).zfill(2)})"
        progress_msg = f"({progress:.2f}%)"

        if result is True:
            if self.outfile is not None:
                with open(self.outfile, "a") as file:
                    file.write(creds_msg + "\n")
            print(f"[+] {progress_msg} {child_msg} {creds_msg}")
            self.found_creds.append(creds_msg)
        else:
            if self.verbose is True:
                print(f"[-] {progress_msg} {child_msg} {creds_msg}")

        return self.finish

    def handle_dir_result(self, args):
        """Handles the operations to be performed given a dir result"""

        data, result, child_id, current = args

        _, directory = data
        status_code, length = result
        progress = self.calc_dir_progress(current)

        dir_stats = f"[Code: {status_code}] (Length: {length})"
        dir_path = f"/{directory}"

        pads = self.get_padding(dir_stats)

        dir_msg = f"{dir_stats}{pads}{dir_path}"
        child_msg = f"(child {str(child_id).zfill(2)})"
        progress_msg = f"({progress:.2f}%)"

        if status_code != 404:
            if self.outfile is not None:
                with open(self.outfile, "a") as file:
                    file.write(dir_msg + "\n")

            if self.verbose is False:
                string = f"[+] {dir_msg}"
                padding = self.get_padding(string, 100)
                print(f"{string}{padding}")
            else:
                print(f"[+] {progress_msg} {child_msg} {dir_msg}")

            self.found_dirs.append(dir_msg)

        else:
            if self.verbose is True:
                print(f"[-] {progress_msg} {child_msg} {dir_msg}")
            else:
                string = f"[-] {progress_msg} {child_msg} {dir_msg}"
                padding = self.get_padding(string, 100)
                print(f"{string}{padding}", end="\r")

    def get_padding(self, string, pads=30):
        """Calculate pads needed based on prefix string"""

        string_len = len(string)
        pads_diff = pads - string_len

        padding = " "
        if pads_diff > 0:
            padding = " " * pads_diff

        return padding

    def calc_brute_progress(self, current):
        """Calculates the progress as a percentage"""

        total_words = self.total_usernames * self.total_passwords
        percentage = (current / total_words) * 100
        percentage_rounded = round(percentage, 2)

        return percentage_rounded

    def calc_dir_progress(self, current):
        """Calculates the progress as a percentage"""

        percentage = (current / self.total_directories) * 100
        percentage_rounded = round(percentage, 2)

        return percentage_rounded

    def get_total_found_creds(self):
        """Gets the total number of found credentials"""

        return len(self.found_creds)

    def get_total_found_dirs(self):
        """Get the total number of found directories"""

        return len(self.found_dirs)

    def display_found_creds(self):
        """Displays the found credentials"""

        total_found_creds = self.get_total_found_creds()
        if total_found_creds == 0:
            print("[-] No credentials found")
        else:
            print(f"[*] Found {total_found_creds} total credentials")
            for credential in self.found_creds:
                print(f"[+] {credential}")

    def display_found_dirs(self):
        """Displays the found directories"""

        total_found_dirs = self.get_total_found_dirs()
        if total_found_dirs == 0:
            print(f"[-] No directories found")
        else:
            print(f"[*] Found {total_found_dirs} total directories")
            for directory in self.found_dirs:
                print(f"[+] {directory}")

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

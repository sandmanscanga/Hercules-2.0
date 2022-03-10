"""Module for handling the browser"""
from parse.base import BrowserBase


class Browser(BrowserBase):
    """Class defining the browser"""

    def __init__(self, valid_args):
        self.username = valid_args.username
        self.userfile = valid_args.userfile
        self.password = valid_args.password
        self.passfile = valid_args.passfile
        self.method = valid_args.method
        self.url = valid_args.url
        self.payload = valid_args.payload
        self.success_msg = valid_args.success_msg
        self.success_code = valid_args.success_code
        self.failure_msg = valid_args.failure_msg
        self.failure_code = valid_args.failure_code
        self.outfile = valid_args.outfile
        self.threads = valid_args.threads
        self.agent = valid_args.agent
        self.cookie = valid_args.cookie
        self.finish = valid_args.finish
        self.verbose = valid_args.verbose

        driver, data_key = self.get_driver()
        user_key, pass_key = self.get_payload_keys()
        total_usernames = self.get_total_usernames()
        total_passwords = self.get_total_passwords()

        self.driver = driver
        self.data_key = data_key
        self.user_key = user_key
        self.pass_key = pass_key
        self.total_usernames = total_usernames
        self.total_passwords = total_passwords

        self.found_creds = []

    def display_final(self):
        """Display final arguments"""

        print("[*] Displaying final arguments...")
        print(f"[*] username      :  {self.username}     ")
        print(f"[*] userfile      :  {self.userfile}     ")
        print(f"[*] password      :  {self.password}     ")
        print(f"[*] passfile      :  {self.passfile}     ")
        print(f"[*] method        :  {self.method}       ")
        print(f"[*] url           :  {self.url}          ")
        print(f"[*] payload       :  {self.payload}      ")
        print(f"[*] success_msg   :  {self.success_msg}  ")
        print(f"[*] success_code  :  {self.success_code} ")
        print(f"[*] failure_msg   :  {self.failure_msg}  ")
        print(f"[*] failure_code  :  {self.failure_code} ")
        print(f"[*] outfile       :  {self.outfile}      ")
        print(f"[*] threads       :  {self.threads}      ")
        print(f"[*] agent         :  {self.agent}        ")
        print(f"[*] cookie        :  {self.cookie}       ")
        print(f"[*] finish        :  {self.finish}       ")
        print(f"[*] verbose       :  {self.verbose}      ")

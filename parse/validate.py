"""Module for validating raw arguments"""
from parse.validations.base import ValidationBase


class Validation(ValidationBase):
    """Validates raw arguments"""

    def __init__(self, raw_args):
        self.raw_args = raw_args
        self.runmode = None
        self.extension = None
        self.wordlist = None
        self.username = None
        self.userfile = None
        self.password = None
        self.passfile = None
        self.method = None
        self.url = None
        self.payload = None
        self.success_msg = None
        self.success_code = None
        self.failure_msg = None
        self.failure_code = None
        self.outfile = None
        self.threads = None
        self.agent = None
        self.cookie = None
        self.finish = None
        self.verbose = None

    def validate(self):
        """Run validation on raw arguments"""

        self.validate_runmode()
        self.validate_wordlist()
        self.validate_extension()
        self.validate_user()
        self.validate_pass()
        self.validate_method()
        self.validate_url()
        self.validate_payload()
        self.validate_signal()
        self.validate_outfile()
        self.validate_threads()
        self.validate_headers()
        self.validate_flags()

    def display_validated(self):
        """Display validated arguments"""

        print("[*] Displaying validated arguments...")
        print(f"[*] runmode       :  {self.runmode}      ")
        print(f"[*] wordlist      :  {self.wordlist}     ")
        print(f"[*] extension     :  {self.extension}    ")
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

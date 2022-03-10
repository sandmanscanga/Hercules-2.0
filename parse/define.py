"""Module for defining raw arguments"""
from parse.definitions.main import get_definitions, get_parser_kwargs


class Definition:
    """Handles defining and parsing of raw arguments"""

    def __init__(self):
        self.parser = None
        self.definitions = None
        self.raw_args = None

    def build_parser(self, argparse):
        """Builds the argument parser"""

        parser_kwargs = get_parser_kwargs()
        self.parser = argparse.ArgumentParser(**parser_kwargs)

    def add_arguments(self):
        """Add argument definitions to parser"""

        self.definitions = get_definitions()
        for args, kwargs in self.definitions:
            self.parser.add_argument(*args, **kwargs)

    def parse_args(self):
        """Parse raw arguments"""

        self.raw_args = self.parser.parse_args()
        return self.raw_args

    def display_raw(self):
        """Display raw arguments"""

        print("[*] Displaying raw arguments...")
        print(f"[*] runmode       :  {self.runmode}               ")
        print(f"[*] wordlist      :  {self.wordlist}              ")
        print(f"[*] username      :  {self.raw_args.username}     ")
        print(f"[*] userfile      :  {self.raw_args.userfile}     ")
        print(f"[*] password      :  {self.raw_args.password}     ")
        print(f"[*] passfile      :  {self.raw_args.passfile}     ")
        print(f"[*] method        :  {self.raw_args.method}       ")
        print(f"[*] url           :  {self.raw_args.url}          ")
        print(f"[*] payload       :  {self.raw_args.payload}      ")
        print(f"[*] success_msg   :  {self.raw_args.success_msg}  ")
        print(f"[*] success_code  :  {self.raw_args.success_code} ")
        print(f"[*] failure_msg   :  {self.raw_args.failure_msg}  ")
        print(f"[*] failure_code  :  {self.raw_args.failure_code} ")
        print(f"[*] outfile       :  {self.raw_args.outfile}      ")
        print(f"[*] threads       :  {self.raw_args.threads}      ")
        print(f"[*] agent         :  {self.raw_args.agent}        ")
        print(f"[*] cookie        :  {self.raw_args.cookie}       ")
        print(f"[*] finish        :  {self.raw_args.finish}       ")
        print(f"[*] verbose       :  {self.raw_args.verbose}      ")

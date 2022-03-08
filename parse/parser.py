"""Module for storing validated arguments"""


class Parser:
    """Parse validated arguments"""

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

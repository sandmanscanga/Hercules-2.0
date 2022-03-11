"""Module for handling validation of raw arguments"""
from parse.validations.utils import ValidationBaseUtils
from urllib.parse import urlparse, unquote_plus
from socket import socket, AF_INET, SOCK_STREAM


class ValidationBase(ValidationBaseUtils):

    THREAD_MIN = 1
    THREAD_MAX = 64

    def validate_runmode(self):
        """Validates runmode"""

        runmode = self.raw_args.runmode
        if runmode.upper() not in ("DIR", "BRUTE"):
            raise Exception("Must provide either DIR or BRUTE as runmode")

        self.runmode = runmode.upper()

    def validate_wordlist(self):
        """Valiates wordlist of directories argument"""

        wordlist = self.raw_args.wordlist
        if self.runmode == "DIR":
            if wordlist is None:
                raise Exception("Must provide a directory wordlist")
            error = self.is_valid_read_file(wordlist)
            if error is not None:
                raise Exception(f"Invalid wordlist: {error}")

            self.wordlist = wordlist

    def validate_extension(self):
        """Validates extension to apply to wordlist"""

        extension = self.raw_args.extension
        if self.runmode == "DIR":
            if extension is not None:
                if not extension.startswith("."):
                    extension = f".{extension}"

        self.extension = extension

    def validate_user(self):
        """Validates username arguments"""

        if self.runmode == "BRUTE":
            username = self.raw_args.username
            userfile = self.raw_args.userfile
            if username is None and userfile is None:
                raise Exception("Must provide either username or userfile")
            elif userfile is not None:
                error = self.is_valid_read_file(userfile)
                if error is not None:
                    raise Exception(f"Invalid userfile: {error}")
            elif username is not None and userfile is not None:
                raise Exception("Cannot provide both username and userfile")

            self.username = username
            self.userfile = userfile

    def validate_pass(self):
        """Validates password arguments"""

        if self.runmode == "BRUTE":
            password = self.raw_args.password
            passfile = self.raw_args.passfile
            if password is None and passfile is None:
                raise Exception("Must provide either a password or passfile")
            elif passfile is not None:
                error = self.is_valid_read_file(passfile)
                if error is not None:
                    raise Exception(f"Invalid passfile: {error}")
            elif password is not None and passfile is not None:
                raise Exception("Cannot provide both password and passfile")

            self.password = password
            self.passfile = passfile

    def validate_method(self):
        """Validates request method argument"""
        
        if self.runmode == "BRUTE":
            method = self.raw_args.method
            if method.upper() not in ("GET", "POST"):
                raise Exception("Method must be either GET or POST")

            self.method = method.upper()

    def validate_url(self):
        """Validates URL argument"""

        raw_url = self.raw_args.url
        parsed_url = urlparse(raw_url)

        scheme = parsed_url.scheme
        if scheme not in ("http", "https"):
            raise Exception("URL scheme must be HTTP or HTTPS")

        if scheme == "http":
            _port = 80
        else:
            _port = 443

        query = parsed_url.query
        if query != "":
            raise Exception("URL query must be set in payload argument")

        netloc = parsed_url.netloc
        if ":" not in netloc:
            host, port = netloc, _port
        else:
            host_port = netloc.split(":")
            try:
                host, port = host_port[0], int(host_port[1])
            except Exception:
                raise Exception("Invalid host/port combination")

        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
        except Exception:
            raise Exception(f"Could not connect to {host} on port {port}")
        finally:
            sock.close()

        uripath = parsed_url.path
        if uripath == "":
            uripath = "/"

        self.url = f"{scheme}://{netloc}{uripath}"

    def validate_payload(self):
        """Validates payload argument"""

        if self.runmode == "BRUTE":
            _payload = self.raw_args.payload
            if "^USER^" not in _payload:
                raise Exception("^USER^ directive not found in payload")
            if "^PASS^" not in _payload:
                raise Exception("^PASS^ directive not found in payload")

            payload = {}
            for field in _payload.split("&"):
                if field != "":
                    key_value = field.split("=", 1)
                    if len(key_value) == 1:
                        key = key_value[0]
                        value = ""
                    else:
                        key, value = key_value
                    payload[key] = unquote_plus(value)

            self.payload = payload

    def validate_signal(self):
        """Validates success/failure signal"""

        if self.runmode == "BRUTE":
            success_msg = self.raw_args.success_msg
            success_code = self.raw_args.success_code
            failure_msg = self.raw_args.failure_msg
            failure_code = self.raw_args.failure_code

            suc_msg_bool = success_msg is not None
            suc_code_bool = success_code is not None
            fail_msg_bool = failure_msg is not None
            fail_code_bool = failure_code is not None

            booleans = (
                suc_msg_bool,
                suc_code_bool,
                fail_msg_bool,
                fail_code_bool
            )

            if any(booleans) is False:
                raise Exception("Must provide a success or failure signal")

            counter = 0
            for boolean in booleans:
                if boolean is True:
                    counter += 1

            if counter > 1:
                raise Exception("Only provide one success or failure signal")

            self.success_msg = success_msg
            self.success_code = success_code
            self.failure_msg = failure_msg
            self.failure_code = failure_code

    def validate_outfile(self):
        """Validates outfile argument"""

        outfile = self.raw_args.outfile
        if outfile is not None:
            error = self.is_valid_write_file(outfile)
            if error is not None:
                raise Exception(f"Invalid outfile: {error}")

        self.outfile = outfile

    def validate_threads(self):
        """Validates threads argument"""

        threads = self.raw_args.threads
        if threads < self.THREAD_MIN:
            raise Exception("Must have at lease one thread to run")
        elif threads > self.THREAD_MAX:
            raise Exception(f"Cannot exceed {self.THREAD_MAX} threads")

        self.threads = threads

    def validate_headers(self):
        """Validates header arguments"""

        agent = self.raw_args.agent
        _cookie = self.raw_args.cookie

        cookie = {}
        if _cookie is not None:
            for field in _cookie.split("; "):
                if field != "":
                    key, value = field.split("=", 1)
                    cookie[key] = value

        self.agent = agent
        self.cookie = cookie

    def validate_flags(self):
        """Validates the finish immediately and verbose flags"""

        finish = self.raw_args.finish
        verbose = self.raw_args.verbose

        if self.runmode == "BRUTE":
            self.finish = finish

        self.verbose = verbose

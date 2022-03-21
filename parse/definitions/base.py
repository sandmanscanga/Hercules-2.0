"""Module containing argument definition base class"""
from parse.definitions.consts import DEFAULT_AGENT


class DefinitionBase:
    """Contains all the argument definition functions"""

    @staticmethod
    def runmode():
        """Determines attack mode to run in"""

        args = ("-r", "--runmode")
        kwargs = dict(
            dest="runmode",
            metavar="runmode",
            required=True,
            type=str,
            help="specify the attack mode to run in"
        )
        return args, kwargs

    @staticmethod
    def wordlist():
        """A wordlist of directories"""

        args = ("-w", "--wordlist")
        kwargs = dict(
            dest="wordlist",
            metavar="wordlist",
            required=False,
            type=str,
            help="specify a wordlist of directories"
        )
        return args, kwargs

    @staticmethod
    def extension():
        """Extension to apply to directory wordlist"""

        args = ("-x", "--extension")
        kwargs = dict(
            dest="extension",
            metavar="extension",
            required=False,
            type=str,
            help="specify an extension to apply to directory wordlist"
        )
        return args, kwargs

    @staticmethod
    def username():
        """Use a single username instead of a wordlist"""

        args = ("-l", "--username")
        kwargs = dict(
            dest="username",
            metavar="username",
            required=False,
            type=str,
            help="specify a single username"
        )
        return args, kwargs

    @staticmethod
    def userfile():
        """Use a wordlist of usernames"""

        args = ("-L", "--userfile")
        kwargs = dict(
            dest="userfile",
            metavar="userfile",
            required=False,
            type=str,
            help="specify a wordlist of usernames"
        )
        return args, kwargs

    @staticmethod
    def password():
        """Use a single password instead of a wordlist"""

        args = ("-p", "--password")
        kwargs = dict(
            dest="password",
            metavar="password",
            required=False,
            type=str,
            help="specify a single password"
        )
        return args, kwargs

    @staticmethod
    def passfile():
        """Use a wordlist of passwords"""

        args = ("-P", "--passfile")
        kwargs = dict(
            dest="passfile",
            metavar="passfile",
            required=False,
            type=str,
            help="specify a wordlist of passwords"
        )
        return args, kwargs

    @staticmethod
    def method():
        """Request method to use (GET or POST)"""

        args = ("-m", "--method")
        kwargs = dict(
            dest="method",
            metavar="method",
            required=False,
            type=str,
            default="GET",
            help="specify request method to use (GET or POST)"
        )
        return args, kwargs

    @staticmethod
    def url():
        """Target URL"""

        args = ("-u", "--url")
        kwargs = dict(
            dest="url",
            metavar="url",
            required=True,
            type=str,
            help="specify target url for attack"
        )
        return args, kwargs

    @staticmethod
    def payload():
        """POST/GET payload to send"""

        args = ("-d", "--data")
        kwargs = dict(
            dest="payload",
            metavar="payload",
            required=False,
            type=str,
            help="specify the GET/POST payload to inject into"
        )
        return args, kwargs

    @staticmethod
    def success_msg():
        """Message indicating the injection was successful"""

        args = ("-s", "--success-msg",)
        kwargs = dict(
            dest="success_msg",
            metavar="success_msg",
            required=False,
            type=str,
            help="specify a message indicating injection was successful"
        )
        return args, kwargs

    @staticmethod
    def success_code():
        """HTTP status code indicating the injection was successful"""

        args = ("-S", "--success-code",)
        kwargs = dict(
            dest="success_code",
            metavar="success_code",
            required=False,
            type=str,
            help="specify a status code indicating injection was successful"
        )
        return args, kwargs

    @staticmethod
    def failure_msg():
        """Message indicating the injection has failed"""

        args = ("-f", "--failure-msg",)
        kwargs = dict(
            dest="failure_msg",
            metavar="failure_msg",
            required=False,
            type=str,
            help="specify a message indicating injection has failed"
        )
        return args, kwargs

    @staticmethod
    def failure_code():
        """HTTP status code indicating the injection has failed"""

        args = ("-F", "--failure-code",)
        kwargs = dict(
            dest="failure_code",
            metavar="failure_code",
            required=False,
            type=str,
            help="specify a status code indicating injection has failed"
        )
        return args, kwargs

    @staticmethod
    def outfile():
        """Write results to output file"""

        args = ("-o", "--outfile")
        kwargs = dict(
            dest="outfile",
            metavar="outfile",
            required=False,
            type=str,
            help="specify output file to write results"
        )
        return args, kwargs

    @staticmethod
    def threads():
        """Total number of threads to use"""

        args = ("-t", "--threads")
        kwargs = dict(
            dest="threads",
            metavar="threads",
            required=False,
            type=int,
            default=16,
            help="specify total number of threads to use"
        )
        return args, kwargs

    @staticmethod
    def agent():
        """Custom User-agent header to use"""

        args = ("-a", "--agent")
        kwargs = dict(
            dest="agent",
            metavar="agent",
            required=False,
            type=str,
            default=DEFAULT_AGENT,
            help="specify a custom user agent to use"
        )
        return args, kwargs

    @staticmethod
    def cookie():
        """Cookie to apply to traffic"""

        args = ("-c", "--cookie")
        kwargs = dict(
            dest="cookie",
            metavar="cookie",
            required=False,
            type=str,
            help="specify a cookie to apply to traffic"
        )
        return args, kwargs

    @staticmethod
    def finish():
        """Finish on first found credential"""

        args = ("-i", "--finish")
        kwargs = dict(
            dest="finish",
            required=False,
            action="store_true",
            default=False,
            help="specify finish on first found credential flag"
        )
        return args, kwargs

    @staticmethod
    def verbose():
        """Verbose mode shows every request"""

        args = ("-v", "--verbose")
        kwargs = dict(
            dest="verbose",
            required=False,
            action="store_true",
            default=False,
            help="specify verbose mode to show every request"
        )
        return args, kwargs

    @staticmethod
    def ssl_no_verify():
        """Don't verify SSL certificate"""

        args = ("--ssl-no-verify",)
        kwargs = dict(
            dest="ssl_no_verify",
            required=False,
            action="store_true",
            default=False,
            help="specify ssl verification flag"
        )
        return args, kwargs

from lib.settings import set_pytest_mode
from lib.spinner import set_spinner_mode


def parser_default_args(parser):
    """Adds default arguments to commands"""

    def log_level():
        """Adds the log level argument"""

    def log_filename():
        parser.add_argument(
            "--log-filename",
            required=False,
            default="",
            help="Log filename to use for logging, use special value 'stdout' to log to stdout",
        )

    def pytest():
        """Flag to indicate if we are running tests with Pytest"""
        parser.add_argument(
            "--pytest",
            required=False,
            action="store_true",
            help="used for running test with Pytest",
        )


    log_level()
    log_filename()
    pytest()
    spinner()


def parser_default_funcs(parser):
    """Adds default functions to commands"""

    def pytest():
        """Sets the pytest mode"""
        set_pytest_mode(parser.pytest)

    def spinner():
        set_spinner_mode(parser.spinner)

    pytest()
    spinner()

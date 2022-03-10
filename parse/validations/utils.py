"""Module containing common validation methods"""


class ValidationBaseUtils:
    
    @staticmethod
    def is_valid_read_file(filepath):
        """Checks if file read throws exception"""

        error = None

        try:
            with open(filepath, "r") as file:
                pass
        except FileNotFoundError as exc:
            error = exc
        except PermissionError as exc:
            error = exc

        return error

    @staticmethod
    def is_valid_write_file(filepath):
        """Checks if file write throws exception"""

        error = None

        try:
            with open(filepath, "w") as file:
                pass
        except PermissionError as exc:
            error = exc

        return error

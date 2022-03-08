"""Module containing common validation methods"""


class ValidationBaseUtils:
    
    @staticmethod
    def is_valid_read_file(filepath):
        error = None

        try:
            file = open(filepath, "r")
        except FileNotFoundError as exc:
            error = exc
        except PermissionError as exc:
            error = exc
        else:
            file.close()

        return error

    @staticmethod
    def is_valid_write_file(filepath):
        error = None

        try:
            file = open(filepath, "w")
        except PermissionError as exc:
            error = exc
        else:
            file.close()

        return error

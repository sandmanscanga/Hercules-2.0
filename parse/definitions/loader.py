"""Module for loading argument definitions"""
from parse.definitions.base import DefinitionBase
from copy import deepcopy


class DefinitionLoader(DefinitionBase):
    """Inherits argument definitions and loads"""

    def __init__(self):
        super().__init__()
        self.definitions = None

    def load_definitions(self):
        """Loads all argument definitions"""

        definitions = [
            self.runmode(),
            self.wordlist(),
            self.username(),
            self.userfile(),
            self.password(),
            self.passfile(),
            self.method(),
            self.url(),
            self.payload(),
            self.success_msg(),
            self.success_code(),
            self.failure_msg(),
            self.failure_code(),
            self.outfile(),
            self.threads(),
            self.agent(),
            self.cookie(),
            self.finish(),
            self.verbose()
        ]
        self.definitions = definitions

    def get_definitions(self):
        """Returns a copy of the argument definitions"""

        definitions = deepcopy(self.definitions)
        return definitions

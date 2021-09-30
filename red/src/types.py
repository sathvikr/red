from enum import Enum


class Token:

    def __init__(self, name, token_type):
        self.name = name
        self.token_type = token_type


class TokenType(Enum):
    # Arithmetic Operators
    EQUALS = "="
    PLUS = "+"
    MINUS = "-"
    ASTERISK = "*"
    FORWARD_SLASH = "/"

    ARITHMETIC_OPERATORS = {EQUALS, PLUS, MINUS, ASTERISK, FORWARD_SLASH}

    # Logical Operators
    DOUBLE_EQUALS = "=="
    EXCLAMATION = "!"
    DOUBLE_AMPERSAND = "&&"
    DOUBLE_PIPE = "||"

    LOGICAL_OPERATORS = {DOUBLE_EQUALS, EXCLAMATION, DOUBLE_AMPERSAND, DOUBLE_PIPE}

    # Miscellaneous
    SPACE = " "
    DOT = "."
    IDENTIFIER = ""

    # Data types
    INTEGER = 0
    DOUBLE = 0.0
    BOOLEAN = False
    STRING = ""

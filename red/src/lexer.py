from types import Token, TokenType

class Lexer:

    def __init__(self, line):
        self.line = line
        self.index = 0


    def get_current_char(self):
        return self.line[self.index]

    def get_next_char(self):
        return self.line[self.index + 1] if self.index < len(self.line) - 1 else None

    def get_previous_char(self):
        return self.line[self.index - 1] if self.index > 0 else None

    def lex(self):
        while self.index < len(self.line):
            current_char = self.get_current_char()

            if current_char != TokenType.SPACE:
                if current_char == TokenType.EQUALS:
                    return Token(None, TokenType.EQUALS)
                elif current_char == TokenType.PLUS:
                    return Token(None, TokenType.PLUS)
                elif current_char == TokenType.MINUS:
                    return Token(None, TokenType.MINUS)
                elif current_char == TokenType.FORWARD_SLASH:
                    return Token(None, TokenType.FORWARD_SLASH)
                elif current_char == TokenType.DOT:
                    return Token(None, TokenType.DOT)

            self.index += 1

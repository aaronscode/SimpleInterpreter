# Token types
#
# EOF (end-of-file) token is used to indicated that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', or None
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
                type=self.type
                value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        # client string input
        self.text = text

        self.pos = 0

        self.current_token = None
        self.current_char = self.text[self.pos]

    ###########################################
    # Lexer code                              #
    ###########################################
    def error(self):
        raise Exception('Invalid Syntax')

    def advance

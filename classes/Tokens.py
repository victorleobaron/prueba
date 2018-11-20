class Tokens:
    tokens = []

    @staticmethod
    def add(value):
        Tokens.tokens.append(value)

    @staticmethod
    def get():
        return Tokens.tokens

    @staticmethod
    def reset():
        Tokens.tokens = []
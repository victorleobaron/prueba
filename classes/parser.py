from dictionaries.manager import get_languaje
from lark import Lark, Transformer, InlineTransformer
from classes.token import Token
from classes.Tokens import Tokens


tokens = []


class Parser:
    def __init__(self, languaje):
        self.languaje = get_languaje(languaje)
        self.p = Lark(self.languaje.get_grammar(), start='sentence', ambiguity='explicit')

    def parse_text(self, text):
        try:
            tree = self.p.parse(text)
            tree_parser = TreeParser()
            return tree_parser.transform(tree).data
        except Exception as e:
            return None


class TreeParser(InlineTransformer):

    def article(self, item):
        Tokens.add(Token('article', item))

    def verb(self, item):
        Tokens.add(Token('verb', item))

    def literal_verb(self, item):
        Tokens.add(Token('', item))

    def past_verb(self, item):
        Tokens.add(Token('past_verb', item))

    def tp_verb(self, item):
        Tokens.add(Token('tp_verb', item))

    def pro_f_s(self, item):
        Tokens.add(Token('pro_f_s', item))

    def pro_third(self, item):
        Tokens.add(Token('pro_third', item))

    def adj(self, item):
        Tokens.add(Token('adj', item))

    def connector(self, item):
        Tokens.add(Token('connector', item))

    def noun(self, item):
        Tokens.add(Token('noun', item))

    def popper_noun(self, item):
        Tokens.add(Token('popper_noun', item))

    def object(self, item):
        Tokens.add(Token('object', item))

    def sym_interrogative(self, item):
        Tokens.add(Token('sym_interrogative', item))

    def pro_f(self, item):
        Tokens.add(Token('pro_f', item))

    def pro_s(self, item):
        Tokens.add(Token('pro_s', item))

    def pro_plural(self, item):
        Tokens.add(Token('pro_plural', item))

    def to_be_f(self, item):
        Tokens.add(Token('to_be_f', item))

    def to_be_s(self, item):
        Tokens.add(Token('to_be_s', item))

    def to_be_t(self, item):
        Tokens.add(Token('to_be_t', item))

    def pa_to_be_f_t(self, item):
        Tokens.add(Token('pa_to_be_f_t', item))

    def pa_to_be(self, item):
        Tokens.add(Token('pa_to_be', item))

    def to_be_plural(self, item):
        Tokens.add(Token('to_be_plural', item))

    def preposition(self, item):
        Tokens.add(Token('', item))

    def adv_freq(self, item):
        Tokens.add(Token('', item))

    def gerund_verb(self, item):
        Tokens.add(Token('gerund_verb', item))

    def ne_tp_auxverb(self, item):
        Tokens.add(Token('ne_tp_auxverb', item))

    def ne_fs_auxverb(self, item):
        Tokens.add(Token('', item))

    def pro_plural(self, item):
        Tokens.add(Token('', item))
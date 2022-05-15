import ply.yacc as yacc
from lib2to3.pgen2 import literals
import ply.lex as lex

# [a-zA-Z|_]+\([^\)]*\)(\.[^\)]*\))? - detetar funçoes

literals = ['%', '=', '!']
tokens = ['id', 'DEF', 'COMMENT', 'aspas', 'reto', 'chav', 'curvo']

def t_curvo(p):
    r'\(.*?\)'
    return p

def t_aspas(p):
    # r'\"[^"]*\"'
    r'\".*\"'
    return p

def t_reto(p):
    r'\[.*?\]'
    return p

def t_chav(p):
    r'{.*?}'
    return p

def t_DEF(p):
    r'(?P<indent>[ \t]*)def[ \t]*(?P<name>\w+)\s*\((?P<params>.*?)\)(?:[ \t]*->[ \t]*(?P<return>\w+))?:(?P<body>(?:\n(?P=indent)(?:[ \t]+[^\n]*)|\n)+)'
    return p

def t_COMMENT(p):
    r'\#.*'
    return p

def t_id(t):
    r'[_a-zA-Z0-9_]\w*'
    return t

t_ignore = " \t\n"

def t_error(t):
    print('Caracter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
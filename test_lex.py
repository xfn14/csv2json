import ply.yacc as yacc
from lib2to3.pgen2 import literals
import ply.lex as lex

# [a-zA-Z|_]+\([^\)]*\)(\.[^\)]*\))? - detetar funçoes

literals = ['%', '=', '[', ']', ':', '{', '}', '(', ')', '’', '*', '+', '-', '/', '.', ',', ';', '<', '>', '!', '?', '|', '&', '^', '~', '@', '#', '$', '%','\'', '"', '\\']
tokens = ['id', 'EOL', 'DEF', 'STAT', 'EXP', 'COMMENT', 'TEXT', 'aspas', 'reto']

def t_id(t):
    r'[_a-zA-Z]\w*'
    return t

def t_EOL(t):
    r'[A-Za-z\t .]+'
    return t

def t_DEF(p):
    r'(?P<indent>[ \t]*)def[ \t]*(?P<name>\w+)\s*\((?P<params>.*?)\)(?:[ \t]*->[ \t]*(?P<return>\w+))?:(?P<body>(?:\n(?P=indent)(?:[ \t]+[^\n]*)|\n)+)'
    return p

def p_COMMENT(p):
    r'\#.*'
    return p

def p_aspas(p): #apanha o que esta dentro de ""
    # r'\"[^"]*\"'
    r'\".*\"'
    return p


def p_reto(p): #apanha o que esta dentro de ""
    r'\[.*\]'
    return p

#def p_parenteses(p): #seria para apanhar o que estava entre [] mas nao sei  se compensa
 

def p_RETURN(p):
    r'return'
    return p

def p_ERROR(p):
    r'error'
    return p

def p_PRECEDENCE(p):
    r'precedence'
    return p

def t_TEXT(p): #duvidas
    # r'.*' #apanha tudo
    r'[_a-zA-Z0-9_]\w*'  #apanha letras e numeros
    return p

def p_content(p):
    r'\{.*\}'
    return p


t_ignore = " \t\n"

def t_error(t):
    print('CarÃ¡ter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
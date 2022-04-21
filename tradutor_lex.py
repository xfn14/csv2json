from lib2to3.pgen2 import literals
import ply.lex as lex

literals = ['+', '-', '/', '*', '=', '(', ')']

tokens = ['VAR', 'NUMBER']

t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

# def t_VAR(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*' 

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


t_ignore = " \t\n"

def t_error(t):
    print('Caracter ilegal: ', t.value[0], [t.lexer.lineno])
    t.lexer.skip(1)
    
lexer = lex.lex()
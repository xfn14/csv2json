from lib2to3.pgen2 import literals
import ply.lex as lex

literals = ['+', '-', '/', '*', '=', '(', ')']

tokens = ['VAR', 'NUMBER']

t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
# def t_VAR(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*' 

# def t_NUMBER(t):
#     r'\d+(\.\d+)?'
#     # r'\d+'
#     t.value = float(t.value)
#     return t


# # Define a rule so we can track line numbers
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# # A string containing ignored characters (spaces and tabs)
# t_ignore  = ' \t'

# # Error handling rule
# def t_error(t):
#     print("Erro lexico no token '%s'" % t.value[0])
#     t.lexer.skip(1)


t_ignore = " \t\n"

def t_error(t):
    print('Caracter ilegal: ', t.value[0], [t.lexer.lineno])
    t.lexer.skip(1)
    
lexer = lex.lex()
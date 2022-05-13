from lib2to3.pgen2 import literals
from ply import lex, yacc

# Criar um lexer/parser de uma nova linguagem definida da seguinte maneira:
# 
#\ %% LEX - para indicar o inicio do lexer
# %literals - para indicar a variavel literals
# %ignore - para indicar os a variavel ignore
# %tokens - para indicar a variavel tokens
#\ %% YACC - para indicar o inicio do parser
# %precedence - para indicar a variavel precedence
# stat : expr { statment }
# exp : expr { statment }
#\ %% - para indicar o inicio da main
#
# Exemplo de ficheiro:
#
# %!% LEX
# %literals = "+-/*=()" ## a single char
# %ignore = " \t\n"
# %tokens = [ ’VAR’,’NUMBER’ ]

# [a-zA-Z_][a-zA-Z0-9_]* return(’VAR’, t.value)
# \d+(\.\d+)? return(’NUMBER’, float(t.value)
# . error(f"Illegal character ’{t.value[0]}’, [{t.lexer.lineno}]",
# t.lexer.skip(1) )
# %!% YACC

# %precedence = [
#     (’left’,’+’,’-’),
#     (’left’,’*’,’/’),
#     (’right’,’UMINUS’),
# ]

# # symboltable : dictionary of variables
# ts = { }
# stat : VAR ’=’ exp { ts[t[1]] = t[3] }
# stat : exp { print(t[1]) }
# exp : exp ’+’ exp { t[0] = t[1] + t[3] }
# exp : exp ’-’ exp { t[0] = t[1] - t[3] }
# exp : exp ’*’ exp { t[0] = t[1] * t[3] }
# exp : exp ’/’ exp { t[0] = t[1] / t[3] }
# exp : ’-’ exp %prec UMINUS { t[0] = -t[2] }
# exp : ’(’ exp ’)’ { t[0] = t[2] }
# exp : NUMBER { t[0] = t[1] }
# exp : VAR { t[0] = getval(t[1]) }

# %!%
# def p_error(t):
#     print(f"Syntax error at ’{t.value}’, [{t.lexer.lineno}]")
# def getval(n):
# if n not in ts: print(f"Undefined name ’{n}’")
# return ts.get(n,0)
# y=yacc()
# y.parse("3+4*7")

literals = ['%', '=', '[', ']', ':', '{', '}', '(', ')']
tokens = ['LEX', 'YACC', 'COMMENT', 'LITERALS', 'TOKENS', 'IGNORE', 'aspas', 'RETURN', 'ERROR', 'PRECEDENCE', 'PRINT']

def t_LEX(p):
    r'LEX'
    return p

def t_YACC(p):
    r'YACC'
    return p

def p_LEX(p):
    r'%% LEX'
    print('import ply.lex as lex') # imprimir para o ficheiro
    
def p_YACC(p):
    r'%% YACC'
    print('import ply.yacc as yacc') # imprimir para o ficheiro

import ply.yacc as yacc
import ply.lex as lex

literals = ['%', '=', '"', '[', ']', ':', '{', '}', '(', ')' ]
tokens = ['LEX', 'YACC', 'COMMENT', 'LITERALS', 'TOKENS', 'IGNORE', 'aspas', 'RETURN', 'ERROR', 'PRECEDENCE', 'PRINT' ] #'parenteses', 'text'

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
    return p

def p_COMMENT(p):
    r'\#.*'
    return p

def p_LITERALS(p):
    r'literals'
    return p

def p_IGNORE(p):
    r'ignore'
    return p

def p_TOKENS(p):
    r'tokens'
    return p

def p_str(p): #apanha o que esta dentro de ""
    r'\"[^"]*\"'
    return t

def p_text(p):
    r'[_a-zA-Z]\w*'
    return p

def p_RETURN(p):
    r'return'
    return p

def p_ERROR(p):
    r'error'
    return p

def p_PRECEDENCE(p):
    r'precedence'
    return p

def p_PRINT(p):
    r'print'
    return p
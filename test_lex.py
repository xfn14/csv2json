import ply.yacc as yacc
from lib2to3.pgen2 import literals
import ply.lex as lex

literals = ['%', '=', '[', ']', ':', '{', '}', '(', ')' ]
tokens = ['id', 'STAT', 'EXP', 'LEX', 'YACC', 'COMMENT', 'LITERALS', 'TOKENS', 'IGNORE', 'aspas', 'RETURN', 'ERROR', 'PRECEDENCE', 'text', 'content', 'FUNC' ] #'parenteses', 

def t_id(t):
    r'[_a-zA-Z]\w*'
    return t

def t_LEX(p):
    r'%% LEX'
    return p

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

def p_text(p): #duvidas
    r'.*' #apanha tudo
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
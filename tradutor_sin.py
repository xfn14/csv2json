import ply.yacc as yacc
from tradutor_lex import tokens, literals

#Parsing rules
precedence = [
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
]

#Dictionary of Names
ts = {}

#alterar a gramatica, fazer uma geral
def p_Stat_Lista(p):
    "Stat : VAR '=' Exp"
    ts[p[1]] = p[3]
    
def p_Stat_Simples(p):
    "Stat : Exp"
    print(p[1])
    
def p_Exp_sum(p):
    "Exp : Exp '+' Exp"
    p[0] = p[1] + p[3]

def p_Exp_sub(p):
    "Exp : Exp '-' Exp"
    p[0] = p[1] - p[3]
    
def p_Exp_mul(p):
    "Exp : Exp '*' Exp"
    p[0] = p[1] * p[3]
    
def p_Exp_div(p):
    "Exp : Exp '/' Exp"
    p[0] = p[1] / p[3]
    
def p_Exp_neg(p):
    "Exp : '-' Exp %prec UNIMUS"
    p[0] = -p[2]
    
def p_Exp_parentesis(p):
    "Exp : '(' Exp ')'"
    p[0] = p[2]
    
def p_Number(p):
    "Exp : NUMBER"
    p[0] = p[1]
    
def p_Var(p):    
    "Exp : VAR"
    p[0] = getval(p[1])
    
def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False
    
def getval(n):
    if n not in ts:
        print("Undefined name", n)
    return ts.get(n,0)
    
        
# Build the parser
parser = yacc.yacc()

# Variaveis de estado
parser.registos = {}
  
#   Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success: 
        print("Frase valida: ", linha)
    else:
        print("Frase Invalida.. corrija")

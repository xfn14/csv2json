from telnetlib import TSPEED
from wsgiref.headers import tspecials
import ply.yacc as yacc
from tradutor_lex import tokens, literals

def p_Stat_Lista(p):
    "Stat : VAR '=' Exp"
    
def p_Stat_Simples(p):
    "Stat : Exp"
    
def p_Exp_sum(p):
    "Exp : Exp '+' Exp"

def p_Exp_sub(p):
    "Exp : Exp '-' Exp"

def p_Exp_mul(p):
    "Exp : Exp '*' Exp"
    
def p_Exp_div(p):
    "Exp : Exp '/' Exp"
    
def p_Exp_neg(p):
    "Exp : '-' Exp " #incompleto.....
    
def p_Exp_parentesis(p):
    "Exp : '(' Exp ')'"
    
def p_Number(p):
    "Exp : NUMBER"
    
def p_Var(p):    
    "Exp : VAR"

    
def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False
    
def getval(n):
    if n not in tspecials:
        print("Undefined name", n)
    return tspecials.get(n,0)
    
        
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
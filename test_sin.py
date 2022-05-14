import ply.yacc as yacc 
from test_lex import tokens, literals

statementN = 0
ts = {}

def p_Statement_Simples(p):
    "Statement : Expression"
    print(p[1])
    
# def p_IdList_list(p):
#     "IdList : IdList ',' id"
#     p[0] = p[1] + [p[3]]

# def p_IdList_single(p):
#     "IdList : id"
#     p[0] = [p[1]] 
    
def p_Expression_EQUALS(p):
    "Expression : '*' '*' id '=' Equal"
    ts[p[3]] = p[5]
    p[0] = p[3] + ' = ' + p[5] + '\n'

def p_Equal_aspas(p):
    "Equal : aspas"
    p[0] = p[1]

def p_Equal_reto(p):
    "Equal : reto"
    p[0] = p[1]

# def p_Expression_LITERALS_LIST(p):
#     "Expression : '%' LITERALS '=' IdList"
#     p[0] = 'literals = ' + p[4] + '\n'

# def p_Expression_TOKENS_LIST(p):
#     "Expression : '%' TOKENS '=' IdList"
#     p[0] = 'tokens = ' + p[4] + '\n'

# def p_Expression_IGNORE_LIST(p):
#     "Expression : '%' IGNORE '=' IdList"
#     p[0] = 'ignore = ' + p[4] + '\n'

# def p_Expression_LITERALS_SINGLE(p):
#     "Expression : '%' LITERALS '=' TEXT"
#     p[0] = 'literals = ' + p[4] + '\n'

# def p_Expression_TOKENS_SINGLE(p):
#     "Expression : '%' TOKENS '=' TEXT"
#     p[0] = 'tokens = ' + p[4] + '\n'

# def p_Expression_IGNORE_SINGLE(p):
#     "Expression : '%' IGNORE '=' TEXT"
#     p[0] = 'ignore = ' + p[4] + '\n'
    
def p_Expression_STAT(p):
    "Expression : STAT ':' TEXT '{' Expression '}'"
    p[0] = 'def p_Statment_' + statementN + '(p):\n\t' + p[1] + ' : ' + p[3] + '\n\t' + p[5] + '\n\n'
    statementN += 1

def p_Expression_EXP(p):
    "Expression : EXP ':' TEXT '{' Expression '}'"
    p[0] = 'def p_Expressions_' + statementN + '(p):\n\t' + p[1] + ' : ' + p[3] + '\n\t' + p[5] + '\n\n'
    statementN += 1
    
def p_Expression_COMMENT(p):
    "Expression : COMMENT"
    p[0] = '\n'
    
def p_Expression_DEF(p):
    "Expression : DEF"
    p[0] = p[1]

def p_Expression_LEX(p):
    "Expression : '%' '%' id"
    if p[3] == 'LEX':
        p[0] = 'import ply.lex as lex\n'
    elif p[3] == 'YACC':
        p[0] = 'import ply.yacc as yacc\n'
        
def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False
    
def getval(n):
    if n not in ts:
        print("Undefined name", n)
    return ts.get(n,0)
    
# def p_Expression_YACC(p):
#     "Expression : '%' '%' id"
#     p[0] = 'import ply.yacc as yacc\n'
    
# Build the parser
parser = yacc.yacc()
parser.ts = {}
parser.contaPos = 0

# Read line from input and parse it
import sys
parser.success = True
program = sys.stdin.read()
codigo = parser.parse(program)
if parser.success:
    print("Programa estruturalmente correto!")
    print(parser.ts)
    print(codigo)
else:
    print("Programa com erros... Corrija e tente novamente!")
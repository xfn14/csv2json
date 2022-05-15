from turtle import st
import ply.yacc as yacc 
from test_lex import tokens, literals

statementN = 0
ts = {}

def p_Statement_Simples(p):
    "Statement : Expression"
    p[0] = p[1]

def p_Statement_Lista(p):
    "Statement : Statement Expression"
    p[0] = p[1] + p[2]
    
def p_Expression_EQUALS(p):
    "Expression : id '=' Equal"
    ts[p[1]] = p[3]
    p[0] = p[1] + ' = ' + p[3] + '\n'

def p_Expression_Parse(p):
    "Expression : id aspas"
    if(p[1] == 'yaccParse'):
        p[0] = 'parser = yacc.yacc()\nparsed = parser.parse(' + p[2] + ')\nprint(parsed)\n'
        
def p_Expression_TOKENIZE(p):
    "Expression : aspas curvo chav"
    p[0] = 'def t_' + p[1].replace('"', '') + '(t):\n\tr\'' + p[2].replace('(', '').replace(')', '') + '\'\n\tt.value = ' + p[3].replace('{', '').replace('}', '') + '\n\treturn t\n'

def p_Equal_aspas(p):
    "Equal : aspas"
    p[0] = p[1]

def p_Equal_reto(p):
    "Equal : reto"
    p[0] = p[1]
    
def p_Equal_chav(p):
    "Equal : chav"
    p[0] = p[1]

def p_Expression_SIN(p):
    "Expression : id '!' aspas chav"
    global statementN
    p[0] = 'def p_Expression_' + str(statementN) + '(t):\n\t\"' + p[1] + ' : ' + p[3].replace('"', '') + '\"\n\t' + p[4].replace('{ ', '').replace('}', '') + '\n\n'
    statementN += 1

def p_Expression_COMMENT(p):
    "Expression : COMMENT"
    p[0] = ''
    
def p_Expression_DEF(p):
    "Expression : DEF"
    p[0] = p[1]

def p_Expression_LEX(p):
    "Expression : '%' '%' id"
    if p[3] == 'LEX':
        p[0] = 'import ply.lex as lex\n'
    elif p[3] == 'YACC':
        p[0] = 'lexer = lex.lex()\n\nimport ply.yacc as yacc\n'
        
def p_error(p):
    print('Erro sintatico: ', p)
    parser.success = False
    
def getval(n):
    if n not in ts:
        print("Undefined name", n)
    return ts.get(n,0)
    
parser = yacc.yacc()
parser.ts = ts
parser.contaPos = 0

import sys
parser.success = True
program = sys.stdin.read()
codigo = parser.parse(program).replace('’', '\'')
if parser.success:
    print("Programa estruturalmente correto!")
    print(parser.ts)
    print('\n')
    print(codigo)
    with open("output.py", "w", encoding="utf-8") as out:
        out.write(codigo)
else:
    print("Programa com erros... Corrija e tente novamente!")
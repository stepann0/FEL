import ply.yacc as yacc
from lexer import tokens
from exec import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQEQ', 'NOT_EQ'),
    ('left', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIVIDE', 'MOD'),
    ('right', 'POW')
)

def p_expression_bin_operator(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression POW expression'''

    p[0] = bin_op(p[1], p[2], p[3])

def p_expression(p):
    '''expression : comparison
                  | func_call
                  | range'''
    p[0] = p[1]

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_bool(p):
    '''expression : TRUE 
                  | FALSE'''
    p[0] = p[1] == 'true'

def p_expression_un_operator(p):
    '''expression : MINUS expression
                  | PLUS expression'''
    p[0] = -p[2] if p[1] == '-' else p[2]

def p_paren_expression(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_comparison(p):
    '''comparison : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQEQ expression
                  | expression NOT_EQ expression'''

    p[0] = compare(p[1], p[2], p[3])

def p_func_call(p):
    '''func_call : ID LPAREN func_args RPAREN'''
    print(p[0], p[1], p[2], p[3], p[4])

def p_func_args(p):
    '''func_args : func_args COMMA expression
                 | expression
                 |'''
    if len(p) == 1: # no args
        p[0] = None
    elif len(p) == 2: # one arg
        p[0] = [p[1]]
    else: # 2+ args, separated by ','
        p[0] = [*p[1], p[3]]

def p_range(p):
    '''range : NUMBER RANGE NUMBER
             | NUMBER RANGE NUMBER COLON NUMBER'''
    if len(p) == 4: # num..num
        p[0] = list(range(p[1], p[3]+1))
    else: # num..num:num
        p[0] = list(range(p[1], p[3], p[5]))


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
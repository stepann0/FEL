import ply.yacc as yacc
from lexer import tokens
import exec

precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("left", "EQEQ", "NOT_EQ"),
    ("left", "GT", "GE", "LT", "LE"),
    ("left", "PLUS", "MINUS"),
    ("left", "MULT", "DIVIDE", "MOD"),
    ("right", "POW")
)

def p_statmenet(p):
    """statment : expression
                | array_literal
                | range"""
    p[0] = p[1]

def p_expression_bin_operator(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression POW expression"""

    p[0] = exec.bin_op(p[1], p[2], p[3])

def p_comparison(p):
    """comparison : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQEQ expression
                  | expression NOT_EQ expression"""

    p[0] = exec.compare(p[1], p[2], p[3])

def p_expression(p):
    """expression : comparison
                  | func_call
                  | paren_expression"""
    p[0] = p[1]

def p_expression_un_operator(p):
    """expression : MINUS expression
                  | PLUS expression"""
    p[0] = -p[2] if p[1] == "-" else p[2]

def p_paren_expression(p):
    "paren_expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_bool(p):
    """expression : TRUE 
                  | FALSE"""
    p[0] = p[1] == "true"

def p_expression_num(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_number(p):
    """NUMBER : INT
              | FLOAT"""
    p[0] = p[1]

def p_func_call(p):
    """func_call : ID LPAREN statment_list RPAREN"""
    p[0] = exec.call_func(p[1], p[3])

def p_statment_list(p):
    """statment_list : statment_list COMMA statment
                     | statment
                     |"""
    if len(p) == 1: # no args
        p[0] = None
    elif len(p) == 2: # one arg
        p[0] = [p[1]]
    else: # 2+ args, separated by ","
        p[0] = [*p[1], p[3]]

def p_range_param(p):
    """range_param : INT
                   | paren_expression"""
    p[0] = p[1]

def p_unary_range_param(p):
    """range_param : MINUS range_param
                   | PLUS range_param"""
    p[0] = -p[2] if p[1] == "-" else p[2]


def p_range(p):
    """range : range_param RANGE range_param
             | range_param RANGE range_param COLON range_param"""
    if len(p) == 4: # start..stop
        p[0] = exec.sequence(p[1], p[3])
    else: # start..stop:step
        p[0] = exec.sequence_step(p[1], p[3], p[5])

def p_array_literal(p):
    """array_literal : LSQUARE statment_list RSQUARE"""
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print(f"{' '*p.lexpos}^")
    exec.error("syntax error:")

# Build the parser
parser = yacc.yacc()

# while True:
#    try:
#        s = input("calc > ")
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)
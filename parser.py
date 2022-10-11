import ply.yacc as yacc
from lexer import tokens
import exec

# precedence = (
#     ("left", "OR"),
#     ("left", "AND"),
#     ("left", "EQEQ", "NOT_EQ"),
#     ("left", "GT", "GE", "LT", "LE"),
#     ("left", "PLUS", "MINUS"),
#     ("left", "MULT", "DIVIDE", "MOD"),
#     ("right", "POW")
# )

def p_expression(p):
    """expression : disjunction"""
    p[0] = p[1]

def p_disjunction(p):
    """disjunction : disjunction OR conjunction
                   | conjunction"""
    if len(p) == 3:
        p[0] = p[1] or p[2]
    else:
        p[0] = p[1]

def p_conjuction(p):
    """conjunction : conjunction AND inversion
                   | inversion"""
    if len(p) == 4:
        p[0] = p[1] and p[3]
    else:
        p[0] = p[1]

def p_invertion(p):
    """inversion : NOT inversion 
                 | comparison"""
    if len(p) == 3:
        p[0] = not p[2]
    else:
        p[0] = p[1]

def p_comp_operator(p):
    """COMP_OP : EQEQ
               | NOT_EQ
               | LE
               | LT
               | GE
               | GT
               | IN
               | IS"""
    p[0] = p[1]

def p_comparison(p):
    """comparison : comparison COMP_OP bitwise_or
                  | bitwise_or"""
    if len(p) == 4:
        p[0] = exec.compare(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_bit_or(p):
    """bitwise_or : bitwise_or BIT_OR bitwise_xor 
                  | bitwise_xor"""
    if len(p) == 4:
        p[0] = p[1] | p[3]
    else:
        p[0] = p[1]

def p_bit_xor(p):
    """bitwise_xor : bitwise_xor BIT_XOR bitwise_and 
                   | bitwise_and"""
    if len(p) == 4:
        p[0] = p[1] ^ p[3]
    else:
        p[0] = p[1]

def p_bit_and(p):
    """bitwise_and : bitwise_and BIT_AND sum 
                   | sum"""
    if len(p) == 4:
        p[0] = p[1] & p[3]
    else:
        p[0] = p[1]

def p_sum(p):
    """sum : sum PLUS term 
           | sum MINUS term 
           | term"""
    if len(p) == 4:
        p[0] = exec.bin_op(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    """term : term MULT factor 
            | term DIVIDE factor 
            | term MOD factor 
            | factor"""
    if len(p) == 4:
        p[0] = exec.bin_op(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_factor(p):
    """factor : PLUS factor 
              | MINUS factor 
              | power"""
    if len(p) == 3:
        p[0] = -p[2] if p[1] == "-" else p[2]
    else:
        p[0] = p[1]

def p_pow(p):
    """power : atom POW factor
             | atom"""
    if len(p) == 4:
        p[0] = p[1] ** p[3]
    else:
        p[0] = p[1]

def p_atom_num(p):
    """atom : NUMBER"""
    p[0] = p[1]

def p_atom_bool(p):
    """atom : TRUE 
            | FALSE"""
    p[0] = p[1] == 'true'

def p_atom_parenth_expr(p):
    """atom : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_atom_array(p):
    """atom : array"""
    p[0] = p[1]

def p_array(p):
    """array : LSQUARE expression_list RSQUARE"""
    p[0] = p[2]

def p_expression_list(p):
    """expression_list : expression_list COMMA expression
                       | expression
                       |"""
    if len(p) == 1: # no args
        p[0] = []
    elif len(p) == 2: # one arg
        p[0] = [p[1]]
    else: # 2+ args, separated by ","
        p[0] = [*p[1], p[3]]

def p_number(p):
    """NUMBER : INT
              | FLOAT"""
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print(f"{' '*p.lexpos}^")
    exec.error("syntax error:")

parser = yacc.yacc()
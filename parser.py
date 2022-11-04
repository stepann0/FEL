import ply.yacc as yacc
from lexer import tokens
from numpy import array
import exec

def p_expression_if_else(p):
    """expression : disjunction IF disjunction ELSE expression"""
    p[0] = p[1] if p[3] else p[5]

def p_expression_disj(p):
    """expression : disjunction"""
    p[0] = p[1]

def p_disjunction(p):
    """disjunction : disjunction OR conjunction
                   | conjunction"""
    if len(p) == 4:
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
            | factor
            | range"""
    if len(p) == 4:
        p[0] = exec.bin_op(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_factor_factorial(p):
    """factor : factor EPOINT"""
    p[0] = exec.un_operator(p[2], p[1])

def p_factor(p):
    """factor : PLUS factor 
              | MINUS factor 
              | SQRT factor
              | power"""
    if len(p) == 3:
        p[0] = exec.un_operator(p[1], p[2])
    else:
        p[0] = p[1]

def p_pow(p):
    """power : atom POW factor
             | atom"""
    if len(p) == 4:
        p[0] = p[1] ** p[3]
    else:
        p[0] = p[1]

def p_atom_id(p):
    """atom : ID"""
    p[0] = p[1]

def p_atom_num(p):
    """atom : NUMBER"""
    p[0] = p[1]

def p_atom_bool(p):
    """atom : TRUE 
            | FALSE"""
    p[0] = p[1] == 'true'

def p_atom_array_range(p):
    """atom : array"""
    p[0] = p[1]

def p_atom_func_call(p):
    """atom : func_call"""
    p[0] = p[1]

def p_atom_parenth_expr(p):
    """atom : paren_expression"""
    p[0] = p[1]

def p_array(p):
    """array : LBRACE expression_list RBRACE"""
    p[0] = array(p[2])

def p_range(p):
    """range : expression RANGE expression RANGE expression
             | expression RANGE expression"""
    if len(p) == 4: # start::stop
        p[0] = exec.sequence(p[1], p[3])
    else: # start::stop::step
        p[0] = exec.sequence_step(p[1], p[3], p[5])

def p_func_call(p):
    """func_call : ID LPAREN expression_list RPAREN"""
    p[0] = exec.call_func(p[1], p[3])

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

def p_paren_expression(p):
    """paren_expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_error(p):
    exec.error("syntax error")

parser = yacc.yacc()
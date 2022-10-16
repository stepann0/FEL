import ply.lex as lex
from ply.lex import TOKEN

reserved = {
   'in' : 'IN',
   'if' : 'IF',
   'else' : 'ELSE',
   'false' : 'FALSE',
   'true' : 'TRUE',
   'or' : 'OR',
   'and' : 'AND',
   'not' : 'NOT',
   'is' : 'IS',
}

tokens = [
   'INT', 'FLOAT',
   'PLUS', 'MINUS',
   'MULT', 'DIVIDE',
   'POW', 'SQRT',
   'MOD','EPOINT',

   'LPAREN', 'RPAREN',
   'LBRACE', 'RBRACE',
   'LSQUARE', 'RSQUARE',

   'COMMA', 'COLON', 'SEMI',

   'ARROW', 'RANGE',
   'LT', 'GT',
   'LE', 'GE',
   'EQEQ', 'NOT_EQ',
   'ID', 'STRING',

   'BIT_OR', 'BIT_AND', 'BIT_XOR',
] + list(reserved.values())

t_BIT_OR  = r'\|'
t_BIT_AND = r'&' 
t_BIT_XOR = r'\^\^'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'
t_DIVIDE  = r'/'
t_POW     = r'\^'
t_SQRT    = r'√'
t_MOD     = r'%'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'

t_COMMA   = r','
t_RANGE   = r'::'
t_COLON   = r':'
t_SEMI    = r';'

t_ARROW   = r'->'
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_EQEQ    = r'=='
t_NOT_EQ  = r'!='
t_EPOINT  = r'!'
t_STRING  = r'".*"'
t_ignore  = ' \t'

# float regexps are taken from https://github.com/eliben/pycparser/blob/master/pycparser/c_lexer.py
exponent_part = r"""([eE][-+]?[0-9]+)"""
fractional_constant = r"""([0-9]*\.[0-9]+)|([0-9]+\.)"""
floating_constant = '(((('+fractional_constant+')'+exponent_part+'?)|([0-9]+'+exponent_part+'))[FfLl]?)'
@TOKEN(floating_constant)
def t_FLOAT(t):
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
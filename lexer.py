import ply.lex as lex

reserved = {
   'if' : 'IF',
   'in' : 'IN',
   'else' : 'ELSE',
   'false' : 'FALSE',
   'true' : 'TRUE',
   'or' : 'OR',
   'and' : 'AND',
   'not' : 'NOT',
}

tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'MULT',
   'DIVIDE',
   'POW',
   'MOD',

   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'LSQUARE',
   'RSQUARE',

   'RANGE',
   'COMMA',
   'COLON',
   'SEMI',

   'ARROW',
   'LT',
   'GT',
   'LE',
   'GE',
   'EQEQ',
   'NOT_EQ',
   'STRING',
   'ID',
] + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'
t_DIVIDE  = r'/'
t_POW     = r'\^'
t_MOD     = r'%'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'

t_RANGE   = r'\.\.'
t_COMMA   = r','
t_COLON   = r':'
t_SEMI    = r';'

t_ARROW   = r'->'
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_EQEQ    = r'=='
t_NOT_EQ  = r'!='
t_STRING  = r'".*"'
t_ignore  = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# data = '''
# sum(2, 3, 4, 5)
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)

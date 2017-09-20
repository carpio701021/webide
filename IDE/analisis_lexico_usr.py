from IDE.ply import lex as lex
# List of token names.   This is always required
tokens = (
    'COR_A', 
    'COR_C',
    'DPTOS', 
    'LOGIN', 
    'USR', 
    'CADENA' 
)

# Regular expression rules for simple tokens
t_COR_A = r'\{'
t_COR_C = r'\}'
t_DPTOS = r':'
t_LOGIN = r'login'
t_USR = r'usr'

# A regular expression rule with some action code
def t_CADENA(t):
	r'\"[^\"]*\"'
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    #print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
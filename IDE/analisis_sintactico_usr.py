# Yacc example

from IDE.ply import yacc as yacc
from IDE.Login import Login

# Get the token map from the lexer.  This is required.
from IDE.analisis_lexico_usr import tokens

def p_plycs(p):
    'plycs : COR_A LOGIN DPTOS CADENA USR DPTOS CADENA  COR_C'
    e=Login()
    e.estado= p[4]
    e.usr =  p[7]
    print('ENTRA A LA PRODUCCION')
    p[0] = e
        
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
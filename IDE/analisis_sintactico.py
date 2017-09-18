# Yacc example

from IDE.ply import yacc as yacc
from IDE.Paquete import Paquete

# Get the token map from the lexer.  This is required.
from IDE.analisis_lexico import tokens

def p_plycs(p):
    'plycs : COR_A PAQUETE  DPTOS CADENA COMA DATOS DPTOS CADENA COMA EJECUCION  DPTOS CADENA COMA MENSAJE  DPTOS CADENA COMA HISTORIAL  DPTOS CADENA COR_C'
    print("anicka")
    e=Paquete()
    e.datos= p[8]
    e.ejecucion =  p[12]
    e.mensaje =  p[16]
    e.historial = p[20] 
    p[0] = e
        
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
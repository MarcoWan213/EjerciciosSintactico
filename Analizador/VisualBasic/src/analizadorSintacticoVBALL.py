import ply.yacc as yacc
import os
import codecs
import re
from analizador import tokens
from sys import stdin

precedence = (
	('right','ID','MODULE'),
	#('right','PROCEDURE'),
	#('right','VAR'),
	('right','IGUAL'),
	('right','UPDATE'),
    #('right','ARGS'),
	('right','NUMERO', 'DOT'),
	('left','NOIGUAL'),
	('left','MENORQ','MAYORQ'),
	('left','SUMA','RESTA'),
	('left','MULTI','DIV'),
	#('right','ODD'),
	('right','PUNTO'),
	('left','PIZQ','PDER'),
	('left','LLIZQ','LLDER'),
	#'a','x','SUMA','RESTA','DIV','MULTI','MENORQ','MAYORQ','IGUAL','NOIGUAL',
	#'PIZQ','PDER','LLIZQ','LLDER','PUNTO','UPDATE'
	)



#def p_module1(p):
#    'init : MODULE PROGRAM'

#def p_readline(p):
    #'read : CONSOLE DOT WRITELINE PIZQ ID PDER'




#def p_id(p):
#    'id : ID | NUMERO'

def p_empty(p):
	'''empty : '''
	pass

def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

direccion ='C:/Users/Marco/Documents/test/'
archivi = buscarFicheros(direccion)
prueba = direccion+archivi
fp = codecs.open(prueba, "r", "utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)

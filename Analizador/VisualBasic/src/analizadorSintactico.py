import ply.yacc as yacc
import os
import codecs
import re
from analizador import tokens
from sys import stdin

precedence = (	#Declaramos todas las precedencias del analizador lexico
	('right','ID','MODULE', 'IMPORTS'),	
	('right','IGUAL'),
	('right','UPDATE'),    
	('right','NUMERO'),
	('left','NOIGUAL'),
	('left','MENORQ','MAYORQ'),
	('left','SUMA','RESTA'),
	('left','MULTI','DIV'), 
	('right','WHILE'),
	('right','PUNTO'),
	('left','PIZQ','PDER'),
	('left','LLIZQ','LLDER'),
	)

#Empiezan las definiciones
def p_module(p): #Principal para cualquier bloque
	'module : program'				
	print ("Module")

def p_program(p): #Para las declaraciones
	'program : constDecl varDecl procDecl statement'	
	print ("Program")


def p_constDecl(p): #Declaracion de una constante
	'''constDecl : DIM constAssignmentList'''
	#p[0] = constDecl(p[2])
	#print "constDecl"
	print ("Conts")

def p_constDecl1(p): #Otro tipo de declaracion de contantes
	'''constDecl : DIM ID IGUAL ID'''
	#p[0] = constDecl(p[2])
	#print "constDecl"
	print ("Conts 1")

def p_constDecl2(p): #Otro tipo de declaracion de contantes
	'''constDecl : DIM ID AS ID IGUAL ID'''
	#p[0] = constDecl(p[2])
	#print "constDecl"
	print ("Conts 2")

def p_constDeclEmpty(p): #Constante vacia
	'''constDecl : empty'''
	#p[0] = Null()
	#print "nulo"
	print ("ContsEmp")

def p_constAssignmentList1(p): #Varias constantes
	'''constAssignmentList : ID IGUAL NUMERO'''
	print ("constAssignmentList 1")

def p_constAssignmentList2(p): #Varias constantes 2
	'''constAssignmentList : constAssignmentList ID IGUAL NUMERO'''
	print ("constAssignmentList 2")

#def p_varDecl1(p):
#	'''varDecl : DIM identList'''
#	print ("varDecl 1")

def p_varDecl2(p): #Declaracion de una variable
	'''varDecl : DIM NUMERO AS ID IGUAL ID'''
	print ("varDecl DIM SAME")
	

def p_varDeclEmpty(p): #Variable vacia
	'''varDecl : empty'''
	print ("nulo")

def p_identList1(p): #Identificador
	'''identList : ID'''
	print ("identList 1")

def p_identList2(p): #varios identificadores
	'''identList : identList ID'''
	print ("identList 2") 

def p_procDecl1(p): #Deeclaracion de un proceso
	'''procDecl : procDecl PROCEDURE ID  module '''
	print ("procDecl 1")

def p_procDeclEmpty(p): #Proceso vacio
	'''procDecl : empty'''
	print ("nulo")

def p_statement1(p): #Estados
	'''statement : ID UPDATE expression'''
	print ("statement 1")

def p_statement2(p):#Estados
	'''statement : ID'''
	print ("statement 2")

def p_statement3(p):#Estados
	'''statement : BEGIN statementList END'''
	print ("statement 3")

def p_statement4(p):#Estados
	'''statement : condition'''
	print ("statement 4")

def p_statement5(p):#Estados
	'statement : IMPORTS ID'
	print ("statement 5")

def p_statement6(p):#Estados
	'''statement : WHILE'''
	print ("statement 6")

def p_statement7(p):#Estados
	'''statement : MODULE PROGRAM'''
	print ("statement 7")

def p_statementEmpty(p):#Estados
	'''statement : empty'''
	print ("StateEmpty")

def p_statementList1(p):#Estados
	'''statementList : statement'''
	print ("statementList 1")

def p_statementList2(p):#Estados
	'''statementList : statementList statement'''
	print ("statementList 2")

def p_condition1(p): #Condiciones
	'''condition : expression'''
	print ("condition 1")

def p_condition2(p):#Condiciones
	'''condition : expression relation expression'''
	print ("condition 2")

def p_relation1(p): #Igual
	'''relation : IGUAL'''
	print ("relation 1")

def p_relation2(p): #Igual 
	'''relation : NOIGUAL'''
	print ("relation 2")

def p_relation3(p): #Menor Que
	'''relation : MENORQ'''
	print ("relation 3")

def p_relation4(p): #Mayor Que
	'''relation : MAYORQ'''
	print ("relation 4")

def p_relation5(p): #Verdadero
	'''relation : TRUE'''
	print ("relation 5")

def p_relation6(p): #Flaso
	'''relation : FALSE'''
	print ("relation 6")

def p_expression1(p): #Expreciones
	'''expression : term'''
	print ("expresion 1")

def p_expression2(p): #Expreciones
	'''expression : addingOperator term'''
	print ("expresion 2")

def p_expression3(p):#Expreciones
	'''expression : expression addingOperator term'''
	print ("expresion 3")

def p_expression4(p):#Expreciones
	'''expression : DATETIME PUNTO NOW'''
	print ("expresion 4")

def p_expression5(p):#Expreciones
	'''expression : LLIZQ ID LLDER'''
	print ("expresion 5")

def p_expression6(p):#Expreciones
	'''expression : VBCRLF'''
	print ("expresion 5")
#vbCrLf

def p_expression7(p):#Expreciones
	'''expression : MODULE PROGRAM'''
	print ("expresion 7")

def p_expression8(p):#Expreciones
	'''expression : END MODULE'''
	print ("EndMod")

def p_expression9(p):#Expreciones
	'''expression : CONSOLE PUNTO READKEY PIZQ boolean PDER'''
	print ("expresion 8")

def p_expression10(p):#Expreciones
	'''expression : DIM ID IGUAL CONSOLE PUNTO READLINE PIZQ PDER'''
	print ("expresion 9")

def p_expression11(p):#Expreciones
	'''expression : CONSOLE PUNTO WRITELINE PIZQ ID PDER'''
	print ("expresion 10")

def p_expression12(p):#Expreciones
	'''expression : END SUB'''
	print ("expresion 12 SUBend")

#def p_expression13(p):
#	'''expression : DIM NUMERO AS ID IGUAL ID'''
#	print ("expresion DIM")

def p_addingOperator1(p): #Suma
	'''addingOperator : SUMA'''
	print ("addingOperator 1 ")

def p_addingOperator2(p): #Resta
	'''addingOperator : RESTA'''
	print ("addingOperator 2")

def p_addingOperator3(p): #mod
	'''addingOperator : MOD'''
	print ("addingOperator 3")

def p_term1(p): #Terminos
	'''term : factor'''
	print ("term 1")

def p_term2(p):#Terminos
	'''term : term multiplyingOperator factor'''
	print ("term 2")

def p_multiplyingOperator1(p): #multiplicacion
	'''multiplyingOperator : MULTI'''
	print ("multiplyingOperator 1")

def p_multiplyingOperator2(p): #divicion
	'''multiplyingOperator : DIV'''
	print ("multiplyingOperator 2")

def p_factor1(p): #Id en un factor
	'''factor : ID'''
	print ("factor 1")

def p_factor2(p): #numero en un factor
	'''factor : NUMERO'''
	print ("factor 2")

def p_factor3(p): #Factor con una exprecion
	'''factor : PIZQ expression PDER'''
	print ("factor 3")

#def p_readline(p):
#    'readline : CONSOLE PUNTO READLINE PIZQ id PDER'

def p_boolean(p): #booleano 
	'boolean : BOOLEAN'

def p_empty(p): #vacio
	'''empty :'''
	pass

def p_error(p): #error
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio): #buscador de ficheros 
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files: #buscador de archivos
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ') #Archivos encontrados
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1]) #archivo sleccionado

	return files[int(numArchivo)-1]

#ruta qen la cual se buscara los archivos
direccion ='C:/Users/Marco/Documents/test/'
#direccion = 'C:/Users/Marco/OneDrive/Documentos/ITSVA/5°Semestre/LENGUAJES Y AUTOMATAS/Tema4/EjerciciosSintactico/Analizador/VisualBasic/pruebas/'
#direccion = 'C:/Users/Marco/OneDrive/Documentos/ITSVA/5°Semestre/LENGUAJES Y AUTOMATAS/Tema4/EjerciciosSintactico/Analizador/VisualBasic/pruebas'
archivi = buscarFicheros(direccion)
prueba = direccion+archivi
fp = codecs.open(prueba, "r", "utf-8") #abrimos el archivo seleccionado 
cadena = fp.read() #guardamos la lectura
fp.close() #cerramos la lectura

parser = yacc.yacc() #usamos el yacc en el parcer
result = parser.parse(cadena) #usamos parse en la cadena donde se encuentra lo leido en el archvo

print (result) #imprecion

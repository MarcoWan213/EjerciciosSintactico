import ply.yacc as yacc
import os
import codecs
import re
from analizador import tokens
from sys import stdin

precedence = (
	('right','ID','MODULE','NUMERO'),
	#('right','PROCEDURE'),
	#('right','VAR'),
	('right','IGUAL'),
	('right','UPDATE'),
    #('right','ARGS'),
	('right','NUMERO'),
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

#def p_module(p):
#	'module : import'	

def p_args(p):
    'args : ARGS'

def p_readline(p):
    'readline : CONSOLE PUNTO WRITELINE PIZQ ID PDER'

def p_boolean(p):
	'boolean : BOOLEAN'


def p_import(p):
	#'''block : constDecl varDecl procDecl statement'''
	'import : IMPORTS "(" ident ")" ";" statement'
    #print "block"	

def p_main(p):
	'main : SUB MAIN PIZQ ARGS AS STRING PIZQ PDER PDER'
#Sub Main(args As String())

def p_constDecl(p):
	'''constDecl : DIM id IGUAL id'''
	#p[0] = constDecl(p[2])
	#print "constDecl"

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	#p[0] = Null()
	#print "nulo"

def p_constAssignmentList1(p):
	'''constAssignmentList : ID IGUAL NUMERO'''
	#print "constAssignmentList 1"

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList ID IGUAL NUMERO'''
	#print "constAssignmentList 2"

def p_varDecl1(p):
	'''varDecl : DIM identList'''
	#print "varDecl 1"

def p_varDeclEmpty(p):
	'''varDecl : empty'''
	#print "nulo"

def p_identList1(p):
	'''identList : ID'''
	#print "identList 1"

def p_identList2(p):
	'''identList : identList COMMA ID'''
	#print "identList 2"

def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID  block '''
	#print "procDecl 1"

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	#print "nulo"

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	#print "statement 1"

def p_statement2(p):
	'''statement : ID'''
	#print "statement 2"

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	#print "statement 3"

#def p_statement4(p):
	#'''statement : IF condition THEN statement'''
	#print "statement 4"

#def p_statement5(p):
#	'''statement : WHILE condition DO statement'''
	#print "statement 5"

def p_statementEmpty(p):
	'''statement : empty'''
	#print "nulo"

def p_statementList1(p):
	'''statementList : statement'''
	#print "statementList 1"

def p_statementList2(p):
	'''statementList : statementList statement'''
	#print "statementList 2"

def p_condition1(p):
	'''condition : expression'''
	#print "condition 1"

def p_condition2(p):
	'''condition : expression relation expression'''
	#print "condition 2"

def p_relation1(p):
	'''relation : IGUAL'''
	#print "relation 1"

def p_relation2(p):
	'''relation : NOIGUAL'''
	#print "relation 2"

def p_relation3(p):
	'''relation : MENORQ'''
	#print "relation 3"

def p_relation4(p):
	'''relation : MAYORQ'''
	#print "relation 4"

def p_relation5(p):
	'''relation : TRUE'''
	#print "relation 5"

def p_relation6(p):
	'''relation : FALSE'''
	#print "relation 6"

def p_expression1(p):
	'''expression : term'''
	#print "expresion 1"

def p_expression2(p):
	'''expression : addingOperator term'''
	#print "expresion 2"

def p_expression3(p):
	'''expression : expression addingOperator term'''
	#print "expresion 3"

def p_expression4(p):
	'''expression : DATETIME PUNTO NOW'''

def p_expression5(p):
	'''expression : LLIZQ ID LLDER'''

def p_expression6(p):
	'''expression : VBCRLF'''
#vbCrLf

def p_expression7(p):
	'''expression : MODULE PROGRAM'''

def p_expression8(p):
	'''expression : END MODULE'''

def p_expression9(p):
	'''expression : CONSOLE PUNTO READKEY PIZQ relation PDER'''

def p_expression10(p):
	'''expression : DIM id IGUAL CONSOLE PUNTO READLINE PIZQ PDER'''

def p_addingOperator1(p):
	'''addingOperator : SUMA'''
	#print "addingOperator 1"

def p_addingOperator2(p):
	'''addingOperator : RESTA'''
	#print "addingOperator 1"

def p_addingOperator3(p):
	'''addingOperator : MOD'''

def p_term1(p):
	'''term : factor'''
	#print "term 1"

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	#print "term 1"

def p_multiplyingOperator1(p):
	'''multiplyingOperator : MULTI'''
	#print "multiplyingOperator 1"

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIV'''
	#print "multiplyingOperator 2"

def p_factor1(p):
	'''factor : ID'''
	#print "factor 1"

def p_factor2(p):
	'''factor : NUMERO'''
	#print "factor 1"

def p_factor3(p):
	'''factor : PIZ expression PDER'''
	#print "factor 1"

def p_empty(p):
	'''empty :'''
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

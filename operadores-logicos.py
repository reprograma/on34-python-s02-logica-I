#operador AND
and_operador = True and True 
print(and_operador)

and_operador = True and False
print(and_operador)

and_operador = False and False 
print(and_operador)

and_operador = (12 == 12) and (True)
print(and_operador) 

and_operador = (13%2 == 0) and (True) and (44>23)
print(and_operador)


#operadores OR
or_operador = True or True
print(or_operador)

or_operador = True or False
print(or_operador)

or_operador = False or False
print(or_operador)

#operador NOT
print(not True)
print(not False)

not_operador = (True and False) or (not (True and True))
#false OR False
print(not_operador)

not_operador = (True and False) or (not (True and True))
#false OR not(False
print(not_operador)


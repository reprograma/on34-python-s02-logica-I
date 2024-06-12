# operador AND
and_operador = True and True
print(and_operador)

and_operador = True and False
print(and_operador)

and_operador = False and False
print(and_operador)

and_operador = (12 == 12) and (True)
print(and_operador)

and_operador = (13%2==0) and (True) and (44>23)
print(and_operador)

# operador OR
or_operador = True or True
print(or_operador)

or_operador = True or False
print(or_operador)

or_operador = False or False
print(or_operador)

and_operador = (12 == 12) or (True)
print(and_operador)

and_operador = (13%2==0) or (True) or (44>23)
print(and_operador)

and_operador = (13%2==0) or (False) or (44<23)
print(and_operador)

# operador NOT
print(not True)
print(not False)

not_operador = (True and False) or (not (True and True))
# (True and False) or (not (True and True))
# False or (not (True and True))
# False or (not True)
# False or False
# False
print(not_operador)
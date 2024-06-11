
print (" calculadora maneira")
print ("Como usar a calculadora ? ")
print ( "conta de adição = + ")
print ( "conta de multi = * ")
print ( "conta de expoente = ** ")
print ( "conta de subtra = - ")
print ( "conta de divisão = / ")


valor_1 = int (input("insira um número:"))
valor_2 = int (input("insira um número:"))
operador_conta = input("insira o operador da conta:")

def par_impar(numero):
 if numero % 2 == 0:
 
  return "par"
 else:
  return "ímpar"
numero = valor_1 + valor_2
resultado = par_impar


# soma
if operador_conta == '+': 
 numero = valor_1 + valor_2
 print (valor_1 + valor_2 )
 resultado = par_impar (numero)
 print (f" o número {numero} é {resultado}")


# multi
if operador_conta == '*':
 numero_1 = valor_1 * valor_2
 print (valor_1 * valor_2 )
 resultado = par_impar (numero)
 print (f" o número {numero_1} é {resultado}")


# divisão
if operador_conta == '/':
 numero_2 = valor_1 / valor_2
 print (valor_1 / valor_2 )
 resultado = par_impar (numero)
 print (f" o número {numero_2} é {resultado}")



# subtração
if operador_conta == '-':
 numero_3 = valor_1 - valor_2
 print (valor_1 - valor_2 )
 resultado = par_impar (numero)
 print (f" o número {numero_3} é {resultado}")


# expoente 
if operador_conta == '**': 
 numero_4 = valor_1 ** valor_2
 print (valor_1 ** valor_2 )
 resultado = par_impar (numero)
 print (f" o número {numero_4} é {resultado}")



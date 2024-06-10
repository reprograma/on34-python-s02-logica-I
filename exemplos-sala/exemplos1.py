'''
Exercícios
'''

# Numérico - int e float

numero1 = 1

print(numero1)
print("O tipo de variavel numero1 é: ", type(numero1))

numero2 = 7.4
print(numero2)
print("O tipo de variavel numero2 é: ", type(numero2))

numero3 = 400
print(numero3)
print("O tipo de variavel numero3 é: ", type(numero3))

numero3 = numero1+numero2
print(numero3)
print("O tipo de variavel numero3 é: ", type(numero3))

# Booleano
trouxe_carteira = False
print("O tipo de variável trouxe_carteira é: ", type(trouxe_carteira))

# String
# texto = "valor do texto em aspas duplas"
# texto = 'valor do texto em aspas simples'
# texto = '''valor do texto com três aspas simples'''
# texto = """valor do texto com três aspas duplas"""

# "Na madrugada abandonada", PERLLA
texto = '"Na madrugada, abandonada, cê não atende o celulaaaar", PERLLA'
print(texto)
print("O tipo de variável texto é: ", type(texto))

# Inputs
entrada = input("Digite um texto: ")
print("O valor do Input é: ", entrada)

# Nome das variáveis - regrinhas
exemplo12345 = True # Apenas nomes e números, começar por uma letra
# Sem acentos gráficos
endereco_residencia = "Rua X, 345" # podemos ter underlines
endereco_trabalho = "Avenida Berimboca, 297" # Sempre dar nomes coerentes :) 

entrada1 = input("Informe o primeiro valor: ")
entrada2 = input("Informe o segundo valor: ")

print(type(entrada1))
print(type(entrada2))
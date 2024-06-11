#Int e Float

numero1 = 1

print(numero1)
print("O tipo de variável do número1 é: ", type(numero1))

numero2 = 7.4

print(numero2)
print("O tipo de variável do número2 é: ", type(numero2))

soma = numero1 + numero2
print(soma)
print("O tipo de variável da soma é: ", type(soma))

# Booleano

trouxe_carteira = False
print("O tipo de variável trouxe_carteira é:", type(trouxe_carteira))

#String
texto = "valor texto"
print(texto)
print("O tipo de variável texto é:", type(texto))

#Inputs
entrada = input("Digite um texto: ")
print("O valor do input é: ", entrada)

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(nome, ", idade: ", idade)

entrada1 = input("Informe o primeiro valor:")
entrada2 = input("Informe o segundo valor: ")

print(type(entrada1))
print(type(entrada2))

concat = entrada1 + entrada2
print("valor da variável", concat)
print("o tipo de concat", type(concat))
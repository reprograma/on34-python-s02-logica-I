"""
Este arquivo será onde veremos os exemplos em sala!
"""
print('Bonjour le monde')
print(type(3*3))


numero1=2
print(numero1)
print("O tipo da variável numero1 é: ", type(numero1))

numero2 = 7.4
print(numero2)
print("O tipo de variável numero2 é: ", type(numero2))

numero3 = 400
print("O tipo de variável numero3 é: ", type(numero3))

numero3 = numero1+numero2
print(numero3)
print("O tipo de variável numero3 é: ", type(numero3))

#Booleano
trouxe_carteira = False
print("O tipo de variável trouxe_carteira é: ", type(trouxe_carteira))

#String
texto = "valor do texto"
print(texto)
print("O tipo de variável texto é: ", type(texto))

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(nome, ", ""idade: ", idade)

exemplo= True

entrada1= input("Informe o primeiro valor: ")
entrada2= input("Informe o segundo valor: ")

concat = entrada1+entrada2
print("valor da variável", concat)
print("tipo do concat:", type(concat))

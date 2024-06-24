print("Olá Mundo")
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10%5)
print(10**5)

'''
O que acontece se coloco print (3*3)
'''
#Tipo Numerico: int e  float
print (3*3)
print (type(3.9))

numero1 = 1
print(numero1)
print("O tipo de variavel do número é:",type(numero1))

numero2 = 7.4
print(numero2)
print("O tipo de variavel do número é:",type(numero2))

numero3 = 400
print(numero3)
print("O tipoe de variavel do número é:", type(numero3))

numero3 = numero1 + numero2
print(numero3)
print("O tipo de variavel do número é:", type(numero3))

#Tipo Booleano: False ou True

trouxe_carteira = False
print("O tipo de variavel de trouxe_carteira é:", type(trouxe_carteira))

#String: Texto (str)

texto = "valor-do-texto"
print(texto)
print("O tipo de váriavel texto é:", type(texto))

#Input () - é uma entrada
entrada = input("Digite um texto:")
print("O valor do input é:", entrada)

Nome = input("Digite seu nome:")
Idade = input("Digite sua idade:")
print(type(Nome), ", idade:", type(Idade))

Entrada1 = input("informe o primeiro valor:")
Entrada2 = input("informa o primeiro valor:")

print(type(entrada1))
print(type(entrada2))

concat = entrada1+entrada2
print("valor da variavel:", type(concat))
print("tipo do concat:", type(concat))

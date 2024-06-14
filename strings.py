# nome = "Carla"
# sobrenome = "dos Santos"

# print(nome+" "+sobrenome)

# conteudo = "Minha data de nascimento é " + str(2002)
# print(conteudo)

# entrada = input("Escreva seu nome: ")
# print("Ola meu nome é",entrada)

# conteudo = "Minha data de nascimento é " + str(2002)
# print(conteudo)

# salario = input('Digite o seu salario: ')
# salario = int(salario)
# salario_ano = salario*12
# print(salario_ano)

# valor = 5
# print(float(valor))

# print(bool(0))
# print(bool(1))
# print(bool("conteudo"))
# print(bool(""))

#Exercício01

# usuário dois numeros
# voce retorna:
# soma, multiplicação, potenciação

entrada01 = input("Digite dois o primeiro numero: ")
entrada02 = input ("Digite o segundo numero: ")

num01 = float(entrada01)
num02 = float(entrada02)

soma = (num01)+(num02)
print(soma)

multiplicação = (num01)*(num02)
print(multiplicação)

pot = (num01)**(num02)
print(pot)

#Exercício
    #usuario digita um valor
    #voce retorna se um numero é par ou impar

var01 = float(input("Digite um numero: "))

if var01 % 2 == 0:
    print("O numero digitado é par")
else:
    print("O numero digitado é ímpar")
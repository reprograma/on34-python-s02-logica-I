nome = "Carla"
sobrenome = "dos Santos"

print(nome+" "+sobrenome)


conteudo = "Meu ano de nascimento é " + str(1996) # converte para string
print(conteudo)

ano_nascimento = 1996
idade = 2024 - ano_nascimento
print("minha idade é: " + str(idade))

# salario = input('Digite o seu salário: ')
# salario = int(salario)
# salario_ano = salario*12
# print(salario_ano)

valor = 5
print(float(valor))

print(bool(0)) # False
print(bool(1)) # True
print(bool("conteudo")) # True
print(bool("")) # False
print(bool(-200)) # True

'''
Exercício
'''
# PRIMEIRO
# usuário digita dois números
# você retorna:
# soma, multiplicação, potenciação

# maneira de resolver

# valor1 = input("Digite o valor1: ")
# valor2 = input("Digite o valor2: ")
# valor1 = int(valor1)
# # valor2 = int(valor2)

# valor1 = float(input("Digite o primeiro numero: "))
# valor2 = float(input("Digite o primeiro numero: "))

# soma = valor1 + valor2
# # print("O resultado da soma é:", soma)

# multiplicacao = valor1 * valor2
# # print("O resultado da multiplicação é:", multiplicacao)

# potenciacao = valor1 * valor2
# # print("O resultado da potenciação é:", potenciacao)

# # outra maneira de resolver
# print("O resultado da soma é", soma, "\nO resultado da multiplicação é", multiplicacao, "\nO resultado da potenciação é", potenciacao) # \n é a quebra de linha

# SEGUNDO
# usuário digita um valor
# você retorna se um número é par ou ímpar
numero = int(input("Digite um número: ")) # pego a entrada, convertendo já

eh_impar = numero%2 # pego o resto da divisão por 2; se for par, o resto da divisão é 0; se for ímpar, o resto é 1.
eh_impar = bool(eh_impar) # retornará True se tiver 1 e False se tiver 0
print("O número", numero,"é ímpar?", eh_impar) # Printando se o número é impar (True) ou não (False)

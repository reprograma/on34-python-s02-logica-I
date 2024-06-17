input("Vamos fazer algumas operaçãoes matemáticas? Click Enter pra começar! ")

'''soma'''

numero1 = int(input(" Digite um número da sua escolha! "))
numero2 = int(input(" Digite outro número da sua escolha! "))

soma = numero1 + numero2
print(" A soma de ", numero1, "e ", numero2, "é igual a ", soma)

eh_impar = soma%2
print("O resultado ", soma, "é ímpar?", bool(eh_impar))

input("Muito bem, vamos continuar? Click Enter pra continuar! ")

'''subtração'''

numero1 = int(input(" Digite um número da sua escolha! "))
numero2 = int(input(" Digite outro número da sua escolha! "))

subtracao = numero1 - numero2
print(" A subtração de ", numero1, "e ", numero2, "é igual a ", subtracao)

eh_impar = subtracao%2
print("O resultado ", subtracao, "é ímpar?", bool(eh_impar))

input("Ainda podemos fazer muitas operações, Deseja continuar? Click Enter pra continuar! ")

'''multiplicação'''


numero1 = int(input(" Digite um número da sua escolha! "))
numero2 = int(input(" Digite outro número da sua escolha! "))

multiplicacao = numero1 * numero2
print(" A multiplicação de ", numero1, "e ", numero2, "é igual a ", multiplicacao)

eh_impar = multiplicacao%2
print("O resultado ", multiplicacao, "é ímpar?", bool(eh_impar))

input("As operações estão ficando mais difíceis, Deseja continuar? Click Enter pra continuar! ")

'''Divisão'''


numero1 = float(input(" Digite um número da sua escolha! "))
numero2 = float(input(" Digite outro número da sua escolha! "))

divisao = numero1 / numero2
print(" A divisão de ", numero1, "e ", numero2, "é igual a ", divisao)

eh_impar = divisao%2
print("O resultado ", divisao, "é ímpar?", bool(eh_impar))

input("Vamos agora ver a potenciação dos números? Deseja continuar? Click Enter pra continuar! ")

'''Potenciação'''

numero1 = int(input(" Digite um número da sua escolha! "))
numero2 = int(input(" Digite outro número da sua escolha! "))

potencia = numero1 ** numero2
print(" A potenciação de ", numero1, "elevado a  ", numero2, "é igual a ", potencia)

eh_impar = potencia%2
print("O resultado ", potencia, "é ímpar?", bool(eh_impar))

print("Agora chegamos ao fim das nossas operações! Se quiser continuar sua calculadora comece o processo novamente! ")



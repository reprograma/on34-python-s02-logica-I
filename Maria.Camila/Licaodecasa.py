#Calculadora : somar, subtrair, multiplicar, dividir e potenciação
def e_par(resultado):
    return resultado % 2 == 0

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))

soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2
potenciacao = numero1**numero2

print("O resultado da sua soma é", soma)
if not e_par(soma):
    print("O seu número é IMPAR")
print("O resultado da sua subtração é:", subtracao)
if not e_par(subtracao):
    print("O seu número é IMPAR")
print("O resultado da sua multiplicação é", multiplicacao)
if not e_par(multiplicacao):
    print("O seu número é IMPAR")
print("O resultado da sua divisão é:", divisao)
if not e_par(divisao):
    print("O seu número é IMPAR")
print("O resultado da sua potenciação é:", potenciacao)
if not e_par(potenciacao):
    print("O seu número é IMPAR")






    





































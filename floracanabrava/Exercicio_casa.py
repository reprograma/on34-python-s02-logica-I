# Exercício Casa Semana 02 - Calculadora com Funções

print("Olá!", "\nAqui você poderá fazer seus cálculos de maneira simples e rápida.", "\nPara isso insira nos espaços abaixo os dois números que você deseja calcular!")

def par_ou_impar(numero):
    if ((numero%2) == 0):
       print("O número é par")
    else:
        print("O número é ímpar") 

def somar(x, y):
    somar = (x+y)
    return somar 

def subtrair(x, y):
    subtrair = (x-y)
    return subtrair

def multiplicar(x, y):
    multiplicar = (x * y)
    return multiplicar

def dividir(x, y):
    dividir = (x / y)
    return dividir

def potenciação(x, y):
    potenciação = (x**y)
    return potenciação
    

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

print("Muito bem! Agora informe abaixo se deseja somar, subtrair, multiplicar, dividir ou potenciação")
funcao = input("Informe a função desejada: ")

if funcao == "somar":
    print("Ótimo! Aqui está o resultado: ", somar(numero1, numero2))
    par_ou_impar(somar(numero1, numero2))

elif funcao == "subtrair":
    print("Ótimo! Aqui está o resultado: ", subtrair(numero1, numero2))
    par_ou_impar(subtrair(numero1, numero2))
   
elif funcao == "multiplicar":
    print("Ótimo! Aqui está o resultado: ", multiplicar(numero1, numero2))
    par_ou_impar(multiplicar(numero1, numero2))
   
elif funcao == "dividir":
    print("Ótimo! Aqui está o resultado: ", dividir(numero1, numero2))
    par_ou_impar(dividir(numero1, numero2))
   
elif funcao == "potenciação":
     print("Ótimo! Aqui está o resultado: ", potenciação(numero1, numero2))
     par_ou_impar(potenciação(numero1, numero2))

else:
    print("Não entendi! Você deve digitar uma das opções abaixo:", "\nsomar", "\nsubtrair", "\nmultiplicar", "\ndividir", "\npotenciação")
     



def calcular():
    num1=int(input("Digite o primeiro número:"))
    num2=int(input("Digite o segundo número:"))

    somar=num1+num2
    subtrair=num1-num2
    multiplicar=num1*num2
    dividir=num1/num2
    potenciaçao=num1**num2
    if somar%2==1: 
        print("o resultado da soma é impar") 
    else:
      print("o resultado da soma não é impar")
    if subtrair%2==1:
     print("o resultado da subtração é impar")  
    else:
        print("o resultado da subtração não é impar") 
    if multiplicar%2==1:
        print("o resultado da multiplicação é impar")   
    else:
        print("o resultado da multiplicação não é impar")
    if dividir%2==1:
        print("o resultado da divisão é impar")
    else:
        print("o resultado da divisão não é impar") 
    if potenciaçao%2==1: 
        print("o resultado da potencição é impar") 
    else:
     print("o resultado da potenciação não é impar")      
   
    return somar,subtrair,multiplicar,dividir, potenciaçao
print(calcular())


  

  
  







valor1 = input("Digite o primeiro número: ")
valor2 = input("Digite o segundo número: ")

valor1 = int(valor1)
valor2 = int(valor2)

# Somar: recebe dois números e retorna a soma.
soma = valor1 + valor2
print("O resultado da Soma é: ", soma)
numero_sendo_impar = soma%2 
numero_sendo_impar = bool(numero_sendo_impar) 
print("O resultado da soma", soma, "é impar?", numero_sendo_impar) 


# subtrair: recebe dois números e retorna a subtração.
Subtração = valor1 - valor2
print("O resultado da Subtração é: ", Subtração)
numero_sendo_impar = Subtração%2 
numero_sendo_impar = bool(numero_sendo_impar) 
print("O resultado da subtração", soma, "é impar?", numero_sendo_impar) 

# multiplicar: recebe dois números e retorna a multiplicação.
multiplicação =  valor1 * valor2
print("O resultado da Multiplicação é: ", multiplicação)
numero_sendo_impar = multiplicação%2 
numero_sendo_impar = bool(numero_sendo_impar) 
print("O resultado da Multiplicação", soma, "é impar?", numero_sendo_impar) 

# dividir: recebe dois números e retorna a divisão do primeiro pelo segundo
Divisão = valor1/valor2
print("O resultado da Divisão é: ", Divisão)
numero_sendo_impar = Divisão%2 
numero_sendo_impar = bool(numero_sendo_impar) 
print("O resultado da Divisão", soma, "é impar?", numero_sendo_impar) 

# potenciação:
potenciação = valor1**valor2
print("O resultado da Potenciação é: ", potenciação)
numero_sendo_impar = potenciação%2 
numero_sendo_impar = bool(numero_sendo_impar) 
print("O resultado da potenciação", soma, "é impar?", numero_sendo_impar) 





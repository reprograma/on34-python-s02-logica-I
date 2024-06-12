
# Exercício Calculadora

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

# Soma
soma = n1 + n2
print("O resultado da soma é: ", soma)

eh_impar = soma % 2 
eh_impar = bool(eh_impar) 
print("O número", soma,"é ímpar?", eh_impar)

# Subtração
subtracao = n1 - n2
print("O resultado da subtração é: ", subtracao)

eh_impar = subtracao % 2 
eh_impar = bool(eh_impar) 
print("O número", subtracao,"é ímpar?", eh_impar)

# Multiplicação
multiplicacao = n1 * n2
print("O resultado da multiplicação é:", multiplicacao)

eh_impar = multiplicacao % 2 
eh_impar = bool(eh_impar) 
print("O número", multiplicacao,"é ímpar?", eh_impar)

# Divisão
divisao = n1 / n2
print(f"O resultado da divisão é: {divisao:.2f}")

eh_impar = divisao % 2 
eh_impar = bool(eh_impar) 
print(f"O número {divisao:.2f}","é ímpar?", eh_impar)

# Potenciação
potenciacao = n1 ** n2
print("O resultado da potenciação é: ", potenciacao)

eh_impar = potenciacao % 2 
eh_impar = bool(eh_impar) 
print("O número", potenciacao,"é ímpar?", eh_impar)

# Divisão Inteira
divisao_inteira = n1 // n2
print("O resultado da divisão inteira é: ", divisao_inteira)

eh_impar = divisao_inteira % 2 
eh_impar = bool(eh_impar) 
print("O número", divisao_inteira,"é ímpar?", eh_impar)





    

    


    

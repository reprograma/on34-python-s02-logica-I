#Convertendo para string

nome ="Williane"
sobrenome = "Fernandes"
conteudo = "Meu ano de nascimento é" + str(1999)

print(nome + " " + sobrenome + ", " + conteudo)


salario = input("Digite o seu salario: ")
salario = int(salario)
salario_ano = salario*12
print(salario_ano)

print(bool(0)) #false
print(bool(1)) #true
print(bool("conteudo")) #true
print(bool("")) #false

#exercicio

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("O valor da soma é: " + str((numero1+numero2)))
print("O valor da multiplicação é: " + str((numero1*numero2)))
print("O valor da potenciação é: " + str((numero1**numero2)))

if numero1 % 2 > 0: 
    print("O número 1 é ímpar")
else: 
    print("O número 1 é par")

if numero2 % 2 > 0: 
    print("O número 2 é ímpar")
else: 
    print("O número 2 é par")
    

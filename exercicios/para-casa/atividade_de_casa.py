print("Boa tarde! Por gentileza, digite um número:")
x = int(input())
print("Agora, por favor, digite outro número:")
y = int(input())

print("Vamos às operações?")

#somar (x,y): recebe dois números e retorna a soma
soma = (x+y)
impar_ou_par = (soma%2)
print("A soma dos números digitados é", soma)
print("O resultado da soma é impar?", bool(impar_ou_par))

#subtrair (x,y): recebe dois números e retorna a subtração
subtracao = (x-y)
impar_ou_par2 = (subtracao%2)
print("A subtração dos números digitados é:", subtracao)
print("O resultado da subtração é impar?", bool(impar_ou_par2))

#multiplicar (x,y): recebe dois números e retorna a multiplicação
multiplicacao = (x*y)
impar_ou_par3 = (multiplicacao%2)
print("A multiplicação dos números digitados é:", multiplicacao)
print("O resultado da multiplicação é impar?", bool(impar_ou_par3))

#dividir (x,y): recebe dois números e retorna a divisão
divisao = (x//y)
impar_ou_par4 = (divisao%2)
print("A divisão dos números digitados é:", divisao)
print("O resultado da divisão é impar?", bool(impar_ou_par4))

#potenciação (x,y): recebe os dois números e retorna a potenciação
potenciacao = (x**y)
impar_ou_par5 = (potenciacao%2)
print("A potenciação dos números digitados é:", potenciacao)
print("O resultado da potenciação é impar ou par?", bool(impar_ou_par5))
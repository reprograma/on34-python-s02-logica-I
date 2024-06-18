'''print('Olá, Mundão! :)')
print(3*3)
print(type(4.1))

# Bool
trouxe_carteira = False
print('O tipo de variável da var trouxe_carteira é: ', type(trouxe_carteira))

# String
texto = 'O valor do texto'
print('O tipo da var texto é: ', type(texto))

# Input

nome = str(input('Qual é o seu nome? '))
print('Muito prazer te conhecer,', nome)'''

num1 = float(input('Digite um número para mim: '))
num2 = float(input('Digite mais um número para mim: '))
soma = num1 + num2
multi = num1 * num2
potenciacao = num1 ** num2

print('Muito bom, a SOMA do {} e {} é: {}\n'.format(num1, num2, soma))
print('A MULTIPLICAÇÃO de {} e {} é: {}\n'.format(num1, num2, multi))
print('A POTENCIAÇÃO de {} elevado a {} é: {}\n'.format(num1, num2, potenciacao))
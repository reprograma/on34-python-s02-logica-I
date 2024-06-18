print('-='*25)
print('              Boas Vindas!')
print('             Vamos Calcular? 👩‍💻')
print('-='*25)

# Usuário deve digitar 2 números

num1 = float(input('Digite seu primeiro número: '))
num2 = float(input('Digite seu segundo número: '))

# Variáveis para a calculadora

soma = num1 + num2
subtracao = num1 - num2
multip = num1 * num2
divisao = num1 / num2
divisao_resto = num1 % num2
divisao_int = num1 // num2
potenciacao = num1 ** num2

print('\nMuito bem, vamos ver os Operadores Aritméticos dos números escolhidos:\n')

print('-='*25)
print('\nSOMA de {} e {} = {}'.format(num1, num2, soma))
print('\nSUBTRAÇÃO de {} e {} = {}: '.format(num1, num2, subtracao))
print('\nMULTIPLICAÇÃO de {} e {} = '.format(num1, num2, multip))
print('\nDIVISÃO de {} e {} = {}'.format(num1, num2, divisao))
print('\nRESTO DA DIVISÃO de {} e {} = {}'.format(num1, num2, divisao_resto))
print('\nDIVISÃO INTEIRA de {} e {} = {}'.format(num1, num2, divisao_int))
print('\nPOTENCIAÇÃO de {} e {} = {}'.format(num1, num2, potenciacao))
print('-='*25)

print('Agradecemos sua participação! 😀')

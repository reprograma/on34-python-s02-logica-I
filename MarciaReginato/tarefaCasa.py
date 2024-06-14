x = int(input('Digite um valor: '))
impar = x%2
print("o numero", x, "é impar?", bool(impar))
y = int(input('Digite outro valor: '))
impar = y%2
print("o numero", y, "é impar?", bool(impar))

soma = x + y
print("Os valores digitados, somados entre si: ", soma)
impar = soma%2
print("o numero", soma, "é impar?", bool(impar))

subtracao = x - y
print("Os valores digitados, subtraídos entre si: ", subtracao)
impar = subtracao%2
print("o numero", subtracao, "é impar?", bool(impar))

multiplicacao = x * y
print("Os valores digitados, multiplicados entre si: ", multiplicacao)
impar = multiplicacao%2
print("o numero", multiplicacao, "é impar?", bool(impar))

divisao = x / y
print("Os valores digitados, divididos entre si: ", divisao)
impar = divisao%2
print("o numero", divisao, "é impar?", bool(impar))

potenciacao = x ** y
print("Os valores digitados, na potência entre si: ", potenciacao)
impar = potenciacao%2
print("o numero", potenciacao, "é impar?", bool(impar))
print("Ola Mundo de Jennifer- Exercio Aula 2")
### Calculadora 1 /Soma com Função : 
def soma(a, b):
  return a + b

def multiplicacao(a, b):
  return a * b

def potenciacao(a, b):
  return a ** b

# Calculadora 2/ Utilizando if e Else e Par_Impar
print(f"A Soma de 15 e 8: {soma(15, 8)}")
print(f"A Multiplicação de 4 e 2: {multiplicacao(4, 2)}")
print(f"A Potenciação de 2 elevado a 3: {potenciacao(2, 3)}")

def par_ou_impar(numero):
  if numero % 2 == 0:
    return "Par"
  else:
    return "Ímpar"

numero=8
resultado = par_ou_impar(int(numero))
print(f"O número {numero} é {resultado}.")

numero=15
resultado = par_ou_impar(int(numero))
print(f"O número {numero} é {resultado}.")


### Calculadora 3/ Soma simples
print("2º Formato de resolução matemática")
##
soma=(100+50)
print(soma)
multiplicacao= (1800*3000)
print(multiplicacao)
potenciacao=(210**50)
print(potenciacao)
##
print ("Numeros(par),Numeros(impar)")
numero=2458
resultado = par_ou_impar(int(numero))
print(f"O número é :{numero} é {resultado},")
numero=10359
resultado = par_ou_impar(int(numero))
print(f"O númerio é :{numero} é {resultado}")


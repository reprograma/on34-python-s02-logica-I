def calcula_imc(peso, altura):
    imc = peso/altura**2
    return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print("Seu IMC é: ", calcula_imc(peso, altura))
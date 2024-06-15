#conversor de metros para centímetros
def conversao_altura(metro):
    centimetro = metro*1000
    print(metro, "metros equivalem a", centimetro, "centímetros")

conversao_altura(float(input("Digite, em metros, a medida que você deseja converter para centímetros:")))

#calculadora de área de círculo
def calculo_area_circulo(raio):
    area = 3.14*raio**2
    print("Um círculo de raio", raio,"possui aréa igual a", area, "metros quadrados")

calculo_area_circulo(float(input("Digite o raio do círculo para que seja calculada a sua área:")))

#calculadora de área de um terreno quadrado
def calculo_area_quadrado(base, altura):
    area2 = base*altura
    dobro_area = area2 * 2
    print("A área do terreno de base", base, "e altura", altura, "é igual a", area2,"metros quadrados")
    print("O dobro do valor dessa área equivale a", dobro_area, "metros quadrados")

base = float(input("Digite, em metros, o valor da base de um terreno para que seja calculada a sua área:"))
altura = float(input("Agora, por favor, digite o valor da altura, para que seja finalizado o cálculo:"))
calculo_area_quadrado(base, altura)

#cálculo de temperatura do local da obra - fahrenheit para celsius
def conversao_temperatura (fahrenheit):
    celsius = 5*((fahrenheit)/9) 
    print(fahrenheit,"graus fahrenheit equivalem a", celsius, "graus celsius")

conversao_temperatura(float(input("Para sabermos qual a temperatura da obra em graus celsius, solicito, por gentileza, que informe qual é a temperatura em graus fahrenheit:")))

#cálculo da temperatura do local da obra - celsius para fahrenheit
def conversao_temperatura2 (celsius):
    fahrenheit = celsius*9/5+32
    print(celsius, "graus celsius em fahrenheit equivalem a", fahrenheit, "graus fahrehnheit")

conversao_temperatura2(float(input("Para sabermos qual a temperatura da obra em graus fahrenheit, solicito, por gentileza, que informe qual é a temperatura em graus celsius:")))

#calculadora das horas de trabalho totais dos obreiros

def horas_totais_obreiros(trabalhadores):
    quantidade_trabalhadores = int(input("Por gentileza, informe quantas pessoas estão trabalhando na obra:"))
    valor_hora = float(input("Por favor, informe quanto cada um ganha por hora:"))
    horas_trabalhadas = float(input("Por último, nos informe quantas horas cada um trabalhou neste mês:"))
    salario_bruto_individual = valor_hora*horas_trabalhadas
    salario_bruto_coletivo = quantidade_trabalhadores*salario_bruto_individual
    total_trabalhadores = horas_trabalhadas*quantidade_trabalhadores
    print("No total, os obreiros trabalharam", total_trabalhadores , "horas este mês")
    print("O salário final de um obreiro foi equivalente a:", salario_bruto_individual, "reais")
    print("O custo total de salários de todos os obreiros para o mês referido foi de:", salario_bruto_coletivo, "reais")

horas_totais_obreiros(float(input("Informe quantas pessoas trabalharam na obra para saber quantas horas foram trabalhadas no total:")))

#calculadora do salário líquido de um obreiro
def salario_liquido_obreiros(horas):
    salario_bruto = valor_hora*horas
    valor_inss = salario_bruto*0.08
    valor_sindicato = (salario_bruto-valor_inss)*0.05
    salario_liquido = salario_bruto-valor_inss-valor_sindicato

    print("Salário Bruto:", salario_bruto, "reais")
    print("INSS (8%):", valor_inss, "reais")
    print("Sindicato ( 5%):", valor_sindicato, "reais")
    print("Salário Liquido:", salario_liquido, "reais")

valor_hora = (float(input("Para saber o salário líquido de um obreiro, por favor, digite quanto o mesmo ganha por hora:")))
horas = float(input("Por fim, informe quantas horas o obreiro trabalhou neste mês:"))
salario_liquido_obreiros(horas)
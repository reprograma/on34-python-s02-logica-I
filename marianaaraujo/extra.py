import math

str(input('Sistema de uma empreiteira 🚧   '))

#Conversor de metros para centímetros
def metros_x_centimetros(metro):
    centimentros = metro * 100
    return print(metro, 'metros convertido em centímetros é igual a', centimentros,'cm')
metros_x_centimetros(float(input('Digite o valor em metro: ')))

#Calculadora de área de círculo
def area_do_circulo(raio):
    area = round((math.pi * raio**2),4)
    return print('A área do círculo é de', area, 'metros')
area_do_circulo(float(input('Digite o valor do raio do círculo em metro: ')))

#Calculadora de área de um terreno quadrado
def terreno_quadrado(lado):
    area = lado**2
    return print('A área do quadrado é', area)
terreno_quadrado(float(input('Digite a altura do quadrado: ')))

#Cálculo de temperatura do local da obra - Fahrenheit para Celsius
def fahrenheit_x_celsius(f):

   c = 5 * ((f-32) / 9)
   c = int(c)
   return print('A temperatura em celsius é: {0}°c'.format(c))
fahrenheit_x_celsius(float(input('Digite a temperatura em fahrenheit: ')))

#Cálculo da temperatura do local da obra - Celsius para Fahrenheit
def celsius_x_fahrenheit(c):

   f = ((9*c)/5) + 32 
   f = int(f)
   return print('A temperatura em fahrenheit é: {0}°f'.format(f))
celsius_x_fahrenheit(float(input('Digite a temperatura em celsius: ')))

#Calculadora das horas de trabalho totais dos obreiros
trabalhadores = int(input('Insira a quantidade de trabalhadores: '))
ganho_por_hora = float(input('Insira o valor por hora trabalhada: '))
horas_trabalhadas = float(input('Insira a quantidade de horas trabalhadas: '))

def total_de_horas(horas_trabalhadas, ganho_por_hora, trabalhadores):
    salario_bruto = ganho_por_hora * horas_trabalhadas
    custo_total = salario_bruto * trabalhadores
    salario_bruto = float(salario_bruto)
    custo_total = float(custo_total)
    return print('O salário bruto de um obreiro é R$',salario_bruto, 'e o custo total de todos os', trabalhadores, 'obreiros é R$', custo_total)
total_de_horas (horas_trabalhadas, ganho_por_hora, trabalhadores)
    
#Calculadora do salário líquido de um obreiro
ganho_por_hora = float(input('Insira o valor por hora trabalhada: '))
horas_trabalhadas = float(input('Insira a quantidade de horas trabalhadas no mês: '))



def salario_liquido(ganho_por_hora, horas_trabalhadas):
    salario_bruto = ganho_por_hora * horas_trabalhadas
    a_inss = 8/100
    a_sindicato = 5/100
    if salario_bruto < 2259.20: a_imposto = 0 
    if salario_bruto > 2259.20: a_imposto = 7.5/100
    if salario_bruto < 2826.65: a_imposto = 7.5/100
    if salario_bruto > 2826.65: a_imposto = 15/100 
    if salario_bruto < 3751.05: a_imposto = 15/100
    if salario_bruto > 3751.05: a_imposto = 22.5/100
    if salario_bruto < 4664.68: a_imposto = 22.5/100
    if salario_bruto > 466468: a_imposto = 27.5/100
    inss = a_inss * salario_bruto
    sindicato = a_sindicato * salario_bruto
    imposto = a_imposto * salario_bruto
    salario_liquido = salario_bruto - inss - sindicato - imposto
    return print('Salário Bruto: R$', salario_bruto,
                 '\n - IR', '(',(a_imposto * 100),'%): R$', imposto,
                 '\n - INSS (8%):', inss,
                 '\n - Sindicato (5%): R$', sindicato,
                 '\n = Salário Líquido: R$', salario_liquido)
salario_liquido (ganho_por_hora, horas_trabalhadas)


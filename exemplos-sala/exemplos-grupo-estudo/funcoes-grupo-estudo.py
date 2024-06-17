'''
FUNÇÕES
'''

# Função: bloco de código que é REUTILIZÁVEL

'''
Exemplo 1: função que imprime Olá (sem parâmetro)
'''
# Função que imprime "Olá!"
def cumprimentar():
    print("Olá!")
#
#

cumprimentar() # chama a função que printa a saudação

'''
Exemplo 2: função COM 1 parâmetro
'''
def cumprimentar_com_nome(nome):
    print("Olá", nome, "!")

#
#

# A regra é: preciso de UM parâmetro
cumprimentar_com_nome("Márcia")
nome_aluna = "Stephanie"
cumprimentar_com_nome(nome_aluna) 
cumprimentar_com_nome(123) 
nome = "Helza"
cumprimentar_com_nome(nome)

'''
Exemplo 3: função com MAIS de 1 parâmetro
'''
def informacoes_aluna(nome, idade, cidade):
    # imprimir as informações passadas E calcula ano de nascimento da pessoa
    print("Olá,", nome, "!")
    ano_atual = 2024
    ano_nascimento = ano_atual-idade
    print("Sua idade é", idade, "e você nasceu em", ano_nascimento)
    print("Você fala de", cidade)
    # A função só vai "conhecer" o que está aqui nela

#
#
#
nome_aluna = "Luana"
idade = 51
cidade = "Rio de Janeiro RJ"
informacoes_aluna(nome_aluna, idade, cidade)
# informacoes_aluna(idade, cidade, nome_aluna) # ERRO, porque os parâmetros não estão corretos

'''
Exemplo 4: funcao SEM parâmetro e COM retorno
'''
def obter_pi():
    #
    print("calculando o pi...")
    return 3.14159 # lançar pra quem chamou a função esse valor
#
#
valor_pi = obter_pi()

'''
Exemplo 5: função COM parâmetro e COM retorno
'''
def calculo_area_quadrada(lado):
    area = lado * lado
    print("Estamos calculando sua área...")
    return area

calculo_area = calculo_area_quadrada(3)
print(calculo_area)
#
#
#
print(calculo_area(5))
print ("Bem vinda a calculadora da Samantha!")
print ("Por aqui, só trabalhamos com números inteiros, ok?")
x= int(input("Escolha um número de 0 a 10:"   ))
y= int (input("Escolha outro número de 0 a 10:"   ))

soma = x+y
print ("A soma dos seus números é:", soma)
eh_impar = soma%2
print ("O número", soma, " é ímpar?", bool( eh_impar) )

sub = x-y
print ("A subtração dos seus números é:", sub)
eh_impar1 = sub%2
print ("O número", sub, " é ímpar?", bool( eh_impar1) )

mult = x*y
print ("O valor dos números multiplicados é :", mult)
eh_impar2 = mult%2
print ("O número", mult, " é ímpar?", bool( eh_impar2) )


div = x/y
print ("O valor dos números divididos é :", div)
eh_impar3 = div%2
print ("O número", div, " é ímpar?", bool( eh_impar3) )

pot = x**y
print ("O valor de exponenciação dos números é:", pot)
eh_impar4 = pot%2
print ("O número", pot, " é ímpar?", bool( eh_impar4) )










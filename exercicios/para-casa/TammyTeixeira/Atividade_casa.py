#Pedro quer saber quantos amiguinhos tem o tenis do Sonic!

Amigos1 = float(input("A quantidade de amigos 1 com tenis é:"))
print("Amigos escola:", Amigos1)

Amigos2 = float(input("A quantidade de amigos 2 com tenis é:"))
print("Amigos rua:", Amigos2)

print(Amigos1 + Amigos2)
print(Amigos1 - Amigos2)
print(Amigos1 * Amigos2)
print(Amigos1 / Amigos2)
print(Amigos1 ** Amigos2)

Resultado_soma = float (Amigos1+Amigos2)
if(Resultado_soma %2 !=0):
   print("A quantidade de amigos com tenis sonic é ímpar")
   print(bool(Resultado_soma))
else:
    print("A quantidade de amigos com tenis sonic é par")
    print(bool(Resultado_soma))
    
Resultado_sub = float (Amigos1-Amigos2)
if(Resultado_sub %2 !=0):
   print("A quantidade de amigos com tenis sonic é ímpar!")
   print(bool(Resultado_sub))
else:
    print("A quantidade de amigos com tenis sonic é par!")
    print(bool(Resultado_sub))

Resultado_multi = float (Amigos1*Amigos2)
if(Resultado_multi %2 !=0):
   print("A quantidade de amigos com tenis sonic é ímpar!")
   print(bool(Resultado_multi))
else:
    print("A quantidade de amigos com tenis sonic é par!")
    print(bool(Resultado_multi))

Resultado_div = float (Amigos1/Amigos2)
if(Resultado_div %2 !=0):
   print("A quantidade de amigos com tenis sonic é ímpar!")
   print(bool(Resultado_div))
else:
    print("A quantidade de amigos com tenis sonic é par!")
    print(bool(Resultado_div))

Resultado_potenc = float (Amigos1**Amigos2)
if(Resultado_potenc %2 !=0):
   print(str("A quantidade de amigos com tenis sonic é ímpar"", e não par!"))
   print(bool(Resultado_potenc))
else:
    print(str("A quantidade de amigos com tenis sonic é par"", e não ímpar!"))
    print(bool(Resultado_potenc))


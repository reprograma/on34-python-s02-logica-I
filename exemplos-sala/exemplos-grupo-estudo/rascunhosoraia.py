def calculo_imc (altura, peso):
  imc = peso/(altura**2)
  print(imc)
  
  
def calculo_imc_retorno(altura, peso):
  imc = peso/(altura**2)
  return imc
  
  
'''print(calculo_imc(1.60, 86))'''
"""
Created on Sun Jan 16 2022

@author: Vieira
Taxa de serviço
"""

value = input("Digite o valor da conta: ")
has_service = input("Deseja pagar a taxa de serviço? S/N ")

account_value = float(value)

if (has_service == "S"):
  service = account_value * 0.1  # Nossos 10%
  resume_account = service + account_value # A soma dos 10% mais o valor da conta


  ## descriminação da conta a ser paga
  print("O valor da conta: ", value)
  print("O valor do serviço: ", service)
  print("O valor do total: ", resume_account)
else:
  print("O valor da fatura foi de: ", value)

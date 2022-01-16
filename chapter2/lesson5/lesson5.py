"""
Created on Sun Jan 16 2022

@author: Vieira
Taxa de serviço
"""

value = input("Digite o valor da conta: ")
has_service = input("Deseja pagar a taxa de serviço? S/N ")

# Calculou os impostos
account_value = float(value)
taxes = account_value * 0.2
resume_taxes = account_value + taxes

print("O valor da conta: ", value)
print("O valor dos impostos: ", taxes)

if (has_service == "S"):
  service = account_value * 0.1  # Nossos 10%
  resume_account = service + resume_taxes # A soma dos 10% mais o valor da conta com impostos


  ## descriminação da conta a ser paga
  print("O valor do serviço: ", service)
  print("O valor do total: ", resume_account)
else:
  print("O valor do total: ", resume_taxes)
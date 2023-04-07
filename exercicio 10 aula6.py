print("valor a ser pago do imposto de renda")
nome=(input("nos informe seu nome:" ))
cpf=float(input("digite seu cpf:" ))
renda_anual=float(input("nos informe sua renda anual:" ))
numero_dependentes=int(input("nos informe sua quantidade de dependentes:" ))
desconto=numero_dependentes*110
renda_liquida=renda_anual-desconto
print("valor de renda liquida", renda_liquida)
if  renda_liquida<800:
    ipg=renda_liquida

elif renda_liquida>=801 and renda_liquida<=4000:
    ipg=renda_liquida*2.5/100

elif renda_liquida>=4001 and renda_liquida<=9000:
    ipg=renda_liquida*5/100
else:
    renda_liquida>9000
    ipg=renda_liquida*0.1
    
print("\nnome ", nome, "\ncpf ", cpf, "\nrenda anual", renda_anual, "\nnumero de dependentes", numero_dependentes, "\no valor do imposto a ser pago é de:" , ipg)
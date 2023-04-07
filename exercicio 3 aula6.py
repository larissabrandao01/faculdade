print("classe eleitoral")
idade=int(input("digite sua idade: "))
if idade>120 or idade <1:
   print( "idade invalida")
elif  idade <16:
    print("não eleitor")
elif idade>=18 and idade <=65:
    print("eleitor obigatorio ")
else:
    print("eleitor facultativo")
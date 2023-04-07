print("calculando o peso ideal")
h=float(input("digite sua altura: "))
sexo=(input("qual o seu sexo: "))

if sexo=="feminino" or sexo=="masculino":
  
    if sexo== "masculino" :
        pi= (72.7*h)-58
        print("seu peso ideal é de: ", pi)
    else:
        pi= (62.1*h)-44.7
        print("seu peso ideal é de: ", pi)
else:
 print("sexo inválido")
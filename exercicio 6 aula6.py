print("valor da pescaria")
peso=float(input("digite o peso do peixe: "))

if peso<=50:
  print('zero')

else:
 excesso=peso-50
 multa=excesso*4
 print('o peso total da pescaria é de', peso, "kg" )
 print( "o excesso de peso é= {excesso:.0f} , o valor da multa é R$ {multa:.2f}")
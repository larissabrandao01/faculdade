print ("calculo de maior, menor e a media de 3 numeros")
numero1=int(input(" digite o primeiro numero: "))
numero2=int(input(" digite o segundo numero: "))
numero3=int(input(" digite o terceiro numero: "))
if numero1>0 and numero2>0 and numero3>0:
  if numero1>numero2 and numero1>numero3:
    maior=numero1
  
  elif numero2>numero3:
    maior=numero2
  else:
    maior=numero3     
else:
  print("valor invalido")

if numero1<numero2 and numero1<numero3:
 menor=numero1
   
elif numero2<numero3:
 menor=numero2
else:
  menor=numero3 

media=(numero1+numero2+numero3)/3
print("o maior numero é: ", maior, "o menor numero é: ", menor, "a media dos numero lidos: ",media )


     
     



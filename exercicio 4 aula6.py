print("\n\n\tMenu de opções")
print("\n\t1 -adição")
print("\n\t2 -subtração")
print("\n\t3 -multiplicação")
print("\n\t4 -divisão")
op=int(input("escolha uma opção: "))

if op>=1 and op<=4:

    n1=float(input("digite um numero: "))
    n2=float(input("digite outro numero: "))
    if op==1:
        r=n1+n2
        print("o resultado é: ",r )
    elif op==2:
        r=n1-n2
        print("o resultado é: ",r )
    elif op==3:
        r=n1*n2
        print("o resultado é: ",r )
    else:
        r=n1/n2
        print("o resultado é: ",r )
else:
     print("opção invalida")




    
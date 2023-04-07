print("tete para descobrir o seu grau de obesidade")
peso=float(input("nos informe seu peso"))
altura=float(input("nos informe a sua altura"))
massa=peso/altura**2
if massa<26:
    print("peso normal")
elif massa>26 and massa<30:
    print("obeso")
else:
    massa>30
    print("obeso morbido")



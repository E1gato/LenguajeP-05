N1=N2=0
N1=int(input("Ingrese el primer numero: "))
N2=int(input("Ingrese el segundo numero: "))
diferencia1=N1-N2
diferencia2=N2-N1
if(N1==N2):
    print("Los numeros son iguales")
else:
    if N1>N2:
        print(N2,"Es menor")
        print("La diferencia es: ",diferencia1)
    else:
        print(N1,"Es menor")
        print("La diferencia es: ",diferencia2)

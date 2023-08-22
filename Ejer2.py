
print("Ingrese su nombre y su edad: ")
Nombre1=input()
Edad1=int(input())

print("Ingrese su nombre y su edad: ")
Nombre2=input()
Edad2=int(input())

diferencia1=Edad1-Edad2
diferencia2=Edad2-Edad1

while Edad1 and Edad2 < 110:
    if Edad1>Edad2:
        print(Nombre1,"es mayor que",Nombre2)
        print("La diferencia es: ",diferencia1)
        break
    else:
        print(Nombre2,"es mayor que",Nombre1)
        print("La diferencia es: ",diferencia2)
        break
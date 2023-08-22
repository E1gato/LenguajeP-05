
print("Ingrese los 3 numeros")
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print(n1, "es el mayor")
        
elif n2 > n1 and n2 > n3:
    print(n2, "es el mayor")
    
else:
    print(n3, "es el mayor")
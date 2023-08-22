"""Desarrolla un programa que permita al usuario agregar, eliminar y mostrar elementos
de una lista de tareas pendientes."""

tareas = []
   
def agregar_tarea(tarea):
    tareas.append(tarea)
    print("Tarea agregada correctamente.")
    
def mostrar_tareas():
    for tarea in tareas:
        print(tarea)
        
def eliminar_tarea(tarea):
    tareas.remove(tarea)
    print("Tarea eliminada correctamente.")

opcion = 0
while opcion != 4:
    print("1. Agregar Tarea")
    print("2. Mostrar Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")
    
    opcion = int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        tarea = input("Ingrese la tarea: ")
        agregar_tarea(tarea)
        
    elif opcion == 2:
        mostrar_tareas()
        
    elif opcion == 3:
        tarea = input("Ingrese la tarea: ")
        eliminar_tarea(tarea)
        
    elif opcion == 4:
        print("Hasta luego.")
        
    else:
        print("Opcion no valida.")

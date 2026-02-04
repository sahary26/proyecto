import core 
print("Bienvenido al taller 'LA LLAVE'")
while True:
        print("""Escriba el numero de la accion que desea realizar:
1-Agendar turno
2-Crear un nuevo servicio
3-Eliminar turno previamente agendado
4-Ver detalles sobre un turno ya agendado
5-Revisar la agenda
6-Cerrar el programa""")
        ans=input(str())
        ans=ans.strip()
        if ans=="1":
            print("Escriba el numero del servicio que desea solicitar")
            for i in range(len(core.Tarea)):
                print(str(i+1)+"----"+core.Tarea[i][0])
            while True:
                try:
                    tarea=int(input())
                    break
                except ValueError:
                    print("Debe ingresar un dato valido")
            if tarea not in range(1,len(core.Tarea)+1):
                print("No hay definida ninguna tarea para ese comando")
            else:
                print(core.agendar_cita(tarea))
        elif ans=="2":
            print(core.crear())
        elif ans=="3":
            print(core.eliminar())
        elif ans=="4":
            print(core.detalles())
        elif ans=="5":
            print(core.motrar_agenda())
        elif ans=="6":
            print( core.guardar())
            break
        else:
            print("Opcion no valida")


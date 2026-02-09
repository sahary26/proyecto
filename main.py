import core 
print("\033[33m"+"Bienvenido al taller 'LA LLAVE'"+"\033[0m")
while True:
        print("\033[34m"+"""Escriba el numero de la accion que desea realizar: \033[0m
1-Agendar turno
2-Crear un nuevo servicio
3-Eliminar turno previamente agendado
4-Agregar herramienta
5-Agregar mecanico
6-Ver detalles sobre un turno ya agendado
7-Revisar la agenda
8-Cerrar el programa""")
        ans=input(str())
        ans=ans.strip()
        if ans=="1":
            print("\033[34m"+"Escriba el numero del servicio que desea solicitar \033[0m")
            for i in range(len(core.Tarea)):
                print(str(i+1)+" ---- "+core.Tarea[i][0]+" ---- Duracion: "+str(core.Tarea[i][1])+" horas")
            while True:
                try:
                    tarea=int(input())
                    break
                except ValueError:
                    print("\033[31m"+"Debe ingresar un dato valido"+"\033[0m")
            if tarea not in range(1,len(core.Tarea)+1):
                print("\033[31m"+"No hay definida ninguna tarea para ese comando"+"\033[0m")
            else:
                print(core.agendar_cita(tarea))
        elif ans=="2":
            print(core.crear())
        elif ans=="3":
            print(core.eliminar())
        elif ans=="4":
            print("\033[34mEscriba el nombre de la herramienta\033[0m")
            herramienta=str(input())
            herramienta=herramienta.lower()
            print("\033[34mEscriba la cantidad que desea agregar\033[0m")
            while True:
                try:
                    cant=int(input())
                    break
                except ValueError:
                    print("\033[31mEscriba una cantidad valida\033[0m")
            print(core.agregar_herramienta(herramienta,cant))
        elif ans=="5":
            print("\033[34mEscriba el nombre del mecanico:\033[0m")
            mecanico=str(input())
            print(core.agregar_mecanico(mecanico))
        elif ans=="6":
            print(core.detalles())
        elif ans=="7":
            print(core.motrar_agenda())
        elif ans=="8":
            print( core.guardar())
            break
        else:
            print("\033[31m"+"Opcion no valida"+"\033[31m")


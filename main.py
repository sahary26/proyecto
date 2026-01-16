import core 
("Bienvenido al taller 'GUASASA'")
def menu():
    print('Escriba el numero de la accion que desea realizar')
    print("1-Agendar turno")
    print('2-Eliminar turno previamente agendado')
    print('3-Ver detalles sobre un turno ya agendado')
    print('4-Revisar la agenda')
    print('5-Cerrar el programa')
    ans=input(str())
    if ans=="1":
        print("Escriba el numero del servicio que desea solicitar")
        print('1-Reparacion de motor')
        print('2-Reparacion de frenos')
        print('3-Reparacion de direccion')
        print('4-Reparacion del aforador')
        print('5-Chapisteria y pintura')
        print('6-Reparacion del sistema electrico')
        print('7-Esmerilado de tapa')
        print('8-Calibrado de tapa')
        print('9-Reparacion del sistema de enfriamiento')
        print('10-Reparacion de cierres y ventanillas')
        tarea=input(str())
        ## quitar espacios en blanco
        if tarea=="1" or tarea=="2" or tarea=="3" or tarea=="4" or tarea=="5" or tarea=="6" or tarea=="7" or tarea=="8" or tarea=="9" or tarea=="10":
            tarea=int(tarea)
            print(core.agendar_cita(tarea))
        else:
            print("Opcion no valida")
            return(menu())
    elif ans=="2":
        print(core.eliminar())
    elif ans=="3":
        print("Escriba el dia de la cita que desea eliminar")
        dia=input(str())
        print('Escriba la hora de la cita')
        hora=input(str())
        ## validar fecha
    elif ans=="4":
        pass
    ## print(jason)
    elif ans=="5":
        return "Gracias por elegirnos" 
        #guardar en json
        ##terminar 
    else:
        print("Opcion no valida")
        return (menu())
    
print(menu())
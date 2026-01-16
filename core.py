import datetime
import main
#completar esto
Tarea=[['Reparacion de motor',5,['llave de torque','juego de llaves','destornilladores','martillo de goma','montador de aro']],
       ['Reparacion de frenos',3,['juego de llaves','destornilladores','liquido de freno','pinzas']],
       ['Reparacion de direccion',4,['herramientas']],
       ['Reparacion del aforador',2,['herramientas']],
       ['Chapisteria y pintura',7,['herramientas']],
       ['Reparacion del sistema electrico',5,['herramientas']],
       ['Esmerilado de tapa',6,['herramientas']],
       ['Calibrado de tapa',6,['herramientas']],
       ['Reparacion del sistema de enfriamiento',2,['herramientas']],
       ['Reparacion del sistema de enfriamiento',2,['herramientas']],
       ['Reparacion de cierres y ventanillas',4,['herramientas']]]


Herramientas=[['llave de torque',3],['juego de llaves',3],['destornilladores',4],['martillo de goma',3],
              ['montador de aro',2],['liquido de freno',2],['pinzas',2],['palanca',2],['martillo',1],
              ['extractores',1],['manometro',1],['pintura',3],['compresor de aire',1],['lija',3],
              ['oxigeno y acetileno',2],['pistola de soldar',2],['tape',3],['cautin',2],['multimetro',2],
              ['pasta de esmerilar',1],['maquina de esmerilar',1],['calibrador',1],['micrometro',1],
              ['silicona',1]]

Mecanicos=['Juan','jose','alberto','josefina','catalina']

Meses=[['enero',31],['febrero',30],['marzo',31],['abril',30],['mayo',31],['junio',30],['julio',31],['agosto',31],['septiembre',30],['octubre',31],['noviembre',30],['diciembre',31]]
Agenda=[]
fecha=()
Clientes=[]

def comprobar_nombre_agendar():
    b=0
    print("Escriba el nombre con el que desea agendar la cita")
    nombre=str(input())
    for i in range(len(Clientes)):
        if nombre==Clientes[i][0]:
            b=1
            print("Ese nombre ya existe. Tiene otro servicio agendado con nosotros? (SI/NO)")
            a=str(input())
            if a=="SI":
                Clientes[i][1]=Clientes[i][1]+1
                print("Su cita ha sido agendada con exito")
            elif a=="NO":
                print("Usted debe registrarse con otro nombre")
                print(comprobar_nombre_agendar())
            else: 
                print("Opcion no valida")
                print(comprobar_nombre_agendar())
    if b==0:
        Clientes.append([nombre,1])
    return nombre

def comprobar_horario_agendar():
    print("Escriba el mes en que quiere agendar su cita. Ejemplo: enero")
    mes=str(input())
    fecha=None
    Mes=0
    for i in range(len(Meses)):
        if mes== Meses[i][0]:
            Mes= i+1
    if Mes==0:
        print('Opcion no valida')
        return fecha
    else:
        print('Escriba el dia en que quiere agendar su cita. Ejemplo: 5')
        ### ver que pasa si es letra
        dia=str(input())
        dia=int(dia)
        if Meses[Mes-1][1] < dia:
            print("Opcion no valida")
            return fecha
        else:
            print('Escriba la hora en que quiere agendar su turno. Ejemplo: 13:30')
            horario=str(input())
            if ":" not in horario:
                print("Opcion no valida")
                return fecha
            ####ver que pasa cuando se escriban letras
            else:
                hora=int(horario[:horario.index(":")])
                if hora>23:
                    print("Opcion no valida")
                    return fecha
                else:
                    minutos=horario[horario.index(":")+1:]
                    if minutos=="00":
                        minutos=0
                    else:
                        minutos=int(minutos)
                    if 0>minutos>59:
                        print("Opcion no valida")
                        return fecha
                    else:
                        fecha=[2026,Mes,dia,hora,minutos]
                        return fecha
                    
def comprobar_herramientas(tarea:int):
    a=0
    falta=''
    count=0
    for j in Tarea[tarea-1][2]:
        for i in Herramientas:
            if j==i[0] and i[1]==0:
                falta=falta+i[0]##poner debajo
            if j==i[0] and i[1]>0:
                count=count+1
            if count==len(Tarea[tarea-1][2]):
                if j==i[0]:
                    i[1]=i[1]-1
                a=1 
    if a==0:
        print("No es posible agendar su cita. No hay disponible: "+falta)
    return a

def agendar_cita(tarea:int):
    ocupado=0
    fecha=comprobar_horario_agendar()
    if fecha==None:
        pass
    else:
        inicio=(fecha[3],fecha[4])
        fin=(fecha[3]+Tarea[tarea-1][1],fecha[4])
        if fin[0]>=17 or inicio[0]<9:
            print('No es posible agendar su cita,pues su realizacion esta fuera del horario establecido')
        else:              
            for i in range(len(Agenda)):
                if Agenda[i][0]==(2026,fecha[1],fecha[2]):
                        for j in range(len(Agenda[i][1])):
                            if inicio<Agenda[i][1][j][0][1]and fin>Agenda[i][1][j][0][0]:
                                ocupado=ocupado+1
                        if ocupado>len(Mecanicos):
                            ##revisar esto
                            print("No hay mecanicos disponibles para ese horario")
                            #ver como muestro la proxima fecha disponible
                        else:
                            if comprobar_herramientas(tarea)==1:
                                nombre=comprobar_nombre_agendar()
                                Agenda[i][1].append([[inicio,fin],nombre,Tarea[tarea-1][0],Tarea[tarea-1][1],Mecanicos[0]])
                                print("Su cita ha sido agenda con exito")
                else:
                        nombre=comprobar_nombre_agendar()
                        Agenda.append([(2026,fecha[1],fecha[2]),[[[inicio,fin],nombre,Tarea[tarea-1][0],Tarea[tarea-1][1],Mecanicos[0]]]])
                        print("Su cita ha sido agenda con exito")
            if len(Agenda)==0:
                nombre=comprobar_nombre_agendar()
                Agenda.append([(2026,fecha[1],fecha[2]),[[[inicio,fin],nombre,Tarea[tarea-1][0],Tarea[tarea-1][1],Mecanicos[0]]]])
                print('Su cita ha sido agendada con exito')  
    return main.menu()

def comprobar_horario_normal():
    print("Escriba el mes en que agendo su cita. Ejemplo: enero")
    mes=str(input())
    fecha=None
    Mes=0
    for i in range(len(Meses)):
        if mes== Meses[i][0]:
            Mes= i+1
    if Mes==0:
        print('Opcion no valida')
        return comprobar_horario_normal()
    else:
        print('Escriba el dia en que agendo su cita. Ejemplo: 5')
        ### ver que pasa si es letra
        dia=str(input())
        dia=int(dia)
        if Meses[Mes-1][1] < dia:
            print("Opcion no valida")
            return comprobar_horario_normal()
        else:
            fecha=(2026,Mes,dia)
            return fecha
        
def eliminar():
    a=0
    coordenadas=[]
    count=0
    Opciones=[]
    b=0
    opcion=0
    print("Escriba el nombre con el que agendo la cita previamente")
    nombre=str(input())
    for n in range(len(Clientes)):
        if nombre== Clientes[n][0]:
            b=1
            fecha=comprobar_horario_normal()
            for i in range(len(Agenda)):
                if Agenda[i][0]==fecha:
                    a=1
                    for j in range(len(Agenda[i][1])):
                        if Agenda[i][1][j][1]==nombre:
                            coordenadas.append((i,j))
            if a==0:
                print("Para esa fecha no hay asignado ningun turno. Escriba correctamente la fecha")
                return comprobar_horario_normal()
            print(coordenadas)
            dia=str(fecha[2])
            if len(coordenadas)==1:
                tarea=str(Agenda[i][1][j][2])###quitar signos 
                print("Desea eliminar su cita para '"+ tarea+ "' el dia "+ dia +" de "+ Meses[fecha[1]-1][0]+ "?. (SI/NO)")
                ans=str(input()) ##quitar mayusculas y espacios
                if ans=="SI":
                    Agenda[i][1].pop(j)
                    if len(Agenda[i][1])==0:
                        Agenda.pop(i)
                    Clientes[n][1]= Clientes[n][1]-1
                    if Clientes[n][1]==0:
                        Clientes.pop(n)
                    for s in Tarea:
                        if Agenda[i][1][j][2]==s[0]:
                            for o in s[2]:
                                for p in Herramientas:
                                    if o==p[0]:
                                        p[1]=p[1]+1
                    print("Su cita ha sido eliminada")
                    return main.menu()
                elif ans=="NO":
                    return main.menu()
                else:
                    print("Opcion no valida")
                    return main.menu()
            else:
                print("Tiene agendado para ese dia " + str(len(coordenadas))+ " citas. Cual desea eliminar?")
                for k in coordenadas:
                    tarea=str(Agenda[k[0]][1][k[1]][2])###quitar signos
                    count=count+1
                    Opciones.append(count)
                    print(str(count)+" ---- "+tarea)
                opcion=int(input())
                if opcion not in Opciones:
                    print("Opcion no valida")
                    return main.menu()
                else:
                    i=coordenadas[Opciones.index(opcion)][0]
                    j=coordenadas[Opciones.index(opcion)][1]
                    tarea=Agenda[i][1][j][2]###quitar signos 
                    print("Desea eliminar su cita para '"+ str(tarea)+ "' el dia "+ dia +" de "+ str(Meses[fecha[1]-1][0])+ "?. (SI/NO)")
                    ans=str(input()) ##quitar mayusculas y espacios
                    if ans=="SI":
                        Agenda[i][1].pop(j)
                        if len(Agenda[i][1])==0:
                            Agenda.pop(i)
                        Clientes[n][1]= Clientes[n][1]-1
                        if Clientes[n][1]==0:
                            Clientes.pop(n)
                        for s in Tarea:
                            if tarea==s[0]:
                                for o in s[2]:
                                    for p in Herramientas:
                                        if o==p[0]:
                                            p[1]=p[1]+1
                        print("Su cita ha sido eliminada")
                        return main.menu()
                    elif ans=="NO":
                        return main.menu()
                    else:
                        print("Opcion no valida")
                        return main.menu()
    if b==0:
        print("No hay ninguna cita agendada a ese nombre")
        return main.menu()

#def detalles():
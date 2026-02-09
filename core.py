import random
import copy
import json

with open('recursos.json','r',encoding='utf-8') as archivo_1:
    recursos=json.load(archivo_1)

with open('agenda.json','r',encoding='utf-8') as archivo_2:
    agenda=json.load(archivo_2)

fecha=[]
Meses=[['enero',31],['febrero',28],['marzo',31],['abril',30],['mayo',31],['junio',30],['julio',31],['agosto',31],['septiembre',30],['octubre',31],['noviembre',30],['diciembre',31]]

Agenda=agenda["Agenda"]
Clientes=agenda["Clientes"]

Tarea=recursos["Tarea"]
Herramientas=recursos["Herramientas"]
Mecanicos= recursos["Mecanicos"]

def agregar_herramienta(herramienta,cant):
    a=0
    for i in Herramientas:
        if Herramientas[1][0]==herramienta:
            a=1
            print("\033[34mYa existe esa herramienta en el taller. Desea agregar "+ str(cant)+" unidades al almacen?(SI/NO)\033[0m")
            ans=str(input())
            ans=ans.lower().strip()
            if ans=="si":
                Herramientas[i][1]=Herramientas[i][1]+cant
                datos_actualizados= {"Tarea": Tarea,
                        "Herramientas": Herramientas,
                        "Mecanicos": Mecanicos}
                with open('recursos.json','w',encoding='utf-8') as archivo_5:
                    json.dump(datos_actualizados,archivo_5,indent=4,ensure_ascii=False)
            elif ans=="no":
                return "\033[31mNo se realizaron cambios en su almacen\033[0m"
            else:
                return agregar_herramienta(herramienta,cant)
    if a==0:
        Herramientas.append([herramienta,cant])
        datos_actualizados= {"Tarea": Tarea,
                "Herramientas": Herramientas,
                "Mecanicos": Mecanicos}
        with open('recursos.json','w',encoding='utf-8') as archivo_5:
            json.dump(datos_actualizados,archivo_5,indent=4,ensure_ascii=False)
        return "\033[32mSe agrego exitosamente su herramienta\033[0m"
    
def agregar_mecanico(mecanico):
    a=0
    for i in Mecanicos:
        if mecanico not in Mecanicos:
            a=1
            Mecanicos.append(mecanico)
            datos_actualizados= {"Tarea": Tarea,
                    "Herramientas": Herramientas,
                    "Mecanicos": Mecanicos}
            with open('recursos.json','w',encoding='utf-8') as archivo_6:
                json.dump(datos_actualizados,archivo_6,indent=4,ensure_ascii=False)
            return "\033[32mMecanico agregado con exito\033[0m"
    if a==0:
        return "\033[31mYa hay un mecanico con ese nombre.No es posible agendar otro\033[0m"

def asignar_mecanico(mes,dia,hora):
    mecanicos_ocupados=[]
    for i in range(len(Agenda)):
        if Agenda[i][0]==[2026,mes,dia]:
            for j in range(len(Agenda[i][1])):
                if hora[0]<Agenda[i][1][j][0][1]and hora[1]>Agenda[i][1][j][0][0]:
                    mecanicos_ocupados.append(Agenda[i][1][j][4])
    mecanicos_disponibles=list(set(Mecanicos)-set(mecanicos_ocupados))
    mecanico=random.choice(mecanicos_disponibles)
    return mecanico

def crear():
    a=0
    print("\033[34m"+"Escriba el nombre del servicio que desea crear\033[0m")
    servicio=str(input())
    k=servicio.lower().strip()
    for i in range(len(Tarea)):
        l=Tarea[i][0].lower().strip()
        if l==k:
            a=1
            return "\033[31m Ya hay un servicio creado con ese nombre\033[0m"
    if a==0:
        falta=""
        solo_herramientas=[]
        for i in Herramientas:
            solo_herramientas.append(i[0])
        print("\033[34mHerramientas disponibles:\033[0m")
        for i in solo_herramientas:
            print(i)
        print("\033[34mEscriba, separado por comas, el nombre de cada una de las herramientas necesarias para el servicio\033[0m")
        entrada=str(input())
        lista_herramientas=entrada.split(",")
        lista_herramientas=[i.strip().lower() for i in lista_herramientas]
        lista_herramientas=list(set(lista_herramientas))
        if (("pistola de soldar" in lista_herramientas)or("cautin"in lista_herramientas)) and ("gasolina" in lista_herramientas):
            return "\033[31mPor cuestiones de seguridad la gasolina no puede estar en el mismo servico que el cautin o la pistola de soldar\033[0m"
        else:
            for i in lista_herramientas:
                if i not in solo_herramientas:
                    falta=falta+i+"\n"
            if falta!= "":
                return "\033[31mNo es posible crear su servicio. No hay disponible en el taller:"+"\n"+falta+"\033[34m"
            else:
                print("\033[34mEscriba el numero de horas que llevara su servicio.(1-8)\033[0m")
                while True:
                    try:
                        tiempo=int(input())
                        break
                    except ValueError:
                        print("\033[33mDebe escribir un numero entero para definir su tiempo\033[0m")
                if 0>tiempo>8:
                    return "\033[31mNo hay servicios que se realicen en esa cantidad de horas\033[0m"
                else:
                    Tarea.append([servicio,tiempo,lista_herramientas])
                    datos_actualizados= {"Tarea": Tarea,
                        "Herramientas": Herramientas,
                        "Mecanicos": Mecanicos}
                    with open('recursos.json','w',encoding='utf-8') as archivo_4:
                        json.dump(datos_actualizados,archivo_4,indent=4,ensure_ascii=False)
                    return ("\033[32mSu servicio ha sido agregado con exito\033[0m")

def comprobar_disponibilidad(mes:int,dia:int,hora:list,tarea:int):
    count=0
    a=0
    tareas_pendientes=[]
    for i in range(len(Agenda)):
        if Agenda[i][0]==[2026,mes,dia]:
            for j in range(len(Agenda[i][1])):
                if hora[0]<Agenda[i][1][j][0][1]and hora[1]>Agenda[i][1][j][0][0]:
                    tareas_pendientes.append(Tarea[Agenda[i][1][j][2]][0])
        if len(tareas_pendientes)>=len(Mecanicos):
            a=1
        else:
            count=0
            Herramientas_ahora=copy.deepcopy(Herramientas)
            for n in range(len(tareas_pendientes)):
                for m in range(len(Tarea)):
                    if tareas_pendientes[n]==Tarea[m][0]:
                        for k in Tarea[m][2]:
                            for l in Herramientas_ahora:
                                if k==l[0]:
                                    l[1]=l[1]-1
            for e in Tarea[tarea-1][2]:
                for y in Herramientas_ahora:
                    if e==y[0] and y[1]>0:
                        count=count+1
            if count!=len(Tarea[tarea-1][2]):
                a=1
    return a

def comprobar_nombre_agendar():
    b=0
    print("\033[34mEscriba el nombre con el que desea agendar la cita\033[0m")
    nombre=str(input())
    nombre=nombre.lower()
    for i in range(len(Clientes)):
        if nombre==Clientes[i][0]:
            b=1
            print("\033[34mEse nombre ya existe. Tiene otro servicio agendado con nosotros? (SI/NO)\033[0m")
            a=str(input())
            a=a.lower().strip()
            if a=="si":
                Clientes[i][1]=Clientes[i][1]+1
                print("\033[32mSu cita ha sido agendada con exito\033[0m")
            elif a=="no":
                print("\033[31mUsted debe registrarse con otro nombre\033[0m")
                print(comprobar_nombre_agendar())
            else: 
                print("\033[31mOpcion no valida\033[0m")
                print(comprobar_nombre_agendar())
    if b==0:
        Clientes.append([nombre,1])
    return nombre

def agendar_hueco(mes:int,dia:int,inicio:list,tiempo:int,tarea:int):
    if inicio[1]<10:
        min="0"+str(inicio[1])
    else:
        min=str(inicio[1])
    print("\033[34mEl proximo espacio para realizar su turno es el "+ str(dia)+" de "+ str(Meses[mes-1][0])+" a las "+str(inicio[0])+":"+min+".")
    print("Desea agendar su turno en ese horario?(SI/NO)\033[0m")
    ans=str(input())
    ans=ans.lower().strip()
    if ans=="si":
        nombre=comprobar_nombre_agendar()
        mecanico=asignar_mecanico(fecha[1],fecha[2],[inicio,[inicio[0]+tiempo,inicio[1]]])
        Agenda.append([[2026,mes,dia],[[[inicio,[inicio[0]+tiempo,inicio[1]]],nombre,tarea-1,Tarea[tarea-1][1],mecanico]]])
        return print("\033[32mSu cita ha sido agendada con exito\033[0m")
    elif ans=="no":
        return print("\033[31mSu cita NO se ha agendado\033[0m")
    else:
        print("\033[31mRespuesta invalida\033[0m")
        return agendar_hueco()
 
def buscar_hueco(mes:int,dia:int,hora:list,tiempo:int,tarea:int):
    horas=[]
    for i in range(len(Agenda)):
        if Agenda[i][0]==[2026,mes,dia]:
            for j in range(len(Agenda[i][1])):
                if hora[0]<Agenda[i][1][j][0][1]and hora[1]>Agenda[i][1][j][0][0]:
                    horas.append(Agenda[i][1][j][0][1])
    horas.sort()
    menor_hora=horas[0]
    if menor_hora[0]+tiempo<17:
        if comprobar_disponibilidad(mes,dia,[menor_hora,[menor_hora[0]+tiempo,menor_hora[1]]],tarea)==0:
            agendar_hueco(mes,dia,menor_hora,tiempo,tarea)
        else: return buscar_hueco(mes,dia,[menor_hora,[menor_hora[0]+tiempo,menor_hora[1]]],tiempo,tarea)
    elif dia<Meses[mes-1][1]:
        if comprobar_disponibilidad(mes,dia+1,[(9,00),(9+tiempo,00)],tarea)==0:
            agendar_hueco(mes,dia+1,[9,00],tiempo,tarea)
        else: return buscar_hueco(mes,dia+1,[[9,00],[9+tiempo,00]],tiempo,tarea)
    elif mes<12:
        if comprobar_disponibilidad(mes+1,1,[[9,00],[9+tiempo,00]],tarea)==0:
            agendar_hueco(mes+1,1,[9,00],tiempo,tarea)
        else: return buscar_hueco(mes+1,1,[[9,00],[9+tiempo,00]],tiempo,tarea)
    else:
       return "\033[31mLo sentimos ya no quedan turnos disponibles en el 2026 para realizar su trabajo.Espere la agenda del  2027 ;)\033[0m"

def comprobar_horario_agendar():
    print("\033[34mEscriba el mes en que quiere agendar su cita. Ejemplo: enero\033[0m")
    mes=str(input())
    fecha=None
    Mes=0
    for i in range(len(Meses)):
        if mes== Meses[i][0]:
            Mes= i+1
    if Mes==0:
        print('\033[31mOpcion no valida\033[0m')
        return fecha
    else:
        print('\033[34mEscriba el dia en que quiere agendar su cita. Ejemplo: 5\033[0m')
        while True:
                try:
                    dia=int(input())
                    break
                except ValueError:
                    print("\033[34mEscriba correctamente el numero del mes\033[0m")
        if Meses[Mes-1][1] < dia:
            print("\033[31mOpcion no valida\033[0m")
            return fecha
        else:
            print('\033[34mEscriba la hora en que quiere agendar su turno. Ejemplo: 13:30\033[0m')
            horario=str(input())
            if ":" not in horario:
                print("\033[31mOpcion no valida\033[0m")
                return fecha
            else:
                while True:
                    try:
                        hora=int(horario[:horario.index(":")])
                        break
                    except ValueError:
                        print("\033[34mEscriba correctamente la hora\033[0m")
                if hora>23:
                    print("\033[31mOpcion no valida\033[0m")
                    return fecha
                else:
                    while True:
                        try:
                            minutos=int(horario[horario.index(":")+1:])
                            break
                        except ValueError:
                            print("\033[34mIngrese los minutos correctamente\033[0m")
                    if 0>minutos>59:
                        print("\033[31mOpcion no valida\033[0m")
                        return fecha
                    else:
                        fecha=[2026,Mes,dia,hora,minutos]
                        return fecha

def agendar_cita(tarea:int):
    tareas_pendientes=[]
    a=0
    fecha=comprobar_horario_agendar()
    if fecha==None:
        pass
    else:
        inicio=[fecha[3],fecha[4]]
        fin=[fecha[3]+Tarea[tarea-1][1],fecha[4]]
        if fin[0]>=17 or inicio[0]<9:
            return '\033[31mNo es posible agendar su cita,pues su realizacion esta fuera del horario establecido.El local se encuentra abrierto desde 9:00 hasta 17:00\033[0m'
        else:              
            for i in range(len(Agenda)):
                if Agenda[i][0]==[2026,fecha[1],fecha[2]]:
                    for j in range(len(Agenda[i][1])):
                        if inicio<Agenda[i][1][j][0][1]and fin>Agenda[i][1][j][0][0]:
                            tareas_pendientes.append(Tarea[Agenda[i][1][j][2]][0])
                    if len(tareas_pendientes)>=len(Mecanicos):
                        print("\033[31mNo hay mecanicos disponibles para ese horario\033[0m")
                        return  buscar_hueco(fecha[1],fecha[2],[inicio,fin],Tarea[tarea-1][1],tarea)
                    else:
                        falta=''
                        count=0
                        Herramientas_ahora=copy.deepcopy(Herramientas)
                        for n in range(len(tareas_pendientes)):
                            for m in range(len(Tarea)):
                                if tareas_pendientes[n]==Tarea[m][0]:
                                    for k in Tarea[m][2]:
                                        for l in Herramientas_ahora:
                                            if k==l[0]:
                                                l[1]=l[1]-1
                        for e in Tarea[tarea-1][2]:
                            for y in Herramientas_ahora:
                                if e==y[0] and y[1]<=0:
                                    falta=falta+y[0]+"\n"
                                if e==y[0] and y[1]>0:
                                    count=count+1
                        if count==len(Tarea[tarea-1][2]):
                            a=1 
                        else: a=2
            if a==1:
                nombre=comprobar_nombre_agendar()
                mecanico=asignar_mecanico(fecha[1],fecha[2],[inicio,fin])
                Agenda[i][1].append([[inicio,fin],nombre,tarea-1,Tarea[tarea-1][1],mecanico])
                return "\033[32mSu cita ha sido agendada con exito\033[0m"
            if a==2:
                print("\033[31mNo es posible agendar su cita. No hay disponible: "+"\n"+falta+"\033[0m")
                return buscar_hueco(fecha[1],fecha[2],[inicio,fin],Tarea[tarea-1][1],tarea)
            if len(Agenda)==0:
                a=3
                nombre=comprobar_nombre_agendar()
                mecanico=asignar_mecanico(fecha[1],fecha[2],[inicio,fin])
                Agenda.append([[2026,fecha[1],fecha[2]],[[[inicio,fin],nombre,tarea-1,Tarea[tarea-1][1],mecanico]]])
                return "\033[32mSu cita ha sido agendada con exito\033[0m"
            if a==0:
                nombre=comprobar_nombre_agendar()
                mecanico=asignar_mecanico(fecha[1],fecha[2],[inicio,fin])
                Agenda.append([[2026,fecha[1],fecha[2]],[[[inicio,fin],nombre,tarea-1,Tarea[tarea-1][1],mecanico]]])
                return "\033[32mSu cita ha sido agendada con exito\033[0m"

def comprobar_horario_normal():
    print("\033[34mEscriba el mes en que agendo su cita. Ejemplo: enero\033[0m")
    mes=str(input())
    fecha=None
    Mes=0
    for i in range(len(Meses)):
        if mes== Meses[i][0]:
            Mes= i+1
    if Mes==0:
        print('\033[32mOpcion no valida\033[0m')
        return comprobar_horario_normal()
    else:
        print('\033[34mEscriba el dia en que agendo su cita. Ejemplo: 5\033[0m')
        while True:
            try:
                dia=int(input())
                break
            except ValueError:
                print("\033[34mEscriba el dia correctamente\033[0m")
        if Meses[Mes-1][1] < dia:
            print("\033[31mOpcion no valida\033[0m")
            return comprobar_horario_normal()
        else:
            fecha=[2026,Mes,dia]
            return fecha

def confirmacion_eliminar(coordenadas,dia,fecha,nombre,tarea):
    print("\033[34mDesea eliminar su cita para '"+tarea+ "' el dia "+ dia +" de "+ Meses[fecha[1]-1][0]+ "?. (SI/NO)\033[0m")
    ans=str(input())
    ans=ans.lower().strip()
    if ans=="si":
        Agenda[coordenadas[0][0]][1].pop(coordenadas[0][1])
        if len(Agenda[coordenadas[0][0]][1])==0:
            Agenda.pop(coordenadas[0][0])
        Clientes[nombre][1]= Clientes[nombre][1]-1
        if Clientes[nombre][1]==0:
            Clientes.pop(nombre)
        return "\033[32mSu cita ha sido eliminada\033[0m"
    elif ans=="no":
        return "\033[34mNO se elimnino su cita\033[0m"
    else:
        print("\033[31mOpcion no valida\033[0m")
        return confirmacion_eliminar(coordenadas,dia,fecha,nombre,tarea)

def eliminar():
    coordenadas=[]
    count=0
    b=0
    print("\033[34mEscriba el nombre con el que agendo la cita previamente\033[0m")
    nombre=str(input())
    nombre=nombre.lower().strip()
    for n in range(len(Clientes)):
        if nombre== Clientes[n][0]:
            b=1
            fecha=comprobar_horario_normal()
            for i in range(len(Agenda)):
                if Agenda[i][0]==fecha:
                    for j in range(len(Agenda[i][1])):
                        if Agenda[i][1][j][1]==nombre:
                            coordenadas.append((i,j))
            if len(coordenadas)==0:
                print("\033[31mPara esa fecha no hay asignado ningun turno. Escriba correctamente la fecha\033[0m")
                return comprobar_horario_normal()
            dia=str(fecha[2])
            if len(coordenadas)==1:
                tarea=str(Tarea[Agenda[coordenadas[0][0]][1][coordenadas[0][1]][2]][0])
                return confirmacion_eliminar(coordenadas,dia,fecha,n,tarea)
            else:
                print("\033[34mTiene agendado para ese dia " + str(len(coordenadas))+ " citas. Cual desea eliminar?\033[0m")
                for k in coordenadas:
                    horario=Agenda[k[0]][1][k[1]][0][0]
                    hora=str(horario[0])
                    if horario[1]<10:
                        min="0"+str(horario[1])
                    else:min=str(horario[1])
                    horario=hora+":"+min
                    tarea=str(Tarea[Agenda[k[0]][1][k[1]][2]][0])
                    count=count+1
                    print(str(count)+" ---- "+tarea+ "----"+ horario)
                while True:
                    try:
                        opcion=int(input())
                        break
                    except ValueError:
                        print("\033[34mEscriba correctamente la opcion deseada\033[0m")
                if opcion not in range(1,count+1):
                    return "\033[31mOpcion no valida\033[0m"
                else:
                    i=coordenadas[opcion-1][0]
                    j=coordenadas[opcion-1][1]
                    tarea=str(Tarea[Agenda[i][1][j][2]][0])
                    return confirmacion_eliminar([(i,j)],dia,fecha,n,tarea) 
    if b==0:
        return "\033[31mNo hay ninguna cita agendada a ese nombre\033[0m"

def detalles():
    a=0
    b=0
    coordenadas=[]
    count=0
    print("\033[34mEscriba el nombre con el que agendo la cita previamente\033[0m")
    nombre=str(input())
    nombre=nombre.lower()
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
                print("\033[31mPara esa fecha no hay asignado ningun turno. Escriba correctamente la fecha\033[0m")
                return comprobar_horario_normal()
            if len(coordenadas)==1:
                return "Fecha: " + str(fecha[2]) + " de " + str(fecha[1])+"\n"+"Trabajo a realizar: "+ str(Tarea[Agenda[i][1][j][2]][0])+"\n"+"Hora de inicio: "+ str(Agenda[i][1][j][0][0])+"\n"+ "Hora de finalizacion: "+str(Agenda[i][1][j][0][1]) +"\n"+ "Mecanico encargado: "+ Agenda[i][1][j][4]
            else:
                print("\033[34mTiene agendado para ese dia " + str(len(coordenadas))+ " citas. De cual desea ver detalles?\033[0m")
                for k in coordenadas:
                    horario=Agenda[k[0]][1][k[1]][0][0]
                    hora=str(horario[0])
                    if horario[1]<10:
                        min="0"+str(horario[1])
                    else:min=str(horario[1])
                    horario=hora+":"+min
                    tarea=str(Tarea[Agenda[k[0]][1][k[1]][2]][0])
                    count=count+1
                    print("["+str(count)+"]"+" ---- "+tarea+"----"+horario)
                while True:
                    try:
                        opcion=int(input())
                        break
                    except ValueError:
                        print("\033[34mEscriba correctamente el numero\033[0m")
                if opcion not in range(1,count+1):
                    return "\033[31mOpcion no valida\033[0m"
                else:
                    i=coordenadas[opcion-1][0]
                    j=coordenadas[opcion-1][1]
                    return "Fecha: " + str(fecha[2]) + " de " + str(Meses[fecha[1]-1][0])+"\n"+"Trabajo a realizar: "+ str(Tarea[Agenda[i][1][j][2]][0])+"\n"+"Hora de inicio: "+ str(Agenda[i][1][j][0][0])+"\n"+ "Hora de finalizacion: "+str(Agenda[i][1][j][0][1])+"\n" + "Mecanico encargado: "+ Agenda[i][1][j][4]
    if b==0:
        return "\033[31mNo hay ninguna cita agendada a ese nombre\033[0m"

def motrar_agenda():
    turnos="\033[34mTURNOS AGENDADOS:" + "\n\n\033[0m"
    if len(Agenda)==0:
        return"\033[31mAun no hay turnos agendados\033[0m"
    for i in range(len(Agenda)):
        for j in range(len(Agenda[i][1])):
            k="Nombre del cliente: "+ Agenda[i][1][j][1]+"\n"+"Fecha: " + str(Agenda[i][0][2]) + " de " + str(Meses[Agenda[i][0][1]-1][0])+"\n"+"Trabajo a realizar: "+ str(Tarea[Agenda[i][1][j][2]][0])+"\n"+"Hora de inicio: "+ str(Agenda[i][1][j][0][0])+"\n"+"Hora de finalizacion: "+str(Agenda[i][1][j][0][1]) +"\n"+ "Mecanico encargado: "+ Agenda[i][1][j][4]
            turnos=turnos+k+ "\n\n"
    return turnos

def guardar():
    if len(Agenda)>1:
        Agenda.sort(key=lambda x: x[0])
    datos_actualizados= {"Agenda": Agenda,
                         "Clientes": Clientes}
    with open('agenda.json','w',encoding='utf-8') as archivo_3:
        json.dump(datos_actualizados,archivo_3,indent=4,ensure_ascii=False)
    return "\033[33mGracias por elegirnos\033[0m"
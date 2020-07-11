import datetime
import io
import random
#Es para ver el dictionary mejor
from pprint import pprint
def valida_campo():
    campos=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    #Validamos que la opcion este dentro de campos
    while True:

        op=input(" a. Nombre \n b. Apellido \n c. Fecha \n d. Numero Entero \n e. Numero Real \n f. Patron de caracteres \n g. Ciudad \n h. Profesion \n i.cedulas \n j.equipos \n k.carros \n l.correos \n m.colores \n--> Opcion : ")
        if op not in campos:
            print("\n Opcion incorrecta , volver a ingresar la opcion \n")
        else:
            op =op.lower()
            break
    return op
#Leemos los archivos
def abrir_archivo(archivo):
    #Creamos una lista y añadimos cada archivo
    lista=list()
    #Abrimos el archivo
    with open(archivo,'r',encoding="utf8") as f:
        #Leemos linea por linea el .txt
        for linea in f:
                #Le quitamos el salto de linea
            linea=linea.rstrip("\n")
            #Le quitamos los espacios en blanco, si es diferente de equipos ya que estos 
            # pueden contener espacios en la mitad del string
            if archivo!="equipos.txt":
                linea=linea.replace(" ","")
        
            lista.append(linea)
    #Retornamos la lista
    return lista 
def genera_aleatorio(archivo):
    aleatorio=len(archivo)-1
    aleatorio=random.randint(0,aleatorio)
    return aleatorio
#Lo codificamos
encoding='utf8'
#archivo_datos=io.open(concatenar,"w",encoding=encoding)
campos=list()
print("Bienvenidos al generador de datos 1.0 \n Creadores : .....")
#Validamos el separador
while True:
    separador=input("¿Cual es el separador?\n\t")
    if separador=="/":
        print("El separador no puede ser / porque genera inconsistencias en las fechas")
    elif separador==" ":
        print("El separador no puede ser un espacio porque genera inconsistencias")
    else:
        break
#Cuantos campos va a generar
campos_generar=int(input(" ¿ Cuantos campos va a generar ? \n\t"))
arreglo=list()
dic={
    "a":"nombres.txt",
    "b":"apellidos.txt",
    "c":{
        1:"fechas_tipo1_dd-mm-yyyy.txt",
        2:"fechas_tipo_2-yyyy-mm-dd.txt",
        3:"fechas_tipo_3-mm-dd-yyyy.txt"
    },
    "d":{
        "minimo":0,
        "maximo":0
    },
    "e":{
        "minimo":0,
        "maximo":0,
        "decimales":0.0
    },
    "f":{
        "#":[0,1,2,3,4,5,6,7,8,9],
        "C":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
        "patron":""
    },
    "g":"ciudades.txt",
    "h":"profesiones.txt",
    "i":"cedulas.txt",
    "j":"equipos.txt",
    "k":"carros.txt",
    "l":"correos.txt",
    "m":"colores.txt"
}
#Lo que falta es preguntar al usuario cada campo y eso se hace con la funcion valida_campo eso se guarda en una lista 
#para que posteriormente sea leida por indice para hacer el random e insertar en el .txt que se desea
for i in range(campos_generar):
    #No puede escoger el mismo campo 2 veces
    while True: 
        valor=valida_campo()
        #Validamos que el campo que desee agregar ya no este seleccionado
        if valor not in arreglo:
            print("Se agrega el campo a generar {}".format(valor))
            arreglo.append(valor)
            #Si el escogido es c entonces es fechas
            if valor=='c':
                print("¿Que formato?")
                #El user escoge el formato de las fechas
                while True:
                    print("\ta.dd/mm/yyyy\n\tb.yyyy/mm/dd\n\tc.mm/dd/yyyy ")
                    escogido_fecha=input()
                    if escogido_fecha=='a':
                        fechas=dic["c"][1]
                        fechas_ar=abrir_archivo(fechas)
                        #print(fechas_ar)
                        break  
                    elif escogido_fecha=='b':
                        fechas=dic["c"][2]
                        fechas_ar=abrir_archivo(fechas)
                        #print(fechas_ar)
                        break 
                    elif escogido_fecha=='c':
                        fechas=dic["c"][3]
                        fechas_ar=abrir_archivo(fechas)
                        #print(fechas_ar)
                        break 
                    else:
                        print("No ha escogido las fechas solicitadas recordar que es de a , b o c")
            elif valor=="d":  
                valor_maximo=int(input("\tDigite el valor maximo: "))
                while True:
                    valor_minimo=int(input("\tDigite el valor minimo: "))
                    if valor_minimo>valor_maximo:
                        print("\tDigite bien las cosas un minimo no puede ser mayor que el maximo")
                    else:
                        break
                dic["d"]["minimo"]=valor_minimo
                dic["d"]["maximo"]=valor_maximo
            elif valor=="e":
                valor_maximo=float(input("\tDigite el valor maximo: "))
                #Validamos que el valor minimo no sea mayor que el valor maximo
                while True:
                    valor_minimo=float(input("\tDigite el valor minimo: "))
                    if valor_minimo>valor_maximo:
                        print("\tDigite bien las cosas un minimo no puede ser mayor que el maximo")
                    else:
                        break
                #Preguntamos el numero de decimales
                decimales=int(input("\tDigite la cantidad de decimales: "))
                #Cada uno de esos valores los añadimos al diccionario para luego generar los datos random
                dic["e"]["minimo"]=valor_minimo
                dic["e"]["maximo"]=valor_maximo
                dic["e"]["decimales"]=decimales
            #Si es f es el patron
            elif valor=="f":
                patron=input("\nEscriba el patron\n\t->")
                #Reemplazamos ese string vacio que declaramos con anterioridad en el diccionario
                dic["f"]["patron"]=patron
            break
        else:
            print("No se puede generar ese campo porque ya ha sido agregado ")
#Comenzamos a llenar los valores
#pprint(dic)
#Leemos el arreglos para comenzar a crear las listas solicitadas
for i in arreglo:
    if i=="a":
        nombres=abrir_archivo(dic["a"])
        #print(nombres)
    elif i=="b":
        apellidos=abrir_archivo(dic["b"])
        #print(apellidos)
    elif i=="g":
        ciudades=abrir_archivo(dic["g"])
        #print(ciudades)
    elif i=="h":
        profesion=abrir_archivo(dic["h"])  
        #print(profesion)  
    elif i=='i':
        cedulas=abrir_archivo(dic["i"])  
    elif i=="j":
        equipos=abrir_archivo(dic["j"])
    elif i=="k":
        carros=abrir_archivo(dic["k"])
    elif i=="l":
        correos=abrir_archivo(dic["l"])
    elif i=="m":
        colores=abrir_archivo(dic["m"])
#Añadimos las listas al arreglo general para ser mejor optimizado
arr2=list()
for i in arreglo:
    if i=="a":
        arr2.append(nombres)
    elif i=="b":
        arr2.append(apellidos)
    elif i=="c":
        arr2.append(fechas_ar)
    elif i=="d":
        valores=list()
        valores.append("entero")
        valores.append(dic["d"]["minimo"])
        valores.append(dic["d"]["maximo"])
        arr2.append(valores)
    elif i=="e":
        valores=list()
        valores.append("real")
        valores.append(dic["e"]["minimo"])
        valores.append(dic["e"]["maximo"])
        valores.append(dic["e"]["decimales"])
        arr2.append(valores)
    elif i=="f":
        valores=list()
        valores.append("patron")
        valores.append(dic["f"]["#"])
        valores.append(dic["f"]["C"])
        valores.append(dic["f"]["patron"])
        arr2.append(valores)
    elif i=="g":
        arr2.append(ciudades)
    elif i=="h":
        arr2.append(profesion)
    elif i=="i":
        arr2.append(cedulas)
    elif i=="j":
        arr2.append(equipos)
    elif i=="k":
        arr2.append(carros)        
    elif i=="l":
        arr2.append(correos)
    elif i=="m":
        arr2.append(colores)
    
#print("Digite el nombre del archivo plano")
nombre_archivo=input("Digite el nombre del archivo plano\n\t -> ")
#Creamos y abrimos el archivo plano

extension=".txt"
print(extension)
if ".txt" in nombre_archivo:
    archivo_datos=io.open(nombre_archivo,"w",encoding=encoding)
else:
    print("No tiene el .txt se agrega " )
    nombre_archivo+=".txt"
    archivo_datos=io.open(nombre_archivo,"w",encoding=encoding)
registros=int(input("Digite los registros a generar\n\t -> "))
#Comenzamos a insertar los registros en el archivo plano
valor=0
for i in range(registros):
    #Insertamos cada registros
    arr3=list()
    for i in arr2:
        #print(i)
        if i[0]=="entero":
            #Le asignamos un valor random 
            entero=random.randint(i[1],i[2])
            #print("El numero entero es {} ".format(entero))
            arr3.append(entero)
        elif i[0]=="real":
            #Generamos un numero aleatorio
            real=random.uniform(i[1],i[2])
            #Redondeamos ese numero aleatorio a lo que digito el user
            real=round(real,i[3])
            arr3.append(entero)
            #print(real)
        elif i[0]=="patron":
            numero_aleatorio=random.randint(0,9)
            #Cantidad de letas -1 para que no se salga del rango
            cantidad_letras=len(i[2])-1
            indice_al=random.randint(0,cantidad_letras)
            letra_al=i[2][indice_al]
            patron=i[3]
            patron=patron.replace("C",str(numero_aleatorio))
            patron=patron.replace("#",letra_al)
            #print(letra_al,numero_aleatorio,patron)
            arr3.append(patron)
        else:
            aleatorio_valor=genera_aleatorio(i)
            valor_aleatorio=i[aleatorio_valor]
            arr3.append(valor_aleatorio)
    registro=""
    valor=0
    for i in arr3:
        if valor==0:
            registro+=i
            valor=1
        else:
            registro+="{}{}".format(separador,i)
    #print(registro)
    archivo_datos.write("{}\n".format(registro))
archivo_datos.close()
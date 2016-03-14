import csv#importar librerias para archivos CSV
import math#importar libreria para funciones matematicas
import os#importar libreria del sistema operativo
import Caracteristicas#importar Caracteristicas.py
def Clasificacion():#asignamos el nombre de la función
    img,tam,mat,imgplot=Caracteristicas.datos()#llamamos a la función datos que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)#llamamos a la función RazonFilascolumnas que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)#llamamos a la función RazonPixelesBlancos que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)#llamamos a la función CambiosPrimeraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)#llamamos a la función CambiosSegundaLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)#llamamos a la función CambiosTerceraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno   
    contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)#llamamos a la función CambioPrimeraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)#llamamos a la función CambioSegundaLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)#llamamos a la función CambioTerceraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)#llamamos a la función ContarPixelesPrimeraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)#llamamos a la función ContarPixelesSegundaLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)#llamamos a la función ContarPixelesTerceraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)#llamamos a la función ContarPixelesPrimeraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)#llamamos a la función ContarPixelesSegundaLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)#llamamos a la función ContarPixelesTerceraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    
    abrir= open('DataSet.csv')#la variable abrir contendra todos los datos que se encuentran en el dataset
    leer_dataset=csv.reader(abrir)#la variable leer_dataset contriene los datos que se encuentran en abrir
    dataset=list(leer_dataset)#la variable dataset contendra el dataset en forma de lista
    print("\n\nIngrese lo que se pide a continuación")#impresión de pantalla
    print("\n\nNumero de vecinos a considerar: ",end="")#impresión de pantalla
    numeroKVecinos=int(input())#la variabl numeroKVecinos contendra el numero de vecinos que evaluaremos
    os.system("cls")#limpieza de pantalla
    contador=0#variable contado
    for i in dataset:#for que recorre el dataset en todas sus posiciones
        dataset[contador][0]=float(dataset[contador][0])#convertirmos a flotante el dataset en la posicion [contador][0]
        dataset[contador][1]=int(dataset[contador][1])#convertirmos a entero dataset en la posicion [contador][1]
        dataset[contador][2]=int(dataset[contador][2])#convertirmos a entero dataset en la posicion [contador][2]
        dataset[contador][3]=int(dataset[contador][3])#convertirmos a entero dataset en la posicion [contador][3]
        dataset[contador][4]=int(dataset[contador][4])#convertirmos a entero dataset en la posicion [contador][4]
        dataset[contador][5]=int(dataset[contador][5])#convertirmos a entero dataset en la posicion [contador][5]
        dataset[contador][6]=int(dataset[contador][6])#convertirmos a entero dataset en la posicion [contador][6]
        dataset[contador][7]=int(dataset[contador][7])#convertirmos a entero dataset en la posicion [contador][7]
        dataset[contador][8]=int(dataset[contador][8])#convertirmos a entero dataset en la posicion [contador][8]
        dataset[contador][9]=int(dataset[contador][9])#convertirmos a entero dataset en la posicion [contador][9]
        dataset[contador][10]=int(dataset[contador][10])#convertirmos a entero dataset en la posicion [contador][10]
        dataset[contador][11]=int(dataset[contador][11])#convertirmos a entero dataset en la posicion [contador][11]
        dataset[contador][12]=int(dataset[contador][12])#convertirmos a entero dataset en la posicion [contador][12]
        dataset[contador][13]=int(dataset[contador][13])#convertirmos a entero dataset en la posicion [contador][13]
        dataset[contador][14]=int(dataset[contador][14])#convertirmos a entero dataset en la posicion [contador][14]
        dataset[contador][15]=int(dataset[contador][15])#convertirmos a entero dataset en la posicion [contador][15]
        
        #Aplicamos la formula para obtener la distancia Euclidiana, es decir una sumatoria de cada caracteristica del dataset menos cada caracteristica de la imagen a clasificar       
        distancia=(((dataset[contador][0]-razonFilasEntreColumnas)**2)+
        ((dataset[contador][1]-contarPixelesBlancos)**2)+
        ((dataset[contador][2]-contarCambiosPrimeraLineaHorizontal)**2)+
        ((dataset[contador][3]-contarCambiosSegundaLineaHorizontal)**2)+
        ((dataset[contador][4]-contarCambiosTerceraLineaHorizontal)**2)+
        ((dataset[contador][5]-contarCambiosPrimeraLineaVertical)**2)+
        ((dataset[contador][6]-contarCambiosSegundaLineaVertical)**2)+
        ((dataset[contador][7]-contarCambiosTerceraLineaVertical)**2)+
        ((dataset[contador][8]-contarPixelesPrimeraLineaHorizontal)**2)+
        ((dataset[contador][9]-contarPixelesSegundaLineaHorizontal)**2)+
        ((dataset[contador][10]-contarPixelesTerceraLineaHorizontal)**2)+
        ((dataset[contador][11]-contarPixelesPrimeraLineaVertical)**2)+
        ((dataset[contador][12]-contarPixelesSegundaLineaVertical)**2)+
        ((dataset[contador][13]-contarPixelesTerceraLineaVertical)**2))
        raiz=math.sqrt(distancia)#la segunda parte de la formula es obtener la raiz cuadrada de la sumatoria
        dataset[contador].append(raiz)#agregamos una nueva fila a nuestra matriz que contendra la raiz cuadrada de cada instancia
        contador+=1#sumamos un numero al contador
    dataset.sort(key=lambda dataset: dataset[14],reverse=True)#aplicamos la funcion sort para ordenar el dataset de acuerdo al numero total de instancias
    print ("\tInformacón del DataSet")#impresión de pantalla 
    print ("No. Total de instancias: ", dataset [0][14])#se imprimen el número total de instancias    
    dataset.sort(key=lambda dataset: dataset[16])#aplicamos nuevo sort para ordenarlo de acuerdo a la distancia
    print("Instancia del K vecino mas cercano: ", dataset[0][14])#imprimimos el numero  de la instancia con la distancia mas cercana a nuestra imagen
    print ("\nK vecinos mas cercanos:")#Impresion de pantalla
    for k_Vecinos_Cercanos in range (0,numeroKVecinos):#numero de kvecinos que deberan imprimirse
        print ("Instancia:", dataset[k_Vecinos_Cercanos][14], "\tDistancia:","%.4f" %dataset[k_Vecinos_Cercanos][16], "    Clase", dataset[k_Vecinos_Cercanos][15])#impresion de los k vecinos mas cercanos
    return dataset, numeroKVecinos#valores que regresa la funcion clasificacion  
    
def instancias():#nombre de la función
    dataset,numeroKVecinos = Clasificacion()#llamamos a la funcion clasificacion y los valores de retorno son almacenados en dos variables
    clase0=0#variable de tipo int
    clase1=0#variable de tipo int
    clase2=0#variable de tipo int
    clase3=0#variable de tipo int
    clase4=0#variable de tipo int
    clase5=0#variable de tipo int
    clase6=0#variable de tipo int
    clase7=0#variable de tipo int
    clase8=0#variable de tipo int
    clase9=0#variable de tipo int
    
    numero_filas=10#variable de tipo int
    numero_columnas=2#variable de tipo int
    clase_final = []#creamos un arreglo
    for filas in range(numero_filas):#limitaremos el numero de filas a 10
        clase_final.append([])#agregaremos mas filas a nuestas matriz
        for columnas in range(numero_columnas):#limitaremos el numero de columnas a 2
            clase_final[filas].append(None)#agregamos nuevas columnas a nuestra matriz     
    
    for caracteristica in range(0,numeroKVecinos):#sumaremos el numero de vecinos que deseamos ver impresos
        if(dataset[caracteristica][15]==0):#condicion para determinar si en una posicion es igual a 0
            clase0=clase0+1#sumamos uno a nuestro contador         
        if(dataset[caracteristica][15]==1):#condicion para determinar si en una posicion es igual a 1
            clase1=clase1+1#sumamos uno a nuestro contador #sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==2):#condicion para determinar si en una posicion es igual a 2
            clase2=clase2+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==3):#condicion para determinar si en una posicion es igual a 3
            clase3=clase3+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==4):#condicion para determinar si en una posicion es igual a 4
            clase4=clase4+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==5):#condicion para determinar si en una posicion es igual a 5
            clase5=clase5+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==6):#condicion para determinar si en una posicion es igual a 6
            clase6=clase6+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==7):#condicion para determinar si en una posicion es igual a 7
            clase7=clase7+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==8):#condicion para determinar si en una posicion es igual a 8
            clase8=clase8+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==9):#condicion para determinar si en una posicion es igual a 9
            clase9=clase9+1#sumamos uno a nuestro contador 
            
    clase_final[0]=clase0,0#llenamos nuestra matriz clase_final con los valores de la clase y el numero 0
    clase_final[1]=clase1,1#llenamos nuestra matriz clase_final con los valores de la clase y el numero 1
    clase_final[2]=clase2,2#llenamos nuestra matriz clase_final con los valores de la clase y el numero 2
    clase_final[3]=clase3,3#llenamos nuestra matriz clase_final con los valores de la clase y el numero 3
    clase_final[4]=clase4,4#llenamos nuestra matriz clase_final con los valores de la clase y el numero 4
    clase_final[5]=clase5,5#llenamos nuestra matriz clase_final con los valores de la clase y el numero 5
    clase_final[6]=clase6,6#llenamos nuestra matriz clase_final con los valores de la clase y el numero 7
    clase_final[7]=clase7,7#llenamos nuestra matriz clase_final con los valores de la clase y el numero 8
    clase_final[8]=clase8,8#llenamos nuestra matriz clase_final con los valores de la clase y el numero 9
    clase_final[9]=clase9,9#llenamos nuestra matriz clase_final con los valores de la clase y el numero 10
    
    clase_final.sort(key=None, reverse=True)#aplicamos sort a nuestra matriz clase_final dejando al principio el numero mayor
    print ("\nNúmero de Instancias por clase: ")#impresion de pantalla
    for conteo_instancias in range(0,10):#contaremos el numero de instancias
            print ("",clase_final[conteo_instancias][0],
            "   Instancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\n\nLa imagen es un :", clase_final[0][1]) #impresion de pantalla del numero de instancias
    
    
    
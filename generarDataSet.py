import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import os #importamos librerias de sistema operativo
import csv #importamos libreria para archivos csv
import Caracteristicas #importamos el archivo Caracteristicas.py
def DataSet():#asignamos el nombre de la funcion
    root="arialSegmented"#Es la ruta de la carpeta en donde estan almacenados los números
    archivo= open ("DataSet.csv", "w",newline='')#creamos un nuevo archivo .csv con el nombre de DataSet.csv    
    salida=csv.writer(archivo)#variable que nos permite escribir en un archivo csv
    clase=-1#varialbe de tipo int
    posiciones_dataset=0#variable de tipo int
    for dirName, subdirlist, filelist in os.walk(root):#este for recorre todas la carpetas y subcarpetas de la ruta
        for fname in filelist:#aqui se leen los archivos que se encuentran en las subcarpetas
            posiciones_dataset=posiciones_dataset+1#aumentamos en uno el valor de la posicion
            nameima=dirName+'/'+fname #entramos a una nueva subcarpeta
            print("Generando DataSet....")#impresión de pantalla
            img=mpimg.imread(nameima)#leemos una imagen
            mat=img#declaramos una matriz y la igualamos a la imagen 
            tam=mat.shape#obtenemos las medidas de la imagen en alto y ancho
            #aqui representa todos los returns y manda a llamar a todas las funciones
            razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)#se obtiene la 1ra característica que es razon de filas y columnas
            contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)#se obtiene la 2da característica que es razon de pixeles blancos
            contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)#se obtiene la 3ra característica que es cambios en la primera linea horizontal   
            contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)#se obtiene la 4ta característica que es cambios en la segundaa linea horizontal 
            contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)#se obtiene la 5ta característica que es cambios en la tercera linea horizontal 
            contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)#se obtiene la 6ta característica que es cambios en la primera linea vertical
            contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)#se obtiene la 7ma característica que es cambios en la segundaa linea vertical
            contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)#se obtiene la 8va característica que es cambios en la tercera linea vertical
            contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)#se obtiene la 9na característica que es contar pixeles en 1 de la primera linea horizonntal
            contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)#se obtiene la 10ma característica que es contar pixeles en 1 de la segunda linea horizonntal
            contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)#se obtiene la 11va característica que es contar pixeles en 1 de la tercera linea horizonntal
            contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)#se obtiene la 13va característica que es contar pixeles en 1 de la primera linea vertical
            contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)#se obtiene la 14va característica que es contar pixeles en 1 de la segunda linea vertical
            contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)#se obtiene la 9na característica que es contar pixeles en 1 de la tercera linea vertical
            #aqui se escribe el dataset en el archivo de excel 
            salida.writerow([razonFilasEntreColumnas,contarPixelesBlancos,contarCambiosPrimeraLineaHorizontal,contarCambiosSegundaLineaHorizontal,contarCambiosTerceraLineaHorizontal,contarCambiosPrimeraLineaVertical,contarCambiosSegundaLineaVertical,contarCambiosTerceraLineaVertical,contarPixelesPrimeraLineaHorizontal,contarPixelesSegundaLineaHorizontal,contarPixelesTerceraLineaHorizontal,contarPixelesPrimeraLineaVertical,contarPixelesSegundaLineaVertical,contarPixelesTerceraLineaVertical,posiciones_dataset,clase])
        clase=clase+1#aumentamos en uno al contador
        os.system("cls")#limpiamos pantalla
    print ("El DataSet esta listo....!!!!")#impresion de pantalla            
    archivo.close()#dejamos de escribir en el dataset

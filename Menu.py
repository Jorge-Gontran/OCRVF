import KNN #importamos el KNN.py para realizar la clasificacion
import generarDataSet #importamos Dataset para la creacion del nuestro Dataset
import os #importamos os para usar comandos propios del Sistema Operativo
print ("Inserte un número:")#impresion del pantalla
opcion=int(input ("1.-Generar Dataset\n2.-Clasificar Imagen\n3.-Salir\n"))#se muestran las opciones del menu y se gurdan en una variable
os.system("cls")#limpia la pantalla
if(opcion<1 or opcion>3):#el número que insertemos no debera ser menor a 1 ni mayor a 3
    print("Error")#si el número insertado no es válido se mostrara esta excepción
if (opcion==1):#si la opción es igual a 1
    generarDataSet.DataSet()#se mandara a llamar la función DataSet que se encuentra en el programa generarDataSet.py
if (opcion==2):#si la opción es igual a 2 
    KNN.instancias()#se manda a llamar a la función instancias que se encuentra el programa KNN.py
if(opcion==3):#si la opción es igual a 3
    os.system("cls")#se limpiara la pantalla 

import matplotlib.pyplot as plt#importamos la libreria pyplot
import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import os #importamos librerias de sistema operativo

def datos():#se asigna el nombre de la función
    print("Inserte el nombre de la imagen: ")#impresion de pantalla
    nombre_imagen=(input())#variable de tipo int
    os.system("cls")#limpiar pantalla
    img=mpimg.imread(nombre_imagen)#leemos la imagen y guardamos en una variable
    imgplot=plt.imshow(img)#copiamos la variable img en imgplot
    mat=img#declaramos una matriz y la igualamos a la imagen 
    tam=img.shape#obtenemos las medidas de la imagen en alto y ancho
    return img,tam,mat,imgplot #regresamos 4 variables

def RazonFilascolumnas(tam):#se asigna el nombre de la función
    razonFilasEntreColumnas=tam[0]/tam[1]#se declara una variable en donde se almacenara el resultado y posteriormente se realiza la operación
    return razonFilasEntreColumnas#regresamos el valor de la primera característica
      
def RazonPixelesBlancos(tam,mat):#se asigna el nombre de la función
    contarPixelesBlancos=0#se declara un contador y se iguala a cero
    for i in range(0,tam[0]):#Se recorre la matriz a lo alto es decir la columnas
       for j in range(0,tam[1]):#se recorre la matriz a lo ancho es decir las filas
           if(mat[i][j]!=0):#revisamos el numero de pixeles que tiene la matriz
              contarPixelesBlancos=contarPixelesBlancos+1#cada vez que los pixeles de la matriz sean blancos se iran almacenando en esta variable
    return contarPixelesBlancos#regresamos el valor de la segunda caracteristica
    
def CambiosPrimeraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionPrimeraLineaHorizontal=int(tam[0]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosPrimeraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionPrimeraLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionPrimeraLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[posicionPrimeraLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosPrimeraLineaHorizontal=contarCambiosPrimeraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionSegundaLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosPrimeraLineaHorizontal#regresamos el valor de la tercera característica
    
def CambiosSegundaLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionSegundaLineaHorizontal=int(tam[0]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosSegundaLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionSegundaLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionSegundaLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtariz
            aux=img[posicionSegundaLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosSegundaLineaHorizontal=contarCambiosSegundaLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionSegundaLineaHorizontal][i]=1 #la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosSegundaLineaHorizontal#regresamos el valor de la cuarta característica
    
def CambiosTerceraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionTerceraLineaHorizontal=int((tam[0]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosTerceraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionTerceraLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionTerceraLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[posicionTerceraLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosTerceraLineaHorizontal=contarCambiosTerceraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionTerceraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosTerceraLineaHorizontal#regresamos el valor de la quinta característica
    
def CambioPrimeraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionPrimeraLineaVerticalal=int(tam[1]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosPrimeraLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionPrimeraLineaVerticalal]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionPrimeraLineaVerticalal]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionPrimeraLineaVerticalal]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosPrimeraLineaVertical=contarCambiosPrimeraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][contarCambiosPrimeraLineaVertical]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios    
    return contarCambiosPrimeraLineaVertical#regresamos el valor de la sexta característica
    
def CambioSegundaLineaVertical(tam,img):#se asigna el nombre de la función
    posicionSegundaLineaVertical=int(tam[1]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosSegundaLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionSegundaLineaVertical]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionSegundaLineaVertical]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionSegundaLineaVertical]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosSegundaLineaVertical=contarCambiosSegundaLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionSegundaLineaVertical]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosSegundaLineaVertical#se regresa el  valor de la septima característica
      
def CambioTerceraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionTerceraLineaVertical=int((tam[1]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosTerceraLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionTerceraLineaVertical]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionTerceraLineaVertical]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionTerceraLineaVertical]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosTerceraLineaVertical=contarCambiosTerceraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionTerceraLineaVertical]#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosTerceraLineaVertical#se regresa el  valor de la octava característica
    
def ContarPixelesPrimeraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionprimeraLineaHorizontal = int(tam[0]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesPrimeraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionprimeraLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            contarPixelesPrimeraLineaHorizontal=contarPixelesPrimeraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionprimeraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesPrimeraLineaHorizontal#se regeresa el valor de la novena caracteristica
    
def ContarPixelesSegundaLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionsegundaLineaHorizontal=int(tam[0]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesSegundaLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionsegundaLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesSegundaLineaHorizontal=contarPixelesSegundaLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionsegundaLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesSegundaLineaHorizontal#se regeresa el valor de la decima caracteristica
    
def ContarPixelesTerceraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionterceraLineaHorizontal=int((tam[0]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesTerceraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionterceraLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesTerceraLineaHorizontal=contarPixelesTerceraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionterceraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesTerceraLineaHorizontal#se regeresa el valor de la onceava caracteristica
    
def ContarPixelesPrimeraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionprimeraLineaVertical=int(tam[1]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesPrimeraLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionprimeraLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesPrimeraLineaVertical=contarPixelesPrimeraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionprimeraLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesPrimeraLineaVertical#se regeresa el valor de la doceava caracteristica
    
def ContarPixelesSegundaLineaVertical(tam,img):#se asigna el nombre de la función
    posicionsegundaLineaVertical=int(tam[1]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesSegundaLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionsegundaLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesSegundaLineaVertical=contarPixelesSegundaLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionsegundaLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesSegundaLineaVertical#se regeresa el valor de la treceava caracteristica
    
def ContarPixelesTerceraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionterceraLineaVertical=int((tam[1]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesTerceraLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionterceraLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesTerceraLineaVertical=contarPixelesTerceraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionterceraLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesTerceraLineaVertical#se regresa el valor de la característica 14
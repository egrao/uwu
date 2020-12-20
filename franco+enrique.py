import os
os.system('cls')

lista=[]
lista2=[]
listaDisparosJ1=[]
listaDisparosJ2=[]
listaLetras=["a","b","c","d","e","f","g","h","i","j"]
dictDianas1={}
dictDianas2={}
numero=10
contadorjugador1=0
contadorjugador2=0  #15/12/2020  variable declarada para limitar barcos jugador2
contadorBarco1,contadorBarco2,contadorBarco3,contadorBarco4 = 0,0,0,0
contadorBarco5,contadorBarco6,contadorBarco7,contadorBarco8 = 0,0,0,0 #segunda declaración de variables para referirnos a la cantidad de barcos del jugador 2
def mostrarBienvenida():
    print("---------------------------------------------------------------------")
    print("+++++++++++++++++ Bienvenido a Battleship en Python +++++++++++++++++")
    print("---------------------------------------------------------------------")
    print("+++++++++++++++++++++++ Para 2 jugadores <3 ++++++++++++++++++++++++")#<3
    print("\n")


def validarCoordenada(coordenada):
    while coordenada.lower() not in lista:
        print("Esa casilla está ocupada o no existe(smh), prueba otra vez: ")
        coordenada=str(input())
    return coordenada.lower()

def hacerTablero(lista,listaLetras):
    for i in listaLetras:
        for j in range(1,numero+1):
            lista_posiciones = (i+str(j))   # aqui convertimos la cadena de 1-10 a str para poder referirnos a la posicion en el tablero de forma visual
            lista.append(lista_posiciones)

def mostrarTablero(lista):
    listaFila = ["A","B","C","D","E","F","G","H","I","J"]   #esta lista se utilizara para imprimir a principio de linea las letras para el tablero
    x=0     #este auxiliar lo coloco aqui para poder referirme a la posicion de la lista que quiero que se imprima, asi puedo ir imprimiendo las filas
    for i in range(10):
        print("  ",i+1,end=" ")
    for i in range(len(lista)):
        if i%numero == 0:
            print("\n")
        if i == 0 or i%10 == 0:
            print (listaFila[x],end=" ")
            x+=1            #aqui incrementando la variable de fila para ir a la siguiente letra
        if lista[i] == "B":
            print("|B|",end="  ")
        elif lista[i] == "X":
            print("|X|",end="  ")
        elif lista[i] == "O":
            print("|O|",end="  ")   #he quitado las barras para que se vea mejor el AGUA, pero podemos buscar algo mas guay.
        else:
            print("|_|",end="  ")
    print("\n")

def evaluarBarcos(lista,opcion,dictDianas):
    print(opcion)
    global contadorBarco1,contadorBarco2,contadorBarco3,contadorBarco4
    global contadorBarco5,contadorBarco6,contadorBarco7,contadorBarco8
    if opcion ==2:  #<------  15/12/2020  aqui traigo el numero de la opcion desde el menu, para saber que camino cogemos, digamos si es el colocar barco del jugador 1 o del jugador 2
        print("Elige la longitud del barco que quieres colocar (1, 2, 3 o 4): ")
        longitud=int(input())
        while 0> longitud > 4 :
            print("Whoops, respuesta incorrecta. Inténtalo otra vez: ")
            longitud=int(input())
        
        # aqui se ha decidido dejar este trozo de funcion repetida y no en funcion, dado que asi podemos incrementar o decrementar la cantidad de barcos que queramos colocar de cada tipo
        if longitud == 1 and contadorBarco1 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco1 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:   # finalmente decidimos ponerlo dentro, es mas facil y ahorramos vueltas al programa de evaluar condiciones
                contadorBarco1+=1       # aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco2 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco2 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco2+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco3 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco3 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco3+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco4 <= 2: #aqui se evalua la cantidad de barcos colocados, permitimos 2 barcos de 1
            if contadorBarco4 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco4+=1       #******** aqui ira una vez la llamada en caso de poder ser
                colocarBarco(lista,longitud,dictDianas)
    
    
    if opcion ==4:  # aqui traemos el numero de la opcion desde el menu, para saber que camino cogemos, digamos si es el colocar barco del jugador 1 o del jugador 2
        print("Elige la longitud del barco que quieres colocar (1, 2, 3 o 4): ")
        longitud=int(input())
        while 0> longitud > 4 :
            print("Whoops, respuesta incorrecta. Inténtalo otra vez: ")
            longitud=int(input())
        
        if longitud == 1 and contadorBarco5 <= 2: 
            if contadorBarco5 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:  
                contadorBarco5+=1       
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 2 and contadorBarco6 <= 2: 
            if contadorBarco6 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco6+=1       
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 3 and contadorBarco7 <= 2: 
            if contadorBarco7 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco7+=1       
                colocarBarco(lista,longitud,dictDianas)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if longitud == 4 and contadorBarco8 <= 2: 
            if contadorBarco8 == 2:
                print("Ya has colocado todo los barcos de esta medida.")
            else:
                contadorBarco8+=1       
                colocarBarco(lista,longitud,dictDianas)
    
    return lista            

def colocarBarco(lista,longitud,dictDianas):
    if longitud==1:
        disposicionBarco=None #no hace falta usar vert/horiz para los de 1
    elif longitud>1:
        disposicionBarco=input("¿Colocar barco en horizontal o vertical? (ej: H o V): ")

    inicioBarco=True
    while inicioBarco:
        print("Introduce la coordenada inicial del barco")
        coordenadaInicial=str(input()) 
        coordenadaInicial=validarCoordenada(coordenadaInicial)
        if longitud==1:
            dictDianas[coordenadaInicial.lower()]=(lista.index(coordenadaInicial.lower()))
            lista[lista.index(coordenadaInicial.lower())]="B"
              #si es un barco de 1, al pasar el while que comprueba la casilla dentro del tablero y disponible pues la asigna como "B" y sale de la función.
            inicioBarco=False
        elif longitud>1:

            print("Introduce la coordenada final del barco")
            coordenadaFinal=str(input())
            coordenadaFinal=validarCoordenada(coordenadaFinal)
            # a partir de aqui vamos a comprobar que las posiciones esten a la misma distancia que la longitud
            listaInicioFinal=[]
            listaInicioFinal.append(lista.index(coordenadaInicial.lower()))
            listaInicioFinal.append(lista.index(coordenadaFinal.lower()))

            # distancia--> (indice de coordenada final == longitud-1  + indice de la coordenada inicial)
            #aqui tenemos un if para barcos en v y otro para horiz.
            # pero ambos comprueban que el barco sea correcto(la primera y la ultima estén a la distancia adecuada, si es un barco imposible te lleva al else que reinicia TODO el bucle y metes coord.inicio y final de nuevo)
            if disposicionBarco.lower()=="h" and (sorted(listaInicioFinal)[0])+(longitud-1)==sorted(listaInicioFinal)[-1]:
                if lista[sorted(listaInicioFinal)[0]+1]!="B" and lista[sorted(listaInicioFinal)[-1]-1]!="B":
                    for i in range(longitud):
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i]]=(sorted(listaInicioFinal)[0]+i)
                        lista[sorted(listaInicioFinal)[0]+i]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")

            elif disposicionBarco.lower()=="v" and (sorted(listaInicioFinal)[-1])-sorted(listaInicioFinal)[0]==(longitud-1)*10:
                if lista[sorted(listaInicioFinal)[0]+10]!="B" and lista[sorted(listaInicioFinal)[-1]-10]!="B":
                    for i in range(longitud):
                        dictDianas[lista[sorted(listaInicioFinal)[0]+i*10]]=(sorted(listaInicioFinal)[0]+i*10)
                        lista[sorted(listaInicioFinal)[0]+i*10]="B"
                    inicioBarco=False
                else:
                    print("Son barcos, no transformers, no los pongas encima de otros barcos. Vuelve a intentarlo")


            else:
                print("FAIL! Vuelve a colocar el barco/El barco no cabe ahí, try again.")

def comenzarPartida(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2):
    jugar = True
    while jugar:
        turno1=True
        turno2=True
        while turno1:
            os.system('cls')
            print("Jugador 1. Introduce coordenada donde disparar: ")
            mostrarJuntos(lista,listaDisparosJ1)
            jugada1=str(input(">"))
            while (jugada1.lower() not in lista2) and (jugada1.lower() not in dictDianas2) :
                print("Apunta mejor, te has salido del tablero. Prueba otra vez: ")
                jugada1=str(input())
            if jugada1.lower() in dictDianas2:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="X"
                lista2[dictDianas2[jugada1.lower()]]="X"
                dictDianas2.pop(jugada1.lower())
                print("¡Diana! ",end="")
                if len(dictDianas2) == 0:
                    print("Victoria")
                    jugar=False
                    turno1=False
                    turno2=False
                else:
                    input("Press any key para disparar otra vez.")
                
            else:
                listaDisparosJ1[listaDisparosJ1.index(jugada1.lower())]="O"
                print("Agua, no has hecho diana. ")
                input("Press any key to continue.")
                turno1=False       
        while turno2:
            os.system('cls')
            print("Jugador 2. Introduce coordenada donde disparar: ")
            mostrarJuntos(lista2,listaDisparosJ2)
            jugada2=str(input(">"))
            while (jugada2.lower() not in lista) and (jugada2.lower() not in dictDianas1) :
                print("Apunta mejor, te has salido del tablero. Prueba otra vez: ")
                jugada2=str(input())
            if jugada2.lower() in dictDianas1:
                listaDisparosJ2[listaDisparosJ2.index(jugada2.lower())]="X"
                lista[dictDianas1[jugada2.lower()]]="X"
                dictDianas1.pop(jugada2.lower())
                print("Diana! ",end="")
                if len(dictDianas1) == 0:
                    print("Victoria")
                    jugar=False
                    turno1=False
                    turno2=False
                else:
                    input("Press any key para disparar otra vez.")
            else:
                listaDisparosJ2[listaDisparosJ2.index(jugada2.lower())]="O"
                print("Agua, no has hecho diana. ")
                input("Press any key to continue.")
                turno2=False

def mostrarJuntos(listaA,listaB):
    auxiliar=0
    listaFila = ["A","B","C","D","E","F","G","H","I","J"]   #esta lista se utilizara para imprimir a principio de linea las letras para el tablero
    x=0     #este auxiliar lo coloco aqui para poder referirme a la posicion de la lista que quiero que se imprima, asi puedo ir imprimiendo las filas
    # print("                           TABLERO MIO                                                      TABLERO ENEMIGO       ")
    # print("\n")
    print("           ",end="")
    for i in range(10):
        print("  ",i+1,end=" ")
    print("            ",end="")
    for i in range(10):
        print("  ",i+1,end=" ")
    print("\n")
    
    for i in range(101):
        # if i%numero == 0:
        #     print("\n")
        if i == 0 or i%10 == 0:
            print ("          ",listaFila[x],end=" ")    
            if i>0 and i%10 == 0: 
                for j in range(10):
                    if listaB[j+auxiliar] == "B":
                        print("|B|",end="  ")
                    elif listaB[j+auxiliar] == "X":
                        print("|X|",end="  ")
                    elif listaB[j+auxiliar] == "O":
                        print("|O|",end="  ")
                    else:
                        print("|_|",end="  ")
                print("\n")
                x+=1            #aqui incrementando la variable de fila para ir a la siguiente letra
                auxiliar+=10
                if x<10:
                    print("          ",listaFila[x],end=" ")
        if i < 100:
            if listaA[i] == "B":
                print("|B|",end="  ")
            elif listaA[i] == "X":
                print("|X|",end="  ")
            elif listaA[i] == "O":
                print("|O|",end="  ")
            else:
                print("|_|",end="  ")
    


def mostrarMenu(lista,lista2):
    global contadorjugador1
    global contadorjugador2
    menuOn = True
    while menuOn:
        # print("¿Qué quieres hacer?")
        print("1: Ver tablero primer jugador \n2: Colocar barco primer jugador \n3: Ver tablero segundo jugador \n4: Colocar barco segundo jugador \n5: Jugar  \n6: Salir" )
        opcion=int(input())
        if opcion == 1:
            mostrarTablero(lista)
        if opcion == 2:
            if contadorjugador1 == 8:#15/12/2020  limita la cantidad de barcos a colocar, si pasa de 8 no te deja entrar.
                print("Ya has colocado todos los barcos.")
            else:
                evaluarBarcos(lista,opcion,dictDianas1)
                contadorjugador1+=1
        if opcion == 3:         #15/12/2020   he creado dos opciones mas para crear segundo tablero. gracias a pasarle tablero a lista2 sabe a cual me estoy refiriendo.

            mostrarTablero(lista2)
        if opcion == 4:
            if contadorjugador2 == 8:
                print("Ya has colocado todos los barcos")
            else:
                evaluarBarcos(lista2,opcion,dictDianas2)
                contadorjugador2+=1
        if opcion==5 :
            comenzarPartida(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2)

            #+++++++ si se descomentan estas filas, se obliga a jugar con 8 barcos cada jugador y el juego no comienzahasta que esten colocados todos los barcos.
            # if contadorjugador1==8 and contadorjugador2==8:
                # comenzarPartida(lista,lista2,dictDianas1,dictDianas2,listaDisparosJ1,listaDisparosJ2)
            # else:
            #     print("Todavía no habéis colocado todos los barcos.")
            menuOn = False
        if opcion == 6:
            menuOn = False
        if opcion== 7:
            mostrarJuntos(lista,lista2)

mostrarBienvenida()
hacerTablero(lista,listaLetras)
hacerTablero(lista2,listaLetras)
hacerTablero(listaDisparosJ1,listaLetras)
hacerTablero(listaDisparosJ2,listaLetras)
mostrarMenu(lista,lista2)

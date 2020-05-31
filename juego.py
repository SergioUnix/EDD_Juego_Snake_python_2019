import curses #import the curses library
import time
import random
import csv
import os.path as path
import os, sys
import subprocess
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN,KEY_BACKSPACE #import special KEYS from the curses library
from lista_snake import linked_list
from pila_snake import pila
from lista_simple import linked_simple
from lista_circular import list_circular
from puntos import pila_puntos
from tecla import pila_tecla
from posicion import pila_posicion
from nivel import pila_nivel
from curses.textpad import Textbox, rectangle

#al principio no hay usuario para iniciar el juego
usuario_nombre=None
#inicio de la Serpiente
serpiente =  linked_list()
pila_de_nivel=pila_nivel()
pila_de_nivel.apilar(1)
puntos=0
key=261  #tecla derecha
bocadillos=0 

ultima_posicion_snake=pila_posicion()

ultima_posicion_snake.apilar([5,5])
pos_x=ultima_posicion_snake.inspeccionar()[0]
pos_y=ultima_posicion_snake.inspeccionar()[1]

############################


#comida, puntos
comida =  pila()
puntos_pila = pila_puntos()
#String tecla
tecla_global=pila_tecla()

tecla_global.apilar(261) # tecla derecha
tecla_global.apilar(261)

#ScoreBoard
score= linked_simple()
score.add_to_the_end("Sergio",24)
score.add_to_the_end("Ariel", 18)
score.add_to_the_end("Madelyn",15)

#Usuarios
usuario=list_circular()
usuario.agregar("Lester")
usuario.agregar("Luis")
usuario.agregar("Bart")

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.box("#", "$")                       ## PINTA EL MARCO    
    win.addstr(7,15, '1. Jugar o (Reanudar Juego)')             
    win.addstr(8,15, '2. Scoreboard (Puntuaciones)')       
    win.addstr(9,15, '3. User Selection (Usuarios)')   
    win.addstr(10,15, '4. Reports (Reportes)')       
    win.addstr(11,15, '5. Bulk Loading (Carga Masiva)')  
    win.addstr(12,15, '6. Exit')           
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
        win.clear()                        
        win.border(0)                       
        x_start = round((60-len(var))/2)    #center the new title to be painted
        win.addstr(0,x_start,var)           

def paint_play(win,var):
    win.clear()                        
    win.border(0)                       
    #x_start = round((60-len(var))/2)    
    #win.addstr(0,x_start,var)          
    win.addstr(13,21, var)  

def probabilidad_seleccion(): 
    bueno = 'B'
    malo = 'M'
    prob = 0.7          #probabilidad de 70/30   probabilidad de bueno seria 0.7 para este juego
    cant = 100
    #con cant=100 y esta formula tomamos 70 valores para B y 30 valores para M
    lista = [bueno]*int(prob*cant)+[malo]*int((1-prob)*cant)
    #aca realizo un diccionario con 1 elemento seleccionado al azar con las probabilidades anteriores
    elemento_azar = {bueno: 0, malo: 0}
    for i in range(1):                   #una seleccion, pueden haber mas
        elemento_azar[random.choice(lista)] +=1  #ingreso el elemento seleccionado al Dic
    #print("Diccionario de elementos seleccionados al azar", elemento_azar)
    valor=int (elemento_azar.get('B'))
    if valor==1:
        return 'B'
    else:
        return 'M'



def play(win):
    win.clear() 
     
    pos_y=ultima_posicion_snake.inspeccionar()[1]
    pos_x=ultima_posicion_snake.inspeccionar()[0]
    bocadillos=comida.tamano()
    win.border(0)
    win.clear()
    posy_comida=random.randint(3, 22) 
    posx_comida=random.randint(3, 56)
    tipo_bocadillo='B' 
    key= tecla_global.inspeccionar()    #ingreso la tecla derecha antes de iniciara el while

    while key != 27:   # mientras sea diferene a tecla ESC
       
        puntos=puntos_pila.tamano()
 
        win.border(0) 
        win.addstr(0,0, 'Bocadillos:'+ str(bocadillos))
        win.addstr(0,15, 'puntos:'+ str(puntos))
        win.addstr(0,25, 'Nivel:'+ str(pila_de_nivel.tamano()))
        win.addstr(0,36, 'Tamaño serpiente'+ str(serpiente.tamano))
        win.addch(posy_comida,posx_comida,tipo_bocadillo)

        win.timeout(150)   #delay of 100 milliseconds
        keystroke =win.getch() #obtengo decla actual presionada
        



        if keystroke == 27 :
            win.clear() 
            ultima_posicion_snake.apilar([serpiente.head.posx,serpiente.head.posy])
            break

        if keystroke is not -1: # tecla presionada
            key = keystroke   #tecla direccion cambiada
          
               

        node =serpiente.head
        while node != None:  
            win.addch(node.posy,node.posx,' ') #borra el pasado
            node=node.next
            win.clear()

        serpiente.delete_first()
        
        

        if key == 261 :    #tecla derecha 261
            tecla_global.apilar(261)
            pos_x = pos_x + 1
        elif key == 260:
            tecla_global.apilar(260)   #tecla derecha 260
            pos_x = pos_x - 1
        elif key == 259:
            tecla_global.apilar(259)  #tecla derecha 259
            pos_y = pos_y - 1
        elif key == 258:
            tecla_global.apilar(258)   #tecla derecha 258
            pos_y = pos_y + 1

        
        
        serpiente.add_to_the_end(pos_x,pos_y)
       
        
        node =serpiente.head
        
        while node != None:
            
            if node.posy==posy_comida and node.posx==posx_comida and node.next==None:
                if tipo_bocadillo=='B':
                    serpiente.add_at_first(posx_comida,posy_comida) #agrego un elemento a la serpiente
                    comida.apilar([posx_comida,posy_comida])   #guardo la coordenada de la comida en la pila
                    win.addch(posy_comida,posx_comida,' ') #borra la comida ingerida
                    puntos_pila.apilar(1)
                    bocadillos=bocadillos+1
                    posx_comida=random.randint(3, 56)       #genero coordenada de nueva comida
                    posy_comida=random.randint(3, 22)       #genero coordenada de nueva comida
                    tipo_bocadillo=probabilidad_seleccion()  #genero el tipo del bocadillo con probabilidad
                    win.addch(posy_comida,posx_comida,tipo_bocadillo) #genero el nuevo bocadillo                  
                elif tipo_bocadillo=='M':
                    serpiente.delete_first()        #elimino un elemento de la serpiente
                    comida.desapilar()              #saco un  bocadillo de la pila ya que es mala la comida
                    win.addch(posy_comida,posx_comida,' ') #borra la comida ingerida
                    puntos_pila.desapilar()
                    bocadillos=bocadillos+1
                    posx_comida=random.randint(3, 56)   #ramdom de coordenada en x
                    posy_comida=random.randint(3, 22)   #ramdom de coordenada en y
                    tipo_bocadillo=probabilidad_seleccion() #genero tipo de bocadillo con probabilidad 
                    win.addch(posy_comida,posx_comida,tipo_bocadillo) #imprimo nuevo bocadillo                                   
            win.addch(node.posy, node.posx, '*')
            node = node.next
    win.clear()    
    score.add_to_the_end(usuario_nombre,puntos_pila.tamano())
    wait_esc(win,"JUEGO QUEDARA EN PAUSA")
    #bocadillos=0
    #puntos=0
    #nivel=1
   
def wait_esc(win,mensaje):
    win.clear() # LIMPIA LA CONSOLA
    win.border(0) 
    win.addstr(9, 15, mensaje)
    win.addstr(11, 14, "Presiona ESC para continuar")
    key = window.getch()
    while key!=27:
        key = window.getch()

def board(win,var):
    win.clear()                        
    win.border(0)                      
    x_start = round((60-len(var))/2)   
    win.addstr(0,x_start,var)         
    y=5
    win.addstr(3,20, 'Nombre')
    win.addstr(3,33, 'Puntos')  
    node=score.head
    while node != None:
        win.addstr(y,20, str(node.usuario))
        win.addstr(y,35, str(node.puntos))
        node =node.next
        y=y+1

def wait_puntuacion(win):
    win.clear() # LIMPIA LA CONSOLA
    win.border(0) 
    board(win,"Puntuaciones")
    #win.addstr(9, 15, mensaje)
    #win.addstr(11, 14, "Presiona ESC para continuar")
    key = window.getch()
    while key!=27:
        key = window.getch()

     

def elegir_usuario(win): #INICIA LAS PROPIEDADES BASICAS
    win.clear() # LIMPIA LA CONSOLA
    win.border(0) 
    curses.curs_set(0) # SETEA EL CURSOR EN LA POSICION 0
    index = 0
    curses.start_color()
    altura, ancho = win.getmaxyx() # OBTIENE LA ALTURA Y ANCHO DE LA PANTALLA
    y = int(altura/2) 
    x = int((ancho/2)-(usuario.tamano/2))
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    win.addstr(10,22, "<=    " + usuario.get_index(0)+"    =>",curses.color_pair(2)) 
    win.addstr(0,x-5, "Elegir Usuarios",curses.color_pair(2))
    win.addstr(13,13, "Tecla END para seleccionar usuario",curses.color_pair(2))
    win.addstr(14,10, "Tecla ESC para Regresar al menu principal",curses.color_pair(2))
    #pintar_menu(win, 0) # VA A INICAR EN EL INDICE 0
    #teclas aceptadas Insert .KEY_IC , Delete .KEY_DC , Home .KEY_HOME, End .KEY_END
    # Page Up .KEY_PPAGE , Page Down .KEY_NPAGE  
    while True:
        tecla = win.getch() # OBTENEMOS EL CARACTER DEL TECLADO
        if(tecla == curses.KEY_RIGHT): # VERIFICAMOS SI EL FLECHA A LA DERECHA
            index = index + 1
        elif (tecla == curses.KEY_LEFT ): # VERIFICAMOS SI ES FLECHA A LA IZQUIERDA
            index = index - 1
        elif (tecla == curses.KEY_END): # tecla End para seleccionar usuario
            comida.vaciar_la_pila()
            puntos_pila.vaciar_la_pila()
            ultima_posicion_snake.vaciar_la_pila()
            ultima_posicion_snake.apilar([5,5])
            tecla_global.apilar(261)
            serpiente.vaciar_snake()
            pila_de_nivel.vaciar_la_pila()
            pila_de_nivel.apilar(1)

            return usuario.get_index(index)
            break
        elif (tecla == 27): # SI ES LA TECLA DE SCAPE....
            break
        if( index < 0): # EN CASO DE QUE EL INDICE SE VUELVA NEGAVITO LO DEJAMOS EN 0
            index = usuario.tamano-1
        if( index >= usuario.tamano): # EN CASO QUE EL INDICE SE VUELVA MAYOR AL SIZE DEL ARREGLO...
            index = 0 # ... LO LIMITAMOS AL ULTIMO INDICE VALIDO
        win.clear() # LIMPIA LA CONSOLA
        win.border(0) # PINTO DE NUEVO EL BORDE
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # COLOR DE LAS OPCIONES, INIICIALIZA UNA PAREJA DE COLORES EL COLOR DE LETRA Y COLOR DE FONDO RESPECTIVAMENTE
        win.addstr(10,22, "<=    " + usuario.get_index(index)+"    =>",curses.color_pair(2)) # HAGREGA UNA CADENA  LA PANTALLA EN COORDENADAS Y, X Y UN ATRIBUTO EN ESTE CASO ES LA PAREJA DE COLORES
        win.addstr(0,x-5, "Elegir Usuarios",curses.color_pair(2))
        win.addstr(13,13, "Tecla END para seleccionar usuario",curses.color_pair(2))
        win.addstr(14,10, "Tecla ESC para Regresar al menu principal",curses.color_pair(2))
        win.refresh() 
        
def pedir_usuario(stdscr):
    stdscr.clear() # LIMPIA LA CONSOLA
    stdscr.border(0) 
    curses.curs_set(0) # SETEA EL CURSOR EN LA POSICION 0
    stdscr.addstr(5, 15, "INGRESA UN NOMBRE DE USUARIO")
    stdscr.addstr(19, 10, "(Ctrl-G para terminar y guardar el Usuario)")

    editwin = curses.newwin(1,30, 12,15) #primer argumento filas,segundo columnas, corrdenada y, coordenada en x donde empieza a escribirse
    rectangle(stdscr, 6,12,18,50) #primer argumento coordenada y, segundo coordenada x de esquina superior izquierda---cuarto y quinto son las coordenadas y y x de la esquina inferior derecha
    stdscr.refresh()

    box = Textbox(editwin)
    #Deje que el usuario edite hasta que presione Ctrl-G.
    box.edit()
    #Obtiene el contenido escrito y el return para mandarlo afuera
    return box.gather()   

def nombre_archivo_carga_masiva(stdscr):
    stdscr.clear() # LIMPIA LA CONSOLA
    stdscr.border(0) 
    curses.curs_set(0) # SETEA EL CURSOR EN LA POSICION 0
    stdscr.addstr(5, 10, "Ingresar el nombre del archivo y su extensión")
    stdscr.addstr(16, 14, "Presionar Enter para continuar")

    editwin = curses.newwin(1,30, 12,15) #primer argumento filas,segundo columnas, corrdenada y, coordenada en x donde empieza a escribirse
    rectangle(stdscr, 6,12,15,50) #primer argumento coordenada y, segundo coordenada x de esquina superior izquierda---cuarto y quinto son las coordenadas y y x de la esquina inferior derecha
    stdscr.refresh()

    box = Textbox(editwin)
    #Deje que el usuario edite hasta que presione Ctrl-G.
    box.edit()
    #Obtiene el contenido escrito y el return para mandarlo afuera
    return box.gather()   

def carga_masiva(win):
    nombre_archivo = nombre_archivo_carga_masiva(win)
    if nombre_archivo != "" and nombre_archivo != " " and path.exists(str(nombre_archivo))==True: #verifico si existe el archivo
        with open(str(nombre_archivo), newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                text=row[0]
                if text != 'Usuario' and text != 'ï»¿Usuario':
                   usuario.agregar(text)
                   print(text)
        wait_esc(win," USUARIOS CARGADOS ")           
    else:
         wait_esc(win,"-- Usuarios no cargados --")
#Este metodo Crea el archivo .txt para luego mandarlo a consola y pasarlo por grahpviz y desplegar la imagen
def graficar(var1,cadena):            #var1 es el nombre del archivo que voy a escribir y posterior a mandar a grahpviz
    file = open(str(var1)+".txt", "w")    #parametro w es para escribir, cuando es r solo es lectura
    file.write(str(cadena))          #recibe todo el string creado con sitaxis dot llamado en este caso cadena
    file.close()


    comando = "dot -Tpng "+str(var1)+".txt -o "+str(var1)+".png"
    resultado = subprocess.Popen(comando,shell=True,stdout=subprocess.PIPE)   #manda a consola la instruccion
    for salida in resultado.stdout:
        print(salida.decode(sys.getdefaultencoding()).rstrip())            #imprime algun posible error que pueda suceder

    comando2 = "start "+str(var1)+".png"
    resultado2 = subprocess.Popen(comando2,shell=True,stdout=subprocess.PIPE)
    for salida2 in resultado2.stdout:
        print(salida2.decode(sys.getdefaultencoding()).rstrip())

def wait_reportes(win):
    win.clear() # LIMPIA LA CONSOLA
    win.border(0) 
    paint_title(win,' Elija reporte a Visualizar ')          #paint title
    win.box("+", "=")                       ## PINTA EL MARCO    
    win.addstr(7,15, '1. SNAKE REPORT')             
    win.addstr(8,15, '2. SCORE REPORT')       
    win.addstr(9,15, '3. SCOREBOARD REPORT')   
    win.addstr(10,15, '4. USERS REPORT')       
    win.addstr(13,15, 'PRESIONA ESC PARA REGRESAR')  
    win.timeout(-1)    
    keystroke = -1
    while keystroke!=27:
        keystroke = window.getch()  #get current key being pressed
        if(keystroke==49): #tecla 1
            graficar("grafo_snake", serpiente.string_estructura()) #grafico la snake
            keystroke=-1
        elif(keystroke==50): #tecla 2
            graficar("grafo_score", comida.string_estructura())
            keystroke=-1
        elif(keystroke==51): #tecla 3
            graficar("grafo_scoreboard", score.string_estructura()) #grafico la scoreboard
            keystroke=-1
        elif(keystroke==52): #tecla 4
            graficar("grafo_users", usuario.string_estructura())
            keystroke=-1
        elif(keystroke==27): # tecla ESC  sale de la funcion
            break


    

window = curses.initscr() #initialize console
window = curses.newwin(25,60,0,0) #create a new curses window (y,x)
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    
    keystroke = window.getch()  #Obtengo la tecla actual presionada
    if(keystroke==49): #1
        window.clear()
        if(usuario_nombre==None):
            usuario_nombre=str(pedir_usuario(window))   #seteo la variable global usuario en uso
            usuario.agregar(usuario_nombre) #mando nuevo usuario a la lista circular
        play(window)              #ejecuto el juego
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        wait_puntuacion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        usuario_nombre=elegir_usuario(window)  #ejecuto Elegir usuario
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):

        wait_reportes(window)   #ejecuto el menu de los reportes
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' Carga Masiva ')
        carga_masiva(window)                  #carga los archivos del .csv
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #
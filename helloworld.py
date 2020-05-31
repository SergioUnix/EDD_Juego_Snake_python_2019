import curses
import csv
import os.path as path
import os, sys
import subprocess
from pila_snake import pila
from lista_snake import linked_list
from pila_snake import pila
from lista_simple import linked_simple
from lista_circular import list_circular
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN,KEY_BACKSPACE 
from tecla import pila_tecla
from posicion import pila_posicion

culebrita =  linked_list()
comida =  pila()
score= linked_simple()
usuario=list_circular()
lista_teclas= pila_tecla()
coordenadas= pila_posicion()


comida.apilar([11,11])
comida.apilar([22,22])
comida.apilar([33,33])
comida.apilar([44,44])
comida.imprimir()
print(comida.string_estructura())


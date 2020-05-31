#imprime un String
print("helloWorld")
#Primero Ve que tipo es y luego imprime que tipo es
print (type("helloworld"))

#unir dos string
print("bye" +" Concatenación")

#numeros
print (30)   
print(type(30))  #tipo de dato entero

#datos booleanos
print(type(True))

#lista de datos
print(type([10, 20, 30, 55])) # typo de lista
print(["Hola", "Adios","bye"])
print([10, 22.5, 30.1])

#tupla  no se puede cambiar
(10, 20, 30, 40, 50)
print(type((10,20,30,40,50)))

#Diccionarios   permiten agrupar datos que pertenecen a una misma entidad
print(type({
"Name":"Sergio",
"Apellido":"Ramirez",
"Apodo":"Chejo",
"Direccion":"9na. Avenida 13-80"
}))

#Variables  en el lenguaje es KeySensitive hay diferencia entre mayusculas y minusculas
name ="Ariel"
print(name)
#Varias variables declaradas en una linea
apellido, edad, fecha_nac= "Ramirez" , 29, 1990
print(apellido, edad, fecha_nac)

#Convensiones , valores que no cambian pueden ser el nombre en mayusculas
PI= 3.1416
MY_NAME= "Sergio"

#Muestra que puedo hacer con un tipo string
myStr= "Hello World"
print(dir(myStr))
#Upper convierte el texto en mayuscula
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())

#Reemplazar texto en una palabra
print(myStr.replace("World","Ariel"))

#Contar cuantos caracteres hay en la palabra
print(myStr.count("o"))

#pregunta si empieza con la palabra puesta, devuelve un boolean
print(myStr.startswith("Hello"))

#Utilizar Split, devuelve una lista de String
print(myStr)
print(myStr.split("o"))

#Encuentra la posicion de la letra
print(myStr.find("o"))

#Cuenta el tamaño de la palabra
print(len(myStr))
#Obtener el valor del indice
print(myStr.index("l"))
#preguntar si es numero o es letra, devuelve un boolean
print(myStr.isnumeric()) #es numerico
print(myStr.isalpha())   #es alfanumerico

#imprimir la letra que esta en la posicion puesta
print(myStr[4])

#maneras de concatenar
print("my name is "+ myStr)
print(f"my name is {myStr}")
print("my name is {0}".format(myStr))

#Insertar desde la consola
edad = input("Inserta tu edad : ")  #Se obtiene siempre un String
new_edad = int(edad)+5  #Casteo a int y luego sumo 
print(new_edad)


#listas
demo_list =["red", "yellow", "green", [1,2,3]]
print(type(demo_list))

r= list(range(1, 10))   # llena una lista con el rango de 1 a 10
print(r)

#            print(dir(demo_list)) # veo que metodos puedo usar con listas

#longitud de la lista
print(len(demo_list))

#lo que se encuentra en un indice de la lista
print(demo_list[2])

#Devuelve valor boolean si le digo que si se encuentra green en la lista
print('green' in demo_list)

#Cambiar un elemento de la lista
demo_list[1] ='red'
print(demo_list)  #verifico al imprimir

#Agregar elementos a una lista existente
demo_list.append('violeta')
demo_list.append('gray')
print(demo_list)
#para agregar varios utilizo este metodo
demo_list.extend(['black', 'wite','brown'])
print(demo_list)  #verifico 

#inserto en la lista en medio de dos elementos
demo_list.insert(1, 'En Medio')
print(demo_list)

#Quito el ultimo con el metodo pop o utilio indice para quitar dentro del pop
demo_list.pop()
print(demo_list)

demo_list.pop(4)
print(demo_list)


#quito con un indice con el metodo Remove 
demo_list.remove('red')
print(demo_list)

#Ordenar alfabeticamente una lista ascendente
demo_list.sort()
print(demo_list)
#Ordenar alfabeticamente una lista Descendente invirtiendolo
demo_list.sort(reverse=True)
print(demo_list)

#Obtener el indice de un elemento en la lista
print(demo_list.index('En Medio'))

#Contar cuantas veces se repite el string
print(demo_list.count('gray'))

#las tuplas son constantes no se puede modificar 
x= (1,2,3) #la tupla tiene que llevar mas de un elemento
print(x)
y=(1,)   #si  quiero un elemento en una tupla se escribe con una coma seguida
print(y)

#Elimino las tuplas
del x
del y

#tipo de datos SET
colors= {"blue", "pink", "orange"}
print(type(colors)) #muestro que tipo de dato es
print(colors) #los imprimo para ver
print('blue' in colors)  # pregunto si esta blue en el set, retorna un boolean

#agrego un nuevo dato en el SET y lo muestro
colors.add('violet')
print(colors)
#Remuevo un elemento en el tipo SET
colors.remove('violet')
print(colors)
#limpia los todos los datos y deja vacio el tipo  SEt
colors.clear()
print(colors) #verifico si esta vacio
#Eliminar el Set
del colors


#Condicionales
#if para numeros
z = 40
if z < 30 :   #### puede ir == , <= , >=
    print("si es menor que treinta")
else:
    print("Es Mayor a treinta")
# Operadores logicos de if  and, or, not   
if (not(z==30)):          #si z no es igual a 30 imprimir
    print("Operador logico a prueba")

#para Strings
color = "blue"
if color == "red":
    print("son iguales")
elif color == "blue":
    print("el color es blue")
else:
    print("no son iguales")

## Ifs anidados             
name= "John"
lastname = "Carter"
if name =="John":
    if lastname == "Carter":
        print("Tu eres John")
    else:
        print("tu no eres")
else:
    print("Falso")



#Ciclo For
foods = ['apples','bread','cheese', 'milk','bananas','pear','Kiwi'] #una lista de foods

for food in foods: # en la lista de alimentos debo recorrer cada alimento
    if food== "pear":
        print("ejemplo if anidado en un for")
    elif food == "Kiwi":
        break      #Este break para la ejecucion del for en cualquier momento
    print(food)

#imprimir un rango con un for
for number in range(1, 5):
    print(number)

#recorrer caracteres de un String por medio de for
for letter in "hello":
    print(letter)



# Ciclo While
count=4
while count <=8:
    print(count)
    count= count + 1


#funciones
def funcion(name):           #defino una funcion
    print("Mi nombre es "+name)

funcion("Ariel")      #llamo la funcion para que se ejecute

def func(name ="no paso nombre"): # si no le paso nombre ala hora de llamar pone lo que esta aqui
    print("Mi nombre es "+ name)

func()


## funciones que devuelven algo
def sumar(num1, num2):
    return num1 + num2

print(sumar(4,5))


#otro tipo de funciones sin nombre
add =lambda num1, num2: num1 + num2
print(add(10, 30))


#Modulos
#para importar modulos creados por mi , solo debo escribir lo siguiente
#import funcion_creada_pormi
#para utilizar sus metodos escribo lo siguiente ejemplo:
#funcion_creada_pormi.Metodo_creado(parametro1, parametro2)

#concatenar int y string en un print
print('Sergio Ariel', ' mi edad es: ', 25)

#utilizar palabras ramdom
l =random.choice(["malo", "bueno"])
print("palabra random es: ", l)
#utilizar numeros ramdom
z=random.randint(0, 5)
print('numero aleatorio es : ', z)



################   EJEMPLO DE COMO HACER UN RAMDOM DE DOS PALABRAS CADA UNA CON UNA PROBABILIDAD
bueno = "B"
malo = "M"
prob = 0.7          #probabilidad de 70/30   probabilidad de bueno seria 0.7
cant = 100
#con cant=100 y esta formula tomamos 70 valores para B y 30 valores para M
lista = [bueno]*int(prob*cant)+[malo]*int((1-prob)*cant) 

resultados = {bueno: 0, malo: 0}
# forma empírica simulando hasta 1000 casos de selección de un elemento al azar.
for i in range(1000):
  resultados[random.choice(lista)] +=1
#aca realizo un diccionario con 1 elemento seleccionado al azar con las probabilidades anteriores
elemento_azar = {bueno: 0, malo: 0}
for i in range(1):
    elemento_azar[random.choice(lista)] +=1
print("Diccionario de elementos seleccionados al azar", elemento_azar)
valor=int (elemento_azar.get('B'))
if valor==1:
    print("hay un elemento en bueno")
else:
    print("Es malo el elemento")

prob_bueno = (100*resultados[bueno])/(resultados[malo] + resultados[bueno])
print("Verificamos que probabilidad de {0} es de: {1}%".format(bueno, prob_bueno))

##############################################################################################
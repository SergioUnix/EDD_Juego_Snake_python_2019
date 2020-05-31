class node:
    def __init__(self, posx=None, posy=None, next =None, prev=None):
        self.posx =posx
        self.posy =posy
        self.next = next
        self.prev = prev

class linked_list:
    def __init__(self):  
        self.tamano=0
        self.head = None
        self.comodin=None

    #agregar elementos al principio de la lista
    def add_at_first(self,posx, posy):
        comodin = node(posx=posx,posy=posy)
        if self.head.prev is None:
            self.head.prev =comodin
            comodin.next = self.head
            self.head =comodin
            self.tamano = self.tamano + 1


    #metodo para verificar la existencia de elementos
    def is_empty(self):
        return self.head == None

    #metodo para agregar elementos al final de la linked list
    def add_to_the_end(self, posx,posy):
        if self.head is None:
            self.head = node(posx = posx , posy =posy)
            self.tamano = self.tamano + 1
        else:      
            temporal = self.head

            while temporal.next is not None:
                temporal =temporal.next

            comodin= node(posx=posx, posy=posy)
            temporal.next =comodin
            comodin.prev = temporal
            comodin=None
            self.tamano = self.tamano + 1
   #eliminar el primero
    def delete_first(self):
       if self.tamano > 3: ### para el juego añadi que se ejecutara cuando fuera mayor a 3 para que no se reduzca la snake
            if self.head is not None: 
                if self.head.next is not None:
                    temporal =self.head.next
                    self.head = temporal
                    self.head.prev=None
                    self.tamano = self.tamano - 1

    #eliminar el ultimo
    def dele_last(self):
        if self.tamano >3:# se añadio que and tamaño no fuera menor a 3 de tamaño
            if self.head.next is not None:
                temp = self.head
                while(temp.next is not None):
                     temp =temp.next

                temp = temp.prev
                temp.next=None
                self.tamano = self.tamano - 1
        
  #metodo para recorrer la edd
    def prin_list(self):
        node =self.head
        
        while node != None:
            print(str(node.posx)+" "+str(node.posy), end=" => ")
            node =node.next
        print("null")
        
  #metodo devuelve el tamaño de la lista
    def longitud(self):
        return self.tamano

    #metodoo verifica si se esta topando con la lista- reprogramar aun no esta
    def delete_node(self, posx, posy):
        temporal=self.head
        prev= None
        while temporal and temporal.posx !=posx and temporal.posy !=posy:
            prev =temporaltemporal =temporal.next
            temporal = temporal.next
        if prev is None:
            self.head =temporaal.next
        elif temporal:
            prev.next =temporal.next
            tempora.next = None
 
        
    #Generar el String para graficar la estructura con Grahpviz
    def string_estructura(self):
        linea1=" digraph G {"
        linea2="nodesep=.02;"
        linea3="rankdir=LR;"
        linea4="node [shape=record,width=.1,height=.1];"   
        linea5="node0 [label = \"null\"];"
        linea6="node [width =1.5];"
        node =self.head
        index=1
        nodos=""
        direccion=""
        while node != None:
            nodos=nodos+"node"+str(index) + "[label = \"{<n> |" +str(node.posx)+","+str(node.posy)+"| <p> }\"];"
            direccion=direccion+"node"+str(index)+":n -> node"+str(index-1)+":p;"
            direccion=direccion+"node"+str(index)+":p -> node"+str(index+1)+":n;"            
            index=index+1
            node =node.next
        nodos=nodos +"node"+str(index) + "[label = \"null\",width=0.5];"
        lineafinal="}"
        grafo= linea1+linea2+linea3+linea4+linea5+linea6+nodos+direccion+lineafinal
        return grafo

 #Vaciar Snake
    def vaciar_snake(self):
        self.tamano=0
        self.head = None
        self.comodin=None
 


  

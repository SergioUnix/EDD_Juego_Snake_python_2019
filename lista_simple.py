class node:
    def __init__(self, puntos=None, usuario=None, next =None):
        self.puntos =puntos
        self.usuario =usuario
        self.next = next
        

class linked_simple:
    def __init__(self):  
        self.tamano = 0
        self.head = None
        self.comodin=None

    #agregar elementos al principio de la lista
    def add_at_first(self,usuario, puntos):
        comodin = node(usuario=usuario, puntos=puntos)
        comodin.next = self.head
        self.head = comodin
        self.tamano = self.tamano + 1


    #metodo para verificar la existencia de elementos
    def is_empty(self):
        return self.head == None

    #metodo para agregar elementos al final de la linked list
    def add_to_the_end(self, usuario,puntos):
        if  self.head is None:
            self.head = node(usuario = usuario , puntos = puntos)
            self.tamano = self.tamano + 1
        else:      
            temporal = self.head

            while temporal.next is not None:
                temporal =temporal.next

            comodin= node(usuario=usuario, puntos=puntos)
            temporal.next =comodin
            comodin=None
            self.tamano = self.tamano + 1
   #eliminar el primero
    def delete_first(self):
        if self.head is not None: 
            if self.head.next is not None:
                temporal =self.head.next
                self.head = temporal
                self.tamano = self.tamano - 1
            elif  self.head.next is None:
                self.head =None
                self.tamano = self.tamano - 1

    #eliminar el ultimo
    def dele_last(self):
        if self.head is not None:
            if self.head.next is not None:
                tem = self.head
                temp = self.head
                while(temp.next is not None):
                    tem=temp
                    temp =temp.next

                tem.next=None
                self.tamano = self.tamano - 1
            elif  self.head.next is None:
                self.head =None
                self.tamano = self.tamano - 1
            
        
  #metodo para recorrer la edd
    def prin_list(self):
        node =self.head
        
        while node != None:
            print(str(node.usuario)+" "+str(node.puntos), end=" => ")
            node =node.next
        print("null")
        
  #metodo devuelve el tamaño de la lista
    def longitud(self):
        return self.tamano

    #obtener el ultimo nodo
    def get_ultimo(self):
        node =self.head
        while node.next != None:
            node =node.next
        return node.usuario





    #metodo para eliminar de la lista
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
        linea6="node [width =1.5];"
        node =self.head
        index=1
        nodos=""
        direccion=""
        while node != None:
            nodos=nodos+"node"+str(index) + "[label = \"{<n>" +str(node.usuario)+","+str(node.puntos)+"| <p> }\"];"
            direccion=direccion+"node"+str(index)+":p -> node"+str(index+1)+":n;"            
            index=index+1
            node =node.next
        nodos=nodos +"node"+str(index) + "[label = \"null\",width=0.5];"
        lineafinal="}"
        grafo= linea1+linea2+linea3+linea4+linea6+nodos+direccion+lineafinal
        return grafo

        

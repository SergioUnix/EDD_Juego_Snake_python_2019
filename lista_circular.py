class node:
    def __init__(self, usuario=None, next =None, prev=None):
        self.usuario=usuario
        self.next = next
        self.prev = prev

class list_circular:
    def __init__(self):  
        self.tamano=0
        self.head = None
        self.comodin=None

    #metodo para verificar la existencia de elementos
    def is_empty(self):
        return self.head == None

    #metodo para agregar elementos al final de la lista circular
    def agregar(self, usuario):
        if self.head is None:
            self.head = node(usuario=usuario)
            self.head.next= self.head
            self.head.prev=self.head
            self.tamano = self.tamano + 1
        else:      
            temporal = self.head

            while temporal.next is not self.head:
                temporal =temporal.next

            comodin= node(usuario=usuario)
            temporal.next =comodin
            comodin.prev = temporal
            self.head.prev=comodin
            comodin.next=self.head
            comodin=None
            self.tamano = self.tamano + 1
    #Obtener por medio del indice
    def get_index(self,index):
        node=self.head
        contador=0
        while node != self.head.prev:
            if contador == index:
                return node.usuario
                break
            contador=contador+1
            node =node.next
        if index ==self.tamano-1:
            return node.usuario

    #Metodo de imprimir lista
    def imprimir(self):
        node =self.head
        
        while node != self.head.prev:        #cuando sea diferente al nodo antes de la cabeza imprimo
            print(str(node.usuario) , end=" => ")
            node =node.next
        print(str(node.usuario) , end=" => ")


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
        while node != self.head.prev:
            nodos=nodos+"node"+str(index) + "[label = \"{<n> |" +str(node.usuario)+"| <p> }\"];"
            if index-1 != 0:
                direccion=direccion+"node"+str(index)+":n -> node"+str(index-1)+":p;"
            direccion=direccion+"node"+str(index)+":p -> node"+str(index+1)+":n;"            
            index=index+1
            node =node.next
        ultimo_nodo="node"+str(index) + "[label = \"{<n> |" +str(node.usuario)+"| <p> }\"];"
        primera_direccion="node"+str(1)+":n -> node"+str(index)+":p;"
        penultima_direccion="node"+str(index)+":n -> node"+str(index-1)+":p;"
        ultima_direccion ="node"+str(index)+":p -> node"+str(1)+":n;"
        lineafinal="}"
        grafo= linea1+linea2+linea3+linea4+linea6+nodos+ultimo_nodo+primera_direccion+direccion+penultima_direccion+ultima_direccion+lineafinal
        return grafo

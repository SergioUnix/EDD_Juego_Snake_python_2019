class pila:
     def __init__(self):
         self.items = []
         
     #si la pila esta vacia devuelve true
     def estaVacia(self):
         return self.items == []
     #Agrega a la pila creada
     def apilar(self, list):
         self.items.append(list)
     #Elimina el primero de la pila 
     def extraer(self):
         return self.items.pop()
     #solo obtiene el que esta hasta arriba
     def inspeccionar(self):
         return self.items[len(self.items)-1]
     #obtiene el tamaño de la pila  
     def tamano(self):
         return len(self.items)
     #Devuelve el elemento tope y lo elimina de la pila.
     #Si la pila está vacía levanta una excepción.    
     def desapilar(self): 
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
     #imprime la lista completa
     def imprimir(self):
         comodin= self.items
         for elementos in comodin: # en la lista de alimentos debo recorrer cada alimento
            print("Elemento :", elementos)

     # vacia la pila
     def vaciar_la_pila(self):
            self.items = []

     #Generar el string para el grafo
     def string_estructura(self):
        linea1=" digraph G {"
        linea2="nodesep=.02;"
        linea3="rankdir=LR;"
        linea4="node [shape=record,width=.1,height=.1];"   
        linea5="node0 [label = \"<f0> "
        linea6="\",height=2.5];"
        linea7="node [width =1.5];"
        index=0
        nodos=""
        sistema=self.items
        sistema.reverse()
        
        while index <= len(sistema)-1:
            nodos=nodos+"|<f"+str(index)+">["+str(sistema[index][0])+","+str(sistema[index][1])+"]"
            index=index+1
       
        
        lineafinal="}"
        grafo= linea1+linea2+linea3+linea4+linea5+nodos+linea6+linea7+lineafinal
        return grafo











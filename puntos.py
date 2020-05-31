class pila_puntos:
     def __init__(self):
         self.items = []
         
     #si la pila esta vacia devuelve true
     def estaVacia(self):
         return self.items == []
     #Agrega a la pila creada
     def apilar(self, numero):
         self.items.append(numero)
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
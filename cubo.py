class NodoMatriz():
    """ 
    NODO DE LA MATRIZ ORTOGONAL
    """
    def __init__(self, x, y, dato):
        # INICIANDO PUNTEROS DEL NODO
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None
        # INICIANDO LOS DATOS DEL NODO
        self.dato = dato
        self.x = x
        self.y = y
    
    def node_str(self):
        return "("+str(self.x)+","+str(self.y)+") = "+str(self.dato)

class Matriz():

    def __init__(self):
        # INICIANDO UN NODO RAIZ
        self.root = NodoMatriz(-1,-1, "Root")

    #BUSCA EL NODO EN Y
    #DE EXISTIR ENTONCES RETORNAR EL NODO SINO RETORNA NULO
    def buscar_fila(self, y):
        temp = self.root
        while temp is not None:
            if(temp.y == y):
                return temp
            temp = temp.abajo
        return None

    #BUSCA EL NODO EN X
    #DE EXISTIR ENTONCES RETORNAR EL NODO SINO RETORNA NULO
    def buscar_columna(self, x):
        temp = self.root
        while temp is not None:
            if(temp.x == x):
                return temp
            temp = temp.siguiente
        return None

    def insertar_ordenado_columna(self, nuevo, cabeza_col):
        # IMPLEMENTAR EN CLASE
        temp = cabeza_col
        bandera = False
        while True:
            if(temp.x == nuevo.x):
                # SI LA POSICION ES LA MISMA SOBRE ESCRIBO
                temp.y = nuevo.y
                temp.dato = nuevo.dato
                return temp #RETORNAMOS EL PUNTERO
            elif(temp.x > nuevo.x):
                # TENGO QUE INSERTARLO ANTES DE TEMP
                bandera = True
                break
            if temp.siguiente is not None:
                temp = temp.siguiente
            else:
                # TENGO QUE INSERTAR NUEVO DESPUES DE TEMP
                # bandera = FALSE
                break
        if bandera:
            # INSERTARLO ANTES DE TEMPORAL
            nuevo.siguiente = temp
            temp.anterior.siguiente = nuevo
            nuevo.anterior = temp.anterior
            temp.anterior = nuevo
        else:
            temp.siguiente = nuevo
            nuevo.anterior = temp
        return nuevo
    
    def insertar_ordenado_fila(self, nuevo, cabeza_fila):
        # IMPLEMENTAR EN CLASE
        temp = cabeza_fila
        bandera = True
        while True:
            if(temp.y == nuevo.y):
                # SI LA POSICION ES LA MISMA SOBRE ESCRIBO
                temp.x = nuevo.x
                temp.dato = nuevo.dato
                return temp #RETORNAMOS EL PUNTERO
            elif(temp.y > nuevo.y):
                # TENGO QUE INSERTARLO ANTES DE TEMP
                bandera = True
                break
            if temp.abajo is not None:
                temp = temp.abajo
            else:
                # TENGO QUE INSERTAR NUEVO DESPUES DE TEMP
                # bandera = FALSE
                break
        if bandera:
            # INSERTARLO ANTES DE TEMPORAL
            nuevo.abajo = temp
            temp.arriba.abajo = nuevo
            nuevo.arriba = temp.arriba
            temp.arriba = nuevo
        else:
            # INSERCION AL FINAL
            temp.abajo = nuevo
            nuevo.arriba = temp
        return nuevo

    def crear_columna(self, x):
        # IMPLEMENTAR EN CLASE
        cabeza_columna = self.root
        columna = self.insertar_ordenado_columna(NodoMatriz(x,-1,"COL"), cabeza_columna)
        return columna

    
    def crear_fila(self, y):
        # IMPLEMENTAR EN CLASE
        cabeza_fila = self.root
        fila = self.insertar_ordenado_fila(NodoMatriz(-1,y,"FIL"), cabeza_fila)
        return fila

    # INSERCION GENERAL
    def insertar_elemento(self, x, y, dato):
        # IMPLEMENTAR EN CLASE
        nuevo = NodoMatriz(x,y,dato)
        NodoColumna = self.buscar_columna(x)
        NodoFila = self.buscar_fila(y)
        # 1 CASO: COLUMNA NO EXISTA Y FILA NO EXISTA
        if NodoColumna is None and NodoFila is None:
            print("caso 1")
            # CREAMOS COLUMNA
            NodoColumna = self.crear_columna(x)
            # CREAR FILA
            NodoFila = self.crear_fila(y)
            # INSERTAMOS DE FORMA ORDENADA EN COLUMA
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            # INSERTAMOS DE FORMA ORDENADA EN FILA
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        # 2 CASO: COLUNMA NO EXISTA Y FILA EXISTA
        elif NodoColumna is None and NodoFila is not None:
            print("caso 2")
            # CREAMOS COLUMNA
            NodoColumna = self.crear_columna(x)
            # INSERTAMOS DE FORMA ORDENADA EN COLUMNA
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            # INSERTAMOS DE FORMA ORDENADA EN FILA
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        # 3 CASO: COLUMNA EXISTA Y LA FILA NO EXISTA
        elif NodoColumna is not None and NodoFila is None:
            print("caso 3")
            # CREAMOS LA FILA
            NodoFila = self.crear_fila(y)
            # INSERTAMOS DE FORMA ORDENADA EN COLUMNA
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            # INSERTAMOS DE FORMA ORDENADA EN FILA
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        # 4 CASO: COLUMNA Y LA FILA EXISTEN
        elif NodoColumna is not None and NodoFila is not None:
            print("caso 4")
            # INSERTAMOS DE FORMA ORDENADA EN COLUMNA
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            # INSERTAMOS DE FORMA ORDENADA EN FILA
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
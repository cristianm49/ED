
import math


class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.valor = valor
        self.altura=0


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def obtenerRaiz(self):
        return self.raiz

    def agregarNodos(self, nodo_valor):
        if (self.raiz == None):
            self.raiz = Nodo(nodo_valor)
        else:
            self._agregarNodos(nodo_valor, self.raiz)

    def _agregarNodos(self, nodo_valor, nodo_raiz):
        if (nodo_valor < int(nodo_raiz.valor)):
            if (nodo_raiz.hijoIzq != None):
                self._agregarNodos(nodo_valor, nodo_raiz.hijoIzq)
            else:
                child=Nodo(nodo_valor)
                child.altura=nodo_raiz.altura+1
                nodo_raiz.hijoIzq = child
        else:
            if (nodo_raiz.hijoDer != None):
                self._agregarNodos(nodo_valor, nodo_raiz.hijoDer)
            else:
                child=Nodo(nodo_valor)
                child.altura=nodo_raiz.altura+1
                nodo_raiz.hijoDer = child
    def encontrar(self, nodo_valor):
        if(self.raiz != None):
            return self._encontrar(nodo_valor, self.raiz)
        else:
            return None

    def _encontrar(self, nodo_valor, nodo_raiz):
        if (nodo_valor == int(nodo_raiz.valor)):
            return nodo_raiz
        elif (nodo_valor < nodo_raiz.valor and nodo_raiz.hijoIzq != None):
            return self._encontrar(nodo_valor, nodo_raiz.hijoIzq)
        elif(nodo_valor > nodo_raiz.valor and nodo_raiz.hijoDer != None):
            return self._encontrar(nodo_valor, nodo_raiz.hijoDer)

    def imprimirArbol(self):
        if(self.raiz != None):
            self._imprimirArbol(self.raiz)

    def _imprimirArbol(self, nodo_raiz):
        if(nodo_raiz != None):
            self._imprimirArbol(nodo_raiz.hijoIzq)
            print(str(nodo_raiz.valor) + ' ' + str(nodo_raiz.altura) )
            self._imprimirArbol(nodo_raiz.hijoDer)
    
    def maximo(self):
         if(self.raiz != None):
             return self._maximonivel(self.raiz);
         
    def _maximonivel(self,nodo_raiz): 
        alturader  = 0
        alturaiz   = 0
        if(nodo_raiz != None):
            if (nodo_raiz.hijoIzq!=None):
                alturaiz = self._maximonivel(nodo_raiz.hijoIzq)
            else:
                alturaiz = nodo_raiz.altura
            if (nodo_raiz.hijoDer!=None):
                alturader = self._maximonivel(nodo_raiz.hijoDer)
            else:
                alturader = nodo_raiz.altura
            return alturader if alturader>alturaiz else alturaiz
        return 0
    
    def imprimirtriangulo(self,altura):
        if(self.raiz != None):
            self._imprimirtriangulo(altura,self.raiz)
    
    def _imprimirtriangulo(self, altura,nodo_raiz):
        maximoHijos=2**altura
        if(nodo_raiz!=None):
            columnas, filas =  (maximoHijos+maximoHijos-1),altura+1 ;
            Matrix = [[0 for x in range(columnas)] for y in range(filas)] 
            posPadre=math.ceil((maximoHijos+maximoHijos-1)/2)
            Matrix[0][posPadre-1]=nodo_raiz.valor
            nodos=[]
            nodos.append(nodo_raiz)
            counter=1
            while (counter<altura+1):
                nodosChild=[]
                for nodo in nodos:
                    if(nodo.hijoIzq!=None):
                        nodosChild.append(nodo.hijoIzq)
                    else:
                        tempNodo=Nodo(-1)
                        tempNodo.altura=nodo.altura+1
                        nodosChild.append(tempNodo)
                    if(nodo.hijoDer!=None):
                        nodosChild.append(nodo.hijoDer)
                    else:
                        tempNodo=Nodo(-1)
                        tempNodo.altura=nodo.altura+1
                        nodosChild.append(tempNodo)   
                cantidaditems=(2**counter) #4
                cantidadSeparador=cantidaditems+cantidaditems-1 # 7
                espaciado= math.ceil((2**(altura+1-counter))/2) # 1
                index=0
                for x in range(1,cantidadSeparador+1):
                    if x%2!=0:
                        Matrix[nodosChild[index].altura][(x*espaciado)-1]=nodosChild[index].valor
                        index+=1
                counter+=1
                nodos=nodosChild
            self.imprimirMatrix(Matrix ,filas,columnas)
            
    def imprimirMatrix(self , Matrix ,filas,columnas):
        for x in range(0,filas):
                text=""
                for j in range (0,columnas):
                    if Matrix[x][j]==-1   or  Matrix[x][j]==0 :
                        text+=" "
                    else:
                        text+=str(Matrix[x][j])
                print(text)
                
    def eliminarArbol(self):
        self.raiz = None


if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.agregarNodos(5)
    arbol.agregarNodos(3)
    arbol.agregarNodos(1)
    arbol.agregarNodos(2)
    arbol.agregarNodos(6)
    arbol.agregarNodos(4)
    arbol.agregarNodos(8)
    arbol.agregarNodos(9)
    arbol.agregarNodos(7)
    


    print("---Raiz---")
    print(arbol.obtenerRaiz().valor)

    print("---Imprimir Arbol---")
    #Imprimir arbol binario
    arbol.imprimirArbol()
    
    print(arbol.maximo())
    arbol.imprimirtriangulo(arbol.maximo())

#Arboles binarios de busqueda
#Arboles AVL


                
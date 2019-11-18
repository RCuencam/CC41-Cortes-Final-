import heapq as hq

def AreaTotal(resultado):
    n=len(resultado)
    sumaa=0
    for i in range(n):
        sumaa+=resultado[i]
    return sumaa

class Bin:
    def __init__(self):
        self.list = []
 
    def AñadirPlaca(self, item):
        self.list.append(item)
 
    def suma(self):
        total = 0
        for elem in self.list:
            total += elem
        return total
 
    def Mostrar(self):
        return self.list
 
def BinPacking(arreglo, areaPlancha):
    """ Returns list of bins with input items inside. """
    a = []
    a.append(Bin()) 
 
    for item in arreglo:
       
        añadir = False
 
        for bin in a:
            if bin.suma() + item <= areaPlancha:
                bin.AñadirPlaca(item)
                añadir = True
                break
       
        
        if añadir == False:
            nuevo = Bin()
            nuevo.AñadirPlaca(item)
            a.append(nuevo)
 
    arreglo = []
    for bin in a:
        arreglo.append(bin.Mostrar())
 
    return(arreglo)

def SepararArea(arreglo):
	n=len(arreglo)
	a=[]

	for i in range(n):
		a.append(arreglo[i][0])
	
	return a



with open('archivo.txt') as f:
    
    TC=[]
    CL=[]
    areas=[]
    contenedor=f.readline().strip()
    contenedor1,contenedor2,contenedor3=[int(x) for x in contenedor.split(' ')]
    volumen=contenedor1*contenedor2*contenedor3

    line = int(f.readline())
    for i in range(line):
        D = f.readline().strip()
        T, Q, X, Y, Z = [x for x in D.split(' ')]
        cantidad = int(T)
        tipo = Q
        G = [[] for _ in range(cantidad)]
        
        for j in range(cantidad):
            G[j].append(((tipo),((X),(Y),(Z))))
            TC.append([(int(X),int(Y),int(Z)),(int(X)*int(Y)*int(Z))])
            CL.append(int(X))
            CL.append(int(Y))
            CL.append(int(Z))
            areas.append(int(X)*int(Y)*int(Z))
        print(G)
        

        
        
        

def areaTotal(areas):
    n=len(areas)
    suma=0
    for i in range(n):
        suma+=areas[i]
    return suma


def Ordenar(G):
    ordenado = sorted(G , key=lambda k: [k[0], k[1]],reverse=True)
    return ordenado





ordenado=SepararArea(Ordenar(TC))
n=len(ordenado)
a=[]
resultado=[]
for i in range(n):
    a.append(ordenado[i])


for i in range(n):
    for j in range(3):
        resultado.append(a[i][j])


def posicionar(largo,ancho,alto,arreglo,cantidad):
    q=0
    x=arreglo[0]
    y=arreglo[1]
    z=arreglo[2]
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    
    
    while z<alto and q<cantidad[0] and y<=ancho:
        A.append((x,y,z))
        z+=arreglo[2]
        q+=1

    y+=arreglo[1]
    z=0
    q=0
   

    while z<alto and q<cantidad[1] and y<=ancho:
        
        B.append((x,y,z))
        z+=arreglo[cantidad[1]*3+2]
        q+=1

    q=0
    y+=arreglo[1]
    z=0


    while z<alto and q<cantidad[2] and y<=ancho:
        
        C.append((x,y,z))
        z+=arreglo[cantidad[2]*3+2]
        
        q+=1

    q=0
    y+=arreglo[1]
    z=0

    while z<alto and q<cantidad[3] and y<=ancho:
        
        D.append((x,y,z))
        z+=arreglo[cantidad[3]*3+1]
        q+=1

    q=0
    y+=arreglo[1]
    z=0

    while z<alto and q<cantidad[4] and y<=ancho:
        
        E.append((x,y,z))
        z+=arreglo[len(arreglo)-1]
        q+=1

    while y>ancho and q<cantidad[3]:
        A.append((x,y,z))
        B.append((x,y,z))
        C.append((x,y,z))
        D.append((x,y,z))
        E.append((x,y,z))
        x+=arreglo[0]
        z+=arreglo[2]
        q+=1

        


    
    resultado=[]
    resultado.append(A)
    resultado.append(B)
    resultado.append(C)
    resultado.append(D)
    resultado.append(E)
    
    return resultado

ga=[4,2,6,4,4]
print(posicionar(20,50,50,resultado,ga))
#
print(ordenado)




desperdicio=((areaTotal(areas)/volumen)*100)

#print(areas)



print("Cortes respecto a áreas: ")
print(BinPacking(areas,volumen))
#print(areaTotal(areas))
#print(volumen)
print("Desperdicio: ")
print(desperdicio,"%")
print("Posiciones: ")
print(posicionar(20,50,50,resultado,ga))
print(ordenado)

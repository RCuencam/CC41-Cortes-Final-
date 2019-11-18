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


def imprimir():
	print("Area,ancho,alto")
	print(MostrarAreas(G))
	volumen=SepararArea(MostrarAreas(G))
	
	print("Sólo las areas")
	print(volumen)
	
	print("Separando los cortes en cada plancha")
	resultado=BinPacking(volumen,planchaArea)
	print(resultado)
	
	nroCortes=len(resultado)
	print("Numero de Planchas: ",nroCortes)
	
	print("Area Total:")
	print(AreaTotal(volumen))
	print(Desperdicio(AreaTotal(volumen)),"%")


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


'''def posicionar(largo,ancho,alto,arreglo,ordenado):
    n=len(arreglo)
    resultado=[]
    resultado.append([0,0,0])
    x=0
    y=0
    z=arreglo[2]
    q=0
    q1=0
    q2=0
    z1=0
    #while x<largo and y<ancho and z<alto:# Para que no sobrepase las dimensiones de la caja
    cambio=False
    

    while z<=alto and q<4:
        
        resultado.append([0,0,z])
        z+=arreglo[2]
        q+=1
        a=ordenado[1]
    while z1<=alto and q1<2:

        resultado.append([0,a[1],z1])
        z1+=arreglo[2]
        q1+=1
    
    while z1<=alto and q2<6:
        
        a+=ordenado[q2]
        resultado.append([0,a[1],z1])
        z1+=arreglo[2]
        q2+=1

        
        
        
    
    return resultado
'''

def posicionar(largo,ancho,alto,arreglo,cantidad):
    q=0
    x=arreglo[0]
    y=arreglo[1]
    z=arreglo[2]
    A=[None]*cantidad[0]
    B=[None]*cantidad[1]
    C=[None]*cantidad[2]
    D=[None]*cantidad[3]
    E=[None]*cantidad[4]
    
    
    while z<alto and q<cantidad[0] and y<=ancho:
        A.append((x,y,z))
        z+=arreglo[2]
        q+=1

    y+=arreglo[1]
    z=0
    q=0
   

    while z<alto and q<cantidad[1] and y<=ancho:
        
        B.append((x,y,z))
        z+=arreglo[cantidad[0]*3+2]
        q+=1

    q=0
    y+=arreglo[1]
    z=0


    while z<alto and q<cantidad[2]:
        
        C.append((x,y,z))
        z+=arreglo[cantidad[1]*3+2]
        q+=1
    while y>ancho and q<cantidad[1]:
        A.append((x,y,z))
        B.append((x,y,z))
        x+=arreglo[0]
        z+=arreglo[2]
        q+=1

        


    
    resultado=[]
    resultado.append(A)
    resultado.append(B)
    resultado.append(C)

    return resultado

ga=[4,2,6,5,4]
print(posicionar(20,30,100,resultado,ga))

#print(posicionar(20,30,50,resultado))
print(ordenado)
print(resultado)



desperdicio=((areaTotal(areas)/volumen)*100)

#print(areas)
#print(areaTotal(areas))


#print(BinPacking(areas,volumen))
#print(volumen)
#print(desperdicio,"%")
#G=[(4,5),(1,3),(2,4),(5,6)]
planchaArea=30
#print(imprimir())
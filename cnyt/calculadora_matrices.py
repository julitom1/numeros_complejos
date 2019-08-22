from sys import stdin
import imaginar
def adicion_vectores(matriz1,matriz2):
    try:
        rta=[]
        matriz1=[[(2,1),(0,0),(1,3)],[(3,2),(4,3),(5,2)]]
        matriz2=[[(2,1),(0,0),(1,3)],[(3,2),(4,3),(5,2)]]
        n=len(matriz1[0])
        for x in range(len(matriz1)):
            lis=[]
            for y in range(n):
                adicion = imaginar.suma(matriz1[x][y],matriz2[x][y])
                lis.append(adicion)
            rta.append(lis)
        return rta
    except:
        return "La suma no tiene las mismas dimensiones"
def inversion_vectores(matriz1):
    #try:
        n=len(matriz1[0])
        matriz2=matriz_adjunta(matriz1)
        matriz2=transpuesta(matriz2)
        adj=cofactores(matriz1)
        lis=[]
        for x in range(len(matriz2)):
            lista=[]
            for y in range(len(matriz2)):
                lista.append(imaginar.division((matriz2[x][y],adj)))
            lis.append(lista)
        return lis
        
        
    #except:print("no tiene las mismas dimensiones")
def multiplicacion_escalar(escalar,matriz):
    matriz2=[]
    n=len(matriz)
    for x in range(n):
        m=[]
        for y in range(n):
            m.append(imaginar.multiplicacion(escalar,matriz[x][y]))
        matriz2.append(m)
    return matriz2

def transpuesta(matriz1):
    matriz2=[]
    for x in range(len(matriz1[0])):
        lis=[]
        for y in range(len(matriz1)):
            lis.append(matriz1[y][x])
        matriz2.append(lis)
    return matriz2

def matriz_conjugada(matriz1):
        n=len(matriz1)
        for x in range(n):
                for y in range(n):
                        matriz1[x][y]=imaginar.conjugado(matriz1[x][y])
        return matriz1


def matriz_adjunta(matriz1):
    lista=[]
    for x in range(len(matriz1)):
        lis=[]
        for y in range(len(matriz1)):
            lis.append(cofactores(matriz1,x,y))
        lista.append(lis)
    return lista

#def matriz_accion():

def norma(matriz):
    norma = multiplicacion_matriz(matriz*matriz)
    for x in range(len(norma)):
        for y in range(len(norma)):
            norma[x][y]=raiz_matriz(norma[x][y])
    return norma

#def distancia_matrices():
    
def matriz_unitaria(matriz1):
        matriz2=matriz1*transpuesta(matriz1)
        return matriz2==matriz1
def matriz_hermitiana(matriz):
        matriz2=transpuesta(matriz)
        print(matriz2)
        matriz2=matriz_conjugada(matriz2)
        return  matriz==matriz2 
def producto_tensor(m1,m2):
    lista=[]
    for x in range(len(m1)):
        for y in range(len(m1)):
            lis=[]
            for k in range(len(m2)):
                for z in range(len(m2)):
                    lis.append(imaginar.multiplicacion(m1[x][y],m2[k][z]))
            lista.append(lis)
    return lista

def cofactores(matriz1,i,j):
    negativos=0
    while len(matriz1)>2:
        n=len(matriz1)
        matriz2=[]
        for x in range(n):
            m=[]
            if x!=i:
                for y in range(n):
                    if y!=j:
                        m.append(matriz1[x][y])
                        print(m)
                matriz2.append(m)
        matriz1=matriz2
        if (i+j)%2!=0:
            negativos+=1
    print(matriz1)
    m=imaginar.multiplicacion(matriz1[0][0],matriz1[1][1])
    n=imaginar.multiplicacion(matriz1[0][1],matriz1[1][0])
    rta=imaginar.resta(m,n)
    if negativos%2!=0:
        rta=imaginar.multiplicacion((-1,0),rta)
    return rta
                
    
def determinante(matriz1):
    rta=cofactores(matriz1,0,0)
    rta=imaginar.multiplicacion(matriz1[0][0],rta)
    return rta
    
def raiz_matriz(valor,y):
    mod=cartesiano_polar(valor)
    rta= mod[0]**(1/y),mod[1]/2
    return rta
            
def multiplicacion_matriz(matriz1,matriz2):
    lista=[]
    for x in range(len(matriz1)):
        lis=[]
        for y in range(len(matriz2)):
            sumar=(0,0)
            for z in range(len(matriz1[0])):
                k=imaginar.multiplicacion(matriz1[x][z],matriz2[z][y])
                lis.append(imaginar.sumar(sumar,k))
        lista.append(lis)
    return lista
        




                
            


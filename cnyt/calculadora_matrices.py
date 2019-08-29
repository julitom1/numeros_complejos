from sys import stdin
import imaginar
def producto_escalar(c,v1):
    for x in range(len(v1)):
        v1[x]=imaginar.multiplicacion(c,v1[x])
    return v1

def adicion_vectores(matriz1,matriz2):
    
    matriz3,matriz4=[],[]
    matriz3.append(matriz1)
    matriz4.append(matriz2)
    return adicion_matrices(matriz3,matriz4)

def inversa_vectores(matriz1):
    
    for x in range(len(matriz1)):
        matriz1[x]=(-matriz1[x][0],-matriz1[x][1])
    return matriz1

def adicion_matrices(matriz1,matriz2):
    try:
        rta=[]
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
def inversa(matriz1):
    #try:
        n=len(matriz1[0])
        matriz2=transpuesta(adjunta(matriz1))
        det=determinante(matriz1)
        lis=[]
        for x in range(len(matriz2)):
            lista=[]
            for y in range(len(matriz2)):
                lista.append(imaginar.division(matriz2[x][y],det))
            lis.append(lista)
        return lis
    #except:print("no tiene las mismas dimensiones")
def multiplicacion_escalar_matrices(escalar,matriz):
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
            z=matriz1[y][x]
            lis.append(z)
        matriz2.append(lis)
    return matriz2

def conjugada(matriz1):
        n=len(matriz1)
        for x in range(n):
                for y in range(n):
                        matriz1[x][y]=imaginar.conjugado(matriz1[x][y])
        return matriz1


def adjunta(matriz1):
    lista=[]
    for x in range(len(matriz1)):
        lis=[]
        for y in range(len(matriz1)):
            k=determinante(cofactores(matriz1,x,y))
            if (x+y)%2!=0:
                k=imaginar.multiplicacion((-1,0),k)
            lis.append(k)
        lista.append(lis)
    return lista

#def matriz_accion():

def norma(matriz):
    matriz2=transpuesta(matriz)
    matriz2=multiplicacion_matriz(matriz2,matriz)
    suma=0
    for x in range(len(matriz2)):
        suma+=matriz[x][x][0]
    return suma**(1/2)

#def distancia_matrices():
    
def matriz_unitaria(matriz1):
        matriz3=transpuesta(matriz1)
        matriz3=conjugada(matriz3)
        matriz2=[]
        matriz1=multiplicacion_matriz(matriz1,matriz3)
        n=matriz1[0][0]
        for x in range(len(matriz1)):
            lis=[]
            for y in range(len(matriz1)):
                if x==y:
                    lis.append((1,0))
                    matriz1[x][y]=imaginar.division(matriz1[x][y],n)
                else:
                    lis.append((0,0))
            matriz2.append(lis)
        return matriz2==matriz1
    
def matriz_hermitiana(matriz):
        matriz2=transpuesta(matriz)
        matriz2=conjugada(matriz2)
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
    n=len(matriz1)
    matriz2=[]
    for x in range(n):
        m=[]
        if x!=i:
            for y in range(n):
                if y!=j:
                    m.append(matriz1[x][y])
            matriz2.append(m)
    return matriz2
                
def determinante(matriz1):
    sumar=0,0
    if len(matriz1)>2:
        for x in range(len(matriz1)):
            matriz2=cofactores(matriz1,x,0)
            rta=imaginar.multiplicacion(matriz1[x][0],determinante(matriz2))
            if x%2!=0:
                rta=imaginar.multiplicacion((-1,0),rta)
            sumar=imaginar.suma(sumar,rta)
        return sumar
    if len(matriz1)==2:
        r1=imaginar.multiplicacion(matriz1[0][0],matriz1[1][1])
        r2=imaginar.resta(r1,imaginar.multiplicacion(matriz1[0][1],matriz1[1][0]))
    else:
        r2=matriz1[0][0]
    return r2
            
def multiplicacion_matriz(matriz1,matriz2):
    lista=[]
    for x in range(len(matriz1)):
        lis=[]
        for y in range(len(matriz2[0])):
            sumar=(0,0)
            for z in range(len(matriz2)):
                k=imaginar.multiplicacion(matriz1[x][z],matriz2[z][y])
                sumar=imaginar.suma(sumar,k)
            lis.append(sumar)
        lista.append(lis)
    return lista

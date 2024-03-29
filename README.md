# Libreria de una calculadora de numeros complejos

Es una libreria para python capaz de calcular las operaciones basicas de los numeros complejos, operaciones con vectores y además operaciones con matrices.

# Operaciones basicas:

Esta libreria se importa con el nombre de imaginar. (**import imaginar**)
El uso de esta libreria es mediante tuplas donde el primer numero representa la parte real y la segunda la parte imaginaria.
A continuacion se encuentra las operaciones que maneja, si se desea manejar alguna operacion es cuestion de llamarla es decir imaginar.funcion(el nombre de la funcion que desea usar) a continuacion se muestra el nombre de las funciones:

  **Suma entre numeros complejos:                sumar(tupla1,tupla2)**
  
  Recibe dos tuplas retorna una tupla con la suma de las dos tuplas enviadas.
  
  **Resta entre numeros complejos:               resta(tupla1,tupla2)**
  
  Recibe dos tuplas retorna una tupla con la resta de las dos tuplas enviadas.
  
  **Multiplicacion entre numeros complejos:      multiplicacion(tupla1,tupla2)**
  
  Recibe dos tuplas retorna una tupla con la multiplicacion de las dos tuplas enviadas.
  
  **Division entre numeros complejos:            division(tupla1,tupla2)**
  
  Recibe dos tuplas retorna una tupla con la division de las dos tuplas enviadas.
  
  **La fase de un numero complejo:               fase(tupla1)**
  
  Recibe una tupla que retorna un flotante que representa la fase.
  
  **Conversion de cartesiano a polar:            cartesiano_polar(tupla1)**
  
  Recibe una tupla que retorna una tupla donde el primer numero representa el ,odulo y el segundo la fase.
  
  **Conversion de polar a cartesiano:            polar_cartesiano(tupla1)**
  
 Recibe una tupla que retorna una tupla donde el primer numero representa el real y el segundo el imaginario.
  
  **El modulo:                                   modulo(tupla1)**
  
  Recibe una tupla que retorna un numero flotante que es el modulo de la tupla enviada
  
  **El conjugado:                                conjugado(tupla1)**
  
  Recibe una tupla que retorna una tupla con el conjugado de la tupla enviada
  
# Calculadora de matrices con numeros imaginarios

Esta libreria se importa con el nombre de calculadora_matrices que se apoya a traves de la libreria de imaginar.
El uso de esta libreria es mediante listas y adentro se colocan las tuplas donde el primer numero representa la parte real y la segunda la parte imaginaria.
A continuacion se encuentra las operaciones que maneja:

Para utilizar la calculadora de matrices imaginarios, se importa con: **import calculadora_matrices** y tiene que tener descargada la libreria de imaginar no es necesario llamarla, puesto que esta ya la llama.

Esta calculadora de matrices al igual que la calculadora normal de imaginarios funciona mediante tuplas de longitud 2, donde el primer numero representa la parte real y el segundo la parte imaginaria, si se van a llamar funciones con listas o matrices, se llena con tuplas. Si es un numero real, sin imaginario se llena el espacio imaginario con un cero, igualmente en diseversa.

Para invocar la calculadora de matrices es cuestion de llamarla como calculadora_matrices.funcion(el nombre de la funcion que desea usar) a continuacion se muestra el nombre de las funciones

**Operaciones con vectores y matrices:**

  **Adición de vectores complejos: adicion_vectores(lista1,lista2)**
  
  Calcula la adicion entre 2 vectores complejos, se le pasa dos listas de la misma longitud y devolvera una lista con la suma de los dos vectores, la lista esta conformada de tuplas.
      
  **Inversa de vectores complejos:   inversa_vectores(lista1)**
  
  Recibe una lista y retorna una lista que contiene la inversa de la lista enviada.
  
  **Multiplicación escalar de vectores complejos:producto_escalar(tupla1,lista1)**
  
  Recibe una tupla de longitud 2 y una lista retorna una lista que contiene la multiplicacion de la tupla con cada componente de la lista.
  
  **Adición de matrices complejos: adicion_matrices(matriz1,matriz2):**
  
  Recibe dos matrices y retorna una matriz que contiene la suma de elemento por elemento de las dos matrices enviadas.
  
  **Inversa de matrices complejos:  inversa(matriz1)** 
  
  Recibe una matriz y devuelve una matriz que contiene la inversa de la matriz.
  
  **Multiplicación escalar de matrices complejas: multiplicacion_escalar_matrices(tupla1,matriz1)**
  
  Recibe una tupla y una matriz y retorna una matriz que contiene la multiplicacion de la tupla con cada componente.
  
  **Matriz transpuesta: transpuesta(matriz1)**
  
  Recibe una matriz y retorna la matriz que contiene la transpuesta de la matriz enviada
  
  **Matriz conjugada:           conjugada(matriz1)** 
  
  Recibe una matriz y retorna una matriz que contiene el signo contrario en la parte imaginaria
  
  **Matriz adjunta:                 adjunta(matriz1)**   
  
  Recibe una matriz y retorna una matrizque contiene la adjunta de la matriz enviada
  
  **Norma de matrices: norma(matriz)**
  
  Recibe una matriz y retorna un float que representa la norma de la matriz.
  
  **Distancia entrematrices: distancia_matrices(matriz1,matriz2)**
  
  Recibe 2 matrices del mismo tamaño y retorna un numero flotante que representa la distancia entre las dos matrices.
  
  **Revisar si es unitaria: matriz_unitaria(matriz1)**
  
  Recibe una matriz y retorna y retorna un booleano diciendo si es una matriz unitaria o no.
  
  **Revisar si es Hermitian:matriz_hermitiana(matriz)**
  
  Recibe una matriz y retorna y retorna un booleano diciendo si es una matriz hermitiana o no.
  
  **Producto tensor: producto_tensor(matriz1,matriz2)**
  
  Recibe 2 matrices y retorna una matriz con el producto tensor de las dos matrices enviadas.
  
 
  # Autores
  
  *Yarit Yajanny Villalobos Jimenez
  
  

# Libreria de una calculadora de numeros complejos

Es una libreria para python capaz de calcular las operaciones basicas de los numeros complejos, operaciones con vectores y además operaciones con matrices.

**Operaciones basicas:**

Esta libreria se importa con el nombre de imaginar.
El uso de esta libreria es mediante tuplas donde el primer numero representa la parte real y la segunda la parte imaginaria.
A continuacion se encuentra las operaciones que maneja:

  * Suma entre numeros complejos:                (sumar(tupla1,tupla2))
  * Resta entre numeros complejos:               (resta(tupla1,tupla2))
  * Multiplicacion entre numeros complejos:      (multiplicacion(tupla1,tupla2))
  * Division entre numeros complejos:            (division(tupla1,tupla2))
  * La fase de un numero complejo:               (fase(tupla1))
  * Conversion de cartesiano a polar:            (cartesiano_polar(tupla1))
  * Conversion de polar a cartesiano:            (polar_cartesiano(tupla1))
  * El modulo:                                   (modulo(tupla1))
  * El conjugado:                                (conjugado(tupla1))
  
**Operaciones con vectores y matrices:**

Esta libreria se importa con el nombre de calculadora_matrices que se apoya a traves de la libreria de imaginar.
El uso de esta libreria es mediante listas y adentro se colocan las tuplas donde el primer numero representa la parte real y la segunda la parte imaginaria.
A continuacion se encuentra las operaciones que maneja:

  * Adición de vectores complejos:   adicion_vectores(lista1,lista2)
  * Inversa de vectores complejos:   inversa_vectores(lista1)       
  * Multiplicación escalar de vectores complejos:   producto_escalar(tupla1,lista1)
  * Adición de matrices complejos: adicion_matrices(matriz1,matriz2): 
  * Inversa de matrices complejos:  inversa(matriz1)  
  * Multiplicación escalar de matrices complejas:       multiplicacion_escalar_matrices(tupla1,matriz1)
  * Matriz transpuesta:           transpuesta(matriz1) 
  * Matriz conjugada:           conjugada(matriz1)          
  * Matriz adjunta:                 adjunta(matriz1)               
  * Función para calcular la "acción" de una matriz sobre un vector: en proceso
  * Norma de matrices: en proceso
  * Distancia entrematrices: en proceso
  * Revisar si es unitaria: matriz_unitaria(matriz1)
  * Revisar si es Hermitian:matriz_hermitiana(matriz)
  * Producto tensor: producto_tensor(matriz1,matriz2)
  

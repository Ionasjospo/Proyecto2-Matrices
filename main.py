import numpy as np
from skimage.io import imshow, imread
import cv2
import os
import matplotlib.pyplot as plt
from utils import utils

## Parte 1) Cargar dos imagenes a elección utilizando imread y mostrarlas como imagen
img1 = utils("Images/img1.jpg")
img2 = utils("Images/img2.jpg")

#img1.showImage('First Image')
#img2.showImage('Second Image')

## Parte 2) Imprimir el tamaño de cada una de las imágenes.
print(f"Tamaño de la imagen 1: {img1.getShape()}")
print(f"Tamaño de la imagen 1: {img2.getShape()}")



##Parte 3) Recortar ambas imágenes para que tengan el mismo tamaño,
# siendo un requisito que la imagen sea cuadrada. Mostrar el resultado obtenido como imágenes.
img1.cut_image("Images/newImage.jpg", 0, 500, 350, 850)
img2.cut_image("Images/newImage1.jpg", 50, 550, 700, 1200)


img1_cortada = utils("Images/newImage.jpg")
img2_cortada = utils("Images/newImage1.jpg")


##Parte 4) Para una de las imágenes recortadas, mostrarla como una matriz. Imprimir el tamaño.

## Matrices de las imagenes
img1_matriz = img1_cortada.imagen_a_matriz()
img2_matriz = img2_cortada.imagen_a_matriz()

# Mostrar la matriz de la imagen en la consola
print("Matriz de la imagen 1:")
print(img1_matriz)

print(f"Tamaño de la imagen 1 recortada: {img1_cortada.getShape()}")
##print("Matriz de la imagen 2:")
##print(img2_matriz)
utils.imprimir_dos_matrices(img1_matriz, img2_matriz, "Matriz")

##Parte 5) Calcular la matriz traspuesta de las imágenes del punto 3.
# Mostrarlas como matriz y como imagen. Comentar los resultados.

## Traspuestas de las imagenes

img1_traspuesta = img1_cortada.calcular_traspuesta()
img2_traspuesta = img2_cortada.calcular_traspuesta()

print("Traspuesta de la imagen 1:")
print(img1_traspuesta)
print("Traspuesta de la imagen 2:")
print(img2_traspuesta)

utils.imprimir_dos_matrices(img1_traspuesta, img2_traspuesta, "Traspuesta")

## Parte 6) Convertir y mostrar las imagenes recortadas a escala de grises.
# Convertir las imágenes recortadas a escala de grises

img1_gris = img1_cortada.convertir_a_escala_de_grises()
img2_gris = img2_cortada.convertir_a_escala_de_grises()

utils.imprimir_dos_matrices(img1_gris, img2_gris, "Escala de grises")

## Parte 7) Verificar para cada una de las matrices correspondientes a las imágenes recortadas,
# si existe su inversa y en caso de que exista, calcular.



## Parte 8) Producto de una matriz por un escalar
# Observar y comentar qué ocurre con las imagenes del punto 6 al
# multiplicarla por un escalar α en dos casos:
#  CASO 1:  α>1
# CASO 2:  0<α<1
# Para este punto elegir solo una de las dos imágenes.



print(f"Matriz antes de multiplicar por escalar 9. {img2_gris}")
utils.matriz_a_imagen("Antes de multiplicar por escalar 9", img2_gris)
img2_por_escalar = utils.matriz_por_escalar(img2_gris, 9)
print(f"Matriz luego de multiplicar por escalar 9. {img2_por_escalar}")
utils.matriz_a_imagen("Despues de multiplicar por escalar 9", img2_por_escalar)

print(f"Matriz antes de multiplicar por escalar 0,5 . {img2_gris}")
utils.matriz_a_imagen("Antes de multiplicar por escalar 0,5 ", img2_gris)
img2_por_escalar = utils.matriz_por_escalar(img2_gris, (0.5))
print(f"Matriz luego de multiplicar por escalar 0,5 . {img2_por_escalar}")
utils.matriz_a_imagen("Despues de multiplicar por escalar 0,5 ", img2_por_escalar)

#utils.imprimir_dos_matrices(img1_por_escalar, img2_por_escalar, "Matrices por escalar")


## Parte 9) Multipicación de matrices y prueba de que la multiplicación de matrices no es conmutativa:
##La multiplicación de matrices el orden en el que se multiplican las matrices sí importa
# Aplicación: Voltear una imágen
# Para voltear una imagen alrededor del eje  x  podemos multiplicar la imagen original por una matriz  W  con 1's en la anti-diagonal.
# Para generar esta última matriz, les recomendamos primero generar la matriz identidad del mismo tamaño que la imagen,
# y luego utilizar la función np.fliplr para obtener  W .
# Comentar el resultado. Qué ocurre si invertimos el orden en el que multiplicamos las matrices?

utils.matriz_a_imagen("Antes de voltear: ", img2_gris)
w = utils.crear_W(img2_gris.shape)

matriz_img2_multiplicada_por_identidad_inversa1 = utils.voltear_imagen(img2_gris, w)
utils.matriz_a_imagen("Luego de voltear: ", matriz_img2_multiplicada_por_identidad_inversa1)

matriz_img2_multiplicada_por_identidad_inversa2 = utils.voltear_imagen(w, img2_gris)


print("efrewrfergertgergergergerg",matriz_img2_multiplicada_por_identidad_inversa1)
utils.matriz_a_imagen("Luego de voltear: ", matriz_img2_multiplicada_por_identidad_inversa2)

print(f"Se cumple la propiedad conmutativa:  {utils.son_iguales(matriz_img2_multiplicada_por_identidad_inversa1,matriz_img2_multiplicada_por_identidad_inversa2)}")


## Parte 10) Calcular el negativo de una de las imagenes utilizando la resta de matrices.
# NOTA: El negativo de la imagen se calcula restando la matriz que se muestra a continuación a la imagen (matriz_auxiliar - imagen):


negativo_img1 = utils.negativo_imagen(img1_gris, img2_gris.shape)
utils.matriz_a_imagen("Negativo de la imagen 1: ", negativo_img1)
import numpy as np
from skimage.io import imshow, imread
import cv2
import os
import matplotlib.pyplot as plt
from utils import utils


## Parte 1 -----------------------------------------
img1 = utils("Images/img1.jpg")
img2 = utils("Images/img2.jpg")

##img1.showImage('First Image')
##img2.showImage('Second Image')

print(f"Tamaño antes de cortar : {img1.getShape()}")
img1.cut_image("Images/newImage.jpg",0, 500, 350, 850)
img2.cut_image("Images/newImage1.jpg",50, 550, 700, 1200)

img1_cortada = utils("Images/newImage.jpg")
img2_cortada = utils("Images/newImage1.jpg")

## Matrices de las imagenes

img1_matriz = img1_cortada.imagen_a_matriz()
img2_matriz = img2_cortada.imagen_a_matriz()

# Mostrar la matriz de la imagen en la consola
print("Matriz de la imagen 1:")
print(img1_matriz)
print("Matriz de la imagen 2:")
print(img2_matriz)

utils.imprimir_dos_matrices(img1_matriz, img2_matriz, "Matriz")


## Traspuestas de las imagenes

img1_traspuesta = img1_cortada.calcular_traspuesta()
img2_traspuesta = img2_cortada.calcular_traspuesta()

print("Traspuesta de la imagen 1:")
print(img1_traspuesta)
print("Traspuesta de la imagen 2:")
print(img2_traspuesta)

utils.imprimir_dos_matrices(img1_traspuesta, img2_traspuesta, "Traspuesta")


# Convertir las imágenes recortadas a escala de grises

img1_gris = img1_cortada.convertir_a_escala_de_grises()
img2_gris = img2_cortada.convertir_a_escala_de_grises()

utils.imprimir_dos_matrices(img1_gris, img2_gris, "Escala de grises")




import tkinter as tk
from tkinter import ttk
import numpy as np
from skimage.io import imshow, imread
import cv2
import os
import matplotlib.pyplot as plt
from utils import utils


def parte1():
    ## Parte 1) Cargar dos imagenes a elección utilizando imread y mostrarlas como imagen
    img1 = utils("Images/img1.jpg")
    img2 = utils("Images/img2.jpg")
    img1.showImage("Imagen 1")
    img2.showImage("Imagen 2")

def parte2():
    ## Parte 2) Imprimir el tamaño de cada una de las imágenes.
    img1 = utils("Images/img1.jpg")
    img2 = utils("Images/img2.jpg")
    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, "Parte 2: \n")
    mostrarTexto.insert(tk.END, f"Tamaño de la imagen 1: {img1.getShape()}\n")
    mostrarTexto.insert(tk.END, f"Tamaño de la imagen 2: {img2.getShape()}\n")


def parte3():
    ##Parte 3) Recortar ambas imágenes para que tengan el mismo tamaño,
    # siendo un requisito que la imagen sea cuadrada. Mostrar el resultado obtenido como imágenes.
    img1 = utils("Images/img1.jpg")
    img2 = utils("Images/img2.jpg")
    img1.cut_image("Images/newImage.jpg", 0, 500, 350, 850)
    img2.cut_image("Images/newImage1.jpg", 50, 550, 700, 1200)

    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_cortada.showImage("Imagen 1 recortada")
    img2_cortada.showImage("Imagen 2 recortada")

def parte4():
    ##Parte 4) Para una de las imágenes recortadas, mostrarla como una matriz. Imprimir el tamaño.
    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_matriz = img1_cortada.imagen_a_matriz()
    img2_matriz = img2_cortada.imagen_a_matriz()

    # Mostrar la matriz de la imagen en la consola
    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, "Parte 4: \n")
    mostrarTexto.insert(tk.END, f"Matriz de la imagen 1: \n {img1_matriz}\n")
    mostrarTexto.insert(tk.END, f"Tamaño de la imagen 1 recortada: \n {img1_cortada.getShape()}\n")

def parte5():
    ##Parte 5) Calcular la matriz traspuesta de las imágenes del punto 3.
    # Mostrarlas como matriz y como imagen. Comentar los resultados.

    ## Traspuestas de las imagenes
    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_traspuesta = img1_cortada.calcular_traspuesta()
    img2_traspuesta = img2_cortada.calcular_traspuesta()

    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, "Parte 5: \n")
    mostrarTexto.insert(tk.END, f"Traspuesta de la imagen 1: \n {img1_traspuesta}\n")
    mostrarTexto.insert(tk.END, f"Traspuesta de la imagen 2: \n {img2_traspuesta}\n")

    utils.matriz_a_imagen("Imagen 1 transpuesta: ", img1_traspuesta)
    utils.matriz_a_imagen("Imagen 2 transpuesta: ", img2_traspuesta)

def parte6():
    ## Parte 6) Convertir y mostrar las imagenes recortadas a escala de grises.
    # Convertir las imágenes recortadas a escala de grises

    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_gris = img1_cortada.convertir_a_escala_de_grises()
    img2_gris = img2_cortada.convertir_a_escala_de_grises()

    utils.matriz_a_imagen("Imagen 1 con escala de grises: ", img1_gris)
    utils.matriz_a_imagen("Imagen 2 con escala de grises: ", img2_gris)

def parte7():

    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_gris = img1_cortada.convertir_a_escala_de_grises()
    img2_gris = img2_cortada.convertir_a_escala_de_grises()



    utils.matriz_inversa(img1_gris)
    img1_inversa = utils.matriz_inversa(img1_gris)
    img2_inversa = utils.matriz_inversa(img2_gris)
    utils.matriz_a_imagen("Imagen 1 inversa: ", img1_inversa)

    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, "Parte 7: \n")
    mostrarTexto.insert(tk.END, f"Matriz inversa de la imagen 1: \n {img1_inversa}\n")

    mostrarTexto.insert(tk.END, f"Matriz inversa de la imagen 2: \n {img2_inversa}\n")
    utils.matriz_a_imagen("Imagen 2 inversa: ", img2_inversa)


def parte8():
    ## Parte 8) Producto de una matriz por un escalar
    # Observar y comentar qué ocurre con las imagenes del punto 6 al
    # multiplicarla por un escalar α en dos casos:
    #  CASO 1:  α>1
    # CASO 2:  0<α<1
    # Para este punto elegir solo una de las dos imágenes.
    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_gris = img1_cortada.convertir_a_escala_de_grises()
    img2_gris = img2_cortada.convertir_a_escala_de_grises()

    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, "Parte 6: \n")
    mostrarTexto.insert(tk.END, f"Matriz antes de multiplicar por escalar 9. {img2_gris}\n")



    utils.matriz_a_imagen("Antes de multiplicar por escalar 9", img2_gris)

    img2_por_escalar = utils.matriz_por_escalar(img2_gris, 9)

    mostrarTexto.insert(tk.END, f"Matriz luego de multiplicar por escalar 9. {img2_por_escalar}\n")
    utils.matriz_a_imagen("Despues de multiplicar por escalar 9", img2_por_escalar)

    mostrarTexto.insert(tk.END, f"Matriz luego de multiplicar por escalar 0,5 . {img2_gris}\n")

    utils.matriz_a_imagen("Antes de multiplicar por escalar 0,5 ", img2_gris)
    img2_por_escalar = utils.matriz_por_escalar(img2_gris, (0.5))
    mostrarTexto.insert(tk.END, f"Matriz luego de multiplicar por escalar 0,5 . {img2_por_escalar}\n")

    utils.matriz_a_imagen("Despues de multiplicar por escalar 0,5 ", img2_por_escalar)

def parte9():
    ## Parte 9) Multipicación de matrices y prueba de que la multiplicación de matrices no es conmutativa:
    ##La multiplicación de matrices el orden en el que se multiplican las matrices sí importa
    # Aplicación: Voltear una imágen
    # Para voltear una imagen alrededor del eje  x  podemos multiplicar la imagen original por una matriz  W  con 1's en la anti-diagonal.
    # Para generar esta última matriz, les recomendamos primero generar la matriz identidad del mismo tamaño que la imagen,
    # y luego utilizar la función np.fliplr para obtener  W .
    # Comentar el resultado. Qué ocurre si invertimos el orden en el que multiplicamos las matrices?

    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_gris = img1_cortada.convertir_a_escala_de_grises()
    img2_gris = img2_cortada.convertir_a_escala_de_grises()

    utils.matriz_a_imagen("Antes de voltear: ", img2_gris)

    w = utils.crear_W(img2_gris.shape)
    matriz_img2_multiplicada_por_identidad_inversa1 = utils.voltear_imagen(img2_gris, w)
    utils.matriz_a_imagen("Luego de voltear (matriz x w) : ", matriz_img2_multiplicada_por_identidad_inversa1)

    matriz_img2_multiplicada_por_identidad_inversa2 = utils.voltear_imagen(w, img2_gris)


    utils.matriz_a_imagen("Luego de voltear(w x matriz): ", matriz_img2_multiplicada_por_identidad_inversa2)
    mostrarTexto.delete("1.0", "end")
    mostrarTexto.insert(tk.END, f"Parte 9: \n")
    mostrarTexto.insert(tk.END, f"Se cumple la propiedad conmutativa:  {utils.son_iguales(matriz_img2_multiplicada_por_identidad_inversa1, matriz_img2_multiplicada_por_identidad_inversa2)}\n")



def parte10():
    ## Parte 10) Calcular el negativo de una de las imagenes utilizando la resta de matrices.
    # NOTA: El negativo de la imagen se calcula restando la matriz que se muestra a continuación a la imagen (matriz_auxiliar - imagen):

    img1_cortada = utils("Images/newImage.jpg")
    img2_cortada = utils("Images/newImage1.jpg")
    img1_gris = img1_cortada.convertir_a_escala_de_grises()
    img2_gris = img2_cortada.convertir_a_escala_de_grises()

    negativo_img1 = utils.negativo_imagen(img1_gris, img2_gris.shape)
    utils.matriz_a_imagen("Negativo de la imagen 1: ", negativo_img1)

def main():
    ventana = tk.Tk()
    ventana.title("Menú Principal")

    # Tamaño de la ventana (ancho x alto)
    ventana.geometry("800x700")

    # Crea un área de texto para mostrar el texto
    global mostrarTexto
    mostrarTexto = tk.Text(ventana, wrap=tk.WORD, height=5, width=50)
    mostrarTexto.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    estilo_botones = ttk.Style()
    estilo_botones.configure("Boton.TButton", background="blue", foreground="white")

    # Crea botones para cada parte con un estilo ttk
    botones = []
    for i in range(1, 11):
        nombre_boton = f"Parte {i}"
        funcion_boton = globals()[f"parte{i}"]  # Obtiene la función por su nombre
        boton = ttk.Button(ventana, text=nombre_boton, command=funcion_boton)
        boton.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    main()







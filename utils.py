import numpy as np
from skimage.io import imshow, imread
import cv2
import matplotlib.pyplot as plt
import os

class utils:
    path = ""
    # Carga la imagen desde la ubicación del archivo
    image = ""
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(self.path)

    def getShape(self):
        return self.image.shape
    def showImage(self, name):
        # Muestra la imagen en una ventana
        cv2.imshow(name, self.image)


        # Espera a que el usuario presione una tecla
        cv2.waitKey(0)

        # Cierra todas las ventanas
        cv2.destroyAllWindows()




    def cut_image(self, ruta_img_crop: str, x_inicial: int, x_final: int, y_inicial: int,
                           y_final: int) -> None:
        """
        Esta función recibe una imagen y devuelve otra imagen recortada.

        Args:
          ruta_img (str): Ruta de la imagen original que se desea recortar.
          ruta_img_crop (str): Ruta donde se guardará la imagen recortada.
          x_inicial (int): Coordenada x inicial del área de recorte.
          x_final (int): Coordenada x final del área de recorte.
          y_inicial (int): Coordenada y inicial del área de recorte.
          y_final (int): Coordenada y final del área de recorte.

        Return
          None
        """
        try:
            # Abrir la imagen
            image = self.image

            # Obtener la imagen recortada
            image_crop = image[x_inicial:x_final, y_inicial:y_final]

            # Guardar la imagen recortada en la ruta indicada
            cv2.imwrite(ruta_img_crop, image_crop)

            print("Imagen recortada con éxito. El tamaño de la imagen es de" + str(image_crop.shape))
        except Exception as e:
            print("Ha ocurrido un error:", str(e))

    def imagen_a_matriz(self):
        imagen = self.image
        # Asegurarse de que la imagen se haya cargado correctamente
        if imagen is not None:
            # Convertir de BGR a RGB
            imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

            
            return imagen_rgb
        else:
            print("No se pudo cargar la imagen.")

    def matriz_a_imagen(titulo, matriz):
        # Normaliza la matriz para que los valores estén en el rango 0-255
        matriz_normalizada = (matriz - np.min(matriz)) / (np.max(matriz) - np.min(matriz)) * 255

        # Utiliza np.clip() para asegurarte de que los valores estén en el rango 0-255
        matriz_normalizada = np.clip(matriz_normalizada, 0, 255)

        # Convierte los valores a enteros de 8 bits
        matriz_normalizada = matriz_normalizada.astype(np.uint8)

        # Muestra la imagen
        cv2.imshow(titulo, matriz_normalizada)
        cv2.moveWindow(titulo, 900, 100)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    @staticmethod
    def imprimir_dos_matrices(img1, img2, texto: str):
        # Mostrar las imágenes en escala de grises
        plt.subplot(121)
        plt.imshow(img1, cmap='gray')
        plt.title('Imagen 1 '+ texto)
        plt.axis('off')

        plt.subplot(122)
        plt.imshow(img2, cmap='gray')
        plt.title('Imagen 2 '+ texto)
        plt.axis('off')

        plt.tight_layout()
        plt.show()

    def calcular_traspuesta(self):
        imagen = self.image
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # Calcular la matriz traspuesta de la imagen
        imagen_traspuesta = np.transpose(imagen_rgb, (1, 0, 2))
        return imagen_traspuesta

    def convertir_a_escala_de_grises(self):
        imagen = self.image
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        return imagen_gris

    @staticmethod
    def matriz_inversa(matriz):
        determinante = np.linalg.det(matriz)
        # Verifica si el determinante es diferente de cero
        if determinante != 0:
            # La matriz tiene inversa
            # Calcula la inversa de la matriz
            matriz_inversa = np.linalg.inv(matriz)
            matriz_inversa_limitada = np.clip(matriz_inversa, 0, 255).astype(np.uint8)
            print("La matriz tiene inversa.")
            return matriz_inversa_limitada
        else:
            # La matriz no tiene inversa
            print("La matriz no tiene inversa, su determinante es igual a cero.")

    def matriz_por_escalar(matriz, alpha):
        resultado =  matriz * alpha
        resultado_limitado = np.clip(resultado, 0, 255)
        return resultado_limitado

    def crear_W(shape):
        if shape[0] != shape[1]: #Tiene que tener el mismo largo que ancho, sino tira excepcion personalizada
            raise ValueError("La matríz debe tener el mismo largo que ancho.")
        # Crear una matriz con unos en la antidiagonal
        I = np.eye(shape[0])
        w = np.fliplr(I)
        return w

    def voltear_imagen(matriz1, matriz2):
        # Multiplicar la matriz original por la matriz con unos en la antidiagonal
        resultado = np.dot(matriz1, matriz2)
        resultado_limitado = np.clip(resultado, 0, 255)

        return resultado


    def son_iguales(matriz1, matriz2):
        return np.array_equal(matriz1, matriz2)

    def negativo_imagen(matriz, shape):
        if shape[0] != shape[1]: #Tiene que tener el mismo largo que ancho, sino tira excepcion personalizada
            raise ValueError("La matríz debe tener el mismo largo que ancho.")
        # Crear una matriz con 255
        matriz255 = np.full((shape[0], shape[1]), 255, dtype=np.uint8)
        return matriz255 - matriz
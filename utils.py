import numpy as np
from skimage.io import imshow, imread
import cv2
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
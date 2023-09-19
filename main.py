import numpy as np
from skimage.io import imshow, imread
import cv2
import os
from utils import utils


## Parte 1 -----------------------------------------
img1 = utils("Images/img1.jpg")
img2 = utils("Images/img2.jpg")

img1.showImage('First Image')
img2.showImage('Second Image')

print(f"Tamaño antes de cortar : {img1.getShape()}")
img1.cut_image("Images/newImage.jpg",0, 450, 750, 1150)
img2.cut_image("Images/newImage1.jpg",0, 400, 400, 800)






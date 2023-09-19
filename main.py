import numpy as np
from skimage.io import imshow, imread
import cv2
import os
from utils import utils


## Parte 1 -----------------------------------------
ut = utils("")

#ut.showImage('First Image', "Images/img1.jpg")
#ut.showImage('Second Image', "Images/img2.jpg")

ut.cut_image("Images/img2.jpg", "Images/newImage.jpg",0, 450, 750, 1150)




import numpy as np
from PIL import Image
import pyautogui
import cv2

# Convierte la imagen en un array de numpy
sample_image_array = np.array(Image.open("friendly-survivor-sensor.png"))

# Obtiene las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Dividimos la pantalla horizontalmente en 3 regiones y buscamos el patrón en la región de la derecha porque es donde se encuentra el tribelog
x1 = screen_width // 3 * 2 # Comienzo de la región de la derecha
x2 = screen_width # Fin de la región de la derecha

# Captura la pantalla completa
screen = pyautogui.screenshot()
# Recorta la captura para obtener la región de la derecha
right_region = screen.crop((x1, 0, x2, screen_height))

# Convierte la región de la derecha en un array de numpy
right_region_array = np.array(right_region)

# Busca el patrón en la región de la derecha 
result = cv2.matchTemplate(right_region_array, sample_image_array, cv2.TM_CCOEFF_NORMED)

# Obtiene la posicion de la coincidencia mas cercana
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Si la similitud es mayor que un umbral, se considera que el patrón se encuentra en la región de la derecha
if max_val > 0.8:
    print("Pattern found in the right region", max_loc)
else:
    print("Pattern not found in the right region")
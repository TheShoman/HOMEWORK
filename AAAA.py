# Detección de bordes utilizando matrices con Python y OpenCV

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread(r"C:\Users\DG\Desktop\The Grid\123.jpg", 0)

# Aplicar filtro Sobel en eje X
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)

# Aplicar filtro Sobel en eje Y
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)

# Combinar ambos bordes
bordes = cv2.magnitude(sobel_x, sobel_y)

# Mostrar resultados
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap="gray")

plt.subplot(1,3,2)
plt.title("Sobel X")
plt.imshow(sobel_x, cmap="gray")

plt.subplot(1,3,3)
plt.title("Bordes Detectados")
plt.imshow(bordes, cmap="gray")

plt.show()
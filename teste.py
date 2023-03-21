import os
import cv2
#
import shutil


# Caminho para a foto no dispositivo externo
src_path = "Este Computador\G71\Armazenamento interno compartilhado\DCIM\Camera\IMG_20230208_105105_715.jpg"

# Caminho para a pasta de downloads no computador
dst_path = "C:/Users/adrie/Downloads/photo.jpg"

# Copia a foto para a pasta de downloads
shutil.copy2(src_path, dst_path)

# Verifica se a cópia foi bem-sucedida
if os.path.exists(dst_path):
    print("A foto foi copiada com sucesso para a pasta de downloads")
else:
    print("Erro ao copiar a foto para a pasta de downloads")



# Caminho para a imagem





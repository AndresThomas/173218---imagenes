from imgurpython import ImgurClient
from multiprocessing import Pool
import os
import urllib.request
import timeit

secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"

cliente = ImgurClient(id_cliente, secreto_cliente)

# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png

def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "C:/Users/andre/OneDrive/Escritorio/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))


def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)

   result = []
   for i in imagenes:
      result.append(i.link)
   
   #pool trabaja con los nucleos del procesador, es decir que se realizará un 
   #proceso,iteracion,llamada a la funcion, por cada nucleo disponible
   
   p = Pool()
   p.map(descarga_url_img,result)


if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))
   """
   lista de tiempos
   4.503513900000001
   4.3199707
   4.2527025
   """
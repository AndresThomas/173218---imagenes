from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor
import os
import urllib.request,logging
import timeit

secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"

cliente = ImgurClient(id_cliente, secreto_cliente)

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

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
   logging.info('<- ejecutado por')
   url_local = "C:/Users/andre/OneDrive/Escritorio/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))


def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   executor = ThreadPoolExecutor(max_workers=10) #creamos un pool de threads con 10 threads
   for imagen in imagenes:
      executor.submit(descarga_url_img,imagen.link) #el pool busca un thread libre,
      # luego asocia el target(funcion) con el thread libre y lo ejecuta


if __name__ == "__main__":
   logging.info("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))
   # lista de tiempos obtenidos
   """
   0.6725085000000001
   0.7319901
   0.5023918999999999
   """
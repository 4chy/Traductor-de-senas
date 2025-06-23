#Importar liberias
import cv2
import os

#Importar la clase
import SeguimientoManos as sm
#prueba de git hub
#creacion de la carpeta
nombre = "Letra_A"
direccion = "C:/Users/usuario/Desktop/proyecto-3ro/Traductor-de-senas/Vocales/data/Vocal_A"
carpeta = direccion + "/" + nombre

#Si no esta creada la carpeta
if not os.path.exists(carpeta):
    print("CARPETA CREADA: ", carpeta)
    #Creamos la carpeta
    os.makedirs(carpeta)

#Lectura de la camara
cap = cv2.VideoCapture()

#Cambiar la resolucion
cap.set(3,1280)
cap.set(4,720)

#Declarar detector
detector = sm.detectormanos(Confdeteccion=0.9)

while True:

    #Realizar la lectura de la cap
    ret,frame = cap.read()

    #Mostrar FPS
    cv2.imshow("LENGUAJES VOCALES", frame)

    #Leer nuestro teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()
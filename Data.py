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
cap = cv2.VideoCapture(0)

#Cambiar la resolucion
cap.set(3,1280)
cap.set(4,720)

#Declarar detector
detector = sm.detectormanos(Confdeteccion=0.9)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer el frame de la cámara.")
        continue
    # Extraer informacion de la mano 
    frame = detector.encontrarmanos(frame, dibujar= True )

    # Aplicar el detector de manos al frame
    frame = detector.encontrarmanos(frame)
    lista, bbox, player = detector.encontrarposicion(frame)

    # Mostrar el frame con manos detectadas
    cv2.imshow("LENGUAJES VOCALES", frame)

    if cv2.waitKey(1) == 27:  # Tecla ESC
        break
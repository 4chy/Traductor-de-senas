#Importar liberias   #source venv/bin/activate  #deactivate
import cv2
import os

#Importar la clase
import SeguimientoManos as sm
#prueba de git hub
#creacion de la carpeta
nombre = "Letra_A"
direccion = "C:/Users/usuario/Desktop/proyecto-3ro/Traductor-de-senas/Vocales/data/Vocal_A"
carpeta = direccion + "/" + nombre
recorte = None
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
#Declaramos contador
cont=0
#Declarar detector
detector = sm.detectormanos(Confdeteccion=0.9)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer el frame de la cámara.")
        continue
    # Extraer informacion de la mano 
    frame = detector.encontrarmanos(frame, dibujar= False )

    # Aplicar el detector de manos al frame
    
    lista1, bbox, player = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=(128, 0, 128))

    # Si detecta una mano:
    if player >= 1: 
        #Extraer informacion del cuadro
        xmin, ymin, xmax, ymax = bbox

        #Añadimos margen
        xmin= xmin -40 #esquina superior izq hacia la izq
        ymin= ymin -40 #esquina superior izq hacia arriba
        xmax= xmax +40 #esquina inferior der hacia la der
        ymax= ymax +40 #esquina inferior der hacia abajo

        # Captura de pantalla de la mano
        recorte= frame [ymin:ymax , xmin:xmax]
        
        #Redimensionamiento
        #recorte= cv2.resize (recorte, (640,640), interpolation=cv2.INTER_CUBIC)# pone todas la ismagenes a 1 solo tamaño

        #Almacenar imagenes
        cv2.imwrite(carpeta + "A_{}.jpg".format(cont), recorte)

        # Aumentamos contador 
        cont = cont + 1
        cv2.imshow("RECORTE", recorte) #Crea una segunda ventana que muestra lo que se va a recortar

        #cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,255,0), 2)
        #Muestra un rectangulo

    # Mostrar el frame con manos detectadas
    cv2.imshow("LENGUAJES VOCALES", frame)

    if cv2.waitKey(1) == 27 or cont == 100 :  # Tecla ESC
        break
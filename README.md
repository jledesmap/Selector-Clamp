# Selector-Clamp

# Table of Contents
   * [Qué es esto?](#Qué-es-esto)
   * [Requisitos software](#requisitos-software)
   * [Documentación](#documentation)
   * [Manual de uso](#manual-de-uso)

# Qué es esto?

Nuestro grupo ha desarrollado el proyecto llamado Selector Clamp. Este consiste en un brazo mecánico que cuenta con 4 grados de libertad para realizar sus movimientos de búsqueda de objetos y una cámara con la cual poder detectar su entorno.

El usuario a través de una aplicación móvil podrá seleccionar los detalles de la búsqueda. La aplicación permitirá hacer búsquedas de forma y/o color de los objetos. A más a más, hay la opción de hacer varias fotografías vía smartphone, a continuación, el usuario seleccionará aquellas imágenes que mejor describan la forma del objeto que desea que el brazo busque. Entre la comunicación del usuario y Selector Clamp tendremos un servidor donde se almacenarán las órdenes dadas por el usuario.

# Requisitos software

Python 3.7.x:

- numpy

- pirebase

- cv2

Unity:

- using Firebase;
- using Firebase.Database;
- using Firebase.Unity.Editor;

Android Studio

Lenguajes de programación usados: Python3, C#, Java.

# Documentación

Coco Datasets:  http://cocodataset.org/#home

YOLO: Real-time Object detection https://pjreddie.com/darknet/yolo/

Firebase: https://firebase.google.com/

Unity assets: https://assetstore.unity.com/

# Manual de uso

1. Descargar repositorio.

> git clone https://github.com/jledesmap/Selector-Clamp

2. Módulo Aplicación:
- Crear cuenta Firebase.
- Vincular aplicación en Android Studio con credenciales de Firebase (Seguir tutorial Firebase).

3. Módulo comunicación:
- En config, se añaden las credenciales para conectar con Base de datos y storage de Firebase.
- Configurar ruta de las imágenes que se descargan.

4. Módulo de detección:
- Importar CV2. 
- Importar numpy.

5. Módulo del Yolo en Unity:
- Compilar YoloSrc\Yolo.sln
- Publicar YoloServer project
- Launch YoloSrc\YoloServer\bin\Release\netcoreapp2.1\win-x64\YoloServer.exe
Abrir el proyecto de Unity y entrar en modo juego.
 

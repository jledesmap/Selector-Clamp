# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:54:58 2020

@author: Ridouan
"""
import detection_objects as do
import numpy as np
import pyrebase #pip install pyrebase
import urllib.request

#Credenciales para la comunicación
config = {
    "apiKey": "AIzaSyAwdK1l55w7MXyBcEU98dvSYSL62ugMgl4",
    "authDomain": "selectorclamp.firebaseapp.com",
    "databaseURL": "https://selectorclamp.firebaseio.com/",
    "projectId" : "selectorclamp",
    "storageBucket": "selectorclamp.appspot.com"

}

#Inicializa la base de datos
firebase = pyrebase.initialize_app(config)
bd = firebase.database()

def image_handler(message):
    """
    Esta escuchando continuamente los eventos sobre imagenes. y se ejecuta automáticamente.
    """
    url = message["data"]
    urllib.request.urlretrieve(url, 'imagen.jpg')
    tipo_objeto = do.detection_object("imagen.jpg")
    print(tipo_objeto)
    bd.child("tipo_objeto").set(tipo_objeto)
    bd.child("buscar").set("si")
    print("Esperando comandos ...")

stream_image = bd.child("image_url").stream(image_handler)


def color_handler(color):
    """
    Esta escuchando continuamente los eventos sobre el color. y se ejecuta automáticamente.
    """
    print(color["data"])
    print("Esperando comandos ...")
stream_color = bd.child("color").stream(color_handler)


def forma_handler(forma):
    """
    Esta escuchando continuamente los eventos sobre la forma. y se ejecuta automáticamente.
    """
    #print(forma["data"])
    #Pasar al robot la forma  para buscar.
stream_forma = bd.child("forma").stream(forma_handler)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:24:29 2021

@author: Navarro
"""
from PIL import Image
import numpy as np
import sys

class LoadImage():
    def __init__ (self,ruta):
        '''
        Args:
            ruta (string): Ruta donde se encuntre nuestra imagen.
        '''  
        self.maxCol = 796 #ancho maximo
        self.maxFila = 1123 #alto maximo 
        
        self.tipoImagen = 'jpg'
        self.jpg_bandera = self.esJPG(ruta,self.tipoImagen)
        
        # Para imagenes con formato .jpg...
        if self.jpg_bandera:
            self.img = self.cargarImg(ruta,self.tipoImagen)
            self.img1 = self.img.copy() #
            self.tamano = np.size(self.img1)
            self.imgVertical_bandera = self.esVertical(self.tamano)
            self.needResize_flag = self.resizeNeeded(self.imgVertical_bandera)
            # Si la imagen es vertical y necesita reescalado...
            if (self.imgVertical_bandera ==1)and(self.needResize_flag==True):
                self.img1.thumbnail((self.maxCol,self.maxFila))#resize
                self.img1.show()
                
            # si la imagen es horizontal y necesita reescalado...
            elif (self.imgVertical_bandera==0)and(self.needResize_flag==True):
                self.img1.thumbnail((self.maxFila,self.maxCol)) #Resize
                self.img1.show()
                pass
            
            # Si la imagen no necesita reescalado
            else:
                self.img1.show()               # pass
            

        # Para el resto de imagenes...
        else:
            print('La imagen debe estar en formato .jpg')
            sys.exit()
            
    # Devuelve bandera sobre si se debe o no reajustar el tamaño.
    def resizeNeeded(self,orientacion):
        # on es mayor de la necesaria    
        if orientacion: #Imagen vertical
            a = self.maxFila>self.tamano[1]         
            
        else: # Imagen horizontal
            a = self.maxCol<self.tamano[0]
            pass
        
        return a
    
    def esVertical(self,shape):
        # Retorna True si la imagen es vertical y False si es horizontal
        print('Tamaño original de la imagen',shape)
        return shape[1]>shape[0]
    
   
    def esJPG(self,ruta,tipoImagen):
        #Funcion para verificar si la imagen tiene el formato requerido (.jpg)
        return ruta.split('.')[-1]==tipoImagen
   
    def cargarImg(self,ruta,tipo):
        # Mirar si el arhcivo se puede abrir'
        try:
            img = Image.open(ruta)
            print('Imagen cargada correctamente')
        except:
            print('Error cargando la imagen')
            sys.exit() # stop
            
        return img
   
    
#Prueba de funcionamiento, si deseea probrar el codigo, debe cambiar la ruta donde se encuentra la imagen.
cargador = LoadImage(r'C:\Users\Navarro\Documents\Navarro\Proteccion_\Proteccion\Media\ioker.jpg') #Vertical
cargador = LoadImage(r'C:\Users\Navarro\Documents\Navarro\Proteccion_\Proteccion\Media\horizontal.jpg') #Horizontal
cargador = LoadImage(r'C:\Users\Navarro\Documents\Navarro\Proteccion_\Proteccion\Media\pequena.jpg') #Imagen pequeña
cargador = LoadImage(r'C:\Users\Navarro\Documents\Navarro\Proteccion_\Proteccion\Media\mas_grande.jpg') #Imagen mas grande
# cargador = LoadImage(r'C:\Users\Navarro\Documents\Navarro\Proteccion_\Proteccion\Media\corona.png')  #Imagen que no cumple el formato

        
        
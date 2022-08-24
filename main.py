import streamlit as st
from PIL import Image
import cv2 
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import time

from shutil import rmtree

from detect import *

#from streamlit import caching
#caching.clear_cache()
from IPython import *
from IPython import get_ipython

from git import Repo

if os.path.exists("/app/detechc/"):
     st.write("SE BORRO TODO")
     rmtree("/app/detechc/")
     

if not os.path.exists("/app/detecthc/pesos"):
     Repo.clone_from("https://gitlab.com/iasolutions_arg/detecthc_weights.git", "/app/detecthc/pesos")

if not os.path.exists("/app/detecthc/imagenes"):     
     os.mkdir("/app/detecthc/imagenes")

#get_ipython().magic('reset -sf')

#rmtree('app/detecthc/')

#SIDEBAR stuff---------------------------------
#imagen
#st.sidebar.image('foto.jpeg')

#umbral
st.sidebar.title('Opciones de Configuración')
st.sidebar.write("Umbral de confianza para detección:")
#H = st.sidebar.slider('Confianza HOS',1)  
C = st.sidebar.slider('Confianza',1)
C2 = st.sidebar.slider('IoU',1)
#st.sidebar.write(e)
#----------------------------------------------

#titulo
st.title('Detector y clasificador HOS-Coomassie')

#descripcion
st.write("Seleccione el conjunto de imágenes a segmentar y clasificar")

#browse files
dir_img = "/app/detecthc/imagenes"
uploaded_files = st.file_uploader("Cargar Imágenes", accept_multiple_files=True, help="Solo se aceptan imágenes en formato .png y .jpg", type=["png", "jpg", "jpeg"])

largo = len(uploaded_files)
for i in range(largo):
     #st.write(uploaded_files[i].name)
     with open(os.path.join(dir_img,uploaded_files[i].name),"wb") as f: 
          f.write(uploaded_files[i].getbuffer())
   
     #im[i] = Image.open(dir_img+'/'+uploaded_files[i].name)
     #st.write(len(im), "largoooo")
     #st.image(im[i],caption=uploaded_files[i].name)
        
     #st.success("Saved File:{} to directory".format(uploaded_files[i].name))    
     #st.image(os.path.join(dir_img,uploaded_files[i].name), caption=uploaded_files[i].name)
        
st.write(os.listdir(dir_img))      
st.write('Imagenes Cargadas: ',largo)
st.write('')
st.write('Haga click en "Comenzar" para realizar el proceso de detección y clasificación de espermatozoides')

#boton detectar
i = st.button("Comenzar")
if i:
#     if os.path.exists("/app/detechc/"):
#          st.write("SE BORRO TODO")
#          rmtree("/app/detechc/")

     for e in range(largo):
          #st.image(os.path.join(dir_img,uploaded_files[e].name), caption=uploaded_files[e].name)
          st.write(dir_img+'/'+uploaded_files[e].name)
          #plt.imshow(os.path.join(dir_img,uploaded_files[e].name) 
          #plt.show()
          
     
     if not os.path.exists("/app/detecthc/pesos"):
          Repo.clone_from("https://gitlab.com/iasolutions_arg/detecthc_weights.git", "/app/detecthc/pesos")
          st.write("directorio de pesos creado satisfactoriamente.")
          
     #st.write(os.getcwd()) #para ver el directorio
     j = detectHOS(C/100)
     st.write("termiando con exito")
     
     if not os.path.exists("runs/detect/exp/"):
          st.write("no existe el directorio /exp/")
     else:
          st.write(os.listdir("runs/detect/exp/"))
     
     ###
     #img = cv2.imread("runs/detect/exp/burro.jpg")
     #st.image(img[:,:,::-1])


#grafico de resultdos
st.write('Resultados:')
y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]


chart_data = pd.DataFrame({
     'index': ['H+C+', 'H+C-', 'H-C+', 'H-C-', 'NC'],
     'clases': [2,1,3,3,15]
}).set_index('index')

st.bar_chart(chart_data)   

#cv2.imwrite('')
st.write('')

#descargar imagenes clasificadas
st.write('Descargar imágenes procesadas:')
j = st.button("Descargar")
if j:
     st.write(os.listdir("/app/detecthc/pesos"))
     
     #st.write("IMAGEN GUARDADA")
     #cv2.imwrite("recorte.jpeg",h)
     #p = cv2.imread("recort.jpeg")
     #st.image(p)
     #p1 = cv2.imread("img1.jpg")
     #st.image(p1[:,:,::-1])
     #p2 = cv2.imread("img2.jpg")
     #st.image(p2)
     #p3 = cv2.imread("img3.jpg")
     #st.image(p3[:,:,::-1])
    

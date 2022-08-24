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
#st.sidebar.write(e)
#----------------------------------------------

#titulo
st.title('Detector y clasificador HOS-Coomassie')

#descripcion
st.write("Seleccione el conjunto de imágenes a segmentar y clasificar")

#browse files
uploaded_files = st.file_uploader("Cargar Imágenes", accept_multiple_files=True)
#st.write(uploaded_files)
i = 0
for file in uploaded_files:
     u = cv2.imread("foto.jpeg")     
     i = i + 1
     #st.write(uploaded_files)
     image = Image.open(file)
     cv2.imwrite("img"+str(i)+".jpg",u)
     #bytes_data = uploaded_file.read()

     st.write(image)
     st.image(image)
     
     
st.write('Imagenes Cargadas: ',i)
st.write('')
st.write('Haga click en "Comenzar" para realizar el proceso de detección y clasificación de espermatozoides')

#boton detectar
st.button("Comenzar")

#grafico de resultdos
st.write('Resultados:')
y = [2,6,2,9,7,1,5,7,5,2,8] 
x = [1,2,3,4,5,6,7,8,9,10,11]


chart_data = pd.DataFrame({
     'index': ['H+C+', 'H+C-', 'H-C+', 'H-C-', 'NC'],
     'clases': [28,20,15,12,35]
}).set_index('index')

st.bar_chart(chart_data)   

#cv2.imwrite('')
st.write('')

#descargar imagenes clasificadas
st.write('Descargar imágenes procesadas:')
i = st.button("Descargar")
if i:
     j = detectHOS(H/100)
     st.write(j)
     img = cv2.imread("runs/detect/exp/burro.jpg")
     st.image(img[:,:,::-1])

     #st.write("IMAGEN ORIGINAL")
     r = cv2.imread("foto.jpeg")
     st.image(r[:,:,::-1])
     caching.clear_cache()
     st.image(r)
     
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
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
 

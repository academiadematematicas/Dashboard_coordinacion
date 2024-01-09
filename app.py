
# Importación de las librerías
# IMPORTACIÓN DE LAS LIBRERÍAS
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from streamlit_option_menu import option_menu
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from PIL import Image

#------------------------------------------------------------------------------------------------#
def pie_de_pagina():
    # Pie de página
    Column1, Column2,Column3, Column4 = st.columns ((2,4,1,2))
    VA1 = Image.open("VA1.png")
    Column4.markdown("")
    Column4.image(VA1, width=100)

    Column2.markdown("<h1 style='text-align: center; color: #4A235A; font-size: 0.8rem;'>AVISO LEGAL | POLÍTICAS DE PRIVACIDAD | AVISO DE PRIVACIDAD</h1>", unsafe_allow_html=True)
    Column2.markdown("<h1 style='text-align: center; color: #4A235A; font-size: 0.8rem;'>©VAMOS ALTO | ACADEMIA DE MATEMÁTICAS | TODOS LOS DERECHOS RESERVADOS</h1>", unsafe_allow_html=True)

    VA2 = Image.open("VA2.jpg")
    Column1.image(VA2, width=100)

#------------------------------------------------------------------------------------------------#

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
#This code helps to hide the main menu of Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#-----------------------------------------------------------------------------------------------------------------------------#
# SIDEBAR
sidebar = st.sidebar
    
# IMPORTACIÓN DE LA BASE DE DATOS
# Resultados de la clase 1
df_links = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vR8AS4LnU66VOzeH0nz6Vbfrw2wQ0xAipWOgwjl81fln6ihf-bXdZ-DvGFXg-ufsFyNSy120q2uPaJT/pub?output=xlsx", sheet_name="Links de Quizizz")
df_links.dropna(how='all', inplace = True)
df_links.reset_index(drop=True, inplace=True)

# Resultados de la clase 1
df1 = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vR8AS4LnU66VOzeH0nz6Vbfrw2wQ0xAipWOgwjl81fln6ihf-bXdZ-DvGFXg-ufsFyNSy120q2uPaJT/pub?output=xlsx", sheet_name="Resultados_Clase1")
df1.dropna(how='all', inplace = True)
df1.reset_index(drop=True, inplace=True)
#st.write(df1)

# Resultados de la clase 2
df2 = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vR8AS4LnU66VOzeH0nz6Vbfrw2wQ0xAipWOgwjl81fln6ihf-bXdZ-DvGFXg-ufsFyNSy120q2uPaJT/pub?output=xlsx", sheet_name="Resultados_Clase2")
df2.dropna(how='all', inplace = True)
df2.reset_index(drop=True, inplace=True)
#st.write(df2)

df = pd.concat([df1, df2], axis=0)
#st.write(df)

#------------------------------------------------------------------------------------------------#
# Navigation Menu
option_selected = option_menu(
    menu_title=None,
    options=["Página principal", "Seguimiento por mentor", "Insights"],
    orientation="horizontal"
)
#------------------------------------------------------------------------------------------------#
if option_selected == "Página principal":
    #sidebar.markdown(" ")
    options=sidebar.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
    sidebar.markdown("<h1 style='text-align: left; color: #884EA0; font-size: 1.6rem;'>Academia de matemáticas</h1>", unsafe_allow_html=True)
    sidebar.markdown("<h1 style='text-align: left; color: #A569BD; font-size: 1.0rem;'>Seguimiento semanal de estudiantes:</h1>", unsafe_allow_html=True)
    sidebar.markdown(" ")
    sidebar.header("`* Quizizz`")
    st.write('You selected:', options)
    st.write(df)
    
    pie_de_pagina()
elif option_selected == "Seguimiento por mentor":
    st.write("Hola")

#------------------------------------------------------------------------------------------------#

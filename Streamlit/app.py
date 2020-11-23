# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import json
import numpy as np

#Inicializar nuestra conexión
def Graficos_Jorge():
    #db.initialize('covid')
    #DataFrame
    df = pd.read_json('../Templates/CollectionQuerry.json',encoding='UTF-8',)
    df=df.drop(['_id'],axis='columns')#Borra la columna _id (creada por el Mongo)
   # print(df)
    #TABLA DE DATOS
    st.dataframe(df)#Crea una tabla en streamlit dataframe
    st.table(df.style.highlight_min())#Crea una tabla estatica en streamlit y le da un colocr a los maximos valores
    df2=pd.read_json('../Json/Regiones_Provincias_comunas.json',orient='records')
    st.dataframe(df2)
   # print(df2)
    with open('../Json/Regiones_Provincias_comunas.json', encoding='utf-8') as f:
        data = json.load(f)
    st.json(data)#->Jorge esto es para ti, ahí resolví el problema que tenias de leer archivos json en codeados en utf-8

#Prueba de graficos con json
def Graficos_Mario():
    df_from_json = pd.read_json('../Json/PCR_Regional.json')
    df_from_json['positividad'] = np.where(np.isnan(df_from_json['positividad']), 0, df_from_json['positividad'])
    print(df_from_json[['Region', 'fecha', 'positividad']])
    st.write("""
    # From Json_PCR_Regional to Streamlit Table
    """
             )
    st.write(df_from_json[['Region', 'positividad', 'fecha']])
    region = st.sidebar.multiselect("Elegir regiones",
                                    ["Atacama", "Ñuble", "Magallanes", "Arica y Parinacota", "Aysén", "Coquimbo",
                                     "Araucanía", "Los Lagos", "Los Ríos", "Magallanes", "Tarapacá", "Valparaíso",
                                     "Biobío", "O’Higgins", "Maule", "Metropolitana"])
    for e in range (len(region)):
        st.write(df_from_json[['Region','positividad','fecha']].loc[(df_from_json['Region'] ==str(region[e])) & (df_from_json['positividad']>=0)])
    chart_data = pd.DataFrame(
        np.random.randn(20, len(region)), columns=region)

    st.line_chart(chart_data)

    # Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
    # map_data = pd.DataFrame(
    #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #  columns=['lat', 'lon'])

    # st.map(map_data)

Graficos_Mario()





#Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
#map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  #  columns=['lat', 'lon'])

#st.map(map_data)


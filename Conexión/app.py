# -*- coding: utf-8 -*-
from Conexion import Database as db
import pymongo as pym
import pandas as pd
import streamlit as st

#Inicializar nuestra conexión
db.initialize('covid')
#DataFrame
df = pd.read_json('../Templates/CollectionQuerry.json',encoding='UTF-8')
st.json(df)


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')
st.header('Proyecto de Sprint 7 | Emyl González')
hist_button = st.button('Mostrar Histograma')
scatter_button = st.button('Mostrar Gráfico de Dispersión')

if hist_button:

    st.write('Histograma de Precios de Autos')

    bins = np.arange(1000, 61000, 1000)
    fig = px.histogram(df,x='price',nbins=500)
    fig.update_xaxes(range=[1000,61000])
    
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:

    st.write('Valor del Vehículo vs Kilometraje')

    fig = px.scatter(df,x='odometer',y='price')

    st.plotly_chart(fig, use_container_width=True)


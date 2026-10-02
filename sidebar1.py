import streamlit as st
st.title("mi primer app con streamlit")
sidebar=st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aqui van los elementos de entrada.")
st.header("Información sobre el conjunto de datos")
st.header("descripción de los datos")
st.write("""
Este es un simple ejemplo de una app para predecir 
¡Esta app predice mis datos!
""")
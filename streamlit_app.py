import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

#Correr la aplicación con: streamlit run streamlit_app.py
APP_TITLE = "Cafe Map Visualizer"
APP_SUBTITLE = "Prueba Dashboard"

@st.cache_data
def load_geojson():
    """Carga el archivo GeoJSON con cache para mejorar rendimiento"""
    geojson_path = 'Data/cober_arborea_2021_dissolve_4326.geojson'
    if not os.path.exists(geojson_path):
        st.error(f"No se encontró el archivo: {geojson_path}")
        return None
    return geojson_path

def display_map():
    try:
        geojson_path = load_geojson()
        if geojson_path is None:
            st.error("No se puede cargar el mapa sin el archivo GeoJSON")
            return
        
        map = folium.Map(location=[9.7489, -83.7534], zoom_start=8, tiles="CartoDB positron")
        
        # Agregamos manejo de errores para la carga del GeoJSON
        choropleth = folium.Choropleth(
            geo_data=geojson_path,
            line_weight=1,
            line_opacity=0.7,
            fill_opacity=0.5
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=850, height=600)
        
    except Exception as e:
        st.error(f"Error al cargar el mapa: {str(e)}")
        st.info("Esto puede deberse al tamaño del archivo GeoJSON (212MB). Considera optimizar el archivo.")


def main():
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    
    display_map()

if __name__ == "__main__":
    main()